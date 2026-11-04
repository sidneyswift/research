---
domain: sources
type: repo
url: https://github.com/openai/codex
retrieved: 2026-11-04
snapshot-location: sources/openai--codex/
upstream-commit: 021fccb046508938c4754982efccfb51d6e8356e
last-reviewed: 2026-11-04
---

# openai/codex — the open agent harness

> Pinned implementation and documentation evidence for [[artifacts/projects/codex]]; complements the earlier feature-level [[artifacts/projects/codex-goals]] investigation.

## Snapshot details

- **Revision:** `021fccb046508938c4754982efccfb51d6e8356e`, committed 2026-11-04; retrieved 2026-11-04. Full tracked working tree saved locally with Git metadata; shallow history, not every historical branch or release.
- **Preservation:** 9,974 tracked entries; ignored clone at `sources/openai--codex/`, registered in `sources/repos.manifest.tsv`. Restore with `./setup.sh --only openai--codex`; verify with `./setup.sh --check --only openai--codex`. The research repository commits this source map, analysis and [capture manifest](openai--codex-evidence/capture.json), **not the source checkout itself**. Restoration depends on upstream accessibility.
- **Scope:** root/core/protocol/client/storage/executor/SDK docs; selected turn loop, tool dispatch/approval, compaction replay, goal lifecycle, skill selection/rendering, child ownership and trace writer/reducer paths. Focused test assertions inspected. This is a bounded architecture study, not a read of all 9,974 files or a security audit.
- **Checks run:** source object connectivity and clean-tree verification; range/hash and wiki-link checks accompany ingestion. No Codex build, upstream test suite, model inference or deployment run. Main-branch manifest versions are not assumed to be published releases.

## Popularity signals

- GitHub API on 2026-11-04: **133,104 stars; 21,075 forks**. Attention signals, not measured correctness or deployment counts.
- Apache-2.0 repository license; existing third-party notices and per-component terms remain in the saved tree.

## Anchor map

### root

- [README.md:1–81](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/README.md#L1-L81)

### license

- [LICENSE:1–25](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/LICENSE#L1-L25)

### core

- [codex-rs/core/README.md:1–98](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/README.md#L1-L98)

### protocol

- [codex-rs/protocol/README.md:1–7](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/protocol/README.md#L1-L7)

### client-runtime

- [codex-rs/app-server-client/README.md:1–66](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server-client/README.md#L1-L66)

### loop

- [codex-rs/core/src/session/turn.rs:498–658](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/session/turn.rs#L498-L658)
- [codex-rs/core/src/session/turn.rs:758–825](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/session/turn.rs#L758-L825)

### parallel-tools

- [codex-rs/core/src/tools/parallel.rs:275–405](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/tools/parallel.rs#L275-L405)

### approval

- [codex-rs/core/src/tools/orchestrator.rs:137–235](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/tools/orchestrator.rs#L137-L235)
- [codex-rs/core/src/tools/orchestrator.rs:432–553](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/tools/orchestrator.rs#L432-L553)

### human-checkpoints

- [codex-rs/app-server/README.md:1–16](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L1-L16)
- [codex-rs/core/src/tools/approvals.rs:1–79](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/tools/approvals.rs#L1-L79)

### network

- [codex-rs/network-proxy/README.md:1–160](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/network-proxy/README.md#L1-L160)

### config-layers

- [codex-rs/config/src/loader/README.md:1–90](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/config/src/loader/README.md#L1-L90)

### project-trust

- [codex-rs/app-server/README.md:209–214](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L209-L214)

### storage

- [codex-rs/thread-store/README.md:1–34](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/thread-store/README.md#L1-L34)

### replay

- [codex-rs/core/src/session/rollout_reconstruction.rs:12–182](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/session/rollout_reconstruction.rs#L12-L182)

### async-compaction

- [codex-rs/core/src/session/async_compaction.rs:1–153](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/session/async_compaction.rs#L1-L153)

### executor

- [codex-rs/exec-server/README.md:1–92](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/exec-server/README.md#L1-L92)

### sdk-typescript

- [sdk/typescript/README.md:1–130](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/sdk/typescript/README.md#L1-L130)

### sdk-python

- [sdk/python/README.md:1–75](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/sdk/python/README.md#L1-L75)
- [sdk/python/docs/faq.md:1–101](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/sdk/python/docs/faq.md#L1-L101)
- [sdk/python/pyproject.toml:1–22](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/sdk/python/pyproject.toml#L1-L22)

### goal-provenance

- [codex-rs/core/src/context/user_goal.rs:1–120](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/context/user_goal.rs#L1-L120)

### goal-tools

- [codex-rs/ext/goal/src/spec.rs:24–94](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/src/spec.rs#L24-L94)
- [codex-rs/ext/goal/src/tool.rs:246–317](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/src/tool.rs#L246-L317)

### goal-continuation

- [codex-rs/ext/goal/src/runtime.rs:412–534](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/src/runtime.rs#L412-L534)
- [codex-rs/ext/goal/src/extension.rs:314–377](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/src/extension.rs#L314-L377)

### goal-tests

- [codex-rs/ext/goal/tests/goal_extension_backend.rs:448–509](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/tests/goal_extension_backend.rs#L448-L509)
- [codex-rs/ext/goal/tests/goal_extension_backend.rs:1088–1110](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/tests/goal_extension_backend.rs#L1088-L1110)
- [codex-rs/ext/goal/tests/goal_extension_backend.rs:1215–1241](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/goal/tests/goal_extension_backend.rs#L1215-L1241)

### skill-selection

- [codex-rs/skills/src/selection.rs:17–204](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/skills/src/selection.rs#L17-L204)

### skill-selection-tests

- [codex-rs/skills/src/selection_tests.rs:227–289](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/skills/src/selection_tests.rs#L227-L289)

### skill-budget

- [codex-rs/ext/skills/src/render.rs:23–198](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/skills/src/render.rs#L23-L198)

### skill-shadow

- [codex-rs/ext/skills/src/dynamic_skill_selector.rs:1–58](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/ext/skills/src/dynamic_skill_selector.rs#L1-L58)

### instruction-refresh

- [codex-rs/codex-home/src/instructions/mod.rs:1–113](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/codex-home/src/instructions/mod.rs#L1-L113)

### agent-spawn

- [codex-rs/core/src/agent/control/spawn_guard.rs:1–125](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/agent/control/spawn_guard.rs#L1-L125)

### agent-residency

- [codex-rs/core/src/agent/control/residency.rs:1–118](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/agent/control/residency.rs#L1-L118)

### agent-budget

- [codex-rs/core/src/agent/control/budget.rs:1–39](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/core/src/agent/control/budget.rs#L1-L39)

### trace

- [codex-rs/rollout-trace/README.md:1–215](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/rollout-trace/README.md#L1-L215)

### trace-writer

- [codex-rs/rollout-trace/src/writer.rs:1–140](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/rollout-trace/src/writer.rs#L1-L140)

### trace-tests

- [codex-rs/rollout-trace/src/reducer/acceptance_tests.rs:1–122](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/rollout-trace/src/reducer/acceptance_tests.rs#L1-L122)

### read-state

- [codex-rs/app-server/README.md:68–109](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L68-L109)

### policy-reload

- [codex-rs/app-server/README.md:155–164](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L155-L164)
- [codex-rs/app-server/README.md:551–557](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L551-L557)
- [codex-rs/app-server/README.md:568–572](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L568-L572)

### api-evolution

- [codex-rs/app-server/README.md:540–549](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/app-server/README.md#L540-L549)

### extraction-boundaries

- [codex-rs/tools/README.md:1–74](https://github.com/openai/codex/blob/021fccb046508938c4754982efccfb51d6e8356e/codex-rs/tools/README.md#L1-L74)

## Why we cite this

Supports the concrete runtime mechanisms and their boundaries: shared clients, authoritative state, execution authority, recovery, bounded discovery and evidence provenance. Test citations are inspected assertions, not evidence of tests run here.

## Related sources

- [[sources/openai--using-goals-in-codex]] — historical feature-level account; current goal tools have additional states and narrower enforceable guarantees.
- [[sources/openai--codex-skills-doc]] — historical skills/distribution docs, not silently refreshed by this pin.
- [[sources/openai--plugins]] — separate marketplace/distribution source.
- [[sources/vercel--eve]] — independent runtime comparison; different execution-recovery contract.
