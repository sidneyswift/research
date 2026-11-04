#!/usr/bin/env python3
"""Append model-authored reviews and update coverage, after visible evidence is read.

This tool validates locators; it does not generate or substantively approve labels.
Notes JSON: list of {alias, episode_observation, interpretation_limits}.
A note covers the complete visible projection only if the caller actually reviewed it.
"""
import argparse
import json
from importlib import import_module
atomic_write=import_module("merge-conversation-review-shards").atomic_write
from pathlib import Path


def annotation_fields(note):
    """Preserve supported annotations; never silently drop caller-supplied fields."""
    required={'alias','episode_observation','interpretation_limits','review_kind'}
    annotations={'interventions','lesson_candidates','holistic_lesson_candidates','observed_agent_corrections'}
    restrictions={'source_reuse_restricted','excluded_from_training_and_publication'}
    metadata={'exact_block_dedup','review_coverage'}
    unknown=set(note)-required-annotations-restrictions-metadata
    if unknown:raise ValueError('Unsupported note fields: '+', '.join(sorted(unknown)))
    result={}
    for key in set(note)-required:
        value=note[key]
        if key in annotations and not (isinstance(value,list) and all(isinstance(x,(str,dict)) for x in value)):
            raise ValueError('Expected annotation list: '+key)
        if key in restrictions and not isinstance(value,bool):raise ValueError('Expected boolean restriction: '+key)
        if key in metadata and not isinstance(value,dict):raise ValueError('Expected metadata object: '+key)
        result[key]=value
    if note.get('review_kind')=='full-visible-projection-with-exact-block-dedup' and not note.get('exact_block_dedup'):
        raise ValueError('Exact-block review requires deduplication metadata')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-corpus',type=Path,required=True)
    p.add_argument('--run',type=Path,required=True)
    p.add_argument('--notes',type=Path,required=True)
    a=p.parse_args()
    queue=json.loads((a.private_corpus/'review-queue.json').read_text())
    coverage=[json.loads(l) for l in (a.run/'coverage.jsonl').read_text().splitlines()]
    prior=[json.loads(l) for l in (a.run/'reviews.jsonl').read_text().splitlines()]
    notes=json.loads(a.notes.read_text()); q={x['alias']:x for x in queue}; cov={x['alias']:x for x in coverage}
    existing={x['alias'] for x in prior};records=[]
    for note in notes:
        optional=annotation_fields(note)
        alias=note['alias']
        if alias in existing:raise ValueError('Already reviewed: '+alias)
        c=q[alias]
        if not c['messages']:raise ValueError('No messages; use an evidence-gap disposition: '+alias)
        for field in ['episode_observation','interpretation_limits']:
            if not note.get(field):raise ValueError('Missing '+field)
        ids=[m['item_id'] for m in c['messages']]
        kind=note.get('review_kind','full-visible-projection')
        if not kind.startswith('full-visible-projection'):raise ValueError('Unsupported full-review method: '+kind)
        review=dict(id='REVIEW-'+alias,alias=alias,source_ref='sources/codex--conversation-corpus-20261102#'+alias,review_kind=kind,reviewer='research-agent',human_review_status='unreviewed',outcome='not_independently_verified',reviewed_message_ids=ids,training_eligible=False,dataset_split='development',allowed_uses=['private_analysis'],episode_observation=note['episode_observation'],interpretation_limits=note['interpretation_limits'])
        review.update(optional)
        records.append(review);existing.add(alias)
        c.update(status='model-reviewed-visible-projection',reviewed_characters=c['chars'])
        cov[alias].update(semantic_review_status=c['status'],reviewed_message_ids=ids,finding_ids=[review['id']])
        if cov[alias]['source_sha256']!=c['source_sha256']:
            cov[alias].update(fallback_sha256=c['source_sha256'],messages_available_after_fallback=len(ids),capture_status='fallback-captured')
    # Validate the batch before replacing any ledger.
    atomic_write(a.run/'reviews.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in prior+records))
    atomic_write(a.run/'coverage.jsonl',''.join(json.dumps(x)+'\n' for x in coverage))
    atomic_write(a.private_corpus/'review-queue.json',json.dumps(queue,ensure_ascii=False))
    print(f'Recorded {len(records)} reviews; {len(prior)+len(records)} reviewed of {len(coverage)} discovered chats.')

if __name__=='__main__':main()
