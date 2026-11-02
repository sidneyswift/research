#!/usr/bin/env python3
"""Restore pinned source clones without changing existing worktrees."""
import argparse
import csv
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def git(*args, cwd=None):
    return subprocess.check_output(
        ["git", *map(str, args)], cwd=cwd, text=True, stderr=subprocess.PIPE
    ).strip()


def evidence_revisions(row):
    value = row.get("evidence_commits") or ""
    return [] if value in ("", "-") else value.split(",")


def load_manifest(path):
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames not in (["slug", "url", "commit"], ["slug", "url", "commit", "evidence_commits"]):
            raise ValueError("Manifest must have slug, url, commit columns, optionally evidence_commits")
        rows = list(reader)
    seen = set()
    for row in rows:
        slug, url, commit = row["slug"], row["url"], row["commit"]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", slug or ""):
            raise ValueError(f"Invalid source slug: {slug!r}")
        if slug in seen:
            raise ValueError(f"Duplicate source slug: {slug}")
        seen.add(slug)
        if not url or url.startswith("-") or not re.fullmatch(r"[0-9a-f]{40}", commit or ""):
            raise ValueError(f"Invalid URL or full commit SHA for {slug}")
        for revision in evidence_revisions(row):
            if not re.fullmatch(r"[0-9a-f]{40}", revision):
                raise ValueError(f"Invalid evidence commit for {slug}")
    return rows


def ensure_evidence(row, checkout, check=False):
    for revision in evidence_revisions(row):
        try:
            git("cat-file", "-e", revision + "^{commit}", cwd=checkout)
        except subprocess.CalledProcessError:
            if check:
                raise ValueError(f"{row['slug']}: missing historical evidence revision {revision}")
            git("fetch", "--quiet", "--depth=1", row["url"], revision, cwd=checkout)


def restore(row, source_dir, check=False, pull=False):
    slug, url, pin = (row[key] for key in ("slug", "url", "commit"))
    destination = source_dir / slug
    if destination.exists() or destination.is_symlink():
        # Do not mistake a plain directory inside the parent wiki for a clone.
        if destination.is_symlink() or not (destination / ".git").exists():
            raise ValueError(f"{slug}: existing path is not an independent Git checkout; left unchanged")
        head = git("rev-parse", "HEAD", cwd=destination)
        if head != pin:
            raise ValueError(f"{slug}: HEAD {head} differs from pin {pin}; left unchanged")
        dirty = bool(git("status", "--porcelain", cwd=destination))
        if pull and not check:
            # Use the manifest URL: a preserved fork can differ from local origin.
            git("fetch", "--quiet", url, pin, cwd=destination)
        ensure_evidence(row, destination, check=check)
        print(f"OK {slug} @ {pin[:12]}" + (" (local changes preserved)" if dirty else ""))
        return
    if check:
        raise ValueError(f"{slug}: missing; run ./setup.sh to restore")
    source_dir.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".restore-", dir=source_dir))
    try:
        git("init", "--quiet", temporary)
        git("remote", "add", "origin", url, cwd=temporary)
        git("fetch", "--quiet", "--depth=1", "origin", pin, cwd=temporary)
        git("-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", pin, cwd=temporary)
        if git("rev-parse", "HEAD", cwd=temporary) != pin:
            raise ValueError(f"{slug}: fetched revision did not match pin")
        ensure_evidence(row, temporary)
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"{slug}: destination appeared during restore; left unchanged")
        temporary.rename(destination)
        print(f"RESTORED {slug} @ {pin[:12]}")
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", metavar="SLUG", help="restore only these manifest entries")
    parser.add_argument("--check", action="store_true", help="check existing pins offline; change nothing")
    parser.add_argument("--pull", action="store_true", help="fetch pinned objects; never move existing HEAD")
    parser.add_argument("--manifest", type=Path, default=root / "sources/repos.manifest.tsv")
    parser.add_argument("--sources-dir", type=Path, default=root / "sources")
    args = parser.parse_args()
    try:
        rows = load_manifest(args.manifest)
        if args.only:
            unknown = set(args.only) - {row["slug"] for row in rows}
            if unknown:
                raise ValueError("Unknown source(s): " + ", ".join(sorted(unknown)))
            rows = [row for row in rows if row["slug"] in args.only]
    except (ValueError, OSError) as error:
        parser.error(str(error))
    failures = []
    for row in rows:
        try:
            restore(row, args.sources_dir, check=args.check, pull=args.pull)
        except (ValueError, OSError, subprocess.CalledProcessError) as error:
            detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
            failures.append(row["slug"])
            print(f"ERROR {row['slug']}: {detail}")
    print(f"{len(rows) - len(failures)}/{len(rows)} sources ready; no source applications or dependencies executed.")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
