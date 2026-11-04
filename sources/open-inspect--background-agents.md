---
domain: sources
type: repo
url: https://github.com/open-inspect/background-agents
retrieved: 2026-11-04
snapshot-location: sources/open-inspect--background-agents/
upstream-commit: 4b7f4e430dbb5c29cf776de41151365d1196d737
last-reviewed: 2026-11-04
---

# open-inspect/background-agents — hosted coding sessions

> Pinned docs and implementation evidence for [[artifacts/projects/background-agents]], maintained by [[creators/open-inspect]].

## Snapshot details

- **Revision:** `4b7f4e430dbb5c29cf776de41151365d1196d737`, committed 2026-11-04T18:38:56+05:30; retrieved 2026-11-04.
- **Preservation:** all 3,239 tracked entries saved locally with Git metadata at `sources/open-inspect--background-agents/`; shallow history, not a historical mirror. The clone is intentionally ignored. The research repo commits this source map, [capture manifest](open-inspect--background-agents-evidence/capture.json), analysis and restore registration, **not the checkout itself**.
- **Restore:** `./setup.sh --only open-inspect--background-agents`; verify with `./setup.sh --check --only open-inspect--background-agents`. Restoration depends on upstream availability.
- **Scope:** architecture, shared protocol, snapshot-to-stream handoff, generation/operation fencing, shutdown/checkpoint policy, child sessions, automation launch, credential and memory boundaries, skill materialization, export consistency, and preview/portability documentation. Selected test assertions inspected; not every file read or a security audit.
- **Execution:** source connectivity, clean-tree, citation/hash and wiki checks only. No source application installation, build, tests, provider calls, model inference or deployment.

## Popularity signals

GitHub API on 2026-11-04: **3,453 stars; 504 forks**. MIT license. These are dated attention signals, not measured adoption or correctness.

## Anchor map

### root

- [README.md:1–90](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/README.md#L1-L90)

### architecture

- [docs/HOW_IT_WORKS.md:37–250](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/HOW_IT_WORKS.md#L37-L250)

### boot

- [docs/HOW_IT_WORKS.md:271–443](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/HOW_IT_WORKS.md#L271-L443)

### boot-code

- [README.md:292–330](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/README.md#L292-L330)
- [packages/sandbox-runtime/src/sandbox_runtime/repository_boot.py:285–334](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/repository_boot.py#L285-L334)
- [packages/sandbox-runtime/src/sandbox_runtime/repository_hooks.py:30–100](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/repository_hooks.py#L30-L100)

### harness

- [docs/HOW_IT_WORKS.md:556–581](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/HOW_IT_WORKS.md#L556-L581)
- [packages/sandbox-runtime/src/sandbox_runtime/harness/base.py:1–194](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/harness/base.py#L1-L194)

### completion

- [packages/sandbox-runtime/src/sandbox_runtime/activity_supervisor.py:108–139](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/activity_supervisor.py#L108-L139)

### attribution

- [docs/HOW_IT_WORKS.md:594–627](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/HOW_IT_WORKS.md#L594-L627)

### protocol

- [docs/adr/0002-shared-session-contracts-and-correlation-boundary.md:1–56](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/adr/0002-shared-session-contracts-and-correlation-boundary.md#L1-L56)

### snapshot-handoff

- [docs/adr/0003-session-snapshot-handoff.md:1–62](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/adr/0003-session-snapshot-handoff.md#L1-L62)
- [packages/control-plane/src/session/connection-authenticator.ts:452–541](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/connection-authenticator.ts#L452-L541)
- [packages/control-plane/src/session/websocket-manager.ts:356–408](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/websocket-manager.ts#L356-L408)

### shutdown-design

- [docs/adr/0004-sandbox-checkpoint-and-shutdown.md:1–153](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/adr/0004-sandbox-checkpoint-and-shutdown.md#L1-L153)

### generation-fence

- [packages/control-plane/src/session/sandbox-shutdown.ts:157–215](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown.ts#L157-L215)
- [packages/control-plane/src/session/sandbox-shutdown.ts:381–409](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown.ts#L381-L409)

### checkpoint

- [packages/control-plane/src/session/sandbox-shutdown.ts:812–925](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown.ts#L812-L925)
- [packages/control-plane/src/session/checkpoint-settlement.ts:9–73](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/checkpoint-settlement.ts#L9-L73)

### continuation

- [packages/control-plane/src/session/sandbox-shutdown.ts:1016–1068](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown.ts#L1016-L1068)
- [packages/control-plane/src/session/sandbox-shutdown.test.ts:1258–1330](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown.test.ts#L1258-L1330)

### lifecycle-tests

- [packages/control-plane/src/session/checkpoint-settlement.test.ts:35–118](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/checkpoint-settlement.test.ts#L35-L118)
- [packages/control-plane/src/session/sandbox-shutdown-replacement.test.ts:55–108](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/sandbox-shutdown-replacement.test.ts#L55-L108)

### compatibility

- [packages/control-plane/src/sandbox/lifecycle/shutdown-policy.ts:1–19](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/sandbox/lifecycle/shutdown-policy.ts#L1-L19)

### child-scope

- [packages/control-plane/src/routes/session-child-spawn.ts:105–118](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/routes/session-child-spawn.ts#L105-L118)
- [packages/control-plane/src/routes/session-child-spawn.ts:163–240](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/routes/session-child-spawn.ts#L163-L240)
- [packages/control-plane/src/routes/session-child-spawn.ts:289–345](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/routes/session-child-spawn.ts#L289-L345)

### child-followups

- [docs/HOW_IT_WORKS.md:529–554](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/HOW_IT_WORKS.md#L529-L554)
- [packages/control-plane/src/routes/session-children.ts:187–255](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/routes/session-children.ts#L187-L255)
- [packages/control-plane/src/session/http/handlers/child-sessions.handler.ts:147–202](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/http/handlers/child-sessions.handler.ts#L147-L202)

### authority

- [docs/AUTH.md:349–385](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTH.md#L349-L385)
- [docs/AUTH.md:443–477](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTH.md#L443-L477)
- [docs/AUTH.md:554–582](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTH.md#L554-L582)

### credentials

- [docs/AUTH.md:572–630](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTH.md#L572-L630)
- [packages/control-plane/src/session/scm-credentials-service.ts:14–77](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/scm-credentials-service.ts#L14-L77)

### automation-delivery

- [docs/AUTOMATIONS.md:203–233](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTOMATIONS.md#L203-L233)
- [packages/control-plane/src/scheduler/session-prompt.ts:20–82](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/scheduler/session-prompt.ts#L20-L82)
- [packages/control-plane/src/scheduler/session-prompt.ts:95–136](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/scheduler/session-prompt.ts#L95-L136)

### automation-retry

- [docs/AUTOMATIONS.md:472–492](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTOMATIONS.md#L472-L492)
- [packages/control-plane/src/scheduler/run-launch-service.ts:27–170](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/scheduler/run-launch-service.ts#L27-L170)
- [packages/control-plane/src/scheduler/launch-services.test.ts:145–238](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/scheduler/launch-services.test.ts#L145-L238)

### automation-breaker

- [docs/AUTOMATIONS.md:605–689](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/AUTOMATIONS.md#L605-L689)

### memory-model

- [docs/MEMORY.md:1–14](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/MEMORY.md#L1-L14)
- [docs/MEMORY.md:56–100](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/MEMORY.md#L56-L100)
- [docs/MEMORY.md:126–166](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/MEMORY.md#L126-L166)

### memory-boundary

- [docs/MEMORY.md:25–54](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/MEMORY.md#L25-L54)
- [packages/control-plane/src/memory/session-rules.ts:1–58](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/memory/session-rules.ts#L1-L58)
- [packages/control-plane/src/memory/session-memory-service.ts:260–309](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/memory/session-memory-service.ts#L260-L309)

### skills-pinning

- [docs/MANAGED_SKILLS.md:242–302](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/MANAGED_SKILLS.md#L242-L302)

### skills-validation

- [packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py:205–245](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py#L205-L245)
- [packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py:280–351](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py#L280-L351)

### skills-install

- [packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py:457–609](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/sandbox-runtime/src/sandbox_runtime/managed_skills.py#L457-L609)

### export

- [docs/TRACE_EXPORT.md:1–111](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/TRACE_EXPORT.md#L1-L111)

### export-code

- [packages/control-plane/src/session/services/message.service.ts:193–252](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/services/message.service.ts#L193-L252)
- [packages/control-plane/src/session/services/message.service.trace-export.test.ts:268–305](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/packages/control-plane/src/session/services/message.service.trace-export.test.ts#L268-L305)

### preview

- [docs/verification/authenticated-preview.md:1–75](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/verification/authenticated-preview.md#L1-L75)

### portability

- [docs/PORTABLE_SQL.md:1–62](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/PORTABLE_SQL.md#L1-L62)
- [docs/adr/0001-single-provider-scm-boundaries.md:1–53](https://github.com/open-inspect/background-agents/blob/4b7f4e430dbb5c29cf776de41151365d1196d737/docs/adr/0001-single-provider-scm-boundaries.md#L1-L53)

## Why we cite this

A concrete control-plane/data-plane example: durable session state does not make provider effects exactly-once; checkpoint success and source retirement are independent; context pinning and live authorization solve different problems. Documentation, implementation and inspected tests are identified separately in the artifact. The source map registers relevant paths, not claims that the whole service was exercised.

## Related sources

- [[sources/openai--codex]] — underlying harness architecture, distinct revision and investigation.
- [[sources/humanlayer--humanlayer]] — collaborative agent control plane and human review.
- [[sources/vercel--eve]] — durable execution and side-effect replay boundaries.
- [[sources/ankrgyl--trace-lake]] — trace analysis and evaluation loops, not equivalent to a manual export API.
- [[sources/zhang--skill-plus-plus]] — routing quality; pinned installation alone does not establish correct selection.
