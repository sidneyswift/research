#!/usr/bin/env python3
"""Verify named documentation captures against local SHA-256/byte receipts.

Read-only, dependency-free, no network. Accepts either a list of capture entries
or an object with a `captures` list. This verifies stored bytes, not source
authority, completeness, semantic support, or runtime behavior.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


def check(receipt):
    receipt = Path(receipt)
    problems = []
    try:
        data = json.loads(receipt.read_text())
        entries = data.get('captures') if isinstance(data, dict) else data
        if not isinstance(entries, list) or not entries:
            raise ValueError('expected a non-empty capture list')
    except (OSError, ValueError) as error:
        return 0, [f'{receipt}: invalid receipt: {error}']

    root = receipt.parent.resolve()
    seen = set()
    checked = 0
    for number, entry in enumerate(entries, 1):
        label = f'{receipt}: entry {number}'
        try:
            if not isinstance(entry, dict):
                raise ValueError('expected an object')
            name = entry.get('file')
            if not isinstance(name, str) or not name:
                raise ValueError('missing file')
            relative = Path(name)
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError('file must be relative and stay inside capture directory')
            target = (root / relative).resolve()
            if target == root or not target.is_relative_to(root):
                raise ValueError('file resolves outside capture directory')
            if target in seen:
                raise ValueError('duplicate file')
            seen.add(target)
            digest, size = entry.get('sha256'), entry.get('bytes')
            if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
                raise ValueError('expected lowercase SHA-256')
            if type(size) is not int or size < 0:
                raise ValueError('expected nonnegative integer bytes')
            if not isinstance(entry.get('url'), str) or not entry['url'].startswith('https://'):
                raise ValueError('expected HTTPS source URL')
            payload = target.read_bytes()
            if len(payload) != size:
                raise ValueError(f'{name}: byte count mismatch')
            if hashlib.sha256(payload).hexdigest() != digest:
                raise ValueError(f'{name}: SHA-256 mismatch')
            checked += 1
        except (OSError, ValueError, RuntimeError) as error:
            problems.append(f'{label}: {error}')
    return checked, problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('receipts', type=Path, nargs='+')
    args = parser.parse_args()
    checked, problems = 0, []
    for receipt in args.receipts:
        count, errors = check(receipt)
        checked += count
        problems.extend(errors)
    for problem in problems:
        print(problem)
    print(f'captures_verified={checked} · receipts={len(args.receipts)} · errors={len(problems)}')
    return bool(problems)


if __name__ == '__main__':
    raise SystemExit(main())
