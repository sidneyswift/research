#!/usr/bin/env python3
"""Check frozen capture lineage and review coverage. Does not judge annotations."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def rows(path):return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-corpus',type=Path,required=True)
    p.add_argument('--run',type=Path,required=True)
    p.add_argument('--require-complete',action='store_true')
    a=p.parse_args();queue=json.loads((a.private_corpus/'review-queue.json').read_text());coverage=rows(a.run/'coverage.jsonl');reviews=rows(a.run/'reviews.jsonl')
    q={c['alias']:c for c in queue};cov={c['alias']:c for c in coverage};rev={c['alias']:c for c in reviews}
    if len(q)!=len(queue) or len(cov)!=len(coverage) or len(rev)!=len(reviews):raise ValueError('Duplicate alias')
    if not set(q)<=set(cov):raise ValueError('Capture/coverage universe mismatch')
    # ChatGPT connector captures have a different envelope from local Codex rows.
    for alias,c in cov.items():
        if alias in q:continue
        if c.get('source_kind')!='chatgpt-read-thread':raise ValueError('Unknown capture kind '+alias)
        source=a.private_corpus/(alias+'.json')
        payload=json.loads(source.read_text())
        q[alias]={'alias':alias,'source_file':alias+'.json','source_sha256':c['source_sha256'],
                  'status':c['semantic_review_status'],
                  'messages':[{'item_id':item['id']} for turn in payload['turns'] for item in turn['items']]}
    anchors=(Path('sources/codex--conversation-corpus-20261102.md')).read_text()
    for alias,c in q.items():
        if '#'+alias not in anchors:raise ValueError('Missing source anchor '+alias)
        source=a.private_corpus/c['source_file']
        if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest()!=c['source_sha256']:raise ValueError('Capture changed/missing '+alias)
        if cov[alias]['semantic_review_status']!=c['status']:raise ValueError('Queue/coverage drift '+alias)
        if c['status'].startswith('model-reviewed'):
            if alias not in rev:raise ValueError('Missing review '+alias)
            r=rev[alias];expected=[m['item_id'] for m in c['messages']]
            if Counter(expected)!=Counter(r['reviewed_message_ids']) or Counter(expected)!=Counter(cov[alias]['reviewed_message_ids']):raise ValueError('Review ID mismatch '+alias)
            if not expected:raise ValueError('Empty source counted reviewed '+alias)
            if r.get('training_eligible') is not False or r.get('human_review_status')!='unreviewed' or r.get('allowed_uses')!=['private_analysis'] or r.get('dataset_split')!='development':raise ValueError('Unexpected training promotion '+alias)
            if r.get('source_ref')!='sources/codex--conversation-corpus-20261102#'+alias:raise ValueError('Wrong source '+alias)
        elif alias in rev:raise ValueError('Uncounted review '+alias)
    records=[]
    for file in ['findings.jsonl','episodes.jsonl','development-probes.jsonl','interventions.jsonl','lessons.jsonl','task-families.jsonl']:
        records+=rows(a.run/file) if (a.run/file).exists() else []
    if len({r['id'] for r in records})!=len(records):raise ValueError('Duplicate derived record ID')
    for r in records:
        if r.get('training_eligible') is not False or r.get('human_review_status')!='unreviewed' or r.get('allowed_uses')!=['private_analysis'] or r.get('dataset_split')!='development':raise ValueError('Unreviewed derived record promoted')
        for ref in r.get('evidence_refs',[]):
            if ref['alias'] not in rev or ref['item_id'] not in {m['item_id'] for m in q[ref['alias']]['messages']}:raise ValueError('Invalid evidence locator '+r['id'])
        for alias in r.get('aliases',[]):
            if alias not in q:raise ValueError('Unknown task-family member '+alias)
        if 'annotation_ref' in r:
            parent=rev[r['alias']];ref=r['annotation_ref']
            values=parent[ref['field']]
            value=(values if isinstance(values,list) else [values])[ref['index']]
            if ref['review_id']!=parent['id'] or value!=r['annotation']:raise ValueError('Generated annotation drift '+r['id'])
            for restriction in ['source_reuse_restricted','excluded_from_training_and_publication']:
                if parent.get(restriction) and not r.get(restriction):raise ValueError('Lost source restriction '+r['id'])
    counts=Counter(c['status'] for c in q.values());pending=counts.get('pending',0)
    print(json.dumps(dict(discovered=len(q),model_reviewed=len(reviews),status_counts=dict(counts),derived_records=len(records),pending=pending,complete_with_documented_gaps=pending==0)))
    if a.require_complete and pending:raise SystemExit(1)

if __name__=='__main__':main()
