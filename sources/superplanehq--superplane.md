---
domain: sources
type: repo
url: https://github.com/superplanehq/superplane
retrieved: 2026-11-04
snapshot-location: sources/superplanehq--superplane/
upstream-commit: 7d755d16b8ae836ecebf61639efc6266d74a4b0b
last-reviewed: 2026-11-04
---

# superplanehq/superplane — engineering workflows and software factory

> Pinned source evidence for [[artifacts/projects/superplane]], maintained by [[creators/superplane]].

## Snapshot details

- **Revision:** `7d755d16b8ae836ecebf61639efc6266d74a4b0b`, committed 2026-11-04T12:14:31Z; retrieved 2026-11-04.
- **Preservation:** all 10,205 tracked entries saved locally, with `.git`, under `sources/superplanehq--superplane/`. Shallow history, not a complete historical mirror. The clone is ignored; this citation page, the [capture manifest](superplanehq--superplane-evidence/capture.json), analysis and restoration registration are committed, **not the checkout itself**.
- **Restore:** `./setup.sh --only superplanehq--superplane`; check with `./setup.sh --check --only superplanehq--superplane`. Upstream availability remains a dependency.
- **Scope:** modular-monolith architecture, event/queue/run lifecycle, configuration publication, work orders, PR repair coordination, merge revision gates, approvals, runner completion/logs, scheduled intake, component UX and authority boundaries. Selected tests inspected. Not every file read, a security audit, or a runtime performance evaluation.
- **Execution:** only source-preservation, citation/hash and research-wiki checks. No app install/build/tests, cloud provisioning, provider calls or deployment.

## Popularity signals

GitHub API at retrieval: **8,785 stars; 690 forks**. Attention signals, not adoption or success-rate measurements. The root license applies Apache-2.0 outside `ee/`; `ee/` has a separate Enterprise license. Do not call the entire tree Apache-licensed. [[sources/superplanehq--superplane#license]]

## Anchor map

### root

- [README.md:1–98](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/README.md#L1-L98)

### architecture

- [docs/contributing/architecture.md:1–126](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/architecture.md#L1-L126)

### factory-draft

- [docs/prd/software-factory.md:1–105](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/prd/software-factory.md#L1-L105)
- [docs/prd/software-factory.md:187–274](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/prd/software-factory.md#L187-L274)

### work-order

- [pkg/models/factory_work_order.go:18–100](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_work_order.go#L18-L100)
- [pkg/models/factory_work_order.go:374–497](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_work_order.go#L374-L497)
- [pkg/models/factory_work_order.go:803–831](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_work_order.go#L803-L831)

### event-routing

- [pkg/workers/event_router.go:45–85](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/event_router.go#L45-L85)
- [pkg/workers/event_router.go:158–264](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/event_router.go#L158-L264)
- [pkg/workers/event_router.go:396–457](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/event_router.go#L396-L457)

### queue

- [pkg/workers/node_queue_worker.go:244–410](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/node_queue_worker.go#L244-L410)
- [pkg/workers/node_queue_worker.go:413–483](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/node_queue_worker.go#L413-L483)

### queue-test

- [pkg/workers/node_queue_worker_queueing_test.go:436–486](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/node_queue_worker_queueing_test.go#L436-L486)

### execution-state

- [pkg/models/canvas_node_execution.go:15–103](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/canvas_node_execution.go#L15-L103)
- [pkg/models/canvas_node_execution.go:479–548](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/canvas_node_execution.go#L479-L548)

### finalization

- [pkg/workers/run_finalizer.go:505–569](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/workers/run_finalizer.go#L505-L569)

### staging

- [pkg/grpc/actions/canvases/commit_canvas_staging.go:27–155](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/canvases/commit_canvas_staging.go#L27-L155)

### approval

- [pkg/components/approval/approval.go:61–229](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/components/approval/approval.go#L61-L229)
- [pkg/components/approval/approval.go:470–511](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/components/approval/approval.go#L470-L511)
- [pkg/components/approval/approval.go:559–620](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/components/approval/approval.go#L559-L620)

### pr-coordination

- [pkg/models/factory_pull_request_activity.go:301–402](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_pull_request_activity.go#L301-L402)

### repair-budget

- [pkg/models/factory_pull_request_activity.go:404–471](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_pull_request_activity.go#L404-L471)
- [pkg/models/factory_pull_request_activity_test.go:299–377](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_pull_request_activity_test.go#L299-L377)

### coordination-test

- [pkg/models/factory_pull_request_activity_test.go:152–182](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_pull_request_activity_test.go#L152-L182)

### pr-revision

- [pkg/models/factory_pull_request_revision.go:48–90](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/factory_pull_request_revision.go#L48-L90)

### merge

- [pkg/grpc/actions/factories/merge_factory_pull_request.go:22–157](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/merge_factory_pull_request.go#L22-L157)
- [pkg/grpc/actions/factories/merge_factory_pull_request.go:203–230](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/merge_factory_pull_request.go#L203-L230)

### merge-tests

- [pkg/grpc/actions/factories/factory_pull_request_merge_test.go:473–485](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/factory_pull_request_merge_test.go#L473-L485)
- [pkg/grpc/actions/factories/factory_pull_request_merge_test.go:488–541](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/factory_pull_request_merge_test.go#L488-L541)

### implementation-template

- [pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml:7–31](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml#L7-L31)
- [pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml:70–189](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml#L70-L189)
- [pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml:209–307](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/templates/github/line-implementation.canvas.yaml#L209-L307)

### confidence

- [pkg/components/factory/merge_confidence_check.go:17–143](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/components/factory/merge_confidence_check.go#L17-L143)
- [pkg/grpc/actions/factories/templates/github/risk-score.canvas.yaml:65–116](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/templates/github/risk-score.canvas.yaml#L65-L116)

### runner-protocol

- [pkg/runners/README.md:1–21](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/runners/README.md#L1-L21)
- [pkg/runners/README.md:75–119](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/runners/README.md#L75-L119)

### runner-completion

- [pkg/models/runner_task.go:403–570](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/runner_task.go#L403-L570)
- [pkg/public/runnerapi/websocket.go:500–637](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/public/runnerapi/websocket.go#L500-L637)

### log-lifecycle

- [pkg/models/runner_task.go:573–596](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/runner_task.go#L573-L596)

### runner-admission

- [pkg/models/runner_task_scheduler.go:34–87](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/runner_task_scheduler.go#L34-L87)
- [docs/contributing/organization-runner-api-rollout.md:15–68](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/organization-runner-api-rollout.md#L15-L68)

### result-file

- [pkg/runners/agent/result_file.go:48–72](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/runners/agent/result_file.go#L48-L72)

### scheduled-intake

- [docs/contributing/scheduled-intake.md:1–33](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/scheduled-intake.md#L1-L33)
- [pkg/grpc/actions/factories/templates/github/scheduled-intake.canvas.yaml:7–73](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/grpc/actions/factories/templates/github/scheduled-intake.canvas.yaml#L7-L73)

### authorization

- [pkg/authorization/gateway_authorizer.go:43–126](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/authorization/gateway_authorizer.go#L43-L126)

### network-policy

- [pkg/networkpolicy/http.go:40–118](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/networkpolicy/http.go#L40-L118)

### component-contract

- [docs/contributing/component-implementations.md:5–75](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-implementations.md#L5-L75)
- [docs/contributing/component-implementations.md:169–220](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-implementations.md#L169-L220)

### operator-interface

- [docs/contributing/component-design.md:102–147](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-design.md#L102-L147)
- [docs/contributing/component-design.md:485–610](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-design.md#L485-L610)
- [docs/contributing/component-design.md:767–875](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-design.md#L767-L875)
- [docs/contributing/component-design.md:881–933](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/component-design.md#L881-L933)

### license

- [LICENSE:1–5](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/LICENSE#L1-L5)
- [ee/LICENSE:1–32](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/ee/LICENSE#L1-L32)
- [docs/contributing/enterprise-licensing.md:27–81](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/docs/contributing/enterprise-licensing.md#L27-L81)

### contributor-checks

- [AGENTS.md:15–32](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/AGENTS.md#L15-L32)
- [AGENTS.md:204–241](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/AGENTS.md#L204-L241)
- [pkg/models/AGENTS.md:9–59](https://github.com/superplanehq/superplane/blob/7d755d16b8ae836ecebf61639efc6266d74a4b0b/pkg/models/AGENTS.md#L9-L59)

## Why we cite this

A workflow-centered complement to a coding harness: durable work identity, typed events, keyed queue admission, PR mutation ownership, bounded repair and revision-bound merging. It also supplies counterexamples to overbroad claims: copied node configuration is not a frozen run graph; a validated risk score is not measured correctness; acknowledged completion is not exactly-once external effects.

## Related sources

- [[sources/openai--codex]] — agent harness inside the orchestration layer.
- [[sources/open-inspect--background-agents]] — session hosting, recovery and authority boundaries.
- [[sources/humanlayer--humanlayer]] — human review and content-version feedback.
- [[sources/vercel--eve]] — durable execution and replay contracts.
- [[sources/ankrgyl--trace-lake]] — using history to improve later evaluations.
