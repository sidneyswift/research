#!/usr/bin/env bash
# Restore the research evidence cache on a local or remote checkout.
set -euo pipefail
root="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$root/scripts/restore-sources.py" "$@"
