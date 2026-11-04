---
domain: creators
type: org
name: SuperPlane
handle: superplanehq
url: https://github.com/superplanehq
last-reviewed: 2026-11-04
---

# SuperPlane

> Maintainers of a workflow engine and software factory that coordinate coding agents, integrations, checks and human decisions.

## Attributes

- **Ships:** Go/React application with PostgreSQL/RabbitMQ engine and integrated runners. [[sources/superplanehq--superplane#architecture]] [[sources/superplanehq--superplane#runner-protocol]]
- **Distribution:** public source; Apache-2.0 core with separate `ee/` license. GitHub API recorded 8,785 stars / 690 forks on 2026-11-04, not an adoption count. [[sources/superplanehq--superplane]] [[sources/superplanehq--superplane#license]]

## Artifacts produced

### Projects

- [[artifacts/projects/superplane]] — 42 portable principles covering durable work records, event execution, PR coordination, approvals and runner protocols.

## Design philosophy

The investigated mechanisms move coordination into explicit state: task intent persists across runs, agents receive bounded steps, exclusive PR mutation is queued, and terminal reports are reconciled by identity. This is an interpretation of the inspected source, not a claim that every subsystem has the same guarantees. [[sources/superplanehq--superplane#work-order]] [[sources/superplanehq--superplane#pr-coordination]] [[sources/superplanehq--superplane#runner-completion]]

## Timeline

- 2026-11-04 — Source investigated at `7d755d1`; full tracked tree preserved locally, selected code/docs/test anchors and restoration manifest recorded. [[sources/superplanehq--superplane]]

## Source citations

- [[sources/superplanehq--superplane#root]]
- [[sources/superplanehq--superplane#architecture]]
