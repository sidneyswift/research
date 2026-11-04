---
domain: sources
type: repo
url: https://github.com/openai/mcp-extensions
retrieved: 2026-11-04
snapshot-location: sources/openai--mcp-extensions/
upstream-commit: 9e6d418439cca0790bece62f6cd886ad4c04f133
last-reviewed: 2026-11-04
---

# OpenAI MCP Extensions — spec, SDKs and Bits & Bolts

> A vendor extension layer over MCP and MCP Apps that adds ChatGPT navigation, settings, files, context, messaging and forms; implemented in TypeScript/Python helpers and a demonstration plugin.

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Local evidence:** live, read-only research clone at `sources/openai--mcp-extensions/`, with `.git/` intact; root manifest/ignore registration accompanies the ingest.
- **Upstream URL:** https://github.com/openai/mcp-extensions.
- **Pinned commit:** `9e6d418439cca0790bece62f6cd886ad4c04f133`.
- **Commit date:** 2026-10-29 17:00:17 -0700; message: “Migrate Bits & Bolts viewer tools to WebMCP (#66).”
- **Version evidence:** both SDK package manifests declare `0.2.1`; this is checked-in metadata, not a verified npm/PyPI publication or production host rollout.
- **Investigated scope:** README, extension spec, UX patterns, SDK setup/package metadata/changelog, TypeScript app capability/resource helpers, server mentions/form helpers, selected app tests, and Bits & Bolts WebMCP/demo OAuth code. No dependency installation, SDK tests, source application, live plugin or production OAuth flow was executed.

## Anchor map

### root

[README.md L1–L63](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/README.md#L1-L63) — project identity, major UX surfaces, TypeScript and Python packages, demonstration plugin, Apache 2.0 license.

### platforms

[docs/spec.md L1–L38](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1-L38) — version reference, documented platform support and version-dependent server capability locations. “Web” means Work browser excluding classic ChatGPT.

### entrypoints

[docs/spec.md L40–L85](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L40-L85) — global, thread and file entrypoints; metadata; visibility exception; title/icon precedence; empty arguments for global opening.

### deep-links

[docs/spec.md L120–L159](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L120-L159) — app-relative deep-link encoding, plugin identity, path rules.

### file-entrypoints

[docs/spec.md L249–L299](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L249-L299) — file-extension registration, opaque resource URI, host-intercepted resource calls and tool input.

### file-authority

[docs/spec.md L359–L384](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L359-L384) — iframe lacks raw paths; server tool call receives absolute path metadata; server may return it to trusted app. This documents a boundary and its escape path, not general server sandboxing.

### resource-writes

[docs/spec.md L386–L473](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L386-L473) — representation, subscriptions, eligible opened-file URI, writable hint, optional ETag match, saved/conflict/too-large outcomes.

### settings

[docs/spec.md L585–L623](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L585-L623) and [L753–L767](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L753-L767) — named read/update tools, typed values/layout, server persistence and changed-values-only updates.

### display-onboarding

[docs/spec.md L836–L906](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L836-L906) — initial UI-resource display metadata, inline/fullscreen behavior, onboarding skill manifest reference.

### model-context

[docs/spec.md L908–L1009](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L908-L1009) and [L1100–L1134](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1100-L1134) — context capabilities, replacement semantics, group labels, host context state, background audience and content-type support. Content-block `_meta` excluded from model input; audience does not prevent model delivery.

### webmcp

[docs/spec.md L1136–L1141](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1136-L1141) — Desktop-only `document.modelContext` tools; ChatGPT does not support Apps SDK `App.registerTool()`.

### messaging

[docs/spec.md L1184–L1215](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1184-L1215) — `ui/message` active/new target and send/draft semantics; default is immediate send to active conversation.

### mentions

[docs/spec.md L1329–L1371](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1329-L1371) — searchable resource references, named read-only tool, app visibility and deprecated discovery alias.

### forms

[docs/spec.md L1407–L1453](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1407-L1453) and [L1497–L1548](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1497-L1548) — registered-server MRTR requirement, direct-connection legacy path, dual capability requirement, empty core form/full extension schema envelope, unsupported forms, numeric precision.

### resource-pickers

[docs/spec.md L1602–L1613](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1602-L1613) and [L1710–L1761](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1710-L1761) and [L1903–L1924](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/spec.md#L1903-L1924) — thumbnails, resource selection, explicit/implicit defaults and preview targets.

### sdk-setup

[typescript/README.md L1–L65](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/README.md#L1-L65) and [L111–L117](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/README.md#L111-L117) — wrappers around MCP server/App SDK, separate server and app dependency generations, initial result handler before connect, optional extension fields, inline/bundled stylesheet under CSP.

### versions

[typescript/package.json L1–L77](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/package.json#L1-L77) and [python/pyproject.toml L1–L11](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/python/pyproject.toml#L1-L11) — checked-in package versions/dependencies/runtime requirements.

### migration

[CHANGELOG.md L1–L36](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/CHANGELOG.md#L1-L36) — 0.2.1 changes and 0.2.0 migration including removed app transport and structured settings entrypoints.

### capability-gates

[typescript/src/app/extensions.ts L21–L65](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/src/app/extensions.ts#L21-L65) — actual optional feature getters gated on host advertisement.

### write-client

[typescript/src/app/resources.ts L18–L63](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/src/app/resources.ts#L18-L63) and [L196–L244](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/src/app/resources.ts#L196-L244) — shape validation and request routing; no local opened-URI or writable permission enforcement in write helper.

### form-client

[typescript/src/server/forms/mrtr.ts L15–L74](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/src/server/forms/mrtr.ts#L15-L74) — version/dual-capability check, keyed continuation, accepted answer schema validation and input-required return.

### mentions-client

[typescript/src/server/mentions.ts L19–L61](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/src/server/mentions.ts#L19-L61) — SDK registers read-only app-visible search tool, current/legacy capabilities and handler.

### app-tests

[typescript/tests/sdk-app.test.ts L19–L147](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/tests/sdk-app.test.ts#L19-L147) and [L189–L230](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/typescript/tests/sdk-app.test.ts#L189-L230) — in-memory bridge tests for capabilities/initial result and write wire/outcomes; inspected, not executed; no real host ACL test.

### interaction-guidance

[docs/patterns.md L5–L41](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/patterns.md#L5-L41) and [L43–L109](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/patterns.md#L43-L109) and [L129–L159](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/docs/patterns.md#L129-L159) — desktop version/capability checks, responsive UI, safe areas, state context, model-callable UI, stale-while-revalidate and distinct entrypoint tools.

### demo-webmcp

[plugins/bits-and-bolts/src/app/controller.ts L934–L1018](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/plugins/bits-and-bolts/src/app/controller.ts#L934-L1018) — actual UI tools for read/open/configure/rotate/save, input parsing and dirty-view guard.

### demo-oauth

[plugins/bits-and-bolts/src/server/remote/auth.ts L1–L15](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/plugins/bits-and-bolts/src/server/remote/auth.ts#L1-L15) and [L87–L144](https://github.com/openai/mcp-extensions/blob/9e6d418439cca0790bece62f6cd886ad4c04f133/plugins/bits-and-bolts/src/server/remote/auth.ts#L87-L144) — intentionally anonymous shared demo accounts, format-based bearer selection and illustrative OAuth flow; not private-data authentication.

## Why we cite this

This source supports concrete host-specific contracts and inspected SDK mechanisms. It does not establish official cross-host extension ratification, live ChatGPT rollout in any account, all-platform conformance, registry availability, production IdP integration, sandbox enforcement or a security audit.

## Popularity signals

- **Signal type:** GitHub repository attention.
- **Value:** 1,126 stars; 54 forks; 5 subscribers, from `https://api.github.com/repos/openai/mcp-extensions`.
- **As-of:** 2026-11-04.
- **Credibility:** OpenAI-owned repository, an explicit specification, implementation and tests. Attention is not adoption or runtime validation.

## Related sources

- [[sources/modelcontextprotocol--mcp-apps-docs]] — base Apps transport/resource/lifecycle specification that these helpers extend.
- [[sources/openai--agent-api-design]] — model/API execution contracts; distinct from host plugin UX.
