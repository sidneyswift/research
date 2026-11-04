#!/usr/bin/env python3
"""Render second-pass annotation views without inferring additional labels."""
import argparse
from collections import Counter
import json
from pathlib import Path

def build(run):
    records=[json.loads(x) for x in (run/'calibration-annotations.jsonl').read_text().splitlines()]
    lines=['# Intent calibration — 24 selected windows','','Generated from `calibration-annotations.jsonl`; edit annotation revisions rather than this surface. Model judgments await human adjudication. This deliberately selected sample is not a prevalence estimate.','']
    review=[]
    for r in records:
        lines += ['## '+r['id'],'','[['+r['source_ref']+']]','',r['observation'],'','- Phase: '+', '.join(r['phase_purpose']),'- Human contribution: '+', '.join(r['human_contribution']),'- Evaluation focus: '+r.get('evaluation_focus','unspecified'),'- Agent response: '+', '.join(r['agent_response']),'- Violation: '+r['violation_status'],'','Limits: '+r['interpretation_limits'],'']
        if r['needs_human_intent_adjudication']:
            review.append(dict(id='REVIEW-'+r['id'],annotation_id=r['id'],alias=r['alias'],source_ref=r['source_ref'],interpretation_to_review=r['observation'],uncertainty=r['interpretation_limits'],status='pending-human-adjudication',reviewer=None,answer=None,training_eligible=False,allowed_uses=['private_analysis']))
    (run/'calibration-catalog.md').write_text('\n'.join(lines))
    (run/'human-review-queue.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in review))
    summary=dict(windows=len(records),deliberate_sample=True,representative=False,human_adjudicated=0,needs_human_intent_adjudication=len(review),phase_labels=dict(Counter(v for r in records for v in r['phase_purpose'])),human_contribution_labels=dict(Counter(v for r in records for v in r['human_contribution'])),violation_status=dict(Counter(r['violation_status'] for r in records)),notice='Multi-label counts overlap. not_established is not proof of absence; selected response windows do not establish corpus failure rates.')
    (run/'calibration-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--run',type=Path,required=True);print(json.dumps(build(p.parse_args().run)))
