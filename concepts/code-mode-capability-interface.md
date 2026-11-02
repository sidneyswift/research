---
domain: concepts
type: concept
name: code-mode-capability-interface
creators: "[[creators/kody-hq]]"
sources: "[[sources/kody-hq--kody]]"
status: emerging
last-reviewed: 2026-11-02
---

# Code Mode capability interface

> Discover just the capabilities a task needs, then compose code that calls them behind a small stable tool interface.

## What it is

Kody puts a large capability graph behind `search` and module-based `execute`, rather than exposing every operation as a separate always-loaded MCP tool. Search moves from domain overview to ranked actions to exact entity contracts; execution composes typed capability calls and package imports. The compactness is at the model/host boundary, while the backend still contains a substantial registry, runtime, identity and authorization system. [[sources/kody-hq--kody#intent]], [[sources/kody-hq--kody#search]], [[sources/kody-hq--kody#execute-contract]]

## Where it came from

Kody's intent document explicitly credits Cloudflare's Code Mode approach. This page studies **Kody's implementation**, not the un-ingested Cloudflare original and not an invention attributed to Kody. The existing [[patterns/behavioral/latent-vs-deterministic-split]] covers the broader division of judgment and code; this concept isolates on-demand capability discovery and code composition as an interface mechanism. [[sources/kody-hq--kody#intent]]

## Why it matters

Large connected tool inventories can be represented by a small reusable interaction vocabulary. Once the plan is known, code can call several operations without exposing every intermediate response to the model. Reusable packages can turn repeated procedures into typed code that works across hosts. **Potential** token/latency benefit needs measurement: compilation, discovery, registry loading and failures can dominate a short task. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#registry]]

## Evidence & claims

- **Documentation:** broad queries return domain summaries, precise searches rank actions, entity lookup supplies exact schemas/examples. Text and structured channels are intended to retain equivalent actionable information. [[sources/kody-hq--kody#search]]
- **Implementation:** lazy built-in registry plus synthesized remote MCP domains, cached with owner/server state and filtered for callers/features. [[sources/kody-hq--kody#registry]]
- **Documentation:** module source is separate from varying `params`; static package exports are publish-verified, visible to dependency tracking and snapshotted in dependents. [[sources/kody-hq--kody#execute-contract]]
- **Implementation:** keyed runs return existing in-progress/retained outcomes instead of launching a duplicate; this makes the compact interface resumable across transport limits. [[sources/kody-hq--kody#execute-replay]]
- **Implementation:** credential resolution/gateway use sites hold enforcement outside generated code; reducing tool count does not remove permission checks. [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#fetch-gateway]]

## Patterns demonstrated

- [[patterns/behavioral/latent-vs-deterministic-split]] — model plans composition; registry/credential code validates and executes contracts. [[sources/kody-hq--kody#registry]], [[sources/kody-hq--kody#credential-resolution]]
- [[patterns/composition/single-source-multi-surface-distribution]] — reusable package modules across host and background surfaces. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#workflows]]
- [[patterns/behavioral/context-is-not-authority]] — discovered metadata and generated code do not independently grant credential access. [[sources/kody-hq--kody#credential-resolution]]
- Code Mode itself is tracked here as a concept until independent implementations are investigated; the already-cloned Executor source is a candidate, not a counted example.

## Tensions & counter-arguments

A small tool menu is not necessarily legible authorization: one `execute` can send, delete or revoke. A workflow can fail after partial external effects. Host/credential approval is narrower than approval of every operation on that host. Agents also need code capability, exact contracts, useful error categories and durable run handles. These costs are visible in Kody's gateway/replay machinery and its explicit destructive annotation, not merely hypothetical objections. [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#fetch-gateway]]

Static snapshots improve repeatability but require dependent republishing; ad hoc current-version resolution improves freshness but can change behavior between retries. Runtime portability across MCP hosts still depends on the server and its deployed runtime. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#architecture]]

## What we'd steal

- ★ **Progressive capability contracts:** overview → ranked action → exact entity; inline signatures only when confidence is high. Use for large internal tool graphs; evaluate discovery misses. [[sources/kody-hq--kody#search]]
- **Mirror actionable information in text and structured output:** prevent a host's channel preference from hiding required call fields. [[sources/kody-hq--kody#search]]
- **Separate stable module code and parameters:** reuse execution graphs and make varying inputs reviewable. [[sources/kody-hq--kody#execute-contract]]
- **Bundle calls only after the plan is clear:** use code for exact composition; return to the person/model when results change scope or require a decision. [[sources/kody-hq--kody#execute-contract]]
- **Graduate repeated code into published exports:** typed contracts plus explicit adoption of snapshots; don't distribute parallel handwritten host copies. [[sources/kody-hq--kody#execute-contract]]
- ★ **Keep authority behind the facade:** generated code calls narrow credential/capability use sites; give errors enough metadata for repair without returning secrets. [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#host-allowlist]]
- **Make a long operation observable through a durable handle:** keyed retry reads the same run; durable workflow retry remains a separate mechanism. [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#workflows]]
- **Measure the whole path:** discovery rounds, contract accuracy, bundling, sandbox startup, returned context, failed retries and end-to-end completion. Kody's phase timing makes this an experiment we can run, not a benefit already established. [[sources/kody-hq--kody#execute-contract]]

## Timeline

- 2026-11-02 — Kody source investigated and concept added; no comparative runtime evaluation.

## Related

- [[artifacts/projects/kody]] — full project study and exhaustive mechanism ledger.
- [[concepts/super-agent-architecture]] — coordination can sit above a compact capability substrate.
- [[concepts/workspace-skill-distribution]] — portable behavior distribution is related but distinct from executable state/capability hosting.

## Open questions

- TODO: ingest Cloudflare's primary Code Mode explanation and independently investigate another implementation.
- TODO: compare static tools against search/execute on equivalent tasks, permission scopes and model budgets.
- TODO: examine how approvals bind to composed code and changed parameters across hosts.
