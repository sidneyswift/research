---
domain: patterns
type: pattern
name: context-is-not-authority
category: behavioral
status: confirmed
last-reviewed: 2026-11-02
example-count: 2
---

# Context is not authority

> Route relevant information broadly enough to do useful work, while deriving permission to act from a separate, explicit authorization object or trusted request identity.

## Longer definition

An incoming review, chat message, webhook or discovered capability can tell an agent something useful without granting new work or credential access. The pattern separates the **information path** from the **authority path**. It appears at two different scopes here: DeepSeek's work-admission Mandate and Kody's actor/enablement/credential resolution. “Confirmed” means observed in two independent artifacts, not certified injection resistance or equal enforcement strength. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]], [[sources/kody-hq--kody#request-context]], [[sources/kody-hq--kody#credential-resolution]]

## Mechanism

1. Normalize the external event and preserve its origin/actor metadata.
2. Deliver relevant information by subscription or request context without treating its content as a permission change.
3. Resolve authority separately: existing scope/Mandate, enabled rules, trusted actor, grant and credential restrictions.
4. Require a new authorized decision when work exceeds that authority; return a structured refusal or handback rather than silently widening it.
5. Revalidate at meaningful lifecycle boundaries and record the decision/version used. These boundaries differ by system. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]], [[sources/deepseek-ai--dsh-superagent-prototype#evals]], [[sources/kody-hq--kody#request-context]], [[sources/kody-hq--kody#credential-resolution]]

## When to use

- Persistent agents ingest bot feedback, public comments or CI while carrying existing task scope. [[sources/deepseek-ai--dsh-superagent-prototype#intake]]
- Scheduled/webhook code acts on behalf of a person and must preserve who enabled it and which credentials it may use. [[sources/kody-hq--kody#request-context]]
- Agents need credential use without plaintext disclosure to generated code. [[sources/kody-hq--kody#credential-resolution]]

## When NOT to use

- Do not add a complex work-admission domain to a pure read-only corpus reader just to imitate this architecture. The mechanism earns its complexity where events can trigger effects; both examples operate there. [[sources/deepseek-ai--dsh-superagent-prototype#domain]], [[sources/kody-hq--kody#intent]]
- Do not substitute this pattern for OS isolation, branch protection or narrow API credentials. Mandates and host allowlists cover different boundaries. [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/kody-hq--kody#credentials]]

## Why it works

Code can check stable identity, policy version and grants independently of a model's interpretation of a message. Semantic reasoning still decides whether a request fits an authorized scope, but an untrusted paragraph cannot itself manufacture a trusted actor or grant. The distinction makes failures inspectable: a bad interpretation is different from an unchecked credential resolution. It does not make semantic scope judgments infallible. [[sources/deepseek-ai--dsh-superagent-prototype#policy]], [[sources/kody-hq--kody#credential-resolution]]

## Detection recipe

- **Look for:** separate information delivery and authorization objects, such as Subscription vs Mandate or trigger Source vs enablement/RequestContext.
- **Confirm with:** owning code that rejects an inferred accept under observe/off, prevents duplicate scope admission, or authorizes credential use before applying it. Inspect negative fixtures as well as documentation.
- **Rule out:** a prompt merely saying “ignore malicious instructions” while event text can mutate permissions; a sender allowlist that becomes unrestricted OS authority; a secret getter that returns plaintext and relies on prose to keep it private. [[sources/deepseek-ai--dsh-superagent-prototype#evals]], [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#credential-tests]]

## Examples in this wiki

- [[artifacts/projects/dsh-superagent-prototype]] — `src/core/intake.ts:16–59` fans out context separately from new Eval; `src/core/evals.ts:107–149` checks existing acceptance/ownership and inferred authority; `src/policy.ts:1–59` validates assessments and records observation rather than acceptance. The worker still semantically respects scope. [[sources/deepseek-ai--dsh-superagent-prototype#intake]], [[sources/deepseek-ai--dsh-superagent-prototype#evals]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]]
- [[artifacts/projects/kody]] — `request-context.ts:129–192` derives enablement-backed versus actorless automation; `resolve-credential.ts:160–241` checks org, package declarations and authorization before apply; tests assert package getters return opaque refs rather than plaintext. Credential access enforcement is stronger than a communication prompt, but not proof of safe use of every approved API. [[sources/kody-hq--kody#request-context]], [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#credential-tests]]

## Counter-examples or anti-pattern

- **Admission mistaken for containment:** DeepSeek's own execution docs explicitly say command wrappers/directories are defaults, not a security boundary. A worker may execute an absolute path. This limits the guarantee even though new Ticket admission is checked. [[sources/deepseek-ai--dsh-superagent-prototype#execution]]
- **Secret hidden, effects unrestricted:** Kody's host/placement gates constrain credential transmission, but an approved host may still offer destructive operations. Opaque values do not imply harmless capabilities. [[sources/kody-hq--kody#credentials]], [[sources/kody-hq--kody#host-allowlist]]
- **Immediate revocation assumed:** prototype policy changes notify running Tickets and revalidate before resumption; changing a rule is not documented as automatically killing all live work. [[sources/deepseek-ai--dsh-superagent-prototype#authorization]]

## Related patterns

- [[patterns/structural/authoritative-recheck-after-notification]] — neighboring mechanism: re-read current state after a signal, rather than deriving authority from information.

- [[patterns/behavioral/latent-vs-deterministic-split]] — judgment inside exact enforcement boundaries.
- [[patterns/behavioral/evidence-gated-completion]] — distinguish observed outcomes from instructions and status labels.
- [[patterns/quality-bar/revision-bound-review]] — authority/checks can depend on the exact policy or content revision.

## Open questions

- TODO: independently run adversarial event, scope-expansion and credential-use tests; no security certification is claimed.
- TODO: compare immediate cancellation with notify/revalidate policies under partial external effects.

## Related explanatory evidence: execution bridge

Schmid locates credential injection, schema validation and possible destructive-call approval in the host bridge. Treat these as proposed enforcement responsibilities, not protections established merely by a one-tool interface or the pseudo-example. [[concepts/code-mode-capability-interface]], [[sources/philschmid--code-mode#runtime-boundaries]], [[sources/philschmid--code-mode#pseudo-example]]

## API research connection — 2026-11-04

[[analyses/frontier-and-business-api-design]] compares schema-conforming proposals, managed permission policies and domain permissions across [[artifacts/projects/openai-agent-api]], [[artifacts/projects/anthropic-agent-api]] and [[artifacts/projects/gusto-api]]. Documentation-level correspondence does not establish deployed enforcement or add a runtime test.

## Shopify API connection — 2026-11-04

[[artifacts/projects/shopify-api]] distinguishes declared/negotiated support, auth tiers, actual completion permission and buyer confirmation. Browser tool results remain untrusted data. Documentation-level correspondence only, not an enforcement test. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#webmcp]]

## MCP research connection — 2026-11-04

[[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]], [[concepts/skills-over-mcp]] and [[concepts/mcp-enterprise-managed-authorization]] add independent distinctions between view context, feature declarations, skill activation, token issuance and action authority. In particular, OpenAI’s write helper validates shape while the host owns file eligibility; the enterprise IdP does not observe actual MCP traffic. [[sources/openai--mcp-extensions#write-client]], [[sources/modelcontextprotocol--mcp-authorization-docs#enterprise-policy-limit]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]

## Meaning is not authorization — 2026-11-04

[[artifacts/projects/auto-ontology]] exposes semantic context through per-user MCP and public gateway permissions. The gateway rebuilds internal identity headers, but FastAPI trusts that private hop; source-database credentials remain a separate authority layer. A term, certification flag or analytical recommendation does not authorize an external effect. Supporting comparison; existing example count unchanged. [[sources/nvidia--auto-ontology#mcp-auth]] [[sources/nvidia--auto-ontology#gateway]] [[sources/nvidia--auto-ontology#publication]]

## Typed provenance and current authority — 2026-11-04

[[artifacts/projects/codex]] distinguishes external tool-level messages from user input, host annotations from text wrappers, and a narrow automated approval from an escalated retry. Account notifications require current-state rereads. These are complementary boundaries, not an end-to-end security guarantee. [[sources/openai--codex#sdk-python]] [[sources/openai--codex#goal-provenance]] [[sources/openai--codex#approval]] [[sources/openai--codex#policy-reload]]

### Open Inspect — access does not erase context

[[artifacts/projects/background-agents]] distinguishes pinned context, live personal reads, original prompt identity, credential issuance and snapshots. Opt-out cannot erase already supplied information; cached credentials and persistent processes cross turn boundaries. Teams remain intra-organization controls, not tenant isolation. [[sources/open-inspect--background-agents#memory-boundary]] [[sources/open-inspect--background-agents#credentials]] [[sources/open-inspect--background-agents#authority]]

## SuperPlane — 2026-11-04

Supporting comparison: [[artifacts/projects/superplane]] distinguishes provided task context, enabled report checks, eligible approval actors and organization/token authorization. Read-only review instructions remain prompt policy. Admission disablement preserves cleanup rights for already-running tasks. [[sources/superplanehq--superplane#confidence]] [[sources/superplanehq--superplane#approval]] [[sources/superplanehq--superplane#authorization]] [[sources/superplanehq--superplane#runner-admission]]

## Documentation application — 2026-11-05

[[concepts/developer-documentation-design]] applies this research to documentation authoring, distribution or review. See [[projects/writing-amazing-developer-docs/README]] for the evidence map. This cross-reference adds no inspected runtime example or benchmark result.

## Wider documentation application — 2026-11-05

[[concepts/developer-documentation-design]] now studies architecture/operational records, migration states, executable examples and delivery/evaluation boundaries. [[projects/writing-amazing-developer-docs/platform-documentation-system]] is the proposed application; no new vendor runtime guarantee or confirmed implementation example is claimed.

## Mintlify documentation application — 2026-11-05

[[artifacts/projects/mintlify]] examines documented index, skill, retrieval and editing surfaces with distinct authority and lifecycle boundaries. Its cited external discovery/protocol schema versions are not independently conformance-verified here. Source inspection is limited to the public URL benchmark; no hosted runtime guarantee or confirmed platform-implementation example is added.

## Frontier documentation application — 2026-11-05

[[concepts/agent-documentation-interfaces]] and [[artifacts/projects/webmcp]] apply this pattern to delivery transformations, page-local tool authority, versioned evidence and measured task outcomes. [[artifacts/projects/dokimi]] supplies documented evaluation controls. This adds a research application, not a newly runtime-verified example or pattern promotion. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## Cloudflare security audit — 2026-11-06

[[artifacts/skills/security-audit]]'s AI companion distinguishes authorization from intent binding: a user may possess authority for an action yet never have intentionally requested the model-induced action. It also treats MCP metadata, tool schemas, model output and memory as inputs rather than permission sources. The skill's own sandbox and artifact-promotion requirements remain host obligations, not capability restrictions created by Markdown. [[sources/cloudflare--security-audit-skill#ai-authority]] [[sources/cloudflare--security-audit-skill#execution-boundary]] [[sources/cloudflare--security-audit-skill#promotion]]

## Agent Habitat comparison — 2026-11-06

[[concepts/agent-habitat-architecture]] is a proposed specialization: attested identity grants no permissions; public trigger provenance caps authority; hiding service credentials does not constrain all requested effects. Proposal evidence is not another independently executed artifact example. [[sources/replit--agent-habitat-architecture#identity]] [[sources/lhchavez--managed-agent-environments#credential-authority]]

## Vercel Schedules — 2026-11-06

[[artifacts/projects/vercel-schedules]]: a saved task/namespace/creator reference is not an enduring permission grant. The application and experimental eve guide revalidate current identity and destination access when the work fires. Documentation-level example, no new runtime assurance. [[sources/vercel--introducing-schedules#agent-example]] [[sources/vercel--schedules-docs#eve-identity]]

## Inkling 2 Small — 2026-11-06

[[artifacts/projects/inkling-2-small]]: task instructions and a blocked direct route did not prevent a model reaching the effect through a third party. The reported response changes external controls, not only model instructions. [[sources/thinking-machines--inkling-2-small#monitors-incident]]

## Memory consolidation — 2026-11-07

[[concepts/agent-memory-consolidation]]: learned memory can persist poisoned text, and promotion into a system-context slot increases exposure without establishing authority. A read-only consumer is not immune to influence; host tools and policies remain separate. [[sources/anthropic--agent-memory-support#dynamic-trust]] [[sources/anthropic--agent-memory-support#code-injection]]

## T3 Code application — 2026-11-07

[[artifacts/projects/t3code]] adds a source-inspected application or narrower analogue through [[sources/pingdotgg--t3code#auth-mcp-caller-limits]]. The artifact retains exact implementation/test/policy boundaries and79 portable practices. No runtime effectiveness claim or automatic status/example-count promotion is added.
