#!/usr/bin/env bash
# Re-clone every source repo listed in repos.manifest.tsv.
#
# Why this exists: source REPOS are not committed into the wiki (they're large and
# re-clonable); only their .md citation pages are. This script reconstructs the
# local evidence cache on a fresh checkout, pinned to the exact commit we cited.
# Article/docs snapshots are committed and need no reconstruction.
#
# Usage:
#   ./clone-all.sh            # clone any missing repos, pinned to their cited commit
#   ./clone-all.sh --pull     # also `git fetch` existing clones (does NOT move the pin)
#
# Updating to a newer upstream is a deliberate RE-INGEST (see CLAUDE.md), not this script:
# pulling can break line-anchored citations, so it must be reviewed and the manifest bumped.

set -euo pipefail

cd "$(dirname "$0")"
manifest="repos.manifest.tsv"
do_pull=false
[[ "${1:-}" == "--pull" ]] && do_pull=true

# Skip the header row, then read slug / url / commit from each tab-separated line.
tail -n +2 "$manifest" | while IFS=$'\t' read -r slug url commit; do
  [[ -z "${slug:-}" ]] && continue

  if [[ -d "$slug/.git" ]]; then
    echo "✓ $slug already cloned"
    if $do_pull; then
      echo "  fetching upstream (pin unchanged at $commit)…"
      git -C "$slug" fetch --quiet origin || echo "  (fetch failed — offline?)"
    fi
    continue
  fi

  echo "→ cloning $slug from $url …"
  # Keep .git so the clone is pull-able; we are NOT stripping it (Option B).
  git clone --quiet "$url" "$slug"
  echo "  checking out cited commit $commit …"
  git -C "$slug" checkout --quiet "$commit"
done

echo "Done. Source repos are local-only evidence; the wiki tracks their .md citation pages."
