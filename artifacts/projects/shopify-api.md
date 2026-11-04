---
domain: artifacts
subdomain: projects
type: project
name: shopify-api
creator: "[[creators/shopify]]"
sources:
  - "[[sources/shopify--agent-commerce-api-design]]"
  - "[[sources/shopify--admin-api-design]]"
ecosystem: commerce / GraphQL Admin / UCP / MCP / WebMCP
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Shopify APIs and agent commerce

> An established commerce platform with explicit agent-facing discovery, negotiation, cart/checkout tools, buyer handoffs, and developer-context tooling alongside its business/Admin APIs.

## Attributes

- **Unit:** bounded study of Shopify's business and agent-facing API surfaces, not every Shopify API or the entire UCP specification.
- **Evidence:** official documentation captured 2026-11-04; per-document URLs/hashes/version boundaries are on the two source maps. UCP examples use dated protocol versions; Admin API versions are a separate axis. [[sources/shopify--agent-commerce-api-design#root]], [[sources/shopify--admin-api-design#root]]
- **Credibility:** first-party contract documentation. “Agent-forward” here means documented agent-facing interfaces, negotiation and tooling—not independently measured agent success, adoption or deployed enforcement.
- **Execution:** no commerce/API calls, merchant or buyer access, payment attempts, toolkit installation, SDK execution, or implementation audit.

## Relationships

- [[creators/shopify]] — publisher.
- [[projects/designing-apis-for-agents/README]] — research group.
- [[analyses/frontier-and-business-api-design]] — comparison across established business platforms and agent runtimes.
- [[concepts/business-platform-api-design]] — capabilities, effects and execution contracts.
- [[concepts/agent-api-learning-and-evolution]] — runtime context rather than reliance on memorized APIs.
- [[artifacts/projects/stripe-api]] — independent commerce/payment lifecycle comparison.

## Mechanism and themes

### One company, distinct audiences and authority

The Admin API is a versioned merchant/app integration surface. UCP Catalog, Cart, Checkout and Order capabilities serve agent-mediated buyer journeys. The AI Toolkit/Dev MCP supplies documentation/schema/validation context to coding agents; authenticated CLI store management has a separate execution context. These are related surfaces, not one universal credential or unrestricted tool set. [[sources/shopify--admin-api-design#root]], [[sources/shopify--agent-commerce-api-design#catalog]], [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#toolkit]]

### Contract matrix

| Dimension | Documented contract and implication |
| --- | --- |
| Identity and scope | Global versus merchant catalog; opaque cart/checkout IDs; buyer, agent and merchant context are distinct. Order access is restricted to orders facilitated by the agent. [[sources/shopify--agent-commerce-api-design#catalog]], [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#orders]] |
| Intent and effects | Search/lookup/product inspection, exploratory cart, purchase checkout, explicit completion, and post-purchase order inspection are separately named capabilities. [[sources/shopify--agent-commerce-api-design#catalog]], [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#orders]] |
| Inputs | UCP cart and checkout updates replace state rather than merge a patch; missing fields can remove prior data. Checkout buyer-consent omission has its own documented preservation exception. [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]] |
| Execution | The agent coordinates commerce tools; Shopify owns commerce execution. Bulk Admin queries execute asynchronously on Shopify. None of these docs establishes a general-purpose hosted agent runtime. [[sources/shopify--agent-commerce-api-design#overview]], [[sources/shopify--admin-api-design#root]] |
| Lifecycle | Checkout states distinguish incomplete, escalation, ready, completion in progress, completed and canceled. Completion produces an order; fulfillment/returns remain later lifecycle events. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#orders]] |
| Composition | Profiles negotiate capabilities and extensions; cart-to-checkout conversion is explicit. This is not evidence of a transaction spanning arbitrary Admin and commerce calls. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#checkout]] |
| Authority | Declaring capabilities is not permission to pay. Token/signed/anonymous tiers have different access; direct completion requires specifically permitted token access and buyer authorization. [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#checkout]] |
| Retries/concurrency | Checkout completion and cancellation require idempotency keys; cart conversion can return an existing incomplete checkout. Do not extend these guarantees to every mutation or transport. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--admin-api-design#root]] |
| Events | Agent Order webhooks and `get_order` use the same order shape; pushes are the primary signal and reads reconcile missed updates. No complete ordered history is implied. [[sources/shopify--agent-commerce-api-design#orders]] |
| Freshness/output | Separate broad search from ID lookup for fresh data and detailed product selection. Results use `structuredContent`; inspect business state/messages rather than only the JSON-RPC envelope. [[sources/shopify--agent-commerce-api-design#catalog]], [[sources/shopify--agent-commerce-api-design#cart]] |
| Evolution | Admin versioning, UCP/capability dates, transport changes and toolkit versions are distinct. Consult captured Admin and profile docs rather than treating “Shopify API version” as one value. [[sources/shopify--admin-api-design#root]], [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#webmcp]] |
| Agent discovery | Hosted profiles describe capabilities; the business selects a compatible intersection and prunes dependent extensions. Browser tools change with page state. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#webmcp]] |

### Discovery becomes negotiated compatibility

Merchant and agent profiles describe supported protocol versions/capabilities. Shopify fetches/validates the agent profile, checks compatible versions, selects the intersection, and removes extensions whose parent capability did not survive. Responses report negotiated metadata where applicable. Invalid or incompatible profiles follow an error path. This is more specific than returning a static tool list: the caller must distinguish declared support from the negotiated contract. [[sources/shopify--agent-commerce-api-design#profiles]]

That negotiation is also distinct from authentication, action-specific authorization, and buyer consent. A profile that advertises checkout support cannot by itself authorize purchase completion. [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#checkout]]

### Separate exploration from commitment and handoff

Cart MCP supports iteration and estimated totals before purchase commitment. Checkout MCP handles the purchase session, with stricter rate limits and explicit escalation. General-access flows finish by handing the buyer to `continue_url`; direct completion is conditional on access, ready state, buyer review/confirmation and payment credentials. A robust integration treats escalation as a valid business outcome rather than an error to bypass. [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#checkout]]

`complete_in_progress` means retrieve again after processing; `completed` plus `order` is the documented purchase confirmation signal. That does not mean fulfillment, returns, or future order changes are over. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#orders]]

### Share business objects across transports without hiding differences

Checkout MCP and Checkout WebMCP share the checkout object/status/message concepts. The server-side API addresses a checkout by ID; browser tools act on the checkout open in that tab and do not take the same ID/meta parameters. Browser agents must refresh tools on `toolchange`, match tool origin/window/name, handle navigation before results, and account for buyer interactions. Browser support and tool availability have documented exclusions. Shared semantics do not imply identical inputs, authentication, or capabilities. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#webmcp]]

### Update semantics must be taught explicitly

Cart MCP's `update_cart` replaces full state and explicitly differs from Storefront/AJAX cart patch operations. Checkout MCP's `update_checkout` also replaces state; sending an abbreviated payload can drop line items, buyer information or attribution. Response-only fields must be removed before input reuse, and nested buyer-consent omission preserves existing consent. An adapter should construct the exact allowed input rather than replay a response object or assume every `update_*` performs a patch. [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]]

### Transport success is not business success

A missing/expired cart can produce a successful JSON-RPC `result` with a business error in `messages`. Checkout docs similarly distinguish protocol errors from application outcomes and escalation. The Admin GraphQL side also needs its own nested error interpretation. This is another direct counterexample to “HTTP 200 means the task succeeded.” [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--admin-api-design#root]]

### Runtime learning rather than just model memory

The AI Toolkit explicitly supplies current docs, API schemas and validation context, alongside separately authenticated CLI execution. That supports the wiki's runtime-context design hypothesis without proving improved success rates: a platform can make current contracts inspectable instead of requiring the agent to have memorized them in training. Docs describe distribution options and validation; this study did not install or test them. [[sources/shopify--agent-commerce-api-design#toolkit]], [[concepts/agent-api-learning-and-evolution]]

### Admin: business intent inside a GraphQL schema

Admin queries and mutations share a POST endpoint, while schema operations and scopes carry the business distinction. HTTP 200 can contain top-level GraphQL errors, including throttling or access-denied errors; mutation clients must also explicitly select payload `userErrors`. A useful adapter interprets the transport, GraphQL and business layers rather than hiding them behind one success flag. [[sources/shopify--admin-api-design#overview]], [[sources/shopify--admin-api-design#errors]]

`bulkOperationRunQuery` is a mutation that starts an asynchronous business read. Its job ID/status, eventual download URL, possible partial results, and finish notification are separate contracts. A finish webhook can describe failure or cancellation, and polling remains a documented fallback. Signed result URLs expire; completed queries with no data can have a null URL. Bulk execution does not grant new query permissions or establish an arbitrary multi-call transaction. [[sources/shopify--admin-api-design#bulk]]

Admin idempotency support is mutation-specific: mutation arguments and the `@idempotent` directive are distinct mechanisms. The directive implementation guide's 24-hour retention, concurrent-request and parameter-mismatch rules apply only to its supporting mutations. Bulk idempotency is per JSONL row. A successful duplicate can return later database state in a reconstructed response while avoiding re-execution, so effect idempotency is not identical-response replay. [[sources/shopify--admin-api-design#idempotency]], [[sources/shopify--admin-api-design#idempotency-implementation]]

Admin version selection is not an indefinite pin: inaccessible requested versions fall forward, and the actual-version response header matters. The version guide lists Catalog as unversioned; do not project Admin's release policy onto every agent-facing layer. Configured app scopes also differ from installed grants, and protected-data/record-horizon restrictions can add gates. [[sources/shopify--admin-api-design#versioning]], [[sources/shopify--admin-api-design#scopes]]

## Patterns demonstrated

- [[patterns/composition/negotiated-capability-intersection]] — proposed, one documented system: server-selected compatibility intersection with dependency pruning, distinct from permission. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#auth]]
- [[patterns/behavioral/context-is-not-authority]] — declared profile capabilities, retrieved text, buyer identity and purchase authorization are separate concerns. Documentation-level correspondence, not a runtime enforcement test. [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#webmcp]]
- [[patterns/composition/single-source-multi-surface-distribution]] — related application: shared checkout semantics across server/browser surfaces. Documentation does not establish one generated implementation, so no inspected-example count is added. [[sources/shopify--agent-commerce-api-design#webmcp]]

## What we'd steal

- ★ **Negotiate the usable capability set.** Validate declared versions and dependencies before composition; expose selected metadata. [[sources/shopify--agent-commerce-api-design#profiles]]
- ★ **Keep exploration, commitment and escalation explicit.** Cheap cart iteration and buyer handoff reduce accidental purchase intent. This benefit is our design inference. [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]]
- ★ **Separate capability support from action authority.** Authentication tier, order provenance, buyer consent and completion permission constrain different things. [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#orders]]
- **Use intent-specific discovery:** search by need, look up known IDs, then retrieve option/detail data. [[sources/shopify--agent-commerce-api-design#catalog]]
- **Preserve full opaque IDs and context.** Do not reconstruct identifiers or assume converted checkout responses repeat the original cart ID. [[sources/shopify--agent-commerce-api-design#checkout]]
- **Document replace/merge semantics down to exceptions.** Distinguish omitted parent fields, preserved consent and response-only properties. [[sources/shopify--agent-commerce-api-design#checkout]]
- **Separate protocol errors from business messages and escalation.** A valid envelope can carry an unavailable resource or incomplete task. [[sources/shopify--agent-commerce-api-design#cart]], [[sources/shopify--agent-commerce-api-design#checkout]]
- **Bind retries to exact actions.** Reuse completion/cancellation keys; do not generalize per-tool idempotency to all APIs. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--admin-api-design#root]]
- **Expose background read work as an operation.** Admin bulk queries supply another business-read versus runtime-mutation example. [[sources/shopify--admin-api-design#root]]
- **Scope order reads by provenance, not only object ID.** Agent-facilitated orders are a narrower boundary than all merchant orders. [[sources/shopify--agent-commerce-api-design#orders]]
- **Use push for proactive updates and reads for reconciliation.** Reuse an order data shape without assuming replay reconstructs authoritative state. [[sources/shopify--agent-commerce-api-design#orders]]
- **Share semantic objects while describing transport differences.** Browser tab context and server IDs have different preconditions. [[sources/shopify--agent-commerce-api-design#webmcp]]
- **Refresh dynamic tool catalogs.** Tools and schemas can change when the browser state changes. [[sources/shopify--agent-commerce-api-design#webmcp]]
- **Make trust tiers and rate behavior explicit.** Honor Retry-After and preserve the actual buyer context required by the chosen surface. [[sources/shopify--agent-commerce-api-design#auth]]
- **Provide current docs/schema/validation access as infrastructure.** Keep developer-context discovery separate from privileged store execution. [[sources/shopify--agent-commerce-api-design#toolkit]]
- **Audit version axes independently.** Admin API, UCP, extensions, browser binding and toolkit releases are different contracts. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#webmcp]], [[sources/shopify--admin-api-design#root]]
- **Parse nested GraphQL errors deliberately.** Select `userErrors` and handle semantic throttling even when HTTP succeeded. [[sources/shopify--admin-api-design#overview]], [[sources/shopify--admin-api-design#errors]]
- **Treat finish events and null result URLs precisely.** Retrieve job state and distinguish no-data completion, failure, cancellation, partial output and expired download links. [[sources/shopify--admin-api-design#bulk]]
- **Scope idempotency by mechanism, row and window.** Preserve a stable intent key before sending; do not require identical response bytes as proof of non-reexecution. [[sources/shopify--admin-api-design#idempotency-implementation]]
- **Verify actual version and effective grants.** Compare requested versus served version and declared versus installed scope sets. [[sources/shopify--admin-api-design#versioning]], [[sources/shopify--admin-api-design#scopes]]

## Tensions and anti-patterns

- **Authentication documentation tension:** Checkout MCP introduction says all requests require authentication or signing; the shared auth matrix explicitly permits anonymous checkout build/edit at the lowest tier. Record this discrepancy; do not infer every checkout call requires the same credential or that anonymous callers may complete purchases. The latter is explicitly excluded by the matrix. [[sources/shopify--agent-commerce-api-design#checkout]], [[sources/shopify--agent-commerce-api-design#auth]]
- **Not every agent is a buyer-present agent:** token-tier merchant tools require the actual buyer IP even on reads, and the doc says unattended requests without a buyer fail. Do not transplant buyer-commerce credentials/context into scheduled Admin work. [[sources/shopify--agent-commerce-api-design#auth]]
- **No global concurrency guarantee:** full replacement makes stale updates consequential; the captured commerce docs do not establish an eTag/CAS contract for every tool. Read-before-write alone is not a proven race solution.
- **Shared vocabulary is not universal support:** WebMCP tools have browser/page exclusions and lack server-side checkout cancellation equivalence. [[sources/shopify--agent-commerce-api-design#webmcp]]
- **Independent platform versus protocol claims:** this is Shopify's documented implementation of UCP, not a compatibility audit across other merchants or an independent UCP specification ingest.
- **Admin examples versus reference:** the captured bulk guide prints `/api/{api_version}/graphql.json`, while the explicit Admin reference uses `/admin/api/2026-10/graphql.json`. Preserve that discrepancy rather than copying the shorthand into an integration. [[sources/shopify--admin-api-design#bulk]], [[sources/shopify--admin-api-design#overview]]
- **CLI convenience versus raw tool input:** the checkout guide's CLI update example sends only buyer email, while the raw `update_checkout` contract requires a complete replacement state. CLI implementation was not inspected; do not assume that shorthand is a valid raw payload or that a helper performs safe read/modify/write. [[sources/shopify--agent-commerce-api-design#checkout]]

## Open questions and verification record

- Which auth statements are authoritative for each currently deployed merchant/tier? Resolve the captured intro/matrix tension before an integration.
- What exact retention, race, timeout/unknown-result and cancellation guarantees apply to every commerce operation? Not runtime-tested.
- How do toolkit/schema retrieval and negotiated discovery change agent task success compared with static tools? No benchmark run.
- Further study: standalone Storefront GraphQL, merchant Admin actions beyond the sample, Shop MCP, Universal Checkout and fulfillment lifecycle. Early-access availability must be checked separately.
- Captured text, source anchors and hashes are checked during integration. No API operation, purchase, registration or install was attempted.

## MCP research connection — 2026-11-04

[[concepts/mcp-extension-architecture]] contrasts MCP extension compatibility with this page’s domain-specific UCP profile negotiation. [[artifacts/projects/mcp-apps]] studies embedded interfaces; neither establishes that Shopify implements those UI contracts. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]], [[sources/modelcontextprotocol--mcp-apps-docs#resource-contract]]
