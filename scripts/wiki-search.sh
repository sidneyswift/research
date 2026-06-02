#!/usr/bin/env bash
# wiki-search.sh — search the wiki's markdown pages.
#
# Grep-based, zero-dependency. This is the cheap first cut of self-improvement
# #18 (a local search tool); a future version may swap in embeddings/qmd, but
# at ~70 pages plain grep over the git file list is plenty. Searching git-tracked
# files automatically excludes the git-ignored source repo clones.
#
# Usage:
#   scripts/wiki-search.sh "skillify"          # wiki pages, grouped by page + title
#   scripts/wiki-search.sh -s "resolver"       # also search sources/ (citation pages + snapshots)
#   scripts/wiki-search.sh -l "ratchet"        # list matching file paths only
#
# Query is treated as a case-insensitive extended regex (ERE).

set -euo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"

include_sources=false
files_only=false
while getopts "sl" opt; do
  case "$opt" in
    s) include_sources=true ;;
    l) files_only=true ;;
    *) echo "usage: wiki-search.sh [-s] [-l] <query>" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))
[ $# -ge 1 ] || { echo "usage: wiki-search.sh [-s] [-l] <query>" >&2; exit 2; }
query="$*"

# Tracked markdown only (ignored repo clones never appear here). Drop sources/
# unless -s, so a search defaults to the analysis layer, not the raw evidence.
file_list="$(git ls-files '*.md')"
if ! $include_sources; then
  file_list="$(printf '%s\n' "$file_list" | grep -v '^sources/' || true)"
fi
[ -n "$file_list" ] || { echo "(no pages to search)"; exit 0; }

# -l: just the file paths that match.
if $files_only; then
  printf '%s\n' "$file_list" | tr '\n' '\0' | xargs -0 grep -liE -- "$query" || {
    echo "no matches for: $query"; exit 1; }
  exit 0
fi

# Default: group matches by file, printing the page's H1 title as a header.
matched_files="$(printf '%s\n' "$file_list" | tr '\n' '\0' | xargs -0 grep -liE -- "$query" || true)"
[ -n "$matched_files" ] || { echo "no matches for: $query"; exit 1; }

count=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  count=$((count + 1))
  title="$(grep -m1 '^# ' "$f" | sed 's/^# //' || true)"
  printf '\n\033[1m%s\033[0m  — %s\n' "$f" "${title:-(no title)}"
  grep -niE -- "$query" "$f" | sed 's/^/    /'
done <<EOF
$matched_files
EOF

printf '\n%s page(s) matched "%s"\n' "$count" "$query"
