---
domain: sources
type: repo
url: https://github.com/pingdotgg/t3code
retrieved: 2026-11-07
snapshot-location: sources/pingdotgg--t3code/
upstream-commit: 33f85846be8bc4bc592f0e621d6f0313e5abd4a4
last-reviewed: 2026-11-07
---

# T3 Code — shared services, durable orchestration and agent authority

## Snapshot details

- **Pinned revision:** `33f85846be8bc4bc592f0e621d6f0313e5abd4a4`, committed2026-11-07 10:45:07+05:30, “fix(server): t3 service install no longer moves a --base-dir service onto an empty ~/.t3 (#23878)”.
- **Preservation:** live shallow Git clone with `.git` intact, ignored from the wiki; full tree contains31,763tracked files, including large third-party reference trees. Restore with `./setup.sh --only pingdotgg--t3code`; `--check --only pingdotgg--t3code` verified the pin and clean working tree. Upstream source availability is required; this is not an independent archival mirror.
- **Committed evidence:** [review-inventory.json](pingdotgg--t3code-evidence/review-inventory.json) holds hashes/bytes/line counts for77cited files; [anchors.json](pingdotgg--t3code-evidence/anchors.json) holds66anchors/173source ranges; [github-metadata.json](pingdotgg--t3code-evidence/github-metadata.json) preserves the bounded attention/license metadata.
- **Reading scope:** domain service conventions and concrete project creation; EventSink/outbox/workers/recovery/finalization; checkpoint/diff/restore; scoped RPC/MCP/provider permissions and remote/session/asset access; shared client cache/cursor lifecycle; structured context/handoff and engineering/test/eval instructions. Source ranges below identify actual claim evidence; large files were selectively inspected. File counts are preservation inventory, not exhaustive-review claims.
- **Excluded:** complete native/mobile/rendering/relay implementation, vendor reference trees, full test suite, every provider integration and independent security/performance audit. Some remote/policy/test-workflow statements remain documentation-level.
- **Executed:** clone, pin/clean-state and source/wiki structural checks only. No T3 dependency install, startup, provider/model call, OAuth, tunnel, Git restore/checkpoint, migration, application test, build or paid eval. Source `AGENTS.md`, skills and shell examples were treated as evidence, never operational instructions.

## Popularity signals

GitHub API retrieved2026-11-07: **50,046stars; 9,769forks; 108watchers**. Attention, not active-user, quality, isolation or success evidence. GitHub identifies `pingdotgg` as the Ping.gg organization. MIT license; source server package declares0.1.7, not a verified published release. The source harness's own user-count claim was not independently validated or adopted as an observed metric.

## Anchor map

### root

- [README.md L1–L48](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/README.md#L1-L48) — Project identity, provider prerequisites and distribution; not installation verified.
- [LICENSE L1–L21](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/LICENSE#L1-L21) — MIT license.
- [apps/server/package.json L1–L16](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/package.json#L1-L16) — Checked-in package identity/version0.1.7, not release verification.

### service-reach

- [docs/internals/effect-services.md L1–L34](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/effect-services.md#L1-L34) — Published service ownership, transport adapters and reach across clients/MCP/jobs.
- [apps/server/src/ws.ts L2892–L2918](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/ws.ts#L2892-L2918) — Named project handler delegates to managed service; clone start/cancel/retry/stream entrypoints.
- [apps/server/src/project/ManagedProjectFolders.ts L422–L459](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/project/ManagedProjectFolders.ts#L422-L459) — Concrete composite service, ownership-aware compensation, partial commitError result.

### service-partial-success

- [apps/server/src/project/ManagedProjectFolders.ts L378–L459](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/project/ManagedProjectFolders.ts#L378-L459) — Repository scaffold, Git commit failure retained as warning, owner check before cleanup.
- [apps/server/src/ws.ts L2855–L2890](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/ws.ts#L2855-L2890) — Clone transport still injects callbacks/enrichment; prescribed thin-handler rule is not universal implementation.

### service-errors

- [docs/internals/effect-services.md L124–L154](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/effect-services.md#L124-L154) — Structured safe error attributes, bounded diagnostics exception and transport translation; prescribed practice.
- [apps/server/src/project/ManagedProjectFolders.ts L28–L85](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/project/ManagedProjectFolders.ts#L28-L85) — Concrete tagged errors keep fixed public messages and causes.

### client-consistency

- [docs/internals/connection-runtime.md L1–L76](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/connection-runtime.md#L1-L76) — Shared environment connection owner; retry vs renewal vs data freshness.
- [docs/internals/connection-runtime.md L78–L132](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/connection-runtime.md#L78-L132) — Partial shell membership, generations, cache/cursor lifetime, no automatic mutation replay.
- [packages/client-runtime/src/state/threads.ts L278–L305](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/client-runtime/src/state/threads.ts#L278-L305) — Applied state and sequence remembered with cache owner check.
- [packages/client-runtime/src/state/threads.ts L421–L449](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/client-runtime/src/state/threads.ts#L421-L449) — Atomic projection/history update to avoid lost concurrent paging state.

### typed-context

- [packages/contracts/src/composerContext.ts L15–L67](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/contracts/src/composerContext.ts#L15-L67) — Context kinds, identity and bounds.
- [packages/contracts/src/composerContext.ts L230–L265](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/contracts/src/composerContext.ts#L230-L265) — Unknown-kind bounded JSON, distinct known union.
- [packages/contracts/src/composerContext.ts L283–L300](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/contracts/src/composerContext.ts#L283-L300) — Record count/serialized bounds and forward-compatible decoding.
- [packages/shared/src/composerContextReferences.ts L225–L258](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.ts#L225-L258) — Escaping envelope structure, not semantic injection prevention.
- [packages/shared/src/composerContextReferences.ts L361–L406](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.ts#L361-L406) — Repeated refs deduped, duplicate identity unavailable, record kind authoritative.
- [packages/shared/src/composerContextReferences.test.ts L262–L365](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.test.ts#L262-L365) — Tests inspected for escaping, ID semantics, lazy thread references and duplicate ambiguity; not executed.

### context-documentation-drift

- [docs/internals/composer-context-references.md L58–L71](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/composer-context-references.md#L58-L71) — Prose says mention/skill marker without entry.
- [packages/shared/src/composerContextReferences.test.ts L280–L307](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.test.ts#L280-L307) — Current tests expect skill and mention envelope payload, contrary to older prose.

### update-activation

- [docs/internals/server-updates.md L1–L64](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/server-updates.md#L1-L64) — Launcher authority, prepared/committed/ready, database/file rollback boundary, client correlation.
- [apps/server/src/serviceLauncher.ts L691–L741](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/serviceLauncher.ts#L691-L741) — Persist pending before acknowledgement, validate trial identity/version then commit state before child release.
- [apps/server/src/serverActivation.ts L1–L29](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/serverActivation.ts#L1-L29) — Park fibers until activation when gate supplied; ordinary launch no gate.
- [apps/server/src/serviceLauncher.test.ts L259–L309](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/serviceLauncher.test.ts#L259-L309) — Inspected subprocess trial flow assertions, not executed.

### architecture-documentation-drift

- [docs/internals/overview.md L45–L81](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/overview.md#L45-L81) — Current overview describes implemented transaction/outbox, retained receipts and pruning limits.
- [docs/orchestration-v2/README.md L1–L12](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/orchestration-v2/README.md#L1-L12) — Target architecture framing.
- [docs/orchestration-v2/README.md L121–L166](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/orchestration-v2/README.md#L121-L166) — Durable outbox still described as conditional follow-up.

### rt-atomic-intent

- [apps/server/src/orchestration-v2/EventSink.ts L665–L740](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EventSink.ts#L665-L740) — Persist accepted intent atomically with the work it entails
- [apps/server/src/orchestration-v2/EventSink.ts L285–L311](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EventSink.ts#L285-L311) — Persist accepted intent atomically with the work it entails

### rt-publication-order

- [apps/server/src/orchestration-v2/EventSink.ts L267–L311](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EventSink.ts#L267-L311) — Serialize publication as well as database mutation

### rt-receipt-identity

- [apps/server/src/orchestration-v2/Orchestrator.ts L13767–L13790](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.ts#L13767-L13790) — Bind idempotency receipts to their intended aggregate
- [apps/server/src/orchestration-v2/Orchestrator.ts L13998–L14013](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.ts#L13998-L14013) — Bind idempotency receipts to their intended aggregate
- [apps/server/src/orchestration-v2/Orchestrator.receipt-race.test.ts L47–L111](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.receipt-race.test.ts#L47-L111) — Bind idempotency receipts to their intended aggregate
- [apps/server/src/orchestration-v2/Orchestrator.receipt-race.test.ts L150–L165](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.receipt-race.test.ts#L150-L165) — Bind idempotency receipts to their intended aggregate

### rt-lock-order

- [apps/server/src/orchestration-v2/Orchestrator.ts L14044–L14090](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.ts#L14044-L14090) — Keep lock ordering explicit across parent/child mutations

### rt-delivery-liveness

- [apps/server/src/orchestration-v2/EventSink.ts L245–L282](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EventSink.ts#L245-L282) — Separate durable state from transient delivery channels
- [apps/server/src/orchestration-v2/EffectWorker.ts L885–L940](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L885-L940) — Separate durable state from transient delivery channels

### rt-replay-classification

- [apps/server/src/orchestration-v2/EffectOutbox.ts L125–L156](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectOutbox.ts#L125-L156) — Classify effects by replay safety after process loss
- [apps/server/src/orchestration-v2/EffectOutbox.ts L487–L518](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectOutbox.ts#L487-L518) — Classify effects by replay safety after process loss

### rt-ambiguous-settlement

- [apps/server/src/orchestration-v2/EffectWorker.ts L659–L738](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L659-L738) — Separate pre-execution failure from post-execution settlement failure
- [apps/server/src/orchestration-v2/EffectWorker.ts L794–L806](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L794-L806) — Separate pre-execution failure from post-execution settlement failure
- [apps/server/src/orchestration-v2/EffectWorker.test.ts L325–L394](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.test.ts#L325-L394) — Separate pre-execution failure from post-execution settlement failure

### rt-cancellation-race

- [apps/server/src/orchestration-v2/EffectWorker.ts L758–L806](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L758-L806) — Close the cancellation registration/read race
- [apps/server/src/orchestration-v2/EffectWorker.test.ts L396–L456](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.test.ts#L396-L456) — Close the cancellation registration/read race

### rt-retry-order

- [apps/server/src/orchestration-v2/EffectOutbox.ts L313–L352](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectOutbox.ts#L313-L352) — Use retry timing as an ordering constraint, not only a delay
- [apps/server/src/orchestration-v2/EffectOutbox.ts L520–L548](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectOutbox.ts#L520-L548) — Use retry timing as an ordering constraint, not only a delay

### rt-bounded-stop

- [apps/server/src/orchestration-v2/EffectWorker.ts L581–L599](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L581-L599) — Bound hanging control operations to preserve queue liveness
- [apps/server/src/orchestration-v2/EffectWorker.ts L648–L649](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L648-L649) — Bound hanging control operations to preserve queue liveness
- [apps/server/src/orchestration-v2/EffectWorker.ts L809–L833](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L809-L833) — Bound hanging control operations to preserve queue liveness
- [apps/server/src/orchestration-v2/EffectWorker.ts L885–L901](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.ts#L885-L901) — Bound hanging control operations to preserve queue liveness
- [apps/server/src/orchestration-v2/EffectWorker.test.ts L172–L216](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EffectWorker.test.ts#L172-L216) — Bound hanging control operations to preserve queue liveness

### rt-lost-callbacks

- [apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts L241–L280](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts#L241-L280) — Reconcile lost callbacks differently from durable questions
- [apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts L497–L525](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts#L497-L525) — Reconcile lost callbacks differently from durable questions

### rt-restart-continuation

- [apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts L215–L239](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts#L215-L239) — Record restart continuation as new durable work
- [apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts L805–L870](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderRuntimeRecoveryService.ts#L805-L870) — Record restart continuation as new durable work

### rt-finalization

- [apps/server/src/orchestration-v2/RunFinalizationService.ts L58–L87](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/RunFinalizationService.ts#L58-L87) — Separate provider completion from finalization and display refresh
- [apps/server/src/orchestration-v2/RunFinalizationQueue.test.ts L25–L38](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/RunFinalizationQueue.test.ts#L25-L38) — Separate provider completion from finalization and display refresh
- [apps/server/src/orchestration-v2/RunFinalizationQueue.test.ts L100–L131](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/RunFinalizationQueue.test.ts#L100-L131) — Separate provider completion from finalization and display refresh

### rt-stale-enrichment

- [apps/server/src/orchestration-v2/RunFinalizationService.ts L103–L127](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/RunFinalizationService.ts#L103-L127) — Guard delayed enrichment against newer work

### rt-pruned-history

- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L41–L45](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L41-L45) — Define what remains authoritative after history pruning
- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L121–L145](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L121-L145) — Define what remains authoritative after history pruning
- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L255–L299](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L255-L299) — Define what remains authoritative after history pruning
- [docs/internals/overview.md L65–L81](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/overview.md#L65-L81) — Explicit inability to rebuild projections from retained event history.

### rt-compaction-references

- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L73–L116](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L73-L116) — Preserve reference integrity during compaction, including concurrent writers
- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L146–L183](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L146-L183) — Preserve reference integrity during compaction, including concurrent writers
- [apps/server/src/orchestration-v2/ProjectionMaintenance.test.ts L248–L301](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.test.ts#L248-L301) — Preserve reference integrity during compaction, including concurrent writers
- [apps/server/src/orchestration-v2/ProjectionMaintenance.test.ts L305–L335](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.test.ts#L305-L335) — Preserve reference integrity during compaction, including concurrent writers

### rt-dedup-lifetime

- [apps/server/src/orchestration-v2/ProjectionMaintenance.ts L222–L256](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProjectionMaintenance.ts#L222-L256) — Keep deduplication lifetime distinct from replay lifetime
- [apps/server/src/orchestration-v2/EventSink.ts L649–L662](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/EventSink.ts#L649-L662) — Keep deduplication lifetime distinct from replay lifetime

### rt-bounded-reconnect

- [apps/server/src/orchestration-v2/ThreadStream.ts L18–L44](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ThreadStream.ts#L18-L44) — Bound reconnect recovery by actual payload costs
- [apps/server/src/orchestration-v2/ThreadStream.ts L52–L84](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ThreadStream.ts#L52-L84) — Bound reconnect recovery by actual payload costs
- [apps/server/src/orchestration-v2/ThreadStream.ts L99–L118](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ThreadStream.ts#L99-L118) — Bound reconnect recovery by actual payload costs

### rt-rollback-boundary

- [apps/server/src/orchestration-v2/CheckpointRollbackService.ts L147–L173](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRollbackService.ts#L147-L173) — Treat rollback as coordinated provider and workspace state, with limits
- [apps/server/src/orchestration-v2/CheckpointRollbackService.ts L237–L292](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRollbackService.ts#L237-L292) — Treat rollback as coordinated provider and workspace state, with limits

### rt-context-handoff

- [apps/server/src/orchestration-v2/ContextHandoffService.ts L348–L353](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffService.ts#L348-L353) — Model context transfer as an inspectable, bounded artifact
- [apps/server/src/orchestration-v2/ContextHandoffService.ts L495–L560](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffService.ts#L495-L560) — Model context transfer as an inspectable, bounded artifact

### rt-provider-transition

- [apps/server/src/orchestration-v2/ProviderSwitchService.ts L73–L112](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderSwitchService.ts#L73-L112) — Plan provider transitions from negotiated capabilities and identity
- [apps/server/src/orchestration-v2/ProviderSwitchService.ts L113–L160](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ProviderSwitchService.ts#L113-L160) — Plan provider transitions from negotiated capabilities and identity

### auth-authority-model

- [docs/internals/environment-auth.md L7–L28](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/environment-auth.md#L7-L28) — Effective authority and delegate narrowing; shell/full-agent authority can mint sessions.
- [apps/server/src/auth/http.ts L443–L461](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/http.ts#L443-L461) — Pairing delegation checks issuing session access:write and every delegated scope.

### auth-rpc-authorization

- [apps/server/src/auth/RpcAuthorization.ts L213–L299](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/RpcAuthorization.ts#L213-L299) — Unknown-method failure, decoded payload checks, scope middleware and device list side-effect flags.
- [apps/server/src/auth/RpcAuthorization.test.ts L33–L91](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/RpcAuthorization.test.ts#L33-L91) — Exhaustive map, sensitive logs, shell side effects and query flag assertions; inspected only.

### auth-mcp-audience

- [apps/server/src/auth/EnvironmentAuth.ts L612–L619](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/EnvironmentAuth.ts#L612-L619) — External MCP audience rejected outside /mcp.
- [apps/server/src/auth/EnvironmentAuth.ts L1298–L1342](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/EnvironmentAuth.ts#L1298-L1342) — External MCP bearer audience, read-only/runtime ceiling and issuance.
- [apps/server/src/mcp/McpHttpServer.ts L197–L247](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpHttpServer.ts#L197-L247) — Per-request MCP registry/client authentication and managed ceiling.

### auth-mcp-tool-access

- [apps/server/src/mcp/McpToolAccess.ts L37–L110](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpToolAccess.ts#L37-L110) — Typed/module-token construction and read-only-client refusal.
- [apps/server/src/mcp/McpToolAccess.ts L121–L207](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpToolAccess.ts#L121-L207) — Read/write/acts-as-caller declarations and target checks.
- [apps/server/src/mcp/McpToolAccess.ts L231–L258](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpToolAccess.ts#L231-L258) — Starts-thread mode attenuation and linked origin stamping.
- [oxlint-plugin-t3code/rules/no-raw-mcp-registration.ts L6–L28](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/oxlint-plugin-t3code/rules/no-raw-mcp-registration.ts#L6-L28) — Raw MCP registration targets and central checked registration prescription.
- [oxlint-plugin-t3code/rules/no-raw-mcp-registration.ts L99–L128](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/oxlint-plugin-t3code/rules/no-raw-mcp-registration.ts#L99-L128) — Static direct-registration bypass detection.

### auth-mcp-caller-limits

- [apps/server/src/mcp/McpInvocationContext.ts L52–L121](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpInvocationContext.ts#L52-L121) — Runtime and interaction lattice; caller and administrator attenuation.
- [apps/server/src/mcp/threadAccess.ts L86–L156](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/threadAccess.ts#L86-L156) — Live caller lookup, provider ownership, background-subagent exception and full-access check.
- [apps/server/src/mcp/McpHttpServer.ts L159–L185](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpHttpServer.ts#L159-L185) — Malformed request limits rejected; transport metadata narrows approved ceiling.

### auth-authority-race

- [apps/server/src/orchestration-v2/Orchestrator.ts L13837–L13885](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Orchestrator.ts#L13837-L13885) — Receipt replay then under-lock target-mode recheck; mutable mode refusals do not poison retry receipt.
- [apps/server/src/mcp/McpToolAccess.race.test.ts L94–L131](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpToolAccess.race.test.ts#L94-L131) — Injected user permission raise between facade check and command.
- [apps/server/src/mcp/McpToolAccess.race.test.ts L171–L181](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/mcp/McpToolAccess.race.test.ts#L171-L181) — Expected escalation refusal and unchanged title; test inspected, not executed.

### auth-provider-permissions

- [apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts L717–L755](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts#L717-L755) — Codex mode to approval/reviewer/sandbox mapping.
- [apps/server/src/orchestration-v2/Adapters/ClaudeAdapterV2.ts L2800–L2892](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/Adapters/ClaudeAdapterV2.ts#L2800-L2892) — Claude mode/override conversion, unavailable bypass downgrade and callback setup.
- [docs/user/permission-modes.md L3–L58](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/user/permission-modes.md#L3-L58) — Full-access default, configuration and provider-specific fallbacks.

### auth-managed-policy

- [apps/server/src/policy/ManagedPolicy.ts L78–L124](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/policy/ManagedPolicy.ts#L78-L124) — Policy settings/provider validation; ceiling shapes launch configuration.
- [docs/user/managed-policy.md L45–L59](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/user/managed-policy.md#L45-L59) — Policy source ownership/ambiguity and administrator-write deployment requirement.
- [docs/user/managed-policy.md L94–L137](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/user/managed-policy.md#L94-L137) — Installed/loaded identity, restart requirement, fail-closed policy parsing, defaults versus locks.

### auth-permission-compatibility

- [packages/contracts/src/auth.ts L79–L115](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/contracts/src/auth.ts#L79-L115) — Legacy scopes plus exact permissions and client-only fallback.
- [docs/internals/environment-auth.md L87–L99](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/environment-auth.md#L87-L99) — Grant narrowing and version-compatible permission responses.

### auth-proof-and-tickets

- [apps/server/src/auth/EnvironmentAuth.ts L792–L819](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/EnvironmentAuth.ts#L792-L819) — DPoP binding cannot fall back to bearer or accept unbound proof.
- [apps/server/src/auth/EnvironmentAuth.ts L1213–L1295](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/EnvironmentAuth.ts#L1213-L1295) — RPC/media ticket exceptions, route audiences and fresh proof.
- [apps/server/src/auth/dpop.ts L43–L95](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/dpop.ts#L43-L95) — Request binding and replay rejection; selected verification path.

### auth-session-invalidation

- [apps/server/src/auth/SessionStore.ts L790–L847](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/SessionStore.ts#L790-L847) — Current session signature/expiry/revocation lookup and stored scopes.
- [apps/server/src/auth/SessionStore.ts L1042–L1095](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/SessionStore.ts#L1042-L1095) — Subscribe-before-read invalidation, renewal chain and original-scope preservation.
- [apps/server/src/ws.ts L3623–L3637](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/ws.ts#L3623-L3637) — Socket lifetime races revocation/expiry invalidation.

### auth-mcp-oauth

- [apps/server/src/auth/McpOAuth.ts L104–L127](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/McpOAuth.ts#L104-L127) — Allowed callback recipients and exact HTTPS/loopback-port matching.
- [apps/server/src/auth/McpOAuth.ts L319–L355](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/McpOAuth.ts#L319-L355) — Stateless signed client registration and public PKCE.
- [apps/server/src/auth/McpOAuth.ts L448–L475](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/McpOAuth.ts#L448-L475) — Pairing or browser approval with CSRF/grant checks.
- [apps/server/src/auth/McpOAuth.ts L515–L555](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/auth/McpOAuth.ts#L515-L555) — Authorization code consumption/bindings/PKCE and session minting.

### auth-asset-authority

- [docs/internals/environment-auth.md L127–L144](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/environment-auth.md#L127-L144) — Filesystem scope is environment-wide; asset capabilities survive minting-session revocation.
- [apps/server/src/assets/AssetAccess.ts L374–L429](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/assets/AssetAccess.ts#L374-L429) — Canonical-file/device/inode identity bound into asset capability.
- [apps/server/src/assets/AssetAccess.ts L878–L893](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/assets/AssetAccess.ts#L878-L893) — Asset signature and expiry checks.
- [apps/server/src/assets/AssetAccess.ts L974–L1007](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/assets/AssetAccess.ts#L974-L1007) — Exact media path and opened-file identity verification.

### auth-remote-boundaries

- [docs/internals/remote.md L9–L56](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/remote.md#L9-L56) — Stable environment identity, route preflight/fallback and encrypted-token route learning.
- [docs/internals/remote.md L93–L140](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/remote.md#L93-L140) — Delegated ceilings, caller-namespaced keys, bounded waits, link-origin write fence and full-access non-isolation.

### review-authored-diff

- [docs/user/source-control.md L6–L14](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/user/source-control.md#L6-L14) — Keep the review projection narrower than the recovery snapshot
- [apps/server/src/vcs/GitVcsDriver.ts L1499–L1554](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/vcs/GitVcsDriver.ts#L1499-L1554) — Keep the review projection narrower than the recovery snapshot
- [apps/server/src/checkpointing/CheckpointDiffQuery.ts L205–L249](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/checkpointing/CheckpointDiffQuery.ts#L205-L249) — Keep the review projection narrower than the recovery snapshot

### review-checkpoint-index

- [apps/server/src/vcs/GitVcsDriver.ts L905–L935](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/vcs/GitVcsDriver.ts#L905-L935) — Checkpoint without consuming the developer staging area
- [apps/server/src/vcs/GitVcsDriver.ts L1247–L1295](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/vcs/GitVcsDriver.ts#L1247-L1295) — Checkpoint without consuming the developer staging area

### review-restore-isolation

- [apps/server/src/orchestration-v2/CheckpointRestoreSafety.ts L9–L104](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRestoreSafety.ts#L9-L104) — A file restore requires current isolation, not just historical ownership
- [apps/server/src/orchestration-v2/CheckpointRollbackService.ts L237–L252](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRollbackService.ts#L237-L252) — A file restore requires current isolation, not just historical ownership
- [apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts L30–L37](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts#L30-L37) — A file restore requires current isolation, not just historical ownership
- [apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts L168–L180](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts#L168-L180) — A file restore requires current isolation, not just historical ownership
- [apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts L207–L250](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRestoreSafety.test.ts#L207-L250) — A file restore requires current isolation, not just historical ownership

### review-rewind-boundaries

- [apps/server/src/orchestration-v2/CheckpointRollbackService.ts L149–L174](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRollbackService.ts#L149-L174) — Conversation rewind and file restoration are separate operations
- [apps/server/src/orchestration-v2/CheckpointRollbackService.ts L284–L300](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointRollbackService.ts#L284-L300) — Conversation rewind and file restoration are separate operations
- [apps/server/src/vcs/GitVcsDriver.ts L1303–L1336](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/vcs/GitVcsDriver.ts#L1303-L1336) — Conversation rewind and file restoration are separate operations
- [apps/server/src/vcs/GitVcsDriver.ts L1351–L1394](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/vcs/GitVcsDriver.ts#L1351-L1394) — Conversation rewind and file restoration are separate operations

### review-capture-idempotency

- [apps/server/src/orchestration-v2/CheckpointCaptureService.ts L68–L99](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointCaptureService.ts#L68-L99) — Idempotent checkpoint finalization must preserve cancellation semantics
- [apps/server/src/orchestration-v2/CheckpointCaptureService.ts L123–L140](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointCaptureService.ts#L123-L140) — Idempotent checkpoint finalization must preserve cancellation semantics
- [apps/server/src/orchestration-v2/CheckpointCaptureService.ts L199–L215](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/CheckpointCaptureService.ts#L199-L215) — Idempotent checkpoint finalization must preserve cancellation semantics

### review-shared-cleanup

- [apps/web/src/worktreeCleanup.ts L1–L29](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/web/src/worktreeCleanup.ts#L1-L29) — Resource cleanup needs shared-ownership awareness

### context-payload-identity

- [docs/internals/composer-context-references.md L11–L37](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/composer-context-references.md#L11-L37) — Bind context to typed payload identity and preserve its position in prose
- [packages/shared/src/composerContextReferences.ts L375–L406](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.ts#L375-L406) — Bind context to typed payload identity and preserve its position in prose

### context-forward-compatibility

- [packages/contracts/src/composerContext.ts L229–L268](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/contracts/src/composerContext.ts#L229-L268) — Preserve unknown extensions without letting malformed known data bypass validation
- [docs/internals/composer-context-references.md L20–L27](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/composer-context-references.md#L20-L27) — Preserve unknown extensions without letting malformed known data bypass validation

### context-envelope-boundary

- [packages/shared/src/composerContextReferences.ts L245–L258](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.ts#L245-L258) — Escape structural boundaries in untrusted context; do not claim complete injection immunity
- [packages/shared/src/composerContextReferences.ts L350–L372](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/shared/src/composerContextReferences.ts#L350-L372) — Escape structural boundaries in untrusted context; do not claim complete injection immunity

### context-historical-migration

- [docs/internals/composer-context-references.md L58–L86](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/composer-context-references.md#L58-L86) — Do not rewrite historical events to migrate presentation
- [docs/internals/composer-context-references.md L122–L142](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/composer-context-references.md#L122-L142) — Do not rewrite historical events to migrate presentation

### context-intact-history

- [packages/provider-core/src/server/handoffBudget.ts L214–L265](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/provider-core/src/server/handoffBudget.ts#L214-L265) — Budget intact historical units and explicitly expose omissions

### context-handoff-drift

- [docs/internals/context-handoffs.md L1–L19](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/context-handoffs.md#L1-L19) — Context handoff documentation must follow the actual mechanism
- [apps/server/src/orchestration-v2/ContextHandoffService.ts L107–L114](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffService.ts#L107-L114) — Context handoff documentation must follow the actual mechanism
- [apps/server/src/orchestration-v2/ContextHandoffService.ts L448–L480](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffService.ts#L448-L480) — Context handoff documentation must follow the actual mechanism
- [apps/server/src/orchestration-v2/ContextHandoffService.ts L523–L557](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffService.ts#L523-L557) — Context handoff documentation must follow the actual mechanism
- [apps/server/src/orchestration-v2/ContextHandoffDelivery.ts L112–L143](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffDelivery.ts#L112-L143) — Context handoff documentation must follow the actual mechanism

### context-delivery-uncertainty

- [apps/server/src/orchestration-v2/ContextHandoffDelivery.ts L19–L38](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffDelivery.ts#L19-L38) — Persist context-delivery uncertainty around the provider boundary
- [apps/server/src/orchestration-v2/ContextHandoffDelivery.ts L55–L111](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffDelivery.ts#L55-L111) — Persist context-delivery uncertainty around the provider boundary
- [apps/server/src/orchestration-v2/ContextHandoffDelivery.ts L112–L153](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/orchestration-v2/ContextHandoffDelivery.ts#L112-L153) — Persist context-delivery uncertainty around the provider boundary

### context-provider-channels

- [packages/provider-core/src/server/orchestrationInstructions.ts L3–L25](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/provider-core/src/server/orchestrationInstructions.ts#L3-L25) — Adapt instruction delivery to provider channel and lifecycle
- [packages/provider-core/src/server/orchestrationInstructions.ts L76–L140](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/provider-core/src/server/orchestrationInstructions.ts#L76-L140) — Adapt instruction delivery to provider channel and lifecycle
- [packages/provider-core/src/server/orchestrationInstructions.test.ts L42–L84](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/packages/provider-core/src/server/orchestrationInstructions.test.ts#L42-L84) — Adapt instruction delivery to provider channel and lifecycle

### eng-context-budget

- [apps/server/src/provider/AgentContextBudget.test.ts L85–L151](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/provider/AgentContextBudget.test.ts#L85-L151) — Measure model-facing context from the real code path and ratchet it deliberately
- [.github/workflows/agent-context-budget.yml L1–L55](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/.github/workflows/agent-context-budget.yml#L1-L55) — Measure model-facing context from the real code path and ratchet it deliberately

### eng-model-facing-evals

- [evals/README.md L3–L15](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/evals/README.md#L3-L15) — Evaluate model-facing prose like executable behavior
- [evals/README.md L26–L48](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/evals/README.md#L26-L48) — Evaluate model-facing prose like executable behavior

### eng-grader-scope

- [evals/README.md L17–L24](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/evals/README.md#L17-L24) — Separate deterministic grader correctness from paid model efficacy
- [evals/test-signal/README.md L1–L19](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/evals/test-signal/README.md#L1-L19) — Separate deterministic grader correctness from paid model efficacy
- [evals/pr-content/README.md L3–L13](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/evals/pr-content/README.md#L3-L13) — Separate deterministic grader correctness from paid model efficacy

### eng-test-milestones

- [docs/internals/testing.md L5–L24](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/testing.md#L5-L24) — Test the actual failure milestone instead of elapsed time or extra layers

### eng-replay-provider

- [.agents/skills/test-t3-app/SKILL.md L13–L35](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/.agents/skills/test-t3-app/SKILL.md#L13-L35) — Replay UI turns through real adapters when testing presentation

### eng-surface-matrix

- [AGENTS.md L65–L76](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/AGENTS.md#L65-L76) — Test multi-surface completeness and reverse states explicitly

### eng-documentation-boundaries

- [AGENTS.md L159–L177](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/AGENTS.md#L159-L177) — Use documentation for durable cross-boundary reasons; let code own implementation facts

### review-revision-absence

- [docs/internals/pull-request-file-revisions.md L1–L61](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/docs/internals/pull-request-file-revisions.md#L1-L61) — Do not collapse absent, deleted and unknown revision states
- [apps/server/src/pullRequest/pullRequestViewedFiles.ts L71–L149](https://github.com/pingdotgg/t3code/blob/33f85846be8bc4bc592f0e621d6f0313e5abd4a4/apps/server/src/pullRequest/pullRequestViewedFiles.ts#L71-L149) — Do not collapse absent, deleted and unknown revision states

## Why we cite this

[[artifacts/projects/t3code]] extracts portable principles with explicit implementation/documentation/test-inspection and outcome limits. Local accepted intent is not remote completion; retained projections are not a complete event archive; a worktree is not a sandbox; context encoding is not instruction authorization; provider/file rollback is not an atomic transaction.

## Related sources

- [[sources/openai--codex]] — separately pinned underlying agent-runtime study, not this app's adapter/runtime version.
- [[sources/open-inspect--background-agents]] — generation/recovery and uncertain execution comparison.
- [[sources/humanlayer--humanlayer]] — task/review/authorization comparison.
- [[sources/superplanehq--superplane]] — durable workflow and shared-mutation comparison.
