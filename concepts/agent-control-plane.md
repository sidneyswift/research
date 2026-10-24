---
domain: concepts
type: concept
name: agent-control-plane
creators: ["[[creators/humanlayer]]"]
sources: ["[[sources/humanlayer--humanlayer]]"]
status: emerging
last-reviewed: 2026-10-23
---

# agent-control-plane

> Separate the durable organization of work from the agent process that happens to execute it: tasks, access, artifacts, commands, and shared review comments can outlive individual sessions and machines. Local review markers have a narrower scope.

## What it is

HumanLayer runs agents on selected hosts while desktop and browser clients share an API-backed view of tasks and sessions. A task is the durable container for related conversations, files, and review. A session carries one conversation's model settings, working directory, messages, and run state. A host supplies execution resources; a workspace supplies checkouts. These are separate lifecycles, not interchangeable labels. “Control plane” is our architectural interpretation of those source structures. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]], [[sources/humanlayer--humanlayer#domain-model]]

## Where it came from

The observed implementation is HumanLayer's Riptide monorepo at commit `2f66a45b186d88488fa356862be0117db1ccae9f`. The general control-plane/data-plane distinction predates this project; this page tracks its concrete application to collaborative coding agents rather than asserting an invention claim. [[sources/humanlayer--humanlayer#root]]

## Why it matters

When the conversation is the only container, changing models, restarting an agent, or handing work to a teammate can fragment the work. A stable task and artifact layer makes those changes ordinary lifecycle operations. Separating execution from steering also lets a browser user operate near-private-infrastructure agents without moving the entire development environment into the browser. The resulting complexity is justified only if those capabilities are needed. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]]

## Evidence & claims

- **Documented product model:** several sessions share a task's files and comments; a fresh session need not discard task context. [[sources/humanlayer--humanlayer#task-model]]
- **Implemented lifecycle separation:** task, session, host, and workspace state have separate schemas and orchestration responsibilities. [[sources/humanlayer--humanlayer#domain-model]]
- **Implemented dispatch discipline:** for V2 workspace launches, replicated state wakes a session actor, which consults authoritative readiness before launching work. [[sources/humanlayer--humanlayer#authoritative-recheck]]
- **Implemented visibility separation:** recoverable event history and live UI delivery have different failure contracts. [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#stream-recovery]]
- **Boundary:** agents inherit the access of the operating-system user running the daemon; a Git worktree is not a security sandbox. [[sources/humanlayer--humanlayer#remote-hosts]], [[sources/humanlayer--humanlayer#permissions]]

## Patterns demonstrated

- [[patterns/structural/authoritative-recheck-after-notification]] — distinguish a signal that work may be available from authoritative permission and readiness to execute it. [[sources/humanlayer--humanlayer#authoritative-recheck]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — agent reasoning is model work; dispatch ownership, identities, tenant checks, and lifecycle state belong in deterministic services. [[sources/humanlayer--humanlayer#auth-boundaries]]
- [[patterns/structural/thin-harness-fat-skills]] — supporting counterpressure on “thin”: the reusable workflow can be portable while the collaborative runtime remains substantial. [[sources/humanlayer--humanlayer#root]]

## Tensions & counter-arguments

- **Distributed state introduces failure modes.** Replication delay, duplicate notifications, process death, stream reconnection, and permission revocation need explicit handling. A single local script may be better for a single local job. [[sources/humanlayer--humanlayer#authoritative-recheck]], [[sources/humanlayer--humanlayer#stream-recovery]]
- **Host-local execution is not zero cloud data.** Task files, session events, and collaboration state flow through the shared service. The task-file sync docs explicitly distinguish selected artifacts from backing up an entire repository. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]]
- **Recoverable history is not exactly-once tool execution.** An ordered, idempotent event append does not make an email, deployment, or shell command transactional. Provider runtime internals are partly external dependencies. [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#runtime-boundary]]
- **Provider interchangeability has limits.** Different agents retain different local history and permission behavior. The host-persistence documentation explicitly distinguishes Claude's local history from HumanLayer-stored Codex conversations. [[sources/humanlayer--humanlayer#remote-hosts]]

## Timeline

- 2026-10-23 — Extracted from HumanLayer's task/host documentation, schemas, session actor, event storage, and authorization paths. [[sources/humanlayer--humanlayer#root]]

## Related

- [[artifacts/projects/humanlayer]] — implementation and the full reuse ledger.
- [[concepts/durable-agent-execution]] — distinguishes history persistence here from step-checkpoint replay in eve.
- [[concepts/artifact-centered-agent-context]] — the context and handoff layer above runtime state.

## What we'd steal

- ★ **Separate task identity from session identity.** Keep the objective and work products together across retries, model changes, and handoffs. [[sources/humanlayer--humanlayer#task-model]]
- ★ **Separate control-plane access from host execution authority.** An API permission check and an operating-system boundary protect different things. [[sources/humanlayer--humanlayer#auth-boundaries]], [[sources/humanlayer--humanlayer#remote-hosts]]
- ★ **Recheck readiness at execution time.** A replicated event is a wakeup hint, not a launch contract. [[sources/humanlayer--humanlayer#authoritative-recheck]]
- **Give each execution grain an owner.** Per-session actors, claims, and cleanup protocols reduce duplicate work without serializing unrelated sessions. [[sources/humanlayer--humanlayer#session-ownership]]
- **Keep durable history separate from a disposable viewing connection.** UI disconnection should not erase work; recovery paths should be bounded. [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#stream-recovery]]
- **Expose capability differences instead of pretending every provider is identical.** Preserve a useful common contract while stating real resume and permission limits. [[sources/humanlayer--humanlayer#runtime-boundary]]
- **Make automation a short-lived instance of the same control plane.** An ephemeral daemon can produce a normal, reviewable session, with stable task history and process exit semantics. [[sources/humanlayer--humanlayer#automation]]

## Open questions

- Which guarantees hold during multi-region outages or provider-internal failures? This ingest did not run fault-injection experiments.
- What portion of the control plane is worth building for a single-user agent product?
- How should task context be handed to another host without implying that an active process migrated?
