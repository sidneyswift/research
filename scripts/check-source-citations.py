#!/usr/bin/env python3
"""Check one repo citation page's anchors and immutable GitHub line references.

Uses only the local pinned Git objects and tracked wiki pages (plus supplied pages).
Does not fetch, edit, execute source code, or assess semantic support for a claim.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)


def field(text, name):
    front = text.split('---', 2)[1] if text.startswith('---\n') else ''
    match = re.search(r'^' + re.escape(name) + r':\s*(.*?)\s*$', front, re.M)
    if not match:
        raise ValueError('missing frontmatter field: ' + name)
    return match[1].strip('\"\'')


def registered_anchors(text):
    # Register only explicit entries in the map, never examples or incidental prose.
    anchors = set()
    in_map = False
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        if re.match(r'^##\s+', line):
            in_map = line.strip() == '## Anchor map'
            continue
        if not in_map:
            continue
        heading = re.fullmatch(r'###\s+([\w.-]+)\s*', line)
        entry = re.match(r'^-\s+`#([^`\s]+)`', line)
        if heading or entry:
            anchors.add((heading or entry)[1])
    return anchors


def check(wiki, source, repo, extra_pages=()):
    text = source.read_text()
    errors = []
    stamp = field(text, 'upstream-commit')
    if not re.fullmatch(r'[0-9a-f]{40}', stamp):
        raise ValueError('upstream-commit must be a full 40-character SHA')
    git(repo, 'cat-file', '-e', stamp + '^{commit}')
    target = source.relative_to(wiki).with_suffix('').as_posix()
    anchors = registered_anchors(text)
    if not anchors:
        errors.append('source page has no registered anchors')
    tracked = git(wiki, 'ls-files', '-z', '--', '*.md').decode().split('\0')
    pages = {wiki / p for p in tracked if p} | set(extra_pages)
    for page in extra_pages:
        if not page.is_file():
            errors.append('explicit page missing or not a file: ' + str(page))
    citations = 0
    for page in sorted(pages):
        if not page.exists():
            continue
        for match in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', page.read_text()):
            dest, sep, anchor = match[1].partition('#')
            if dest != target or not sep:
                continue
            citations += 1
            if anchor not in anchors:
                line = page.read_text()[:match.start()].count('\n') + 1
                errors.append(f'{page.relative_to(wiki)}:{line}: unregistered #{anchor}')
    urls = set(re.findall(r'https://github\.com/[^\s)<>]+/blob/[^\s)<>]+', text))
    expected = urlparse(field(text, 'url')).path.strip('/').split('/')[:2]
    cache = {}
    ranges = 0
    for url in sorted(urls):
        parsed = urlparse(url)
        parts = parsed.path.strip('/').split('/')
        if len(parts) < 5 or parts[:2] != expected:
            errors.append('unexpected repository permalink: ' + url)
            continue
        revision, path = parts[3], unquote('/'.join(parts[4:]))
        if revision != stamp:
            errors.append('unpinned or mismatched revision: ' + url)
            continue
        if path not in cache:
            try:
                cache[path] = len(git(repo, 'show', stamp + ':' + path).decode().splitlines())
            except (subprocess.CalledProcessError, UnicodeDecodeError):
                cache[path] = None
        count = cache[path]
        if count is None:
            errors.append('missing or non-text Git blob: ' + path)
            continue
        bounds = re.fullmatch(r'L(\d+)(?:-L(\d+))?', parsed.fragment)
        if not bounds:
            errors.append('missing or invalid line range: ' + url)
            continue
        start, end = int(bounds[1]), int(bounds[2] or bounds[1])
        ranges += 1
        if not 1 <= start <= end <= count:
            errors.append(f'{path}: invalid lines {start}..{end}; blob has {count}')
    if not urls:
        errors.append('no immutable GitHub blob links found')
    return errors, {'registered_anchors': len(anchors), 'wiki_citations': citations,
                    'source_files': len(cache), 'line_ranges': ranges}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', help='citation page relative to the wiki root')
    parser.add_argument('--wiki', type=Path, default=Path.cwd())
    parser.add_argument('--repo', type=Path, help='override snapshot-location clone')
    parser.add_argument('--page', type=Path, action='append', default=[],
                        help='include an untracked page (repeatable); otherwise stage new pages first')
    args = parser.parse_args()
    wiki = args.wiki.resolve()
    source = (wiki / args.source).resolve()
    try:
        repo = args.repo or wiki / field(source.read_text(), 'snapshot-location')
        errors, counts = check(wiki, source, repo, [(wiki / p).resolve() for p in args.page])
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print('ERROR:', str(exc), file=sys.stderr)
        return 2
    print(' · '.join(f'{key}={value}' for key, value in counts.items()))
    for error in errors:
        print('FAIL:', error)
    print(f'{len(errors)} error(s); structural checks only, not semantic validation')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
