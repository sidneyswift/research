---
domain: artifacts
subdomain: projects
type: project
name: dsh-superagent-prototype
creator: "[[creators/deepseek]]"
source: "[[sources/deepseek-ai--dsh-superagent-prototype]]"
ecosystem: DeepSeek Harness
status: source-investigated
last-reviewed: 2026-11-02
---

# dsh-superagent-prototype

> A persistent team coding-agent control plane: events become authorized Tickets, isolated workers execute them, and a main session handles communication across GitHub and Feishu.

## Attributes

- **Unit:** runnable DeepSeek Harness bundle, not the base Harness or DeepSeek model. MIT research code, expressly not an official product or production-ready release. Pinned at `6337fc823ce20251c8de8085948165c81aaa701e`. [[sources/deepseek-ai--dsh-superagent-prototype#root]], [[sources/deepseek-ai--dsh-superagent-prototype#license]]
- **Attention:** GitHub displayed 12.2k stars and 1.3k forks, rounded, on 2026-11-02; no adoption inference. [[sources/deepseek-ai--dsh-superagent-prototype]]
- **Investigated:** numbered domain/authorization/execution/prompt docs, core intake/engine/decision code, durable effects/outbox, prompt policy and selected recovery/concurrency tests. No installation, agent run, test execution or independent security audit. [[sources/deepseek-ai--dsh-superagent-prototype#engine]], [[sources/deepseek-ai--dsh-superagent-prototype#effect-tests]]

## Relationships

- [[creators/deepseek]]; [[sources/deepseek--super-agent-design]]; [[concepts/super-agent-architecture]]. The essay, internal deployment and released prototype are distinct evidence objects. [[sources/deepseek-ai--dsh-superagent-prototype#root]]
- [[artifacts/projects/humanlayer]] — compare durable task/host ownership; [[artifacts/projects/eve]] and [[concepts/durable-agent-execution]] — compare runtime durability with domain-level recovery.
- [[artifacts/projects/kody]] — compare portable state and credentials with this project's persistent team coordinator; neither is a drop-in replacement for the other. [[sources/kody-hq--kody#intent]], [[sources/deepseek-ai--dsh-superagent-prototype#domain]]

## Mechanism and themes

### A business object owns the work

**Documentation + implementation:** Source → immutable Trigger → Thread queue or Subscription fan-out → Eval → Decision/Mandate → Ticket → Assignment/Executor → Channel. The Ticket owns authorized scope and lifecycle; an Assignment binds it to an execution instance. A conversation can hold several Tickets; one Ticket can span conversations. The Engine wraps mutations in repository transactions and exposes role-scoped TypeScript interfaces. Those interfaces organize callers; they alone are not runtime security enforcement. [[sources/deepseek-ai--dsh-superagent-prototype#domain]], [[sources/deepseek-ai--dsh-superagent-prototype#engine]]

### Context delivery and authorization are separate

**Implementation:** Intake normalizes timestamps, deduplicates Trigger IDs, filters Source scope and fans out subscribed events. Correlation adds context; subscriptions route it. A human follow-up already owned by a worker bypasses new Eval; out-of-scope work must be handed back. All owning workers must release it before fresh routing. A context-only subscription supplies evidence without the resume/ownership effects of a Ticket's own Thread. Bots/CI can inform live work but do not wake ended Tickets. [[sources/deepseek-ai--dsh-superagent-prototype#intake]], [[sources/deepseek-ai--dsh-superagent-prototype#authorization]], [[sources/deepseek-ai--dsh-superagent-prototype#followup-tests]]

**Implementation:** direct acceptance checks the gate, policy revision, existing accepted Triggers and worker ownership. Inferred acceptance requires enabled matching rules and `auto` mode. Assessment validation requires each enabled rule exactly once, settled direction and intent evidence. Default `observe` records a would-accept proposal without launching it; explicit requests still work. These are structural gates around a semantic decision, not a proof that the model correctly inferred scope. [[sources/deepseek-ai--dsh-superagent-prototype#evals]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]]

**Documentation:** policy change invalidates in-flight Evals, not every running Ticket. Live workers receive relevant changes; Mandates are revalidated before ended work resumes. Human stop withdraws a Mandate and prevents automatic resumption. Removing an allowed sender therefore is not documented as an immediate kill switch for work already running. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]]

### Persist commands before dispatching effects

**Implementation:** SQLite-backed effects coalesce by `(kind,key)` and carry sequence and generation values. Completion deletes only the generation it processed, preserving a newer payload queued during execution. Per-kind handlers define ordering, concurrency and exponential backoff. `Later` defers paused/capacity-limited work without incrementing failures. Tests inspect rollback, replacement while running, limits, restart and backoff. [[sources/deepseek-ai--dsh-superagent-prototype#effects]], [[sources/deepseek-ai--dsh-superagent-prototype#effect-tests]]

The outbox atomically records a receipt and enqueues delivery. It checks pause/source/destination state, preserves per-Ticket conversation order until earlier messages repeatedly fail, and records permanent drops separately from sent. **Limit:** remote send occurs before local settlement; a crash between them leaves an ambiguous external outcome. This code is not a universal exactly-once delivery guarantee; adapter idempotency/reconciliation remains necessary. [[sources/deepseek-ai--dsh-superagent-prototype#outbox]]

### Concurrency includes background work and human intervention

**Documentation:** each Ticket has a worker session and directory. Preparation can create a worktree; slow preparation affects that Ticket. Slots include preparation, active turns and background work. One extra slot prioritizes a person's follow-up or status request over new launches. Handoff releases the slot; background shell work can survive a review handoff under distinct rules. A 30-minute background limit kills shell jobs but permits subagents to continue; restart/shutdown have separate cleanup rules. Selected tests explicitly cover bot capacity and the extra human slot. [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/deepseek-ai--dsh-superagent-prototype#concurrency-tests]]

Recovery reuses session/directory/branch and tells the executor to inspect local and remote state before repeating external actions. Input delivery, history uptake and subsequent reporting/turn completion are tracked separately, so unread follow-ups can return to Eval. That is domain recovery around the Harness, not evidence of replaying every external action atomically. [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/deepseek-ai--dsh-superagent-prototype#engine]]

### Spend attention only when it changes a person's next action

**Prompt policy:** acknowledge a request once, keep unfinished work internal, deliver the ready result or necessary blocker to the originating conversation. A PR existing is not readiness. The worker retains full verification records while IM carries the usable result and next action. Bot reviews are fallible input; defaults cap addressing rounds per reviewer/PR and preserve human review separately. These are instructions, not host-enforced engineering outcomes. [[sources/deepseek-ai--dsh-superagent-prototype#communication]], [[sources/deepseek-ai--dsh-superagent-prototype#worker-prompt]]

**Implementation:** Feishu outbound text passes a 100-word limit using `Intl.Segmenter('zh')` across mixed text; rejection asks for rewriting, not splitting. **Documentation:** prompt saves have immutable history, base-revision conflict detection and per-request refresh without waking sessions. [[sources/deepseek-ai--dsh-superagent-prototype#im-limit]], [[sources/deepseek-ai--dsh-superagent-prototype#outbox]], [[sources/deepseek-ai--dsh-superagent-prototype#prompts]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — subscriptions carry untrusted context while the Mandate defines work; see its deliberately limited guarantee. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]], [[sources/deepseek-ai--dsh-superagent-prototype#intake]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — deterministic scope/gate checks precede semantic rule assessment. [[sources/deepseek-ai--dsh-superagent-prototype#policy]]
- [[patterns/behavioral/evidence-gated-completion]] — ready, unfinished, failed and human-action states are distinct; readiness instructions still require truthful worker reporting. [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/deepseek-ai--dsh-superagent-prototype#communication]]
- Candidate mechanisms retained in [[concepts/super-agent-architecture]]: routing-only coordinator, subscription pass-through, attention budget and semantic watchdog. No independent second implementation or performance proof is inferred from modules in this repository.

## What we'd steal

Every entry is an **adaptation**, not a recommendation to deploy this prototype unchanged.

| Portable mechanism | Purpose and adaptation | Important limit / evidence |
| --- | --- | --- |
| ★ Ticket separate from session and Assignment | Track a business outcome through restarts and replacement executors | Domain ownership is not OS isolation. [[sources/deepseek-ai--dsh-superagent-prototype#domain]] |
| ★ Mandate separate from subscribed context | Let review/CI inform existing work without granting arbitrary new work | Semantic scope compliance still relies on the worker. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]] |
| Observe before auto | Inspect proactive acceptance decisions before enabling actions | Explicit requests remain enabled. [[sources/deepseek-ai--dsh-superagent-prototype#policy]] |
| Rule-by-rule judgment plus intent evidence | Make proactive admission inspectable; reject missing/duplicate rule assessments | Valid structure does not imply correct judgment. [[sources/deepseek-ai--dsh-superagent-prototype#policy]] |
| Version policy; requeue stale assessments | Prevent an old decision silently using changed permissions | Live work is notified rather than instantly revoked. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]] |
| Many-to-many subscriptions, context-only follow mode | Route routine follow-ups cheaply; retain separate context and ownership | A shared Thread exposes untrusted content to workers. [[sources/deepseek-ai--dsh-superagent-prototype#intake]] |
| Hand back out-of-scope follow-ups | Let the worker reject routing without dropping a user's request | Multiple owners delay fresh Eval until all release it. [[sources/deepseek-ai--dsh-superagent-prototype#followup-tests]] |
| ★ Persist effects in the domain transaction | Preserve intent across crash/restart | Remote effects still need idempotency. [[sources/deepseek-ai--dsh-superagent-prototype#effects]] |
| Sequence + generation match on queue completion | Avoid deleting a newer coalesced update | Per-key coalescing may intentionally omit intermediate payloads. [[sources/deepseek-ai--dsh-superagent-prototype#effects]] |
| Separate deferred capacity from failure | Pause or wait for slots without generating false error alarms | Needs a future dispatcher tick. [[sources/deepseek-ai--dsh-superagent-prototype#effects]] |
| Receipt states and per-conversation ordering | Distinguish sent, waiting, withdrawn and permanently dropped outcomes | Persisted receipt does not settle an ambiguous remote send. [[sources/deepseek-ai--dsh-superagent-prototype#outbox]] |
| Extra human continuation slot | Prevent new work starving intervention on existing work | A finite policy, not unrestricted parallelism. [[sources/deepseek-ai--dsh-superagent-prototype#execution]] |
| Track delivery, history uptake and follow-up disposition | Recover unread instructions without duplicating already owned work | Complex races deserve explicit fixtures. [[sources/deepseek-ai--dsh-superagent-prototype#engine]] |
| Recovery note requiring inspection before repetition | Check git/GitHub after interruption before mutating again | Prompt policy rather than an atomic side-effect ledger. [[sources/deepseek-ai--dsh-superagent-prototype#execution]] |
| Structured human question + derived attention stage | Surface the smallest decision and reserve panels for actionable states | Worker must report the actual blocker. [[sources/deepseek-ai--dsh-superagent-prototype#execution]] |
| ★ Original-thread delivery and ready-result gate | Close the loop where the person requested work | Communication instructions do not establish readiness. [[sources/deepseek-ai--dsh-superagent-prototype#communication]] |
| Host-enforced multilingual IM limit | Make a communication budget mechanically testable | Word count cannot measure usefulness. [[sources/deepseek-ai--dsh-superagent-prototype#im-limit]] |
| Immutable prompt revisions + optimistic save conflicts | Audit what instructions each session used without losing edits | Session behavior can change during a turn. [[sources/deepseek-ai--dsh-superagent-prototype#prompts]] |
| Bounded automated-review rounds | Prevent endless bot-driven scope/cost expansion | Serious unresolved findings still need a human decision. [[sources/deepseek-ai--dsh-superagent-prototype#communication]] |
| Ordered domain documentation and rejected-concept table | Teach concepts before use and preserve why abstractions were declined | Useful discipline, not evidence fewer concepts always wins. [[sources/deepseek-ai--dsh-superagent-prototype#domain]] |

## Tensions and anti-patterns

- **Authorization language has a narrower runtime scope than it may suggest.** Executors run as the operator's OS user without per-command approval. Docs explicitly say directory/wrapper defaults are not a security boundary and absolute paths bypass named-command wrappers. Merge conditions live in prompts; branch protection is the external enforcement mechanism. Do not translate Mandate admission into a claim of sandboxed execution or guaranteed scope containment. [[sources/deepseek-ai--dsh-superagent-prototype#execution]]
- **Prototype ≠ essay ≠ private production system.** Distributed compute/state/environment separation and the independent semantic Watchdog are essay designs; the released paths studied here show local durable orchestration, not proof of the whole cloud/BYOM topology. [[sources/deepseek-ai--dsh-superagent-prototype#root]], [[sources/deepseek--super-agent-design#separation-watchdog]]
- **Quiet communication can conceal unhealthy work if status is inaccurate.** The design depends on honest structured reports and useful operator visibility; word limits alone are insufficient. [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/deepseek-ai--dsh-superagent-prototype#communication]]

## Open questions and verification record

- TODO: execute focused fixtures in an isolated environment with approved dependencies; tests cited here were only inspected.
- TODO: examine crash-after-remote-send behavior per adapter and its dedupe/reconciliation contract.
- TODO: test prompt injection through subscribed review comments and scope expansion beyond a Mandate under constrained credentials.
- TODO: measure real human interruptions, accepted results, provider spend and completed coding tasks; the essay's synthetic scheduling benchmark cannot settle these.
- Source SHA/path/line and wiki link checks are recorded in [[log]]; no source application or provider behavior was verified.
