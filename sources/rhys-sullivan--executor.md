---
domain: sources
type: repo
url: https://github.com/RhysSullivan/executor
retrieved: 2026-11-04
snapshot-location: sources/rhys-sullivan--executor/
upstream-commit: 3cf6e54659cb34ac731fe3cf747ca139be769b93
last-reviewed: 2026-11-04
---

# Executor capability contracts and dispatch

> Primary-source map for general integration/tool registration, discovery and sandbox dispatch.

## Snapshot details

- Inspected the existing clean source clone at `3cf6e54659cb34ac731fe3cf747ca139be769b93`, dated October 26. `sources/executor` is its compatibility link; the manifest retains the earlier `9c67fd5` evidence commit separately.
- Read selected source paths and nearby contracts. No source application, integration or provider calls were run; source behavior is not runtime qualification.
- Review date is November 4; this does not claim a new upstream pull or original clone date.

## Anchor map

### tool-contract

[SDK tool definitions](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/sdk/src/tool.ts#L1-L58) distinguish plugin-produced `ToolDef` metadata from persisted addressable tools. Tools carry integration/owner/connection identity, description and optional schemas/annotations. The common representation is not a business ontology or proof of equal schema/permission guarantees across plugins.

### plugin-boundary

[Plugin tool production](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/sdk/src/plugin.ts#L355-L407) runs on connection creation, refresh or OAuth completion. It returns tools/shared definitions and can mark an incomplete enumeration so existing catalog entries survive. [Invocation hooks](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/sdk/src/plugin.ts#L741-L778) separate resolving tools, projecting schemas, invoking tools with resolved credentials and side-effect-free argument checks.

### openapi

[OpenAPI definition compilation](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/plugins/openapi/src/sdk/definitions.ts#L291-L311) plans tool names from operation IDs, explicit tool paths, methods, paths and tags. [Bindings and compilation](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/plugins/openapi/src/sdk/backing.ts#L196-L250) retain method/server/path/parameter/body/response information. [Public definition/binding projections](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/plugins/openapi/src/sdk/backing.ts#L315-L343) create tool metadata and stored operations. [The public core entry](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/plugins/openapi/src/sdk/index.ts#L1-L69) exports compilation and request-building helpers separately from the full application.

### persisted-catalog

[SDK persistence](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/sdk/src/executor.ts#L3820-L3865) shows catalog preservation and stamping rows with tenant, owner, subject, integration, connection, plugin, schemas and timestamps. Specs produce tools at configured create/refresh points; a remote-catalog plugin also has TTL/stale refresh behavior. This is not rebuilding every spec for every model request.

### discovery

[Search scoring and paging](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/execution/src/tool-invoker.ts#L604-L752) use token/phrase matches over tool path, integration, name and description. Namespace-only enumeration is exact and paged. This inspected default is deterministic keyword retrieval, not automatic reconciliation of human/business meanings. [Engine dispatch](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/execution/src/engine.ts#L338-L487) exposes search, integration listing and exact tool description through the same invoker and delegates ordinary calls onward. Host tool surfaces have modes/optional extras; the source does not establish an invariant of exactly two top-level tools.

### sandbox

[Kernel contract](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/kernel/core/src/types.ts#L17-L28) defines the general invoker as `{path,args}`. [QuickJS proxy](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/kernel/runtime-quickjs/src/index.ts#L225-L251) collects property segments and dispatches the function call; [the bridge](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/kernel/runtime-quickjs/src/index.ts#L304-L331) calls the host invoker. Arbitrary path construction is not permission to invoke an unknown tool.

### policy-and-invocation

[Invocation path](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/core/sdk/src/executor.ts#L6788-L6865) validates arguments before required approval, enforces the decision, resolves connection credentials afterward and invokes the owning plugin. [OpenAPI plugin wiring](https://github.com/RhysSullivan/executor/blob/3cf6e54659cb34ac731fe3cf747ca139be769b93/packages/plugins/openapi/src/sdk/plugin.ts#L1389-L1420) delegates those generic hooks to the HTTP adapter. These are source mechanisms, not qualification of another application's delegated identity or approval requirements.

## Why we cite this

Supports a general adapter → stored definition → discover/describe → sandbox path/args → policy/credential → provider adapter model. Public helper exports are reuse candidates; package-version, schema fidelity, request serialization, runtime packaging and application-specific authorization must be checked before adoption.

## Popularity signals

Not collected; popularity is not the evidence for these implementation claims.

## Related sources

- [[sources/kody-hq--kody]] — another compact capability discovery/execution design with different registry and policy behavior.
