---
domain: sources
type: docs-page
url: https://modelcontextprotocol.io/extensions/apps/overview
retrieved: 2026-11-04
snapshot-location: sources/modelcontextprotocol--mcp-apps-docs/
upstream-commit: 92195a772fe42efe6eeda3d1a3a90482464631f1
last-reviewed: 2026-11-04
---

# MCP Apps — official overview, stable/draft specification, and SDK guides

> An immutable documentation collection showing the portable UI contract, host responsibilities, security limits, and the boundary between stable MCP Apps and newer draft/SDK features.

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Publication/version:** overview and support matrix are living pages; stable Apps wire specification `2026-01-26`; separate development draft. SDK repository documentation captured at full commit `92195a772fe42efe6eeda3d1a3a90482464631f1` (upstream commit timestamp `2026-11-04T03:28:51Z`). These are three different version axes.
- **Storage:** [capture-map.json](modelcontextprotocol--mcp-apps-docs/capture-map.json) records each URL, retrieval date, SHA-256, byte count and commit where available. `snapshot.md` is the official overview's Markdown representation; the other files are named captures. None is a live source clone; no source software was installed or executed.
- **Evidence class:** official specification and documentation inspected. SDK implementation, test execution, live host interoperability, authentication flows and sandbox effectiveness were not independently verified.
- **Capture limitation:** the support matrix's Markdown representation has blank support cells. The prose and linked partial-support cells remain inspectable; blank cells are not treated as negative support evidence.

## Anchor map

### root

[Official overview capture](modelcontextprotocol--mcp-apps-docs/snapshot.md), lines 1–236; [upstream overview](https://modelcontextprotocol.io/extensions/apps/overview). Explains tool-linked HTML resources, examples, framework independence and documented client support.

### stable-version

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 1–53; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L1-L53). SEP-1865, authors, `Stable (2026-01-26)`, extension identifier `io.modelcontextprotocol/ui`, and influence of MCP-UI/OpenAI Apps SDK. The spec's claimed Apps SDK launch month is its account, not independently verified chronology.

### resource-contract

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 55–318; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L55-L318). `ui://`, `text/html;profile=mcp-app`, HTML resource content, CSP, permissions, host-dependent domain, restrictive defaults.

### discovery-visibility

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 319–410; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L319-L410). `_meta.ui.resourceUri`, model/app visibility, same-server app access, meaningful fallback and prefetch/cache. Flat `ui/resourceUri` metadata is deprecated.

### bridge-sandbox

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 411–530; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L411-L530). JSON-RPC `postMessage`, web-host cross-origin sandbox proxy, routing restrictions and `ui/initialize` / `ui/notifications/initialized`. The early illustrative transport snippet still says `initialize`; the lifecycle and normative proxy instructions use `ui/initialize`.

### host-context

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 531–958; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L531-L958). Host capabilities, dimensions, display modes, theme, styles, CSS variables, fonts and fallbacks.

### messages-context

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 959–1103; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L959-L1103). `ui/open-link`, `ui/message`, display-mode requests, replaceable future-turn `ui/update-model-context`, host discretion and consent.

### lifecycle

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 1104–1390; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L1104-L1390). Partial/complete input, results, cancellation, size/context change, teardown and sequence diagrams. Partial input must not drive critical operations.

### data-negotiation

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 1391–1561; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L1391-L1561). Tool data, model-context wording, older `initialize` capability example, required MIME-type declaration and meaningful text fallback. This older client/server negotiation example is not the same channel as iframe `ui/initialize`.

### security-limits

[Stable specification](modelcontextprotocol--mcp-apps-docs/apps-stable.mdx), lines 1584–1768; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/2026-01-26/apps.mdx#L1584-L1768). Design rationale, host validation/audit/template review/CSP duties, social engineering and resource-consumption risks.

### draft-tools-webmcp

[Draft specification](modelcontextprotocol--mcp-apps-docs/apps-draft.mdx), lines 1739–2193; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/draft/apps.mdx#L1739-L2193). App-provided tools, semantic state introspection, lifecycle-bounded app work, WebMCP bridging/mirroring, duplicate/echo rules and Permissions Policy. This capture is explicitly Draft, not the stable baseline.

### draft-lifecycle

[Draft specification](modelcontextprotocol--mcp-apps-docs/apps-draft.mdx), lines 1027–1637; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/specification/draft/apps.mdx#L1027-L1637). Host-mediated download, host-to-app tools, view teardown request and lifecycle expansion beyond the stable capture.

### sdk-version

[SDK README](modelcontextprotocol--mcp-apps-docs/sdk-readme.md), lines 1–284, and [v2 migration](modelcontextprotocol--mcp-apps-docs/migrate-to-v2.md), lines 1–130; [immutable migration guide](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/docs/migrate-to-2.md#L1-L130). Three SDK roles, Node/peer requirements, no supported production host in this repo, 1.x/2.x `ui/*` wire compatibility and error/schema/API differences.

### authorization

[Authorization guide](modelcontextprotocol--mcp-apps-docs/authorization.md), lines 1–211; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/docs/authorization.md#L1-L211). Public/protected tools, HTTP-401 OAuth escalation, discovery, server-side token verification, user scoping and defence in depth. Illustrative JWT snippets include issuer checking; surrounding prose separately requires tokens issued for the MCP resource.

### csp-cors

[CSP/CORS guide](modelcontextprotocol--mcp-apps-docs/csp-cors.md), lines 1–64; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/docs/csp-cors.md#L1-L64). Browser policy versus API-origin policy; read-response metadata location; host-specific stable domains. API-key presence alone must not be inferred to disable browser CORS enforcement.

### migration-openai

[OpenAI migration guide](modelcontextprotocol--mcp-apps-docs/migrate-from-openai.md), lines 1–393; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/docs/migrate_from_openai_apps.md#L1-L393). Metadata and MIME mapping, explicit async App connection instead of `window.openai`, notifications and documented gaps. Historical migration notes may lag current OpenAI extensions; compare [[sources/openai--mcp-extensions]].

### recipes

[Patterns guide](modelcontextprotocol--mcp-apps-docs/patterns.md), lines 1–627; [immutable upstream](https://github.com/modelcontextprotocol/ext-apps/blob/92195a772fe42efe6eeda3d1a3a90482464631f1/docs/patterns.md#L1-L627). App-only polling, chunking, binary resources, error feedback, host theming, explicit model context, local/server state, offscreen pausing, partial-input previews.

### support-testing

[Overview](modelcontextprotocol--mcp-apps-docs/snapshot.md), [support matrix](modelcontextprotocol--mcp-apps-docs/client-matrix.md), and [testing guide](modelcontextprotocol--mcp-apps-docs/testing.md), lines 1–93. Host support is a current documentation claim; reference-host and production-host tests are distinct. No host test was run in this research.

### openai-implementation-guides

Follow-up captures retrieved November 4, 2026, retained separately in [implementation-followup-capture-map-2026-11-04.json](modelcontextprotocol--mcp-apps-docs/implementation-followup-capture-map-2026-11-04.json), with SHA-256 and byte counts. Original captures remain unchanged.

- [Current OpenAI UI guide](modelcontextprotocol--mcp-apps-docs/openai-ui-guide-2026-11-04.md): standards-first bridge, same-server tools, React bundles, model-context updates, server-owned durable state and CSP. [Official page](https://developers.openai.com/plugins/build/chatgpt-ui).
- [Current extension guide](modelcontextprotocol--mcp-apps-docs/openai-extension-guide-2026-11-04.md): sidebar/global and conversation/thread entrypoints. Its composer-mentions availability says Desktop only, unlike the pinned repository's Desktop/Web table. [Official page](https://developers.openai.com/plugins/build/extensions).
- [Current UI guidelines](modelcontextprotocol--mcp-apps-docs/openai-ui-guidelines-2026-11-04.md): optional component library, inline versus immersive layouts, accessible host-native presentation. Its general picture-in-picture guidance is broader than the pinned OpenAI extensions mode contract. [Official page](https://developers.openai.com/plugins/concepts/ui-guidelines).
- [Current plugin guidelines](modelcontextprotocol--mcp-apps-docs/openai-plugin-guidelines-2026-11-04.md), Iframes and embedded pages: own-registrable-domain full editor/admin embeds are possible with declared origins, justification and review; shared hosting tenants remain distinct. [Official policy](https://developers.openai.com/plugins/plugin-guidelines#iframes-and-embedded-pages).

### registry-compatibility-followup

The same follow-up receipt retains exact public npm metadata for [OpenAI MCP Extensions 0.2.1](modelcontextprotocol--mcp-apps-docs/openai-extensions-npm-0.2.1-2026-11-04.json) and [ext-apps 2.0.4](modelcontextprotocol--mcp-apps-docs/ext-apps-npm-2.0.4-2026-11-04.json). November 4 registry requests and `npm view` confirm these versions exist; the latter was the current version returned by `npm view @modelcontextprotocol/ext-apps version` at that time. OpenAI 0.2.1 peers on ext-apps ^1.7.5, SDK ^1.29 and server ^2; ext-apps 2.0.4 peers on split core/client/server ^2 and zod ^4.2. This is dependency metadata, not an installed compatible combination. Primary endpoints: [OpenAI package](https://registry.npmjs.org/@openai%2fmcp-extensions/0.2.1), [Apps package](https://registry.npmjs.org/@modelcontextprotocol%2fext-apps/2.0.4).

## Why we cite this

It supports the portable MCP Apps contract and implementation responsibilities, while preserving specification generation, SDK generation, draft features, host claims and unverified runtime behavior separately. [[artifacts/projects/mcp-apps]] is the durable analysis.

## Popularity signals

- **Signal:** official MCP extension specification and documentation; stable version dated `2026-01-26`, inspected 2026-11-04. This is governance/credibility evidence, not an install, usage or market-share count.
- **Attention/adoption:** overview names multiple compatible hosts and examples. These are publisher-reported support claims, not independently tested installations.

## Related sources

- [[sources/openai--mcp-extensions]] — OpenAI-specific capabilities compose with Apps; support remains host and capability specific.
