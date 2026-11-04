#!/usr/bin/env python3
"""Validate disjoint review shards against private capture IDs, then merge ledgers."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re


def atomic_write(path, text):
    temporary=path.with_name(path.name+'.next')
    temporary.write_text(text)
    temporary.chmod(0o600)
    temporary.replace(path)


def read(path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-corpus',type=Path,required=True)
    p.add_argument('--run',type=Path,required=True)
    a=p.parse_args()
    queue=json.loads((a.private_corpus/'review-queue.json').read_text());q={c['alias']:c for c in queue}
    coverage=read(a.run/'coverage.jsonl');cov={c['alias']:c for c in coverage}
    prior=read(a.run/'reviews.jsonl');known={r['alias']:r for r in prior};added=[];updated=0;shard_aliases=set()
    for path in sorted(a.run.glob('reviews-agent-*.jsonl')):
        # A concurrent incomplete write is left for the next pass.
        try:rows=read(path)
        except json.JSONDecodeError:
            print('Deferred incomplete shard:',path.name);continue
        for r in rows:
            alias=r['alias']
            if alias in shard_aliases:raise ValueError('Overlapping reviewer shards: '+alias)
            shard_aliases.add(alias)
            if alias not in q:raise ValueError('Unknown capture: '+alias)
            c=q[alias];expected=[m['item_id'] for m in c['messages']]
            if not expected:raise ValueError('No visible messages: '+alias)
            if Counter(r.get('reviewed_message_ids',[]))!=Counter(expected):
                raise ValueError('Full review IDs do not match capture: '+alias)
            kind=r.get('review_kind','')
            if kind=='full-dialogue-with-tool-inventory':
                tool_ids=[];dialogue_ids=[]
                for message in c['messages']:
                    text=message['text'].strip()
                    is_tool=(text.startswith('[external_agent_tool_call:') and text.endswith('[/external_agent_tool_call]')) or (text.startswith('[external_agent_tool_result') and text.endswith('[/external_agent_tool_result]'))
                    (tool_ids if is_tool else dialogue_ids).append(message['item_id'])
                if Counter(r.get('reviewed_dialogue_message_ids',[]))!=Counter(dialogue_ids):
                    raise ValueError('Dialogue coverage mismatch: '+alias)
                if Counter(r.get('inventoried_tool_message_ids',[]))!=Counter(tool_ids):
                    raise ValueError('Tool inventory mismatch: '+alias)
                if not r.get('tool_payload_review_limits'):
                    raise ValueError('Tool-payload limits required: '+alias)
                required=[m['item_id'] for m in c['messages'] if m['item_id'] in tool_ids and re.search(r'^\[external_agent_tool_call:\s*(?:SendUserMessage|AskUserQuestion|[^\]\n]*request_user_input)',m['text'].strip(),re.I)]
                if not set(required)<=set(r.get('inspected_tool_evidence_ids',[])):
                    raise ValueError('User-facing tool payload not inspected: '+alias)
            elif not kind.startswith('full-visible-projection'):
                raise ValueError('Partial review cannot be counted full: '+alias)
            if r.get('source_ref')!='sources/codex--conversation-corpus-20261102#'+alias:
                raise ValueError('Source mismatch: '+alias)
            if r.get('human_review_status')!='unreviewed' or r.get('training_eligible') is not False:
                raise ValueError('Do not promote unreviewed labels: '+alias)
            for field in ['episode_observation','interpretation_limits']:
                if not r.get(field):raise ValueError('Missing '+field+': '+alias)
            if alias not in known:added.append(r)
            elif known[alias]!=r:updated+=1
            known[alias]=r
            c.update(status='model-reviewed-dialogue-tool-inventory' if kind=='full-dialogue-with-tool-inventory' else 'model-reviewed-visible-projection',reviewed_characters=c['chars'] if kind!='full-dialogue-with-tool-inventory' else None)
            cov[alias].update(semantic_review_status=c['status'],reviewed_message_ids=expected,finding_ids=[r['id']])
            if c['source_sha256']!=cov[alias]['source_sha256']:
                cov[alias].update(fallback_sha256=c['source_sha256'],messages_available_after_fallback=len(expected),capture_status='fallback-captured')
    atomic_write(a.run/'reviews.jsonl',''.join(json.dumps(known[r['alias']],ensure_ascii=False)+'\n' for r in prior+added))
    atomic_write(a.run/'coverage.jsonl',''.join(json.dumps(c)+'\n' for c in coverage))
    atomic_write(a.private_corpus/'review-queue.json',json.dumps(queue,ensure_ascii=False))
    counts=Counter(c['semantic_review_status'] for c in coverage)
    print(json.dumps({'added':len(added),'updated':updated,'reviewed':len(prior)+len(added),'discovered':len(coverage),'coverage':dict(counts)}))

if __name__=='__main__':main()
