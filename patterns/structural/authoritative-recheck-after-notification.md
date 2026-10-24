---
domain: patterns
type: pattern
name: authoritative-recheck-after-notification
category: structural
status: proposed
last-reviewed: 2026-10-23
example-count: 1
---

# authoritative-recheck-after-notification

> Treat a replicated notification as a reason to look, not as authority to execute. Re-read current readiness and acquire execution ownership immediately before starting work.

## Longer definition

An agent control plane can receive delayed or duplicate state updates. Starting a process directly from the received row confuses “this was eligible” with “this is eligible now.” For V2 workspace launches, HumanLayer separates observation from launch: session actors receive wakeup signals, re-query authoritative readiness, and guard concurrent dispatch. Other launches and continuations have separate paths. This page names that observed mechanism; it does not claim a novel distributed-systems invention. [[sources/humanlayer--humanlayer#authoritative-recheck]], [[sources/humanlayer--humanlayer#session-ownership]]

## Mechanism

1. Consume the sync event and route it to the owning session actor.
2. Fetch the current readiness record from the authoritative API.
3. Reject work that is no longer eligible or lacks its prerequisites.
4. Acquire the claim or in-flight ownership required for that execution grain.
5. Retain ownership until the previous local run and its finalizers finish; external effects require separate cancellation or idempotency guarantees.

The recheck and the ownership guard solve different races. A fresh read alone does not eliminate the interval before a concurrent launch; local serialization alone is not a cross-process lease. [[sources/humanlayer--humanlayer#authoritative-recheck]], [[sources/humanlayer--humanlayer#session-ownership]]

## When to use

- A background agent launches work from an eventually consistent feed.
- Multiple event paths can wake the same task or session.
- User cancellation or workspace readiness can change between notification and execution.

## When NOT to use

- A single transaction already owns and dequeues the job with the necessary guarantees; an extra remote recheck may only add latency.
- A low-stakes notification has no execution side effect.
- As a substitute for idempotent external actions or cross-process ownership where those are required.

## Why it works

It gives replicated state one job—discovery—and authoritative state another—eligibility. Explicit ownership then limits concurrent execution. This is a concrete instance of [[patterns/behavioral/latent-vs-deterministic-split]]: readiness and ownership should not be guessed by an LLM or inferred from stale UI state. [[sources/humanlayer--humanlayer#authoritative-recheck]]

## Detection recipe

- **Look for:** a notification handler that signals an actor instead of launching directly.
- **Confirm with:** an authoritative readiness fetch on the execution path, plus separate ownership/claim handling and tests for repeated wakeups or changed state.
- **Rule out:** merely debouncing UI events, refreshing a display, or putting a mutex around stale input without rechecking eligibility.

## Examples in this wiki

- [[artifacts/projects/humanlayer]] — V2 workspace launch actors re-fetch readiness and coordinate dispatch ownership after sync wakeups. [[sources/humanlayer--humanlayer#authoritative-recheck]], [[sources/humanlayer--humanlayer#session-ownership]]

Only one artifact has been verified; multiple modules inside HumanLayer do not count as independent examples.

## Counter-examples or anti-pattern

- **Hypothetical inverse:** launching from an old replicated row after the user cancelled the task. It has the same data shape but lacks the execution-time check.
- HumanLayer's own separation of best-effort live streaming from authoritative event history illustrates why not every event should carry the same authority. This is a contrast in roles, not a claim that its live stream launches work incorrectly. [[sources/humanlayer--humanlayer#stream-recovery]]

## Related patterns

- [[patterns/behavioral/latent-vs-deterministic-split]] — exact lifecycle checks belong in code.
- [[patterns/quality-bar/revision-bound-review]] — both reject transferring authority from an old observation to new state.
- [[concepts/agent-control-plane]] — the architecture that makes the distinction necessary.

## Open questions

- What second independently maintained agent system demonstrates the same notification→recheck→claim sequence?
- Which claims survive daemon process death, and which are only local concurrency protection? Read each claim's storage and recovery path before relying on it.
