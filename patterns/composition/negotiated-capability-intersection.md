---
domain: patterns
type: pattern
name: negotiated-capability-intersection
category: composition
status: proposed
last-reviewed: 2026-11-04
example-count: 1
---

# Negotiated capability intersection

> Parties declare supported capabilities and versions; the business selects the compatible intersection and removes extensions whose dependencies are absent. The result describes compatibility, not permission to perform every supported action.

## Longer definition

This proposed pattern is grounded in Shopify's UCP documentation. A hosted business profile describes its services, capabilities and versions; a caller supplies its own profile URI. The server validates both compatibility and dependencies and reports the negotiated set. It avoids composing a flow from a tool name alone when protocol generations or optional features differ. Only one API system is documented here; no independent implementation test or confirmed recurrence is claimed. [[sources/shopify--agent-commerce-api-design#profiles]]

## Mechanism

1. Publish business and caller capability/version profiles.
2. Include the caller profile URI on applicable requests.
3. Fetch/validate the profile and protocol alignment.
4. Intersect compatible capability names/versions.
5. Prune extensions whose parent capability was not selected.
6. Return negotiated metadata; reject invalid/incompatible paths.
7. Apply authentication, action permissions and user-consent checks separately.

Steps 1–6 are documented Shopify negotiation; step 7 reflects the separate auth/completion contracts rather than an extra negotiation guarantee. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#checkout]]

## When to use

- Multiple independent clients compose optional, versioned business capabilities.
- Extensions require compatible parent features.
- A static tool catalog would conceal meaningful support differences. These are inferred use cases from the documented mechanism. [[sources/shopify--agent-commerce-api-design#profiles]]

## When NOT to use

- One fixed internal client and server already share a versioned contract; extra negotiation may add cost without value.
- As a replacement for tenant authorization, buyer consent or payment authority.
- To claim a declared capability or reachable schema proves the deployed operation succeeds. [[sources/shopify--agent-commerce-api-design#auth]]

## Why it works

Compatibility becomes an explicit selected contract instead of an assumption made from an endpoint or tool name. Dependency pruning prevents claiming an extension without its parent. These are intended structural benefits, not measured latency/reliability or agent-performance improvements. [[sources/shopify--agent-commerce-api-design#profiles]]

## Detection recipe

- **Look for:** independently published profiles with protocol/capability versions.
- **Confirm with:** actual intersection/version/dependency selection and returned negotiated metadata or explicit incompatibility errors.
- **Rule out:** a static schema catalog, a permission-scope list, a model picking a tool, or a feature flag without peer compatibility negotiation.

## Examples in this wiki

- [[artifacts/projects/shopify-api]] — Shopify UCP profile negotiation, documentation-inspected only. [[sources/shopify--agent-commerce-api-design#profiles]]
- A second independent artifact is still needed; multiple Shopify surfaces do not supply independent examples.

## Counter-examples or anti-pattern

- A declared checkout capability does not authorize `complete_checkout`: token permission and buyer confirmation remain separate. [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#checkout]]
- [[artifacts/projects/openai-agent-api]] deferred tool loading selects useful context; this study does not establish the same two-party business-profile negotiation mechanism. [[sources/openai--agent-api-design#tool-design]]

## Related patterns

- [[patterns/composition/resolver-routing-table]] — routing chooses a capability; negotiation checks compatible support.
- [[patterns/behavioral/context-is-not-authority]] — declared context/support does not grant action authority.
- [[patterns/composition/single-source-multi-surface-distribution]] — related presentation concern; negotiation does not prove shared source generation.

## Open questions

- Which second independent implementation has equivalent version/dependency selection?
- How are cached-profile changes, revocation, signing-key changes and active-session compatibility handled under failures?
- Which parts should a generic business platform adopt rather than keep as fixed internal contracts? Requires actual consumer/version evidence.

## MCP research connection — 2026-11-04

[[concepts/mcp-extension-architecture]], [[artifacts/projects/mcp-apps]] and [[artifacts/projects/openai-mcp-extensions]] provide adjacent version/capability prerequisite checks. They do not yet demonstrate the full profile/dependency-selection mechanism above; status remains proposed and example-count remains one. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]], [[sources/openai--mcp-extensions#form-client]]
