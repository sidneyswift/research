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

## Meaning is not authorization — 2026-11-04

[[artifacts/projects/auto-ontology]] exposes semantic context through per-user MCP and public gateway permissions. The gateway rebuilds internal identity headers, but FastAPI trusts that private hop; source-database credentials remain a separate authority layer. A term, certification flag or analytical recommendation does not authorize an external effect. Supporting comparison; existing example count unchanged. [[sources/nvidia--auto-ontology#mcp-auth]] [[sources/nvidia--auto-ontology#gateway]] [[sources/nvidia--auto-ontology#publication]]

## Typed provenance and current authority — 2026-11-04

[[artifacts/projects/codex]] distinguishes external tool-level messages from user input, host annotations from text wrappers, and a narrow automated approval from an escalated retry. Account notifications require current-state rereads. These are complementary boundaries, not an end-to-end security guarantee. [[sources/openai--codex#sdk-python]] [[sources/openai--codex#goal-provenance]] [[sources/openai--codex#approval]] [[sources/openai--codex#policy-reload]]

### Open Inspect — access does not erase context

[[artifacts/projects/background-agents]] distinguishes pinned context, live personal reads, original prompt identity, credential issuance and snapshots. Opt-out cannot erase already supplied information; cached credentials and persistent processes cross turn boundaries. Teams remain intra-organization controls, not tenant isolation. [[sources/open-inspect--background-agents#memory-boundary]] [[sources/open-inspect--background-agents#credentials]] [[sources/open-inspect--background-agents#authority]]
