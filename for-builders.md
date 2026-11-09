# for-builders.md — mining this wiki while you build

**Audience:** a coding agent (or person) pointed at this repo from *another* project, to extract design guidance while building a skill, plugin, MCP server, agent, or agent-shaped product.

This is the **consumer** front door. The other two: `README.md` (humans browsing), `CLAUDE.md` (the agent that *maintains* this wiki). You are neither — you're here to **mine**, then leave. This file is a routing surface only; it points at pages and never restates their content.

---

## Set expectations first (the honest scope)

This is a wiki about **how to architect agents, skills, plugins, and agent-products** — distilled from a small, opinionated set of frontier sources (Anthropic, Garry Tan's gstack/gbrain, Every's compound-engineering, OpenAI Codex). Calibrate before you rely on it:

- **High value, in-domain:** you're building something *agent-shaped* — a skill, a plugin/pack, a resolver, a self-improving loop, a multi-surface distribution, an MCP server. The patterns here are grounded, cited, and carry explicit `When NOT to use` + anti-patterns. Steal freely.
- **Limited scope outside agent products:** HumanLayer adds concrete examples of task/session data models, review UX, and execution authorization. These are source-specific examples, not a general app-architecture or security handbook.
- **Known gaps (2026-10-23):** individual skills have pages, but standalone MCP servers remain a candidate queue. The corpus is selective and several patterns still have only one verified example; watch their status and same-creator caveats. `analyses/` now contains draft engineering-skill studies and a source catalogue; their review and behavioral-validation limits remain explicit.

## The protocol (follow in order)

1. **Read `CLAUDE.md` → the `QUERY` operation.** Your task is a QUERY. The discipline there governs you.
2. **Enter through `index.md`**, then use the routing table below to jump to pages.
3. **Read *whole* pattern/artifact pages** — including each artifact's `## What we'd steal` ledger. Do **not** skim only the steal sections (the wiki's own anti-rule: a thin read narrows attention and discards ideas).
4. **Start in the wiki, not the source clones.** The analysis lives in the pages; `sources/` is evidence. Only follow a `[[sources/...#anchor]]` citation when you need to *verify* a claim before acting on it.
5. **If the cited source bodies are missing** (a fresh checkout git-ignores the repo clones), run `sources/clone-all.sh` once to rebuild them, then follow citations.
6. **If the answer isn't in the wiki, you found a gap** — note it in your output so the maintainer can file it back (`CLAUDE.md` QUERY step 2). Don't silently paper over a hole.

## Routing table — build-intent → read these first

| You're building… | Patterns / concepts to read first | Worked artifacts to study |
| --- | --- | --- |
| **Reduce repeated model-decision cost / route uncertain cases** | [[concepts/typed-decision-cascades]], [[patterns/behavioral/latent-vs-deterministic-split]], [[concepts/review-cost-aware-workflows]] | [[sources/typesafe--decision-model-docs]]: statistic semantics and shared-state batching; [[sources/nutlope--jev-fraud]]: separate queues, recorded outcomes and cost basis. Compare equal-quality baselines before adopting. |
| **Always-on assistants / event triage / deciding when to interrupt** | [[concepts/proactive-agent-discernment]], [[concepts/super-agent-architecture]], [[patterns/behavioral/context-is-not-authority]] | [[sources/rubriclabs--always-on-agents]]: wake/action/message separation and explicit responsibility; [[sources/rubriclabs--jev-use-cases]]: abstention and threshold choices, exploratory evidence only. |
| **Multi-provider agent app / reusable service facade / reconnect and review** | [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]], [[concepts/review-cost-aware-workflows]] | [[artifacts/projects/t3code]]:79 practices; atomic intent, replay classification, auth ceilings and authored review versus full restore |
| **Documentation retrieval / API guidance / WebMCP** | [[concepts/agent-documentation-interfaces]], [[concepts/developer-documentation-design]], [[concepts/business-platform-api-design]] | [[artifacts/projects/context7]], [[artifacts/projects/fern]], [[artifacts/projects/readme]], [[artifacts/projects/webmcp]], [[artifacts/projects/dokimi]] |
| **Cross-session memory / dreaming / knowledge-wiki consolidation** | [[concepts/agent-memory-consolidation]], [[concepts/artifact-centered-agent-context]], [[concepts/trace-lake]] | [[sources/anthropic--components-of-agent-memory]]: raw-search/wiki/hybrid baselines, measured construction/maintenance cost and claim provenance; [[sources/anthropic--agent-memory-support]]: adoption, concurrency, retention and session-coverage boundaries. |
| **Choose/customize an agent model or assess an RL result** | [[concepts/evidence-calibrated-research]], [[concepts/imitation-vs-correctness-eval]], [[concepts/agent-habitat-architecture]] | [[artifacts/projects/inkling-2-small]]: held-out adaptation curves, expert-label routing, complete eval budgets, sampler provenance and independent execution controls; source-reported, not replicated. |
| **User/agent-created reminders, recurring jobs or deferred tasks** | [[concepts/durable-agent-execution]], [[concepts/completion-contract]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/vercel-schedules]]: target-specific retries, current-permission checks, deployment selection, cancellation cutoff and timing/retention windows; documentation evidence only. |
| **Agent isolation / credential brokerage / effect authorization / containment** | [[concepts/agent-habitat-architecture]], [[patterns/behavioral/context-is-not-authority]], [[concepts/durable-agent-execution]] | Agent Habitat is a proposal; compare [[artifacts/projects/codex]], [[artifacts/projects/background-agents]] and [[artifacts/skills/security-audit]] for distinct implementation/evidence contracts, not claimed compliance. |
| **Security-review evidence / coverage ledgers / independent claim checks** | [[concepts/evidence-calibrated-research]], [[concepts/review-cost-aware-workflows]], [[patterns/behavioral/evidence-gated-completion]] | [[artifacts/skills/security-audit]] (48 principles; source-inspected and validator fixtures executed, not an audit-quality benchmark) |
| **Issue-to-PR factory / repair loops / shared mutation ownership** | [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]], [[concepts/review-cost-aware-workflows]] | [[artifacts/projects/superplane]] (keyed admission, repair budgets, exact-head merge and completion boundaries; source-inspected) |
| **Hosted background coding / sandbox recovery / automation retries** | [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/background-agents]] (saved state versus retirement, uncertain delivery and effective context; source-inspected) |
| **Embed an agent runtime / audit recovery and authority** | [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/codex]] (shared runtime, model-visible evidence and scoped resume; source-inspected, not benchmarked) |
| **Agents answering business-data questions / semantic models** | [[concepts/ubiquitous-language-for-agents]], [[concepts/imitation-vs-correctness-eval]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/auto-ontology]] (source inspection; no replicated accuracy claim) |
| **Growing skill libraries / routing collisions** | [[concepts/lifelong-skill-routing]], [[patterns/composition/resolver-routing-table]], [[concepts/imitation-vs-correctness-eval]] | [[sources/zhang--skill-plus-plus]] (reported benchmark, not replicated); [[artifacts/skills/writing-great-skills]] |
| **Production traces → investigations → regression evals** | [[concepts/trace-lake]], [[concepts/review-cost-aware-workflows]], [[concepts/verification-model-fidelity]] | [[sources/ankrgyl--trace-lake]] (article + vendor docs, not an independently run system) |

| **Local domain assistant + sandboxed worker factory** | [[concepts/agent-control-plane#principle-persistent-domain-orchestration-with-sandboxed-execution]], [[concepts/super-agent-architecture]], [[concepts/durable-agent-execution]] | [[sources/mattpocock--domain-orchestrator-factory]] (proposal); [[artifacts/projects/humanlayer]] (separate implementation comparison) |
| **Persistent team agent / cross-channel coordination** | [[concepts/super-agent-architecture]], [[patterns/behavioral/context-is-not-authority]], [[concepts/durable-agent-execution]] | [[artifacts/projects/dsh-superagent-prototype]], [[artifacts/projects/humanlayer]] |
| **Portable capabilities, memory and credential use** | [[concepts/code-mode-capability-interface]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/kody]] |
| **A single skill** (`SKILL.md` ± thin code) | [[concepts/convergent-agent-plugin-spec]], [[patterns/quality-bar/skill-pack-bundle]], [[patterns/behavioral/skill-as-method-call]], [[patterns/behavioral/latent-vs-deterministic-split]], [[patterns/structural/thin-harness-fat-skills]] | [[artifacts/plugins/gstack]], [[artifacts/plugins/compound-engineering]], [[artifacts/plugins/openai-codex-plugins-marketplace]] |
| **A plugin / pack of many skills** | [[concepts/convergent-agent-plugin-spec]], [[patterns/structural/marketplace-as-multi-plugin]], [[patterns/composition/resolver-routing-table]], [[patterns/composition/single-source-multi-surface-distribution]], [[patterns/quality-bar/version-as-update-gate]], [[patterns/quality-bar/complexity-ratchet]] | [[artifacts/plugins/anthropic-skills-marketplace]], [[artifacts/plugins/anthropic-financial-services-marketplace]], [[artifacts/plugins/compound-engineering]], [[artifacts/plugins/gstack]], [[artifacts/plugins/gbrain]], [[artifacts/plugins/openai-codex-plugins-marketplace]] |
| **An MCP server** | [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[concepts/mcp-enterprise-managed-authorization]], [[concepts/code-mode-capability-interface]] | [[analyses/mcp-and-extensions]] (draft synthesis), [[artifacts/plugins/gbrain]] (single-source delivery) |
| **Interactive apps inside an MCP host** | [[concepts/mcp-extension-architecture]], [[patterns/behavioral/context-is-not-authority]] | [[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]]; verify the exact host and SDK generation before using entrypoints |
| **Routing** — how the agent picks what to do | [[patterns/composition/resolver-routing-table]], [[patterns/behavioral/skill-as-method-call]] | [[artifacts/plugins/gbrain]] (`RESOLVER.md`), [[artifacts/plugins/gstack]] |
| **Verification vs. adversarial review budget** | [[concepts/review-cost-aware-workflows#principle-verification-over-abstract-adversarial-review]], [[concepts/verification-model-fidelity]] | [[artifacts/projects/tibo-dog]], [[artifacts/plugins/pstack]] |
| **Reliability** — how the agent knows it's *done* | [[patterns/behavioral/evidence-gated-completion]], [[concepts/completion-contract]] | [[artifacts/projects/codex-goals]] |
| **A self-improving / compounding system** | [[patterns/quality-bar/complexity-ratchet]], [[patterns/behavioral/diarization]] | [[concepts/compound-engineering]], [[artifacts/plugins/compound-engineering]] |
| **Code-vs-prose** — what to freeze in code vs leave to the model | [[patterns/behavioral/latent-vs-deterministic-split]], [[patterns/structural/thin-harness-fat-skills]] | [[artifacts/plugins/gstack]], [[artifacts/plugins/compound-engineering]] |
| **Untrusted input / multi-agent privilege / security** *(proposed, single example — caveat)* | *(tracked as a proposed bullet)* | [[artifacts/plugins/anthropic-financial-services-marketplace]] (trust-tiered subagents: only the reader touches untrusted docs; one leaf holds Write; a critic re-verifies) |
| **Release / versioning / distribution** | [[patterns/quality-bar/version-as-update-gate]], [[patterns/composition/single-source-multi-surface-distribution]] | [[artifacts/plugins/anthropic-financial-services-marketplace]], [[artifacts/plugins/compound-engineering]] |
| **Collaborative agent work and human review** | [[concepts/agent-control-plane]], [[concepts/review-cost-aware-workflows]], [[concepts/artifact-centered-agent-context]], [[patterns/quality-bar/revision-bound-review]] | [[artifacts/projects/humanlayer]], [[artifacts/plugins/humanlayer-rpi]] |

No row fits? Run `scripts/wiki-search.sh "<your terms>"`, or browse [patterns/_index.md](patterns/_index.md). Still nothing → that's a gap; report it.

## Output contract (what to hand back to the human)

Produce a short **design brief**, not a dump:

- **3–7 stolen ideas**, each one sentence, **each citing the wiki page** it came from (`[[patterns/...]]` / `[[artifacts/...]]`). Prefer ideas with a clear `When NOT to use` so you carry the boundary, not just the technique.
- **Boundaries applied:** name which `When NOT to use` / counter-examples rule *out* an idea for this build (this is the high-value part — say what you deliberately did *not* steal and why).
- **Portability note:** for a skill/plugin, name what stays inside the shared core (`SKILL.md`, local `references/`/`scripts/`, marketplace grammar) vs. what is harness-specific (connectors, hooks, env vars, storefront metadata).
- **Out-of-domain flag:** explicitly list what the wiki did *not* cover for this task, so the human doesn't mistake silence for endorsement.
- **Gaps found:** anything you expected and the wiki lacked — flag for filing back (`CLAUDE.md` QUERY step 2).

## Copy-paste prompt (for a fresh agent in your build project)

```text
Read Research/for-builders.md, then Research/CLAUDE.md (the QUERY operation).
I'm building: <describe the skill / plugin / MCP / agent / feature>.
Use the routing table to read the relevant whole pattern + artifact pages
(including each "What we'd steal" ledger), start in the wiki not the source
clones, and follow citations only to verify before you rely on a claim.
Return a design brief per the output contract: stolen ideas (each citing a
wiki page), boundaries you applied (what you did NOT steal and why), a
portability note for shared-core vs harness-specific pieces, an out-of-domain
flag for what the wiki didn't cover, and any gaps to file back.
```

## Developer documentation

For developer portals, API guides, examples, troubleshooting and agent-readable docs, start at [[projects/writing-amazing-developer-docs/README]], then read [[concepts/developer-documentation-design]] and [[projects/writing-amazing-developer-docs/page-blueprints]].

For internal architecture, runbooks, migrations and documentation delivery/evaluation, follow [[concepts/developer-documentation-design]] into [[projects/writing-amazing-developer-docs/platform-documentation-system]]. [[_schemas/documentation-case-study]] is the reusable study matrix.

For a concrete documentation platform with indexes, Markdown conversion, skills, MCP and agent-maintenance workflows, study [[artifacts/projects/mintlify]]; retain its research-method and access-boundary caveats.
