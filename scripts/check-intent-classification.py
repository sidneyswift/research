#!/usr/bin/env python3
"""Validate additive intent annotations against frozen evidence; never judge intent."""
import argparse
import hashlib
import json
from pathlib import Path

PURPOSES={'explore_options','develop_requirements','plan','execute','diagnose','evaluate_review','unknown'}
CONTRIBUTIONS={'reaffirm_requirement','clarify_ambiguity','add_fact','add_requirement','change_decision','express_preference','approve','reject','ask_probe','none_observed','unknown'}
CLARITY={'explicit','inferred','unresolved','conflicting','outside_captured_context'}
RESPONSES={'helpful_discovery','follows_established_state','conflicts_with_established_state','unsupported_assumption_or_expansion','justified_challenge','appropriate_boundary','unresolved'}

def check(record,window,rubric_hash):
    if record['rubric_sha256']!=rubric_hash:raise ValueError('Rubric drift')
    digest=hashlib.sha256(json.dumps(window,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    if record['window_sha256']!=digest:raise ValueError('Window drift')
    if record['alias']!=window['alias'] or record['selection_id']!=window['id']:raise ValueError('Wrong window')
    messages=window.get('earlier_context_messages',[])+window['messages']
    known={m['item_id']:m for m in messages};order={m['item_id']:i for i,m in enumerate(messages)}
    for key,allowed in [('phase_purpose',PURPOSES),('human_contribution',CONTRIBUTIONS),('agent_response',RESPONSES)]:
        values=record[key]
        if not values or not isinstance(values,list) or not set(values)<=allowed:raise ValueError('Invalid '+key)
    if 'none_observed' in record['human_contribution'] and len(record['human_contribution'])!=1:raise ValueError('Conflicting feedback authorship')
    if set(record['clarity'])!={'objective','deliverable','audience','constraints','success_criterion','action_authority'} or not set(record['clarity'].values())<=CLARITY:raise ValueError('Invalid clarity dimensions')
    if not record.get('clarity_rationale') or not record.get('interpretation_limits'):raise ValueError('Evidence rationale required')
    if record.get('human_review_status')!='unreviewed' or record.get('training_eligible') is not False or record.get('allowed_uses')!=['private_analysis'] or record.get('dataset_split')!='development':raise ValueError('Unexpected promotion')
    refs=[x['item_id'] for x in record['evidence_refs']]+record['evaluated_action_refs']
    for key in ['prior_action_refs','human_feedback_refs','post_feedback_response_refs']:refs+=record.get(key,[])
    for key in ['establishment_refs','acknowledgement_refs','supersedes_refs','prior_decision_context_refs','candidate_establishment_refs']:refs+=record['decision'].get(key,[]) or []
    cutoff=record.get('decision_time_cutoff')
    if cutoff is not None:refs.append(cutoff)
    if not set(refs)<=set(known):raise ValueError('Unknown evidence locator')
    if record['information_state']=='captured_at_cutoff' and cutoff is None:raise ValueError('Claimed decision context without cutoff')
    if record.get('evaluation_focus')=='prior_action' and record['evaluated_action_refs']!=record.get('prior_action_refs'):raise ValueError('Prior action evaluation silently replaced by repair')
    if cutoff is not None and any(order[x]<=order[cutoff] for x in record['evaluated_action_refs']):raise ValueError('Action must follow its decision cutoff')
    if any(known[x]['role']!='userMessage' for x in record['decision']['establishment_refs']):raise ValueError('Human establishment requires a user message; authorship still needs semantic review')
    if record['violation_status']=='supported':
        requirement=record.get('violation_requirement_ref');action=record.get('violation_action_ref')
        if cutoff is None or requirement not in known or action not in known or not order[requirement]<=order[cutoff]<order[action] or record['information_state']!='captured_at_cutoff':raise ValueError('Unsupported temporal violation claim')
        if not record.get('violation_rationale'):raise ValueError('Missing conflict rationale')
    return True

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',type=Path,required=True);p.add_argument('--private-corpus',type=Path,required=True);a=p.parse_args()
    manifest=json.loads((a.run/'first-pass-manifest.json').read_text())
    for v in manifest['files'].values():
        for file in [Path(v['source']),a.private_corpus/'intent-pass-first-revision'/v['private_frozen_copy']]:
            if hashlib.sha256(file.read_bytes()).hexdigest()!=v['sha256']:raise ValueError('First-pass baseline changed: '+str(file))
    windows=json.loads((a.private_corpus/'intent-calibration-windows.json').read_text());ws={w['id']:w for w in windows}
    queue={q['alias']:q for q in json.loads((a.private_corpus/'review-queue.json').read_text())}
    for w in windows:
        if w['alias']!='PILOT-SOW':
            c=queue[w['alias']]
            if c['source_sha256']!=w['source_sha256'] or c['messages'][w['start']:w['end']]!=w['messages']:raise ValueError('Window/capture mismatch')
        else:
            pilot_messages={}
            for src in w['source_files']:
                file=a.private_corpus.parent/'conversation-learning-evidence'/src['file']
                if hashlib.sha256(file.read_bytes()).hexdigest()!=src['sha256']:raise ValueError('Pilot capture drift')
                for turn in json.loads(file.read_text())['turns']:
                    for item in turn['items']:
                        text=item.get('text') or '\n'.join(b.get('text','') for b in item.get('content',[]) if isinstance(b,dict))
                        if text:pilot_messages[item['id']]=dict(item_id=item['id'],turn_id=turn['id'],role=item['type'],text=text)
            for message in w.get('earlier_context_messages',[])+w['messages']:
                if pilot_messages.get(message['item_id'])!=message:raise ValueError('Pilot message differs from source')
    annotations=[json.loads(x) for x in (a.run/'calibration-annotations.jsonl').read_text().splitlines()]
    if len({x['id'] for x in annotations})!=len(annotations):raise ValueError('Duplicate annotation')
    if {x['selection_id'] for x in annotations}!=set(ws):raise ValueError('Calibration coverage gap')
    rubric_hash=hashlib.sha256((a.run/'rubric.md').read_bytes()).hexdigest()
    for r in annotations:check(r,ws[r['selection_id']],rubric_hash)
    print(json.dumps({'annotations':len(annotations),'first_pass_unchanged':True,'calibration_windows_covered':len(ws),'human_adjudicated':0,'structural_integrity':'pass','semantic_correctness':'not established by this validator'}))

if __name__=='__main__':main()
