---
domain: concepts
type: concept
name: code-mode-capability-interface
creators: "[[creators/kody-hq]], [[creators/philipp-schmid]]"
sources: "[[sources/kody-hq--kody]], [[sources/philschmid--code-mode]]"
status: emerging
last-reviewed: 2026-11-03
---

# Code Mode capability interface

> Discover just the capabilities a task needs, then compose code that calls them behind a small stable tool interface.

## What it is

Kody puts a large capability graph behind progressive `search` and module-based `execute`, rather than exposing every operation as a separate always-loaded MCP tool. Its pinned registration also exposes `api(operationId, params)` for one direct operation without a sandbox, making the actual MCP tool count three. Search moves from domain overview to ranked actions to exact entity contracts; execution composes typed capability calls and package imports. The compactness is at the model/host boundary, while the backend still contains a substantial registry, runtime, identity and authorization system. [[sources/kody-hq--kody#intent]], [[sources/kody-hq--kody#mcp-surface]], [[sources/kody-hq--kody#search]], [[sources/kody-hq--kody#execute-contract]]

Schmid describes the model writing scripts against typed host functions, composing dependencies and emitting selected results. A single model-visible execution tool still fronts many backend operations; Kody’s separate discovery and direct-dispatch tools show that the mechanism does not require a literal tool count of one or two. Direct dispatch selects one operation; it is not code composition. [[sources/philschmid--code-mode#typed-interface]], [[sources/kody-hq--kody#mcp-surface]]

## Where it came from

Kody's intent document explicitly credits Cloudflare's Code Mode approach. This page combines **Kody's implementation** with Philipp Schmid's 2026-11-01 explanatory article; neither establishes original invention, and Cloudflare's original remains an ingest gap. [[sources/philschmid--code-mode#root]] The existing [[patterns/behavioral/latent-vs-deterministic-split]] covers the broader division of judgment and code; this concept isolates on-demand capability discovery and code composition as an interface mechanism. [[sources/kody-hq--kody#intent]]

## Why it matters

Large connected tool inventories can be represented by a small reusable interaction vocabulary. Once the plan is known, code can call several operations without exposing every intermediate response to the model. Reusable packages can turn repeated procedures into typed code that works across hosts. **Potential** token/latency benefit needs measurement: compilation, discovery, registry loading and failures can dominate a short task. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#registry]]

## Evidence & claims

- **Documentation:** broad queries return domain summaries, precise searches rank actions, entity lookup supplies exact schemas/examples. Text and structured channels are intended to retain equivalent actionable information. [[sources/kody-hq--kody#search]]
- **Implementation:** lazy built-in registry plus synthesized remote MCP domains, cached with owner/server state and filtered for callers/features. [[sources/kody-hq--kody#registry]]
- **Implementation correction, 2026-11-03:** the same pinned commit registers `search`, `execute` and `api`. The latter invokes one HTTP/API operation by `operationId` and params without sandbox/execute quota; some discovered capabilities remain execute-only. No latency benchmark or live tool listing was run. [[sources/kody-hq--kody#mcp-surface]]
- **Documentation:** module source is separate from varying `params`; static package exports are publish-verified, visible to dependency tracking and snapshotted in dependents. [[sources/kody-hq--kody#execute-contract]]
- **Implementation:** keyed runs return existing in-progress/retained outcomes instead of launching a duplicate; this makes the compact interface resumable across transport limits. [[sources/kody-hq--kody#execute-replay]]
- **Implementation:** credential resolution/gateway use sites hold enforcement outside generated code; reducing tool count does not remove permission checks. [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#fetch-gateway]]

### Article evidence added 2026-11-02

- **Illustrated interface:** schema-derived declarations expose argument and return shapes before execution; optional catalog search avoids eagerly loading all signatures. This is an interface sketch, not proof of universal schema fidelity. [[sources/philschmid--code-mode#workflow-composition]], [[sources/philschmid--code-mode#typed-interface]]
- **Illustrated data path:** dependent calls, parallel reads and filtering happen inside the runtime; only explicitly emitted text or media enters the next model turn. Host-side key/value helpers retain intermediate data across turns. That state mechanism alone establishes no crash durability. [[sources/philschmid--code-mode#typed-interface]]
- **Proposed enforcement site:** the host bridge can inject credentials, validate calls and seek approval; merely exposing typed functions does not implement those checks. [[sources/philschmid--code-mode#runtime-boundaries]]
- **Author-reported, unverified:** ecosystem adoption and Factory accuracy/cost figures have not been independently checked; the pseudo-example’s model/API identifiers and execution isolation have not been tested. [[sources/philschmid--code-mode#adoption-claims]], [[sources/philschmid--code-mode#pseudo-example]]

## Patterns demonstrated

- [[patterns/behavioral/latent-vs-deterministic-split]] — model plans composition; registry/credential code validates and executes contracts. [[sources/kody-hq--kody#registry]], [[sources/kody-hq--kody#credential-resolution]]
- [[patterns/composition/single-source-multi-surface-distribution]] — reusable package modules across host and background surfaces. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#workflows]]
- [[patterns/behavioral/context-is-not-authority]] — discovered metadata and generated code do not independently grant credential access. [[sources/kody-hq--kody#credential-resolution]]
- Code Mode itself is tracked here as a concept until independent implementations are investigated; the already-cloned Executor source is a candidate, not a counted example.

## Tensions & counter-arguments

A small tool menu is not necessarily legible authorization: one `execute` can send, delete or revoke. A workflow can fail after partial external effects. Host/credential approval is narrower than approval of every operation on that host. Agents also need code capability, exact contracts, useful error categories and durable run handles. These costs are visible in Kody's gateway/replay machinery and its explicit destructive annotation, not merely hypothetical objections. [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#fetch-gateway]]

Static snapshots improve repeatability but require dependent republishing; ad hoc current-version resolution improves freshness but can change behavior between retries. Runtime portability across MCP hosts still depends on the server and its deployed runtime. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#architecture]]

Schmid's headline is stronger than his conclusion, which explicitly leaves universal adoption unresolved. His contrast with standard tools also acknowledges independent batching; the useful distinction is scripting dependencies and controlling returned context, rather than asserting every other harness permits only one action. The minimal example mocks APIs and uses `node:vm`, with a separate comment recommending other runtimes for untrusted code; it cannot establish production isolation. These are limits of the captured evidence, not runtime test results. [[sources/philschmid--code-mode#workflow-composition]], [[sources/philschmid--code-mode#pseudo-example]], [[sources/philschmid--code-mode#caveats]]

## What we'd steal

- ★ **Progressive capability contracts:** overview → ranked action → exact entity; inline signatures only when confidence is high. Use for large internal tool graphs; evaluate discovery misses. [[sources/kody-hq--kody#search]]
- **Mirror actionable information in text and structured output:** prevent a host's channel preference from hiding required call fields. [[sources/kody-hq--kody#search]]
- **Separate stable module code and parameters:** reuse execution graphs and make varying inputs reviewable. [[sources/kody-hq--kody#execute-contract]]
- **Bundle calls only after the plan is clear:** use code for exact composition; return to the person/model when results change scope or require a decision. [[sources/kody-hq--kody#execute-contract]]
- **Graduate repeated code into published exports:** typed contracts plus explicit adoption of snapshots; don't distribute parallel handwritten host copies. [[sources/kody-hq--kody#execute-contract]]
- ★ **Keep authority behind the facade:** generated code calls narrow credential/capability use sites; give errors enough metadata for repair without returning secrets. [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#host-allowlist]]
- **Make a long operation observable through a durable handle:** keyed retry reads the same run; durable workflow retry remains a separate mechanism. [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#workflows]]
- **Measure the whole path:** discovery rounds, contract accuracy, bundling, sandbox startup, returned context, failed retries and end-to-end completion. Kody's phase timing makes this an experiment we can run, not a benefit already established. [[sources/kody-hq--kody#execute-contract]]
- **Allow a compact direct-dispatch path when measurement justifies it:** compare one-operation dispatch with composed execution instead of optimizing for a sacred tool count. Kody implements both, but the relative benefit remains unmeasured here. [[sources/kody-hq--kody#mcp-surface]]

### Additional portable choices from Schmid

- ★ Emit the smallest useful result after in-runtime joins/filtering; retain identifiers or evidence handles so summaries remain auditable. The emission mechanism is sourced; audit handles are our design inference. [[sources/philschmid--code-mode#typed-interface]]
- Supply return types as well as inputs so generated code can compose dependencies before seeing outputs. [[sources/philschmid--code-mode#workflow-composition]]
- Expose searchable capability metadata when full declarations become costly. [[sources/philschmid--code-mode#typed-interface]]
- Use native objects, asynchronous fan-out and exception handling instead of shell string protocols for structured APIs. [[sources/philschmid--code-mode#runtime-boundaries]]
- Attach actual images/audio through dedicated emission helpers. [[sources/philschmid--code-mode#typed-interface]]
- Retain large intermediate values in host memory across turns; document lifetime and cleanup separately. [[sources/philschmid--code-mode#runtime-boundaries]]
- Keep credentials and per-call policy in the host bridge, including checks for destructive operations. [[sources/philschmid--code-mode#runtime-boundaries]]
- Audit existing skills and CLIs for structured input/output compatibility before migrating orchestration. [[sources/philschmid--code-mode#caveats]]
- Prototype with mocked host functions to expose the interface, while labeling what the example does not test. [[sources/philschmid--code-mode#pseudo-example]]

## Timeline

- 2026-11-02 — Kody source investigated and concept added; no comparative runtime evaluation.

- 2026-11-02 — Ingested Schmid’s 2026-11-01 article; extended this page after overlap review. Adoption/performance claims remain author-reported. [[sources/philschmid--code-mode#root]]

- 2026-11-03 — Followed the existing pinned registration path and corrected the actual three-tool surface: `search`, `execute`, `api`. This is additional inspection of the same source revision, not an upstream refresh or tested performance claim. [[sources/kody-hq--kody#mcp-surface]]

## Related

- [[artifacts/projects/shopify-api]] — negotiated schemas and browser/server commerce tools provide a complementary discovery/composition case.

- [[projects/designing-apis-for-agents/README]] — ongoing research group; questions, evidence map, and future investigations.

- [[artifacts/projects/kody]] — full project study and exhaustive mechanism ledger.
- [[concepts/super-agent-architecture]] — coordination can sit above a compact capability substrate.
- [[concepts/workspace-skill-distribution]] — portable behavior distribution is related but distinct from executable state/capability hosting.

## Open questions

- TODO: ingest Cloudflare's primary Code Mode explanation and independently investigate another implementation.
- TODO: compare static tools against search/execute on equivalent tasks, permission scopes and model budgets.
- TODO: examine how approvals bind to composed code and changed parameters across hosts.

- TODO: independently verify the article’s adoption/benchmark claims and current API examples before using them for a migration recommendation. [[sources/philschmid--code-mode#adoption-claims]], [[sources/philschmid--code-mode#pseudo-example]]

## API design connection — 2026-11-04

[[concepts/business-platform-api-design]] — Agent composition needs explicit side-effect and asynchronous lifecycle contracts on the capabilities being composed.

## Cross-system API research — 2026-11-04

[[analyses/frontier-and-business-api-design]] compares nine documented systems and preserves the distinction between capability intent, presentation, execution and business outcome. [[concepts/agent-api-learning-and-evolution]] separates training familiarity from current interface context and observable task performance. The synthesis remains draft; no runtime or agent-success guarantee is added to this page.

## MCP research connection — 2026-11-04

[[concepts/model-context-protocol]] supplies protocol/transport context for compact facades; [[concepts/skills-over-mcp]] delivers workflow instructions separately. [[artifacts/projects/openai-mcp-extensions]] adds view-scoped Desktop WebMCP tools, a distinct layer from server-side code composition. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]], [[sources/openai--mcp-extensions#webmcp]]

## Executor's general capability implementation — 2026-11-04

Executor normalizes provider operations into plugin-produced definitions with names, descriptions, input/output schemas and policy hints. Connection create/refresh stamps them with integration/owner/connection addresses and persists them; provider-specific configuration and credentials stay outside the public tool definition. OpenAPI operations compile into this representation with separate HTTP bindings. [[sources/rhys-sullivan--executor#tool-contract]], [[sources/rhys-sullivan--executor#plugin-boundary]], [[sources/rhys-sullivan--executor#openapi]], [[sources/rhys-sullivan--executor#persisted-catalog]]

The sandbox is deliberately generic: a lazy `tools` proxy sends `{path,args}` to the host invoker. Search and exact description discover the stored tools; ordinary calls pass through policy and connection-credential resolution into the owning plugin. The inspected search default scores tokens/phrases, not an automatically learned business ontology. Generalizing execution and reconciling business meanings remain separate responsibilities. The host has modes and additional tool surfaces; exactly two top-level tools is not a source-wide invariant. [[sources/rhys-sullivan--executor#sandbox]], [[sources/rhys-sullivan--executor#discovery]], [[sources/rhys-sullivan--executor#policy-and-invocation]]

The public OpenAPI compilation and request-building helpers were subsequently exercised against Flex's pinned API contract using isolated published-package fixtures (1.6.7 and 1.6.11), then reused in Flex MCP PR #66. The consuming application retains full input/output validation, fixed-origin transport, caller identity and reviewed admission. Local and hosted review found that the 1.6.7 compiler skips chained or JSON Pointer-escaped parameter references; Flex resolves admitted local references before compilation and rejects unresolved/external/cyclic references. Required-argument and serialized-request regression cases cover operation- and path-level references. These fixture/source checks do not establish provider execution or actual-client qualification. [[sources/rhys-sullivan--executor#openapi]]
