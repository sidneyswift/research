---
domain: sources
type: docs-page
url: https://platform.claude.com/docs/en/managed-agents/memory
retrieved: 2026-11-07
snapshot-location: sources/anthropic--agent-memory-support/
last-reviewed: 2026-11-07
---

# Anthropic agent memory — supporting contracts and examples

## Snapshot details

- **Version:** living documentation captured November 7, 2026; quickstart README pinned to `4a4224bdf0e9cfb3332167b69c90457403813625`.
- **Preserved:** eleven hash-verified files, including original cookbook HTML. Not a complete source checkout.
- **Read scope:** Dreams/store lifecycle and access prose plus representative request examples; full self-hosted sync/conflict prose; selected Claude Code auto-memory and memory-tool handler/security sections; dynamic cookbook overview, prompts, adoption and nightly lifecycle; complete quickstart README and Google Sleep blog. Not every SDK language variant, linked page or notebook cell.
- **Evidence class:** documented behavior and author-reported examples. No sessions/dreams invoked, no installed tools changed and no benchmarks reproduced. The CL-Bench release is a partial capture. Raw source remains unedited; this citation map owns interpretation.


## Anchor map

### root

[Capture receipt](anthropic--agent-memory-support/capture.json) and [coverage](anthropic--agent-memory-support/coverage.json): eleven files. Full text captured for seven supporting pages, plus title-only CL-Bench release, cookbook original HTML, pinned quickstart README and its license. Eight fetched page captures total, not eight fully reviewed documentation corpora.

### dream-lifecycle

[Dreams](anthropic--agent-memory-support/dreams.md): research preview; input store plus 1–100 session IDs; asynchronous clone into a distinct output store, input unchanged. Pending/running/completed/failed/canceled. Running may briefly lack a store ID; a returned ID does not establish completion. Failed/canceled output can be partial. Adopt output explicitly in future sessions after inspection.

### dream-cancellation

Dreams sections on cancel/archive/errors: cancel pending/running; repeated cancellation idempotent, terminal completed/failed cancellation invalid. In-flight work may continue briefly and add usage. Terminal-only dream archival is irreversible, leaves status/output store intact and hides default listing, not deletion. Deleting/archiving inputs during a run can cause failure.

### dream-cost

Dreams usage/limits: standard token pricing, input-size sensitivity, test a small representative set before scaling. Terminal session archival is not deletion. Stateful Managed Agents/Dreams have different data-handling eligibility from client-owned Messages memory.

### store-access

[Managed memory](anthropic--agent-memory-support/managed-memory.md): workspace-scoped text collections, up to eight mounts/session, read_write default, explicit read_only for references. Hosted read-only enforcement is filesystem-level; shared cloud changes visible nearly immediately. Tool events record reads/writes; tenant/user/topic partitioning is an application design choice.

### store-versions

Managed memory mutation/audit sections: immutable memory versions, content_sha256 optimistic preconditions, re-read on mismatch. Versions retained 30 days with newest live version retained beyond that if needed; deleting a memory does not automatically delete its version history. Recovery reads an old version then writes it back; redaction removes historical content but preserves metadata, and current head must be updated/deleted first.

### store-lifecycle

Managed memory limits/maintenance: 10k memories/store; new writes fail at cap, existing content remains readable/editable. Archive read-only/no new attachments/no unarchive; deletion removes store/history. Current memory-store request header agent-memory-2026-07-22 must not be combined with managed-agents-2026-04-01; session attachments use the latter. Record API surface rather than copy all beta headers everywhere.

### self-hosted-sync

[Self-hosted stores](anthropic--agent-memory-support/self-hosted-memory.md): local copy, not live mount. Sync after tool calls, at most once per interval (default 15s, minimum 5); visibility needs both workers to sync. Final sync up to 30s then cleanup. Killed worker loses unsynced edits and can leave directories. Shared store requires separate per-session filesystems because mount paths collide; marker must remain intact.

### self-hosted-conflicts

Self-hosted Read-only stores and conflicts: store wins conflict, overwrites local edit and logs warning; write/edit may have succeeded with no error shown to agent. Those tools block read_only writes, but bash/custom tools can alter local copies; worker never uploads them. Read-only remote persistence is not local filesystem immutability. POSIX/O_NOFOLLOW required; case-sensitive filesystem recommended.

### self-hosted-controls

Self-hosted options: disabled memory support can leave prompt descriptions without actual mounted memory. Deletion modes enabled/log_only/disabled change delete propagation, not uploads/downloads. Default deletes require a later confirming sync. Platform restrictions and host preparation are documented, not exercised here.

### client-memory

[Memory tool](anthropic--agent-memory-support/memory-tool.md), architecture/security/commands: client implements storage and validates every requested path, including canonical containment; /memories is logical namespace, not an automatic filesystem boundary. Reject root deletion; enforce content/size limits in handler. Demonstration in-memory SDK handlers are not complete persistence/security implementations.

### code-injection

[Claude Code memory](anthropic--agent-memory-support/code-memory.md): auto MEMORY.md loads first 200 lines or 25 KB, whichever first; topic files on demand. Oversized index writes can succeed while excess is not loaded next session. This is not the CLAUDE.md hard limit. Main auto memory is not normally loaded into subagents; forks inherit parent context. Both learned memory and written guidance are context, not enforceable action policy.

### code-retention

Claude Code Auto memory: repo/worktrees share machine-local memory; not automatically synced across hosts. Transcript retention sweep excludes memory files; deleting old session logs does not retire derived notes. File timestamps show modification, not independent verification.

### dynamic-workflow

[Dynamic dreaming cookbook](anthropic--agent-memory-support/dynamic-dreaming.txt): lead delegates one analyzer/transcript in groups of about twenty, then organizer after analysis. Verifies evidence, preserves exact identifiers, downgrades uncertain claims, retains dated conflicts; targeted edits/readback during concurrency, merges/renames only after writers finish. Prompt policy, not a verified atomic concurrency guarantee.

### dynamic-trust

Cookbook safety/adoption: analyzers get five file tools, no shell/web, empty network allowlist, unattended approval pauses declined; transcripts and memory treated as untrusted data. These are documented controls, not tested by us. Read-only consumers still ingest potentially poisoned text. Optional 4,096-character mount instructions move memory text into system context; review first.

### dynamic-nightly

Cookbook Dream every night: creates or reuses a store; nightly script modifies it in place with no review, unlike built-in Dreams clone-and-adopt. Saves pre-run copy; failed run retains window for retry. Creation-time window exports only idle/terminated sessions: running sessions and later turns can be missed. Manual lookback also reprocesses other sessions. Notebook cache contains private text and has no automatic purge; default temporary records need durable export.

### dynamic-fidelity

Readable cookbook extraction loses code indentation. [Original HTML](anthropic--agent-memory-support/dynamic-dreaming.html) retained; no notebook/helper-module execution or full source audit. Reviewed workflow prose, prompts and displayed nightly logic, not every output cell. Completion checks distinguish processed inputs, agent failures and organizer completion; a report alone is not semantic validation.

### knowledge-wiki

[Quickstart README](anthropic--agent-memory-support/knowledge-wiki-readme.md) pinned to anthropics/claude-quickstarts 4a4224bdf0e9cfb3332167b69c90457403813625; [license](anthropic--agent-memory-support/quickstarts-LICENSE). Build→extract→resolve gaps→analyze→organize, then read-only question sessions. Preserves provenance, conflicting bases and superseded figures; synthetic documents marked. Only README inspected, not whole repo or recorded notebook.

### quickstart-boundaries

Pinned README reports ~$19 average build/$16 recorded, ~240-question breakeven versus its larger-model search baseline, ~1/15 answer price and within one point. These are benchmark/model/corpus-specific and not the article Stainless experiment. README explicitly accepts ~5% line loss on busiest shared entity page from overwrites. Do not transfer article per-contract 57/57 retention into a guarantee about this quickstart.

### sleep-contrast

[Google Sleep blog](anthropic--agent-memory-support/sleep.md): wake/sleep scheme updates preallocated MoE memory weights through distillation/training, with synthetic dream data. Same label, different mechanism from Anthropic external-context memory. Blog reviewed for mechanism distinction; papers/results not independently evaluated.

### incomplete-context

[CL-Bench release capture](anthropic--agent-memory-support/cl-bench.md) contains only title/byline/date, not methodology. Do not cite it as external corroboration of the article results. Other unreviewed linked research/media listed in coverage.

## Why we cite this

External-memory selection, consolidation, evaluation, adoption and runtime boundaries. Described results and product contracts are not independent replication.

## Popularity signals

Primary Anthropic publication/documentation, captured 2026-11-07. No adoption or popularity count asserted.

## Related sources

- [[sources/anthropic--components-of-agent-memory]] — motivating research report.
- [[sources/anthropic--dynamic-workflows]] — earlier orchestration research; current examples have narrower inspected scope.
