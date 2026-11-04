#!/usr/bin/env python3
"""Check pilot annotation structure and lineage; never judge labels or train models.

Usage: python3 scripts/check-conversation-learning.py <pilot-directory>
Reads records.jsonl and evaluations.jsonl. Does not fetch private evidence.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pilot', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    rows, errors = [], []
    for name in ('records.jsonl', 'evaluations.jsonl'):
        for line_no, line in enumerate((args.pilot / name).read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError('record must be an object')
                rows.append((f'{name}:{line_no}', row))
            except (ValueError, json.JSONDecodeError) as exc:
                errors.append(f'{name}:{line_no}: {exc}')
    required = {'schema_version', 'id', 'record_type', 'revision', 'created_at',
                'created_by', 'origin', 'evidence_refs', 'review_status', 'owner_id',
                'project_id', 'access_class', 'allowed_uses', 'rights_basis_ref',
                'retention_policy_ref'}
    registry = {}
    for where, row in rows:
        missing = required - row.keys()
        if missing:
            errors.append(f'{where}: missing {sorted(missing)}')
        key = (row.get('id'), row.get('revision'))
        if key in registry:
            errors.append(f'{where}: duplicate ID/revision {key}')
        registry[key] = row
        if row.get('schema_version') != 1:
            errors.append(f'{where}: unsupported schema version')
        if not isinstance(row.get('allowed_uses'), list):
            errors.append(f'{where}: allowed_uses must be a list')
        if not isinstance(row.get('evidence_refs'), list):
            errors.append(f'{where}: evidence_refs must be a list')
        if row.get('review_status') == 'confirmed' and not row.get('reviewer_id'):
            errors.append(f'{where}: confirmation needs reviewer attribution')
        if row.get('record_type') == 'evaluation':
            if not row.get('expected_checks'):
                errors.append(f'{where}: missing evaluation criteria')
            if row.get('dataset_split') != 'development':
                errors.append(f'{where}: studied-case fixtures must stay development')
    for where, row in rows:
        for ref in row.get('evidence_refs', []) if isinstance(row.get('evidence_refs'), list) else []:
            if not isinstance(ref, dict):
                errors.append(f'{where}: evidence reference must be an object')
                continue
            if (ref.get('record_id'), ref.get('revision')) not in registry:
                errors.append(f'{where}: unresolved evidence reference {ref}')
            source = ref.get('source_ref')
            if source:
                page, _, anchor = source.partition('#')
                path = root / (page + '.md')
                if not path.is_file() or not anchor or f'`#{anchor}`' not in path.read_text():
                    errors.append(f'{where}: unregistered source anchor {source}')
        for field in ('task_id', 'episode_id'):
            target = row.get(field)
            if target and (target, 1) not in registry:
                errors.append(f'{where}: unresolved {field} {target}')
        for field in ('capture_ids', 'episode_ids', 'intervention_ids'):
            for target in row.get(field, []):
                if (target, 1) not in registry:
                    errors.append(f'{where}: unresolved {field} {target}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(rows)} records; required envelopes, IDs, lineage, source anchors and development fixture boundaries.')
    print('Not checked: semantic correctness, private-source completeness, consent, export eligibility or model behavior.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
