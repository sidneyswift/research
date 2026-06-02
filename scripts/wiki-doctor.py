#!/usr/bin/env python3
"""wiki-doctor — health check + score for the LLM wiki.

Self-improvement #19 (the gbrain-`doctor` analogue) + #16 (the wiki health score).
It runs the *deterministic* LINT checks — the ones that are same-in/same-out and
so belong in a script rather than burning model judgment (latent-vs-deterministic
split, applied to ourselves). The judgment-heavy LINT checks (contradictions,
"is this concept worth a page", "what to read next") stay with the model.

Usage:
    scripts/wiki-doctor.py              # human report + health score
    scripts/wiki-doctor.py --json       # machine-readable
    scripts/wiki-doctor.py --strict     # exit 1 if score < target or hard failures
    scripts/wiki-doctor.py --target 95  # set the health target (default 90, per gbrain)

It only reports; it does not edit pages. Remediation stays a reviewed step
(REFLECT/LINT discipline) — a doctor that silently rewrites prose is a Foxconn cage.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
FENCED = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`]*`")
DATE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
TODAY = dt.date.today()


def strip_code(text: str) -> str:
    """Drop code spans/fences so illustrative `[[...]]` examples aren't read as live links."""
    return INLINE_CODE.sub("", FENCED.sub("", text))

# Pages excluded from "content" checks (orphans / required sections / staleness).
# Schemas are templates (full of illustrative [[patterns/.../...]] placeholders),
# and the navigation/meta files are entry points, not leaf content.
NAV_FILES = {"index.md", "README.md", "CLAUDE.md", "log.md"}

REQUIRED_SECTIONS = {
    "artifact": ["## Patterns demonstrated", "## What we'd steal"],
    "concept": ["## Patterns demonstrated", "## What we'd steal"],
    "pattern": [
        "## Detection recipe",
        "## Examples in this wiki",
        "## Counter-examples or anti-pattern",
        "## When NOT to use",
    ],
    "source": ["## Anchor map"],
}


def repo_root() -> Path:
    out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True)
    return Path(out.strip())


def tracked_md(root: Path) -> list[str]:
    out = subprocess.check_output(["git", "ls-files", "*.md"], cwd=root, text=True)
    return [p for p in out.splitlines() if p]


def classify(path: str) -> str:
    """Map a path to a page kind, or '' if it's not a checkable content page."""
    if path in NAV_FILES or path.startswith("_schemas/") or Path(path).name == "_index.md":
        return ""
    if path.startswith("sources/"):
        # Top-level citation pages are content; snapshots inside dirs are raw evidence.
        return "source" if path.count("/") == 1 else ""
    if re.match(r"artifacts/(skills|plugins|mcp-servers|projects)/", path):
        return "artifact"
    if path.startswith("concepts/"):
        return "concept"
    if re.match(r"patterns/[^/]+/", path):
        return "pattern"
    return ""


def parse_dates(label: str, text: str) -> list[dt.date]:
    """Extract real dates from `label:` lines, skipping template placeholders."""
    found = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith(label):
            continue
        if "YYYY" in s:  # schema placeholder
            continue
        m = DATE.search(s)
        if m:
            try:
                found.append(dt.date(int(m[1]), int(m[2]), int(m[3])))
            except ValueError:
                pass
    return found


def gitlinks(root: Path) -> list[str]:
    out = subprocess.check_output(["git", "ls-files", "-s", "sources/"], cwd=root, text=True)
    return [ln.split("\t", 1)[1] for ln in out.splitlines() if ln.startswith("160000")]


def main() -> int:
    ap = argparse.ArgumentParser(description="Health check + score for the wiki.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--strict", action="store_true", help="exit 1 on hard failures / low score")
    ap.add_argument("--target", type=int, default=90, help="health-score target (default 90)")
    args = ap.parse_args()

    root = repo_root()
    files = tracked_md(root)
    texts = {p: (root / p).read_text(encoding="utf-8", errors="replace") for p in files}
    tracked = set(files)

    broken: list[str] = []          # "src -> [[target]]"
    inbound: dict[str, int] = {}    # target.md path -> inbound link count
    todos: list[str] = []           # "path:line text"
    stale_reviewed: list[str] = []  # "path (N days)"
    stale_signals: list[str] = []   # "path as-of YYYY-MM-DD (N days)"
    missing: list[str] = []         # "path — missing '## X'"

    for path, text in texts.items():
        # Wikilinks: record inbound counts + flag links whose target file is absent.
        # _schemas templates hold illustrative [[a/.../b]] placeholders — skip them.
        if not path.startswith("_schemas/"):
            for raw in WIKILINK.findall(strip_code(text)):
                # Strip #anchor and |alias (Obsidian); drop doc placeholders.
                target = raw.split("#", 1)[0].split("|", 1)[0].strip().strip('"').strip("'").strip()
                if not target or "..." in target or "<" in target or ">" in target:
                    continue
                tgt_md = target if target.endswith(".md") else target + ".md"
                inbound[tgt_md] = inbound.get(tgt_md, 0) + 1
                if tgt_md not in tracked and not (root / tgt_md).exists():
                    broken.append(f"{path} -> [[{target}]]")

        for i, line in enumerate(text.splitlines(), 1):
            if "TODO" in line:
                todos.append(f"{path}:{i}  {line.strip()[:100]}")

        for d in parse_dates("last-reviewed:", text):
            age = (TODAY - d).days
            if age > 90:
                stale_reviewed.append(f"{path} ({age}d)")
        for d in parse_dates("as-of:", text):
            age = (TODAY - d).days
            if age > 30:
                stale_signals.append(f"{path} as-of {d} ({age}d)")

        kind = classify(path)
        if kind in REQUIRED_SECTIONS:
            for section in REQUIRED_SECTIONS[kind]:
                if section not in text:
                    missing.append(f"{path} — missing '{section}'")

    # Orphans: content pages with zero inbound wikilinks.
    orphans = [
        p for p in files
        if classify(p) and inbound.get(p, 0) == 0
    ]

    links = gitlinks(root)

    # Health score: start at 100, subtract capped penalties. Transparent on purpose.
    def cap(n: int, per: int, limit: int) -> int:
        return min(n * per, limit)

    penalties = {
        "broken_links": cap(len(broken), 5, 30),
        "orphans": cap(len(orphans), 4, 20),
        "missing_sections": cap(len(missing), 4, 24),
        "stale_reviewed": cap(len(stale_reviewed), 1, 10),
        "stale_signals": cap(len(stale_signals), 1, 10),
        "gitlinks": cap(len(links), 10, 20),
    }
    score = max(0, 100 - sum(penalties.values()))

    result = {
        "score": score,
        "target": args.target,
        "pages_checked": len(files),
        "penalties": penalties,
        "findings": {
            "broken_links": broken,
            "orphans": orphans,
            "missing_sections": missing,
            "stale_reviewed": stale_reviewed,
            "stale_signals": stale_signals,
            "gitlinks": links,
            "todo_backlog": todos,
        },
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    hard_fail = bool(broken or links)
    if args.strict and (score < args.target or hard_fail):
        return 1
    return 0


def print_report(r: dict) -> None:
    f = r["findings"]
    bar = "█" * (r["score"] // 5) + "░" * (20 - r["score"] // 5)
    print(f"\n  WIKI HEALTH  {r['score']}/100  [{bar}]   target {r['target']}")
    print(f"  {r['pages_checked']} pages checked · {TODAY}\n")

    def section(title: str, items: list[str], good: str) -> None:
        if items:
            print(f"  ✗ {title} ({len(items)})")
            for it in items[:25]:
                print(f"      {it}")
            if len(items) > 25:
                print(f"      … and {len(items) - 25} more")
        else:
            print(f"  ✓ {good}")

    section("Broken wikilinks", f["broken_links"], "no broken wikilinks")
    section("Orphan pages", f["orphans"], "no orphan pages")
    section("Missing required sections", f["missing_sections"], "all required sections present")
    section("Stray embedded clones (gitlinks)", f["gitlinks"], "no stray clones")
    section("Stale last-reviewed (>90d)", f["stale_reviewed"], "no stale last-reviewed dates")
    section("Stale popularity signals (>30d)", f["stale_signals"], "no stale popularity signals")
    print(f"\n  ℹ TODO / open-question backlog: {len(f['todo_backlog'])} item(s)"
          " (run with --json to list)")
    print("\n  Note: judgment checks (contradictions, DRY/overlap, 'what to read next')"
          " are not automated — run a model-driven LINT for those.\n")


if __name__ == "__main__":
    sys.exit(main())
