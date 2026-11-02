#!/usr/bin/env bash
# Compatibility entry point; setup.sh also supports --only, --check and --pull.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
exec "$root/setup.sh" "$@"
