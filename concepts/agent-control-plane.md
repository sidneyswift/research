---
domain: concepts
type: concept
name: agent-control-plane
creators: ["[[creators/humanlayer]]", "[[creators/matt-pocock]]"]
sources: ["[[sources/humanlayer--humanlayer]]", "[[sources/mattpocock--domain-orchestrator-factory]]"]
status: emerging
last-reviewed: 2026-11-04
---

# agent-control-plane

> Separate the durable organization of work from the agent process that happens to execute it: tasks, access, artifacts, commands, and shared review comments can outlive individual sessions and machines. Local review markers have a narrower scope.

## What it is

HumanLayer runs agents on selected hosts while desktop and browser clients share an API-backed view of tasks and sessions. A task is the durable container for related conversations, files, and review. A session carries one conversation's model settings, working directory, messages, and run state. A host supplies execution resources; a workspace supplies checkouts. These are separate lifecycles, not interchangeable labels. “Control plane” is our architectural interpretation of those source structures. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]], [[sources/humanlayer--humanlayer#domain-model]]

A related proposed shape puts a local, long-running, single-domain conversation in front of a CLI-controlled software factory. Matt Pocock describes the orchestrator managing threads, retrospectives and recurring jobs while sandboxed workers implement and explore and the human speaks in plain language. This adds a human-facing coordination role to the separation, without proving persistence or sandbox guarantees. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]] [[sources/mattpocock--domain-orchestrator-factory#cli-control]] [[sources/mattpocock--domain-orchestrator-factory#operating-loop]] [[sources/mattpocock--domain-orchestrator-factory#human-interface]]

## Where it came from

The observed implementation is HumanLayer's Riptide monorepo at commit `2f66a45b186d88488fa356862be0117db1ccae9f`. The general control-plane/data-plane distinction predates this project; this page tracks its concrete application to collaborative coding agents rather than asserting an invention claim. [[sources/humanlayer--humanlayer#root]]

## Why it matters

When the conversation is the only container, changing models, restarting an agent, or handing work to a teammate can fragment the work. A stable task and artifact layer makes those changes ordinary lifecycle operations. Separating execution from steering also lets a browser user operate near-private-infrastructure agents without moving the entire development environment into the browser. The resulting complexity is justified only if those capabilities are needed. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]]

## Principle: persistent domain orchestration with sandboxed execution

**Keep the human-facing coordinator continuous and domain-focused; delegate implementation and exploration to a separate execution system.** Pocock proposes a local, long-running thread, potentially using `/chief-of-staff`, attached through a CLI to a factory of sandboxed workers. The coordinator would manage threads, run retrospectives and accumulate cron jobs; the human would steer it in plain language. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]] [[sources/mattpocock--domain-orchestrator-factory#sandboxed-factory]] [[sources/mattpocock--domain-orchestrator-factory#cli-control]] [[sources/mattpocock--domain-orchestrator-factory#operating-loop]] [[sources/mattpocock--domain-orchestrator-factory#human-interface]]

| Layer | Proposed responsibility | Evidence boundary |
| --- | --- | --- |
| Human | Express goals and steering in ordinary language | No evaluated interface or ambiguity-resolution protocol shown |
| Local domain orchestrator | Maintain one domain thread; coordinate factory work, retrospectives and recurring jobs | Long-running conversation proposed; recovery, context management and permissions unspecified |
| Factory CLI | Provide the interface for the orchestrator to manage work/threads | No command schema, lifecycle protocol or idempotency contract shown |
| Sandboxed workers | Implement and explore away from the coordinating thread | Isolation intended; filesystem, network, credential and host boundaries unspecified |

The table restates responsibilities in the screenshot and names what it does not establish. The author is **considering a trial**, not reporting a successful implementation. [[sources/mattpocock--domain-orchestrator-factory#proposal-status]] [[sources/mattpocock--domain-orchestrator-factory#provenance-limits]]

Portable adaptations, not extra claims about the proposed system:

1. **Scope continuity to a domain.** Retain its goals, decisions and unresolved work without making one conversation the owner of every unrelated project. The source proposes one domain; the context-contamination rationale is our inference. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]]
2. **Separate continuity from worker lifetime.** Keep task identity, work products and resumable state outside any single process if continuity must survive interruption. A long-running chat alone is not a durable execution mechanism. This adaptation combines the proposal with the observed task/session separation, rather than attributing storage semantics to the screenshot. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]] [[sources/humanlayer--humanlayer#task-model]]
3. **Make the execution interface explicit.** Use bounded work orders and inspectable task status/results at the CLI boundary. Establish failure and retry behavior before relying on it for unattended work; a command interface by itself supplies neither safety nor exactly-once execution. [[sources/mattpocock--domain-orchestrator-factory#cli-control]] [[sources/humanlayer--humanlayer#runtime-boundary]]
4. **Isolate workers at a real enforcement boundary.** Match filesystem, network and credential access to the task. The word sandbox is not an implementation specification, and a separate thread or worktree does not establish containment. [[sources/mattpocock--domain-orchestrator-factory#sandboxed-factory]] [[sources/humanlayer--humanlayer#permissions]]
5. **Close the operating loop.** Have retrospectives turn observed recurring work into maintained routines, with purpose, owner, budget and stop conditions. The post proposes retrospectives and cron accumulation; those ownership/budget controls are our adaptation, not a reported feature. [[sources/mattpocock--domain-orchestrator-factory#operating-loop]]
6. **Keep the human interface at the level of intent.** Translate plain-language goals into worker assignments and return outcomes, evidence and decisions. Do not require the human to manage thread IDs or CLI commands to use the system. [[sources/mattpocock--domain-orchestrator-factory#human-interface]]

**Adoption trigger:** recurring work in one domain where repeatedly rebuilding context and manually coordinating execution is a real cost. For one isolated task, the extra persistent coordinator/factory machinery has not earned its complexity. This is a proposed decision rule; the screenshot supplies no cost or outcome measurements. [[sources/mattpocock--domain-orchestrator-factory#proposal-status]]

## Evidence & claims

- **Documented product model:** several sessions share a task's files and comments; a fresh session need not discard task context. [[sources/humanlayer--humanlayer#task-model]]
- **Implemented lifecycle separation:** task, session, host, and workspace state have separate schemas and orchestration responsibilities. [[sources/humanlayer--humanlayer#domain-model]]
- **Implemented dispatch discipline:** for V2 workspace launches, replicated state wakes a session actor, which consults authoritative readiness before launching work. [[sources/humanlayer--humanlayer#authoritative-recheck]]
- **Implemented visibility separation:** recoverable event history and live UI delivery have different failure contracts. [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#stream-recovery]]
- **Boundary:** agents inherit the access of the operating-system user running the daemon; a Git worktree is not a security sandbox. [[sources/humanlayer--humanlayer#remote-hosts]], [[sources/humanlayer--humanlayer#permissions]]

- **Proposed architecture:** a local single-domain orchestrator controls sandboxed implementation/exploration through a CLI, with retrospective and scheduled-work responsibilities. No completed trial or current `/chief-of-staff` source was verified. [[sources/mattpocock--domain-orchestrator-factory#root]]

## Patterns demonstrated

- [[patterns/structural/authoritative-recheck-after-notification]] — distinguish a signal that work may be available from authoritative permission and readiness to execute it. [[sources/humanlayer--humanlayer#authoritative-recheck]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — agent reasoning is model work; dispatch ownership, identities, tenant checks, and lifecycle state belong in deterministic services. [[sources/humanlayer--humanlayer#auth-boundaries]]
- [[patterns/structural/thin-harness-fat-skills]] — supporting counterpressure on “thin”: the reusable workflow can be portable while the collaborative runtime remains substantial. [[sources/humanlayer--humanlayer#root]]

## Tensions & counter-arguments

- **Distributed state introduces failure modes.** Replication delay, duplicate notifications, process death, stream reconnection, and permission revocation need explicit handling. A single local script may be better for a single local job. [[sources/humanlayer--humanlayer#authoritative-recheck]], [[sources/humanlayer--humanlayer#stream-recovery]]
- **Host-local execution is not zero cloud data.** Task files, session events, and collaboration state flow through the shared service. The task-file sync docs explicitly distinguish selected artifacts from backing up an entire repository. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#remote-hosts]]
- **Recoverable history is not exactly-once tool execution.** An ordered, idempotent event append does not make an email, deployment, or shell command transactional. Provider runtime internals are partly external dependencies. [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#runtime-boundary]]
- **Provider interchangeability has limits.** Different agents retain different local history and permission behavior. The host-persistence documentation explicitly distinguishes Claude's local history from HumanLayer-stored Codex conversations. [[sources/humanlayer--humanlayer#remote-hosts]]

- **Long-lived is not durable; local is not automatically private.** The proposal does not specify checkpoint/replay, context compaction, backend data movement or isolation enforcement. Treat those as design questions, not consequences of its labels. [[sources/mattpocock--domain-orchestrator-factory#provenance-limits]]

## Timeline

- 2026-10-23 — Extracted from HumanLayer's task/host documentation, schemas, session actor, event storage, and authorization paths. [[sources/humanlayer--humanlayer#root]]

- 2026-11-04 — Ingested a supplied screenshot of Matt Pocock's proposed domain-orchestrator/factory combination; original publication date unknown. [[sources/mattpocock--domain-orchestrator-factory#root]]

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

- ★ **Pair a persistent domain coordinator with a separate worker factory.** Plain-language human steering, CLI task control, sandboxed implementation/exploration and retrospective/recurring-work loops are the proposed bundle. See the dedicated principle section for all six adaptations and their limits. [[sources/mattpocock--domain-orchestrator-factory#root]]

## Open questions

- Which guarantees hold during multi-region outages or provider-internal failures? This ingest did not run fault-injection experiments.
- What portion of the control plane is worth building for a single-user agent product?
- How should task context be handed to another host without implying that an active process migrated?

## Pstack comparison — 2026-10-24

[[artifacts/skills/poteto-mode]] is a useful smaller-grain comparison: a local work ledger and PR watcher coordinate evidence and ownership, while scheduling, role authority, and external execution remain outside the implemented store. PR-plus-SHA lookup does not establish authenticated approval or durable execution. [[sources/cursor--plugins-pstack#OR07]] [[sources/cursor--plugins-pstack#OR11]]

## New comparison — 2026-11-02

[[artifacts/projects/dsh-superagent-prototype]] supplies a distinct Ticket/Mandate/Assignment model. [[concepts/super-agent-architecture]] specializes the broader control-plane idea into continuous interaction, subscription pass-through and a routing-only coordinator, rather than duplicating this page's task/host lifecycle role. [[artifacts/projects/kody]] separates org/actor/credential identity in portable execution infrastructure. [[sources/deepseek-ai--dsh-superagent-prototype#domain]], [[sources/deepseek--super-agent-design#router-workers]], [[sources/kody-hq--kody#request-context]]

## Trace Lake comparison — 2026-11-04

[[concepts/trace-lake]] adds a complementary evidence loop: a persistent coordinator can query historical runs, schedule bounded investigations and convert confirmed findings into regression evals. The coordinator is not the trace store, and a reported pattern is not permission to mutate the product. Loop docs distinguish scheduled Braintrust write permissions from connected MCP authority and note that created scoring rules outlive their creator. This is a documented product comparison, not evidence that Matt Pocock's proposed factory was implemented. [[sources/ankrgyl--trace-lake#trace-to-eval]] [[sources/ankrgyl--trace-lake#automation-authority]]
