# Local and remote research setup

This research repository serves work across projects. Its canonical local location is `Projects/Research`; its GitHub repository remains `sidneyswift/research`.

## Start a remote workspace

```bash
git clone https://github.com/sidneyswift/research.git Research
cd Research
./setup.sh
```

Requirements: Git, Python 3, network access, and credentials for any private source repositories. The setup command restores all entries in [the source manifest](sources/repos.manifest.tsv) as shallow Git checkouts at full commit SHAs. Optional `evidence_commits` entries (`-` means none) fetch historical Git objects needed by older citations without moving the checkout. It downloads evidence; it does not install dependencies, run agents, connect provider accounts, or deploy applications. Credentials and local `.env` files are not reconstructed.

In a remote workspace that supports a startup/setup command, configure `./setup.sh` from the repository root. Cloning the research repository alone does not run setup automatically.

For a smaller task, restore only the relevant sources:

```bash
./setup.sh --only humanlayer--humanlayer cursor--plugins-pstack
./setup.sh --only googleads--google-ads-mcp
```

Inspect source availability without network access or mutations:

```bash
./setup.sh --check
```

The original entry point, `sources/clone-all.sh`, forwards the same options. `--pull` fetches pinned objects without changing an existing checkout's HEAD. Existing checkouts at a different revision are reported as errors and left unchanged; local edits at the expected revision are reported and preserved. Review revision changes deliberately rather than resetting evidence or moving pins automatically.

## What GitHub preserves

| Material | Storage |
| --- | --- |
| Research pages, draft analyses, citations, scripts | Tracked in this repository |
| Captured articles and documentation | Tracked immutable snapshots |
| Public source repositories | Ignored local clones; restored from manifest URL and commit |
| Modified Google Ads MCP source | Preserved branch in `sidneyswift/google-ads-mcp`; manifest points at that fork's commit |
| Purchased PM OS material | Ignored local evidence; restore separately from an authorized purchase |
| Credentials, dependencies, caches, local configuration | Local only; configure separately if needed |

Do not ignore all of `sources/`: it also contains tracked citation pages and evidence snapshots. Add each new clone directory to `.gitignore` and its exact source URL and full commit SHA to the manifest. Preserve unique code in a controlled fork before recording its revision. Clone membership alone does not establish that a project has been fully researched or tested.

## Sources consolidated on 2026-11-02

The former standalone `Projects/Sources` collection now uses the wiki's existing source naming convention:

| Former folder | Canonical source directory | Reconciliation |
| --- | --- | --- |
| `cursor-plugins` | `sources/cursor--plugins-pstack/` | Identical working files and matching revision; one canonical copy |
| `humanlayer` | `sources/humanlayer--humanlayer/` | Identical working files and matching revision; one canonical copy |
| `executor` | `sources/rhys-sullivan--executor/` | Moved intact; exact revision added to manifest |
| `google-ads-mcp` | `sources/googleads--google-ads-mcp/` | Existing Vercel hosting changes saved in Sidney's fork |
| `hermes-agent` | `sources/nousresearch--hermes-agent/` | Moved intact; exact revision added to manifest |
| `open-agents-main` | `sources/vercel-labs--open-agents/` | Every file, mode and symlink matched upstream commit `cf865e94de7729751c747171785b6ce57e7b178c`; Git metadata restored |
| `openclaw` | `sources/openclaw--openclaw/` | Moved intact; exact revision added to manifest |

The Google Ads fork's `research/vercel-snapshot-20261102` branch preserves the five pre-existing local changes. This records those files, not a claim that the hosting configuration works. Original upstream remains the local checkout's `origin`; the restore script uses the fork URL in the manifest.

Old local paths remain compatible: `Projects/Sidney/research` links to `Projects/Research`; the former `Projects/Sources` directory contains only compatibility links and a notice. Source aliases inside the cache preserve old names. These local migration links are not needed on a fresh remote checkout. New work should use the canonical Research path and source names.

The two removed duplicate checkouts had byte-identical working files. Their Git refs and histories were saved as local bundles under ignored `scratch/source-migration-20261102/`, with a migration receipt. The research folder was moved intact, including existing uncommitted draft studies. No source applications were run as part of the move.

Gstack already had two research revisions before this move: the older wiki cites `029356e`, while the existing draft engineering-skill inventory uses `c7ae632`. Its manifest now restores the latter checkout and also fetches the former as historical evidence. Older citation pages remain anchored to their original revision.

## Maintaining and checking setup

```bash
python3 -m unittest discover -s scripts/tests -p 'test_restore_sources.py'
./setup.sh --check
```

The restoration tests use temporary local repositories and do not require provider access. They check exact pins, repeat setup, preservation of local edits, mismatched revisions, partial-download cleanup, manifest validation, and selective restoration.

The manifest depends on the recorded repositories and commits remaining accessible. A shallow checkout contains the pinned source, not every historical branch. Fetch additional history within a source clone when a research task requires it. Purchased evidence remains an explicit manual prerequisite rather than an undisclosed public upload.
