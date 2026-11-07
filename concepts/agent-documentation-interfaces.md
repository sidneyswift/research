---
domain: concepts
type: concept
name: agent-documentation-interfaces
creators: [Mintlify, Upstash, Fern, ReadMe, Intel, Anthropic, WebMCP community]
sources: [frontier-docs--platforms-20261105, frontier-docs--webmcp-20261105, frontier-docs--empirical-20261105, frontier-docs--tool-design-evaluation-20261105]
status: emerging
last-reviewed: 2026-11-05
---

# Agent documentation interfaces

> Documentation for an agent includes how it discovers a capability, obtains the right contract, learns its use, performs an action and checks what happened.

## What it is

This page owns **delivery and interaction contracts for agent-facing knowledge**. [[concepts/developer-documentation-design]] owns general writing, information architecture and maintenance; [[concepts/business-platform-api-design]] owns business query/command/workflow contracts. This is a separate role: interfaces that bring those contracts into a particular agent's working context. The evidence below shows that “docs for agents” can mean an index, a source retriever, a generated answer, a skill, a tool definition or an executable application interface. Those objects have different correctness and authority boundaries. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]]

## Where it came from

This is our descriptive grouping, not a claimed new standard or a vendor-coined term. It extends the existing [[artifacts/projects/mintlify]] and [[sources/cloudflare--docs-for-agents#root]] investigations with three other documentation platforms, WebMCP's draft/browser contracts, Intel's evaluation methodology, Anthropic's tool-design reports and independent API-agent studies. Current product documentation was captured 2026-11-05; research publication dates and versions are recorded on their source pages. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--empirical-20261105#root]] [[sources/frontier-docs--tool-design-evaluation-20261105#root]]

## Evidence & claims

### Classify by what the interface does

| Interface role | Observed example | What must be checked |
| --- | --- | --- |
| Inventory/navigation | Fern scoped llms indexes and API catalogs | Coverage, locale/version, private inventory, redirects |
| Evidence retrieval | Context7 snippets/fetch; Fern self-hosted search/fetch | Source identity, served version, limits, omissions, continuation |
| Answer generation | Fern hosted site MCP's single RAG answer tool | Which evidence supports the answer, synthesis errors, costs |
| Procedural guidance | Fern skill bundles; Mintlify skill surfaces | Prerequisites, selection, artifact identity and authority |
| Business API execution | ReadMe Project MCP execute-request | Target server, actual caller credentials, allowed operation/effects |
| Browser interaction | WebMCP callbacks and browser form tools | Origin/frame, current state, navigation, user interaction, cancellation |
| Administration/authoring | Mintlify Admin MCP | Content revision, branch/publish semantics, credential scope |

These rows are **roles**, not mutually exclusive product categories or a requirement to build seven services. Fern itself distinguishes hosted and self-hosted site MCP from organization management and generated API MCP. ReadMe deliberately combines reference discovery with API execution. A server's name or MCP transport does not disclose its authority. [[sources/frontier-docs--platforms-20261105#fern-mcp]] [[sources/frontier-docs--platforms-20261105#readme-mcp]] [[sources/mintlify--agent-documentation-docs#admin-mcp]]

### Retrieval has a contract beyond returned text

Context7 documents both automatic v3 search and explicit v2 source resolution followed by retrieval. Automatic convenience need not remove lower-level control. Machine outputs can distinguish requested versus served versions, fallback reasons and operational partial results. Its `X-Context7-Search-Status: partial` response header is not a relevance score. Most significantly, requesting an unindexed public-GitHub version can queue indexing while returning available documentation: retrieval can initiate background work. Do not design a business integration around the assumption that a GET, “search” name or documentation server is operationally inert. These are documented side effects, not effects observed through execution here. [[sources/frontier-docs--platforms-20261105#context7-api-guide]] [[sources/frontier-docs--platforms-20261105#context7-search-contract]]

For our platform, a proposed read contract should specify evidence identity, version, completeness, fallback and background effects. If a read can refresh or enqueue work, disclose it explicitly and give callers a way to request the exact stored version when required. This is a design inference; we have not established Context7's indexing idempotency, job visibility or lifecycle guarantees. [[sources/frontier-docs--platforms-20261105#context7-search-contract]]

Source text and generated answers also require different verification. Fern's hosted MCP synthesizes an answer while its self-hosted version offers keyword search and page fetching. Context7 JSON separates evidence snippets and source metadata. A caller that needs exact enum values, permission scope or retry guarantees should be able to reach an authoritative contract, even if its first interaction is conversational. [[sources/frontier-docs--platforms-20261105#fern-mcp]] [[sources/frontier-docs--platforms-20261105#context7-search-api]]

### Markdown is a transformation, not a completeness guarantee

Fern flattens endpoint schemas into textual sections, omitting internal schema names and reference chains; changelog Markdown contains only the latest 20 public entries and points onward. ReadMe adds OpenAPI server/security context to relevant Markdown and useful index routes to missing-page responses. These choices can make content usable, but a format checkbox does not establish semantic parity. Test that auth, required fields, optionality, pagination and failure conditions survive conversion; keep the full specification reachable. [[sources/frontier-docs--platforms-20261105#fern-markdown]] [[sources/frontier-docs--platforms-20261105#readme-llms-upgrade]]

Fern declines a full-corpus llms-full export; Mintlify supplies hierarchical bounded indexes and broader exports. These are different delivery choices, not evidence for one universal file-size rule. Preserve useful hierarchy, descriptions, stable URLs, version/locale paths and recoverable 404s. Test the actual reader's traversal rather than assuming every agent recognizes an informal discovery convention. [[sources/frontier-docs--platforms-20261105#fern-llms]] [[sources/mintlify--agent-documentation-docs#llms]]

### Descriptions, examples and errors are runtime documentation

Anthropic's tool-design article treats names, namespaces, parameter descriptions, result size and actionable errors as agent-facing design. Its later tool-use report adds on-demand discovery and concrete call examples. The article's internal parameter-handling test reports 72%→90% accuracy with examples; this is vendor-reported, with insufficient public experimental detail in the capture to generalize the effect. Examples cost context, and deferred discovery adds lookup latency. Neither mechanism establishes a universal ideal tool count. [[sources/frontier-docs--tool-design-evaluation-20261105#anthropic-writing-tools]] [[sources/frontier-docs--tool-design-evaluation-20261105#anthropic-advanced-tools]]

Independent evidence adds counterexamples. The API-demonstrations study shows summaries can omit an identifier prefix, generated summaries can incorrectly mark optional parameters as required, and more demonstrations can overflow context. One narrow tau-bench repair inserts the correct order-ID format and increases success 10%→49% in that specific condition; the original docs score 78% on the same subset. This supports explicit validated format rules and useful validation errors, not replacing contracts with a large bag of examples. [[sources/frontier-docs--empirical-20261105#api-learning]]

For a vendor-reconciliation workflow, a proposed operation page should name the business goal, required identifiers and how to obtain them, a minimal call, an optional-parameter example, side effects, acceptance/result semantics and recovery. Parameter names and validation should come from the maintained contract; generated explanation and examples need a check against it. A tool named “start reconciliation” should not imply completed reconciliation. This connects the runtime guidance evidence to the existing [[concepts/business-platform-api-design]] responsibility split. [[sources/frontier-docs--tool-design-evaluation-20261105#anthropic-writing-tools]] [[sources/frontier-docs--webmcp-20261105#design-practices]]

### WebMCP adds a stateful browser surface

[[artifacts/projects/webmcp]] owns the detailed version/lifecycle study. Its current Community Group draft extends `Document`, exposes structured page tools and defines origin-related gates. Chrome also documents declarative form tools, but the repository says that proposal is separate from the current specification. These are not equivalent maturity claims. Playwright's current introductory API text still uses `navigator.modelContext`, while the captured draft and Chrome guide use `document.modelContext`. This is observed documentation disagreement, not a reproduced runtime failure. [[sources/frontier-docs--webmcp-20261105#draft-status]] [[sources/frontier-docs--webmcp-20261105#declarative-proposal]] [[sources/frontier-docs--webmcp-20261105#documentation-drift]]

A page tool can act with current application state and reflect a result in the visible UI. That is distinct from a backend job that must continue after the tab closes. Registration removal, execution cancellation, page navigation and business rollback are separate lifecycle events. An operation can disappear while already-running work continues; navigation can interrupt the expected result channel. Document the commit point and how to recover outcome identity. [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]] [[sources/frontier-docs--webmcp-20261105#tool-lifecycle]]

The same application service can serve UI controls, agent tools and tests, reducing divergent behavior. Browser origin gates and metadata hints still do not replace backend permission checks or transaction-specific approval. Read-only retrieval can disclose private content; consequential hints are not enforced business authorization. [[sources/frontier-docs--webmcp-20261105#design-practices]] [[sources/frontier-docs--webmcp-20261105#origin-gates]] [[sources/frontier-docs--webmcp-20261105#tool-author-security]]

### Training familiarity is a test variable, not a roadmap guarantee

The user's hypothesis is plausible: familiar public APIs and newer/internal interfaces may need different amounts of explicit guidance. Agent-Diff's relevant-docs condition improves pooled binary pass by about seven percentage points, but its assertion-weighted score gain is only 2.4 points with weaker support. Its small Box Hub subset benefits more than the older non-Hub subset. The authors interpret the release-date difference through training cutoffs; actual inclusion in model training was not observed, and the task groups differ. This is evidence consistent with a familiarity effect, not proof of the cause. [[sources/frontier-docs--empirical-20261105#agent-diff]]

ReadMe explicitly says machine-readable docs do not change training data or force providers to fetch them. Intel Dokimi describes artifact/model-specific probes that classify added, redundant, degraded or still-missing knowledge; those classifications do not reveal training membership either. No captured study establishes what agents will know in one, five or ten years. A defensible evolution strategy is to keep authoritative runtime contracts discoverable and repeat the same task evaluation across model upgrades. [[sources/frontier-docs--platforms-20261105#readme-ai-ready]] [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-measurement]]

## Evaluation that answers the right question

A proposed platform evaluation should separate: discovery of the right capability; retrieval of the exact governing contract; correct call construction; authorized execution; verified task state; and unintended effects. A URL benchmark tests the first portion. An answer judge tests a different portion. A state-diff benchmark or executable task can test actual changes within its environment, while still not proving a production/customer outcome. [[sources/mintlify--docs-url-discovery-bench#grading]] [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]] [[sources/frontier-docs--empirical-20261105#agent-diff]]

Dokimi documents fixed questions/models, source provenance, separate model roles and recommended answer/judge model independence, grounded rubrics, retrieval-hit accounting and repeated runs. It distinguishes forced context from a skill that must first be discovered. Its trust gate can PASS with checks marked not measured, so retain individual checks and denominators. The with-docs treatment also changes the answer instruction; isolating an editorial change requires matching that prompt across documentation revisions. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]] [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-measurement]]

Beyond Browsing supplies one concrete hierarchical design: a short endpoint list followed by exact endpoint-document lookup for larger APIs. Hybrid browser/API agents outperform its browser baseline, but the experiment changes available actions as well as documentation. It does not isolate the benefit of two-stage discovery. Treat it as an observed workable mechanism and a reminder to distinguish missing capability from missing guidance. [[sources/frontier-docs--empirical-20261105#web-api]]

## Tensions & counter-arguments

- Bigger context can help unfamiliar APIs while introducing irrelevant evidence, misleading examples and selection cost. No single source establishes a universal cutoff. [[sources/frontier-docs--empirical-20261105#agent-diff]] [[sources/frontier-docs--empirical-20261105#api-learning]]
- Generated answers reduce reader work but add an inference layer between caller and authoritative contract. Retain source-level escape routes. [[sources/frontier-docs--platforms-20261105#fern-mcp]]
- Dynamic browser metadata can track state while creating stale-contract/navigation races. Validate again at execution. [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]]
- OpenAPI catalogs, skill manifests and server cards are product-documented conventions here; their linked standards were not independently audited in this pass. Runtime interoperability remains untested. [[sources/frontier-docs--platforms-20261105#fern-catalog]] [[sources/frontier-docs--platforms-20261105#fern-skills]]

## Patterns demonstrated

- [[patterns/composition/single-source-multi-surface-distribution]] — authored knowledge/specifications rendered into scoped indexes, Markdown and tool surfaces; semantic parity still needs checking. [[sources/frontier-docs--platforms-20261105#fern-markdown]]
- [[patterns/behavioral/context-is-not-authority]] — retrieved knowledge, skill digests and browser metadata are not permission to execute business effects. [[sources/frontier-docs--webmcp-20261105#origin-gates]]
- [[patterns/behavioral/evidence-gated-completion]] — discovered URL, accepted invocation, judged answer and verified state are different completion claims. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]
- [[patterns/quality-bar/revision-bound-review]] — served versions and dated protocol/browser contracts need explicit receipts. [[sources/frontier-docs--platforms-20261105#context7-search-contract]] [[sources/frontier-docs--webmcp-20261105#documentation-drift]]

These are applications/analogues; documentation inspection adds no independently executed implementation examples or automatic pattern promotion.

## What we'd steal

- ★ Classify discovery, evidence retrieval, synthesized answers, guidance, execution and administration separately.
- ★ Return requested/served version and explicit fallback/partial reasons.
- ★ Test final task state and unintended effects, alongside selection and token cost.
- Preserve a lower-level source-selection route beside automatic search.
- Declare background indexing, refresh and analytics side effects.
- Link every generated answer back to inspectable authoritative evidence where supported.
- Keep scoped indexes and stable continuation paths rather than assume full-corpus loading.
- Make Markdown transformations, omitted history and schema flattening explicit.
- Return useful Markdown 404s with paths to the correct index.
- Test locale/version/private-content parity across every representation.
- Separate private-document tokens from business API credentials.
- Separate discovery visibility from authorization to fetch or act.
- Treat integrity digests as artifact identity, not approval of its instructions.
- Include minimal, full and deliberately omitted optional inputs in validated examples.
- State exact identifier/date conventions and prerequisite lookups.
- Put recoverable guidance in validation errors and truncated responses.
- Measure deferred-discovery latency as well as saved context.
- Keep UI, tools and tests on shared application services where appropriate.
- Bind consequential previews to current resource/state and revalidate at confirmation.
- Distinguish unregistration, cancellation, navigation and committed business outcome.
- Pin browser/host/tooling versions and record official documentation conflicts.
- Evaluate known public, novel and internal API tasks separately.
- Rebaseline model upgrades rather than assuming training-data progress.
- Preserve failure/exclusion denominators, grounded rubric identity and missing measurements.
- Test discretionary context discovery separately from forced prompt injection.
- Keep source instructions as evidence until authorized by the user/task.

## Timeline

- 2026-11-05 — Expanded the Mintlify investigation across three documentation platforms, WebMCP, tool-design guidance and three independent API-agent papers. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--empirical-20261105#root]]

## Related

- [[projects/writing-amazing-developer-docs/README]] — evidence hub and practical authoring work.
- [[artifacts/projects/context7]], [[artifacts/projects/fern]], [[artifacts/projects/readme]] — delivery and authority case studies.
- [[artifacts/projects/webmcp]] — browser contract, lifecycle and drift.
- [[artifacts/projects/dokimi]] — documented evaluation design and limits.

## Open questions

- Which minimum context package reliably supports a real cross-business workflow after a model upgrade?
- Can every evidence result carry a retrievable exact revision, including fallback and generated answers?
- What is the measurable cost of wrong-version evidence versus no evidence?
- Which task failures come from missing APIs, inaccurate docs, retrieval misses, planning or permission boundaries?
- How should explicit refresh/index jobs coexist with query-only calls when background work has material cost?
