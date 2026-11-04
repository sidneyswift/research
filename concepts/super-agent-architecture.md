---
domain: concepts
type: concept
name: super-agent-architecture
creators: "[[creators/deepseek]]"
sources: "[[sources/deepseek--super-agent-design]]"
status: emerging
last-reviewed: 2026-11-02
---

# Super-agent architecture

> Keep one continuous agent identity for people, while the system manages event routing, concurrent isolated workers, persistent state and recovery behind it.

## What it is

DeepSeek's essay argues that improving single-task models moves the bottleneck toward **human attention across tasks**. Its four desired properties are continuous interaction, productive concurrency, proactive response and persistent availability. A routing-only coordinator maintains global continuity, while workers perform isolated tasks; users should not need to remember which model session contains the relevant context. This is an architecture proposal and reported internal experience, not a new model capability or a proven universal throughput result. [[sources/deepseek--super-agent-design#definition]], [[sources/deepseek--super-agent-design#router-workers]]

## Where it came from

Yujia Qiao wrote the DeepSeek Harness team's essay, published 2026-11-01. We captured X's English machine translation on 2026-11-02. The argument applies classic systems ideas—fast/slow paths, batching, locality, speculative execution, compute/storage separation and external control loops—to agent systems. The linked prototype is an intentionally different, incomplete released realization. Do not equate it with the internal deployment, base Harness or full design. [[sources/deepseek--super-agent-design#root]], [[sources/deepseek-ai--dsh-superagent-prototype#root]]

## Why it matters

It separates **the user's unit of work** from **the model's unit of context**. A task can move from chat to a pull request without becoming a new project to coordinate manually. More parallel workers alone do not provide this continuity: the architecture also needs task identity, subscriptions, memory retrieval, delivery ownership and authorization. Compare [[artifacts/projects/humanlayer]] for durable task coordination and [[artifacts/projects/kody]] for portable state/capabilities; their purposes overlap without being the same system. [[sources/deepseek--super-agent-design#router-workers]], [[sources/deepseek-ai--dsh-superagent-prototype#domain]], [[sources/kody-hq--kody#intent]]

## Evidence & claims

| Module | Claimed mechanism | Evidence boundary |
| --- | --- | --- |
| Router / Workers | Router coordinates and speaks; workers execute in isolated contexts. Lighter router model, stronger worker models; no peer communication by default | Essay design/experience; prototype has a corresponding main/worker split. [[sources/deepseek--super-agent-design#router-workers]], [[sources/deepseek-ai--dsh-superagent-prototype#domain]] |
| Fast/slow paths | Code filters source/sender noise; model judges semantic candidates. Subscribed follow-ups pass directly to workers; Router sees notices | Prototype intake and policy code support this subset. [[sources/deepseek--super-agent-design#triggers]], [[sources/deepseek-ai--dsh-superagent-prototype#intake]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]] |
| Inline & Spill | Inline short useful neighbors; keep bulky material outside the context with retrievable pointers | Design; budget and useful locality depend on workload. [[sources/deepseek--super-agent-design#context]] |
| Chain of Recall | Object IDs connect Triggers, Threads and Sessions; each read exposes next-hop IDs and summaries | On-demand graph traversal, not a solution to arbitrary long-term memory. [[sources/deepseek--super-agent-design#context]], [[sources/deepseek--super-agent-design#open-problems]] |
| Full duplex | Start returns immediately; completion arrives as another event; stop can cancel background work | Essay says Harness mechanism exists but is not enabled by default. Prototype documents five-second foreground limits and background lifecycle. [[sources/deepseek--super-agent-design#interaction]], [[sources/deepseek-ai--dsh-superagent-prototype#execution]] |
| Speculative preparation | Perform authorized useful work silently; surface only worthwhile results | Spending more compute may reduce waiting; not permission for unrequested effects. Prototype defaults to observe for inferred work. [[sources/deepseek--super-agent-design#interaction]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]] |
| Compute/state/environment separation | Stateless cloud loop, external persistent state, endpoint daemons including intermittently connected personal machines | Proposed topology; not established by this released prototype investigation. [[sources/deepseek--super-agent-design#separation-watchdog]] |
| External Watchdog | Independent scheduled agent judges goal progress as well as process health, diagnoses and repairs | Article design; no independently run progress detector or recovery evaluation. [[sources/deepseek--super-agent-design#separation-watchdog]] |

### What the experiment actually measures

Each of four designs ran five times, with about 300 messages and about 20 work requests per run. Coding was a **time-consuming mock tool**, so the study tests scheduling/coordination. Message intervals and work durations were scaled by one quarter while model calls were not. These are author-reported synthetic results, not a replicated coding benchmark. [[sources/deepseek--super-agent-design#experiments]]

| Design | Completion p50 / p95, minutes | Cache-read tokens/run |
| --- | --- | --- |
| Super-agent | 12.4 / 15.7 | 23.2M |
| Without pass-through | 12.6 / 15.5 | 31.8M |
| Single session + neutral subagent prompt | 20.4 / 29.5 | 6.1M |
| Single session + delegation-first prompt | 13.8 / 29.0 | 10.8M |

The neutral prompt never delegated in five runs; delegation-first delegated in four. The structural separation reduced reliance on that particular on-the-spot choice, while using substantially more cache-read tokens. Pass-through had similar completion times in this workload, with lower routing/cache overhead; it did **not** show a task-latency win. A separate real-router/mock-worker test reports average batch size 1.0→2.8, request time 2.5→3.9 seconds and amortized decision time 6.4→1.6 seconds over roughly 1→40 decision-requiring Triggers/minute. Do not extrapolate that curve into unbounded scaling or real coding quality. [[sources/deepseek--super-agent-design#experiments]]

## Patterns demonstrated

- [[patterns/behavioral/latent-vs-deterministic-split]] — explicit fast-path filtering/routing versus slow-path semantic judgment. [[sources/deepseek--super-agent-design#triggers]]
- [[patterns/behavioral/context-is-not-authority]] — the released implementation distinguishes subscribed context from Mandates; the essay leaves broader security open. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]], [[sources/deepseek--super-agent-design#open-problems]]
- [[patterns/behavioral/evidence-gated-completion]] — prototype's original-thread delivery separates a ready result from intermediate work. [[sources/deepseek-ai--dsh-superagent-prototype#communication]]
- Candidate techniques: attention as a design budget, non-executing router, follow-up pass-through, progress-aware watchdog. Retained as concept-level mechanisms; not promoted to confirmed patterns solely from this source family.

## Tensions & counter-arguments

- A single Router preserves continuity but remains a global bottleneck and privacy boundary. Sharding buys throughput by losing shared context; the essay explicitly leaves the threshold and topology open. [[sources/deepseek--super-agent-design#open-problems]]
- A user's limited ability to track 3–5 sessions is team experience in the essay, not a measured population fact. Higher latency stability can cost more tokens. The benchmark's synthetic execution cannot establish economically superior completed work. [[sources/deepseek--super-agent-design#definition]], [[sources/deepseek--super-agent-design#experiments]]
- Shared global context becomes an organizational access decision. A2A here means communication between separately scoped agents, not adoption of a specific protocol. [[sources/deepseek--super-agent-design#open-problems]]
- BYOM avoids copying difficult environments but connects untrusted event processing to private local resources. The authors explicitly identify endpoint compromise and credentials entering model context as unsolved risks. [[sources/deepseek--super-agent-design#open-problems]]
- Quiet proactive work needs explicit spending/effect boundaries and observability. Kody's protected credential uses and the prototype's Mandate/observe machinery are useful narrower components, not proof of complete injection resistance. [[sources/kody-hq--kody#credential-resolution]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]]

## What we'd steal

- ★ **Make tasks durable and sessions replaceable.** Let people work in their own domain conversations while routing sessions behind the scenes; retain explicit task ownership and links. [[sources/deepseek--super-agent-design#router-workers]]
- **Keep coordination non-executing by construction.** Use a smaller tool/model budget for routing; task workers own technical decomposition. This differs from forcing a team lead to plan every substep. [[sources/deepseek--super-agent-design#router-workers]]
- **Batch events accumulated during inference.** Exploit shared prefill without prematurely sharding global context; evaluate routing accuracy and tail latency as batch size grows. [[sources/deepseek--super-agent-design#router-workers]]
- ★ **Route established follow-ups by subscription.** Pay semantic routing for cold starts and genuine handbacks; retain lightweight coordinator visibility. [[sources/deepseek--super-agent-design#triggers]]
- **Use separate context and authority graphs.** A related Thread is evidence; authorized work needs an independent basis. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]]
- **Inline likely neighbors, spill bulk, retain identifiers.** Bound immediate context while exposing next-hop references; don't pretend summaries retain every fact. [[sources/deepseek--super-agent-design#context]]
- **Treat tool results as events for long-running work.** Start/stop handles allow new instructions without blocking on shell completion. Cancellation and external outcomes still need explicit semantics. [[sources/deepseek--super-agent-design#interaction]]
- **Speculate within an approved scope and budget.** Draft/reproduce quietly, then deliver useful evidence; start new rules in observation mode. [[sources/deepseek--super-agent-design#interaction]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]]
- **Tailor communication density to the channel.** Keep detailed engineering evidence in durable artifacts and short decisions/results in IM; silence is appropriate only while useful work remains observable. [[sources/deepseek--super-agent-design#interaction]]
- **Separate compute, state and execution environment decisions.** Evaluate what must persist and what cannot be cheaply reconstructed before choosing cloud migration versus remote tools. [[sources/deepseek--super-agent-design#separation-watchdog]]
- **Monitor semantic progress independently of process liveness.** A running loop can be stuck; investigate an external progress evaluator with bounded repair authority and measured false positives. [[sources/deepseek--super-agent-design#separation-watchdog]]
- **Ablate architecture and prompt choices separately.** Report model delegation decisions, cost and p95, not only average completion; replicate with real work before claiming productivity. [[sources/deepseek--super-agent-design#experiments]]

## Timeline

- 2026-11-01 — Essay published; companion prototype explicitly marks implementation differences. [[sources/deepseek--super-agent-design#root]], [[sources/deepseek-ai--dsh-superagent-prototype#root]]
- 2026-11-02 — Captured full English rendering and figures, investigated prototype, preserved empirical limits in this wiki.

## Related

- [[concepts/agent-control-plane]] — broader durable-work/host lifecycle concept; this page specializes continuous routing and event-driven concurrency.

- [[artifacts/projects/dsh-superagent-prototype]] — implementation study.
- [[concepts/durable-agent-execution]] — replay/checkpoint semantics rather than global coordination alone.
- [[concepts/code-mode-capability-interface]] — compact tools and portable state complementing the coordinator.

## Open questions

- TODO: obtain original Chinese and benchmark scripts/raw observations; assess translation and reproduce before numerical recommendations.
- TODO: compare real attention cost, false proactive starts, task success, provider spend and security incidents across systems.
- TODO: find independent source-investigated examples before promoting the router/pass-through/watchdog candidates.

## Domain-scoped coordinator comparison — 2026-11-04

[[concepts/agent-control-plane#principle-persistent-domain-orchestration-with-sandboxed-execution]] captures Matt Pocock's proposed local, long-running domain thread attached to a sandboxed software factory through a CLI. It shares the continuity/execution separation, but it is **not** evidence of DeepSeek's entire router/pass-through architecture: the proposed coordinator manages retrospectives and cron jobs, is scoped to one domain, and is not stated to be routing-only. It is a proposed trial with no reported result. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]] [[sources/mattpocock--domain-orchestrator-factory#operating-loop]] [[sources/mattpocock--domain-orchestrator-factory#proposal-status]]
