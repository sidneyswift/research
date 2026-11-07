---
domain: artifacts
subdomain: projects
type: project
name: webmcp
creator: "[[creators/w3c]]"
source: "[[sources/frontier-docs--webmcp-20261105]]"
ecosystem: browser-agent-interfaces
status: source-investigated
last-reviewed: 2026-11-05
---

# WebMCP: page-local capabilities as an agent interface

> A running application can describe callable capabilities alongside its human interface. Browser context, business authorization and durable completion remain separate contracts.

## Attributes

The unit studied is the Web Machine Learning Community Group's WebMCP design, Chrome implementation documentation, an Edge preview announcement and Playwright's testing reference. Eleven immutable captures/notes cover bounded primary-source sections. The CG report is dated2026-11-02 and explicitly neither a W3C Standard nor Standards Track. Chrome documents an origin trial; Microsoft describes early testing. No browser implementation, demo, installer, flag, service or business action was executed. [[sources/frontier-docs--webmcp-20261105#root]] [[sources/frontier-docs--webmcp-20261105#draft-status]] [[sources/frontier-docs--webmcp-20261105#browser-availability]] [[sources/frontier-docs--webmcp-20261105#edge-preview]]

Evidence class is specification/documentation inspected, plus original Edge retrieval notes; no measured agent-success claim. Google/Microsoft participation and a Playwright reference establish documented ecosystem work, not adoption or universal support. Raw GitHub documents are dated captures of living pages, not commit-pinned implementation code. [[sources/frontier-docs--webmcp-20261105#root]]

## Relationships

- [[concepts/developer-documentation-design]] and [[projects/writing-amazing-developer-docs/README]] own general documentation findings.
- [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[artifacts/projects/mcp-apps]] and [[artifacts/projects/openai-mcp-extensions]] distinguish remote protocols/host UI from page-local browser tools.
- [[artifacts/projects/mintlify]] and [[artifacts/projects/shopify-api]] supply vendor documentation/API comparisons; current namespace claims need dated qualification rather than rewriting prior evidence.
- [[projects/designing-apis-for-agents/README]] owns broader retrieval/command/workflow/status distinctions.
- [[creators/w3c]], [[creators/google]], [[creators/microsoft]] identify institutions, not a single product-support guarantee.

## Mechanism and themes

### Browser capability is a distinct documentation surface

The explainer's browser-local tools reuse page logic and current context, complementing backend integrations and ordinary browser actuation. It does not directly adopt the full remote MCP wire protocol. The human interface remains meaningful; the central scenario is collaboration with a user, rather than purely server-side autonomous processing. [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]]

Our inference: distinguish four interfaces when designing a business platform: explanatory documentation, documentation retrieval tools, page-local action tools and backend operations. They can describe the same business capability without sharing one transport or lifecycle. A browser affordance can initiate a durable job, but its declaration cannot prove the job survives closing the page. Documentation should say which contract the caller receives. [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]]

### Current contract and lifecycle

The captured draft exposes `document.modelContext`, structured tool metadata/schemas and asynchronous callbacks. Chrome documents discovery/invocation and separate signals for registration lifetime and execution cancellation. Chrome153 guidance separates unregistration from cancelling in-flight calls; Chrome155 deprecates JSON-stringified invocation arguments. Navigation can produce a null result. These details are versioned published behavior, not behavior tested here. [[sources/frontier-docs--webmcp-20261105#current-imperative-contract]] [[sources/frontier-docs--webmcp-20261105#tool-lifecycle]]

Our inference: documentation must distinguish capability removal, cancellation request, committed change and recovery. A success response should identify its actual business boundary. Returning from JavaScript, updating a screen, backend acceptance and finishing an ERP task can be different events. An operation should expose enough identity/state for the next caller to determine what happened. [[sources/frontier-docs--webmcp-20261105#design-practices]]

### Declarative semantics and user review

Chrome turns annotated forms into tools: names/descriptions describe purpose; fields become parameters; invocation populates the visible form. User submission is the default, while `toolautosubmit` changes it. `agentInvoked` and `respondWith` support agent-specific submit handling. The separate declarative proposal explores schema synthesis and response mechanisms. Importantly, the current repo explainer says declarative APIs are not part of the current CG specification. [[sources/frontier-docs--webmcp-20261105#declarative-chrome]] [[sources/frontier-docs--webmcp-20261105#declarative-proposal]]

Our inference: form labels and choices become operational documentation. Auto-submit changes the action boundary, so it deserves the same review as an API side effect. Generate related representations from one business model, then inspect whether generated descriptions still convey required context and consequences.

### Authority and security

Context delivery → authority basis → enforcement → revalidation: page metadata tells an agent what a tool claims to do; browser-origin gates control exposure; application identity/permissions govern the business action; execution must recheck current inputs/state. Cross-origin document use has three draft gates: policy delegation, provider exposure and consumer discovery. These differ from a user authorizing a specific payment or deletion. [[sources/frontier-docs--webmcp-20261105#origin-gates]] [[sources/frontier-docs--webmcp-20261105#design-practices]]

Site metadata/output can be malicious. Hints assist interpretation but do not establish safe behavior. Even a read-only tool can disclose private information. Agent-side origin restrictions, limits and confirmation complement probabilistic treatment of untrusted text. The published guidance is not an effectiveness experiment. [[sources/frontier-docs--webmcp-20261105#tool-author-security]] [[sources/frontier-docs--webmcp-20261105#agent-security]]

### Testing and publication drift

Playwright documents frame-specific tools/calls, marked addedv1.64, with experimental browser setup. It distinguishes returned tool errors from thrown execution errors. This enables a published testing interface; nothing was run here. Its introduction still uses `navigator.modelContext` and its annotations differ from current Chrome's Hint-suffixed names. Chrome security guidance links `requestUserInteraction`, absent from the captured current draft/imperative guide. Preserve those conflicts instead of declaring implementation failure. [[sources/frontier-docs--webmcp-20261105#playwright-testing]] [[sources/frontier-docs--webmcp-20261105#documentation-drift]]

## Documentation study matrix

| Dimension | Finding / boundary |
| --- | --- |
| Reader/task | Site developers exposing current-page capabilities; agent developers consuming them |
| Discovery | Page-local registry; visiting site differs from discovering a remote server |
| Applicability | Draft/date × browser build/trial × frame origin × tool availability; no universal support claim |
| Page purpose | Specification, implementation guide, preliminary security advice, proposal, testing reference |
| Examples | Illustrative JavaScript/forms; linked demos not executed |
| Meaning in transit | Text captures retain code/links; visual form focus, extension interactions and demos not preserved |
| Lifecycle | Draft design, documented implementation and executed compatibility remain distinct |
| Failure/recovery | Cancellation commit boundary, stale plans, navigation results and task errors need explicit contracts |
| Evidence strength | First-party design/guidance; no benchmark, intervention or independent replication |

All rows are scoped by the capture/review record. [[sources/frontier-docs--webmcp-20261105#root]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — metadata and current session do not approve every business effect. [[sources/frontier-docs--webmcp-20261105#origin-gates]]
- [[patterns/quality-bar/revision-bound-review]] — draft, browser guide and test wrapper can disagree. [[sources/frontier-docs--webmcp-20261105#documentation-drift]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — evaluate model choices separately from coded validation/state transitions. [[sources/frontier-docs--webmcp-20261105#design-practices]]

## What we'd steal

- ★ **Shared application service:** keep UI/tool/tests aligned on validation, permission and effects; adapt to ERP workflows without assuming browser transport supplies backend durability. [[sources/frontier-docs--webmcp-20261105#design-practices]]
- ★ **Names distinguish initiation from completion:** describe the actual action; useful for “open invoice review” versus “post invoice.” Business wording is our illustration. [[sources/frontier-docs--webmcp-20261105#design-practices]]
- ★ **Bind consequential transitions to current state:** invalidate stale previews and recompute on confirmation; include the exact resource/scope in platform contracts. [[sources/frontier-docs--webmcp-20261105#design-practices]]
- **Separate availability from cancellation:** remove unavailable tools without pretending completed effects reversed. [[sources/frontier-docs--webmcp-20261105#tool-lifecycle]]
- **State-relevant catalogs:** reduce overlapping choices; default simple apps to static registration rather than adding lifecycle complexity unnecessarily. [[sources/frontier-docs--webmcp-20261105#design-practices]]
- **Semantic forms:** reuse labels/types for agent inputs, while explicitly deciding review/submit behavior. [[sources/frontier-docs--webmcp-20261105#declarative-chrome]]
- **Actionable failures and understandable inputs:** return enough information to correct a call; normalize routine strings in application code. [[sources/frontier-docs--webmcp-20261105#design-practices]]
- **Test frames and error classes:** assert real application state separately from a wrapper returning; test agent selection as another layer. [[sources/frontier-docs--webmcp-20261105#playwright-testing]]
- **Publish compatibility/conflict receipts:** preserve older evidence and qualify new instructions with target build/contract. [[sources/frontier-docs--webmcp-20261105#documentation-drift]]

## Tensions and anti-patterns

Tool catalogs can become stale or overload context; automatic registration is not a guarantee of selection. Shared authenticated context simplifies interaction while making leakage consequential. Human review defaults and auto-submit have different effects. Suggested character budgets are preliminary guidance, not protocol limits. A docs site can expose five knowledge tools without becoming a general durable agent runtime. [[sources/frontier-docs--webmcp-20261105#browser-vs-backend]] [[sources/frontier-docs--webmcp-20261105#tool-author-security]]

## Open questions and verification record

Hashes/bytes:11captures verified, zero receipt errors. No conformance tests/browser launches. Remaining gaps: exact builds/trial expiry, actual namespace compatibility across vendors, navigation behavior, and durable backend outcomes. Resolve with explicitly scoped runtime tests before implementation recommendations. The completed ingest adds indexes, backlinks, log and scoped checks in [[meta/2026-11-05-frontier-docs-lint]]. [[sources/frontier-docs--webmcp-20261105#root]]

## Agent documentation research connection

[[concepts/agent-documentation-interfaces]] owns the cross-system delivery, authority and evaluation comparison; this page owns the source-specific mechanisms.
