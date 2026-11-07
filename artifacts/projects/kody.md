---
domain: artifacts
subdomain: projects
type: project
name: kody
creator: "[[creators/kody-hq]]"
source: "[[sources/kody-hq--kody]]"
ecosystem: MCP / Cloudflare Workers
status: source-investigated
last-reviewed: 2026-11-03
---

# Kody

> A shared cloud home for agent capabilities and state across MCP hosts: discover a capability, compose code to call it, and keep durable packages, credentials and personal memory outside any one chat product.

## Attributes

- **Unit:** multi-component platform, not merely an MCP connector and not a general agent harness. Pinned at `9d96cfb916552b889ee8989027618b35ecd554ba`. 894 GitHub stars and 85 forks as-of 2026-11-02; attention rather than adoption. [[sources/kody-hq--kody#intent]], [[sources/kody-hq--kody]]
- **Distribution/license:** repository uses FSL-1.1-ALv2 with a competing-use restriction and per-version Apache-2.0 transition after two years. Public packages have a separate contribution/distribution model. Preserve this distinction when borrowing code; the platform is fair source, not an unrestricted Apache release today. [[sources/kody-hq--kody#license]], [[sources/kody-hq--kody#root]]
- **Investigated:** intent/topology, discovery/execute contracts and owning registry/replay paths, request identity, selected authorization and credential paths, fetch gateway, memory design, workflows and repo-session contracts. No installation, tests, live MCP calls, deployment or security audit. [[sources/kody-hq--kody#architecture]], [[sources/kody-hq--kody#execute-replay]]

## Relationships

- [[creators/kody-hq]]; [[concepts/code-mode-capability-interface]] — the core interface technique.
- [[artifacts/projects/dsh-superagent-prototype]] and [[concepts/super-agent-architecture]] — complementary event coordination versus portable state/capability infrastructure. DeepSeek's essay names credential-without-disclosure as open; Kody supplies concrete mechanisms, without proving the entire distributed threat model solved. [[sources/deepseek--super-agent-design#open-problems]], [[sources/kody-hq--kody#credentials]]
- [[artifacts/projects/eve]] / [[concepts/durable-agent-execution]] — runtime, state and durable-work comparison. [[patterns/composition/single-source-multi-surface-distribution]] — shared packages and runtime rather than host-specific copies. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#workflows]]

## Mechanism and themes

### A compact entry point into a large capability graph

**Documentation:** `search` returns task-ranked capabilities, guides, packages/exports, integration and secret metadata, or a domain index for broad queries. Known entity refs open full contracts or bounded heading/line fragments. High-confidence results inline signatures and ready-to-run code. Connected MCP servers appear first as server entities; their individual tools are discovered within the server/domain. Public community packages use a separate discovery path. [[sources/kody-hq--kody#search]]

**Implementation:** built-in domains form a lazily loaded, memoized registry; connected-server snapshots synthesize dynamic domains. Caller/feature filtering is applied to the assembled registry. The dynamic cache includes owner and remote-server state. This saves cold-start and repeated assembly costs but does not establish zero cache drift or end-to-end authorization for every capability. [[sources/kody-hq--kody#registry]]

**Documentation:** `execute` takes an ES module with a default export and separate JSON `params`. It imports `kody:runtime`, saved package exports via `kody:@scope/package/export`, and compatible npm dependencies. Put changing arguments in `params` to reuse the same module graph. Static package imports are checked at publication and snapshotted in dependent packages; republish dependents to adopt changes. Ad hoc imports can resolve current versions, which is convenient but weakens reproducibility unless inputs/dependencies are recorded. [[sources/kody-hq--kody#execute-contract]]

**Implementation correction, 2026-11-03:** the pinned `register-tools.ts` registers **three** tools: `search`, `execute` and `api`. The additional `api(operationId, params)` invokes one HTTP/API operation without sandbox execution or execute quota; its description sends composed calls, transformations, external fetches and execute-only capabilities to `execute`. The direct path is not Code Mode composition, and not every discovered capability is on the HTTP/API surface. This corrects a literal-two-tool interpretation of the intent discussion without changing the compact-interface thesis. [[sources/kody-hq--kody#mcp-surface]]

The result is a **small discovery/execution vocabulary over a large backend**, not a small system. Code can compose calls, branching and parallel work before returning only the useful result. The host still needs adequate code generation, permission visibility and error recovery. [[sources/kody-hq--kody#intent]], [[sources/kody-hq--kody#execute-contract]]

### Identity survives the transport and the trigger

**Implementation:** RequestContext separates org, actor, attribution and credential. Scheduled/webhook/event runs carry an enablement with the enabler's identity, current role and narrowed credential scopes; a trigger without enablement carries no person/membership. Nested lineage retains identity rather than becoming an arbitrary owner. Authorization types represent org mismatch, missing permission, scope narrowing, profile restrictions and credential locks. Selected code is evidence of the design, not a whole-platform isolation proof. [[sources/kody-hq--kody#request-context]], [[sources/kody-hq--kody#authorization]]

**Documentation:** one user may have concurrent chats and distinct agents. A user ID or MCP connection is not a conversation. Caller-passed `conversationId` handles progressive disclosure; personal-memory snippets may repeat after context compaction rather than being hidden globally after one display. This is a valuable distinction between shared durable knowledge and per-conversation state. [[sources/kody-hq--kody#conversation-identity]], [[sources/kody-hq--kody#memory]]

### Use credentials without returning plaintext to package code

**Documentation + implementation + test inspected:** secret getters return opaque references; trusted credential resolution validates actor/org, declared package needs and grants before applying the use. The inspected test crosses real SQLite-backed storage and a capability proxy, uses selected mocks, asserts no plaintext in outcomes and rejects a manifest `raw` escape hatch. It has not been run in this research session. [[sources/kody-hq--kody#credentials]], [[sources/kody-hq--kody#credential-resolution]], [[sources/kody-hq--kody#credential-tests]]

**Implementation:** outbound fetch traverses a trusted gateway that consumes quota, resolves credential placement and placeholders, imposes deadlines, suppresses credential-bearing redirect following, seals relevant returned tokens and redacts echoed secrets/errors. OAuth helper code has its own exact-host allowlist checked before attaching a token. **Limit:** these checks do not prevent harmful API operations on an approved host, nor establish protection against every encoding or indirect disclosure path. Host approval, credential placement, package rights and operation authorization are separate questions. [[sources/kody-hq--kody#fetch-gateway]], [[sources/kody-hq--kody#host-allowlist]]

### Transport retry, durable retry and external mutation differ

**Implementation:** keyed execute checks for an existing run before admission and claims a record before sandbox work. Existing running records return a follow handle; terminal records replay bounded retained success/error results. If an explicit key cannot be claimed, it fails rather than knowingly launching an untracked duplicate. Requests without a caller key use a generated-key/best-effort recording path. [[sources/kody-hq--kody#execute-replay]]

**Documentation:** execute can return `inProgress`, `runId` and `idempotencyKey` before the MCP transport deadline, while work continues. Client disconnect before that handoff has different cancellation semantics. A stranded run can become `platform_interrupted`, with outcome unknown. This is deduplication and outcome visibility at the run boundary, not exactly-once external effects. [[sources/kody-hq--kody#execute-contract]]

**Documentation + selected implementation:** long work goes into Cloudflare Workflows. Workflow package attempts deliberately bypass the package invocation result cache, allowing a retry to execute rather than replay a prior timeout. Enqueue and per-attempt source revisions are recorded. `latest` can pick up republished fixes; `pinned` refuses if publication moved, because older bundles are not retained for execution. Inline code is stored, but imported packages can still resolve current revisions. Cancellation does not cancel independently created successor workflows. [[sources/kody-hq--kody#workflows]], [[sources/kody-hq--kody#workflow-implementation]]

### Portable state does not mean all state is memory

**Documentation:** memory is personal and can follow the person into an org-bound tool call. Shared team knowledge belongs in packages/instructions; runtime cursors in package storage; versioned configuration in repos; credentials in the credential system. Compact personal snippets are labeled; copying them into org packages should require asking. Verify-first memory writes are an agent workflow rule, not demonstrated here as an unbypassable host prerequisite. [[sources/kody-hq--kody#memory]]

**Documentation:** repo sessions expose file edits, diff, commit, checks, rebase and publish to filesystem-less agents. Checks can become outdated, source base can move, and locked package approval binds to one commit without unlocking the package. Publish tracks running/interrupted/published/pushed/not-published/failed outcomes. A pushed source commit and a live published revision are distinct. [[sources/kody-hq--kody#repo-sessions]]

### Execution can move; authority must remain explicit

**Documentation:** experimental execution contexts move code onto a registered machine with an ordered fallback chain and capability requirements. Credentialed requests still leave through Kody cloud. Sharing a context requires the requester to opt in because the operator sees code/results and can use the requester's credential capabilities while a run is active. Hiding credential values does not hide returned data. [[sources/kody-hq--kody#execution-contexts]]

Host commands require both local machine opt-in and a grant; remote controls can disable but cannot enable them. When enabled they run with the daemon user's OS authority, without approval per command. Filesystem policies must not be presented as containment for arbitrary shell commands. These are source contracts, not a verified installation. [[sources/kody-hq--kody#execution-contexts]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — a trigger's origin alone does not supply an enabled actor/grant; credential use is resolved outside agent code. [[sources/kody-hq--kody#request-context]], [[sources/kody-hq--kody#credential-resolution]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model-generated composition uses typed registered operations and trusted credential enforcement. [[sources/kody-hq--kody#registry]], [[sources/kody-hq--kody#credential-resolution]]
- [[patterns/composition/single-source-multi-surface-distribution]] — package/runtime contracts reused across execute, jobs, apps and workflows; snapshot adoption remains explicit. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#workflows]]
- [[patterns/quality-bar/revision-bound-review]] — supporting analogue: publish checks/approval refer to a specific source state; workflow pins mean exact revision or refusal. [[sources/kody-hq--kody#repo-sessions]], [[sources/kody-hq--kody#workflows]]

## What we'd steal

| Portable mechanism | Purpose and adaptation | Important limit / evidence |
| --- | --- | --- |
| ★ Search → entity contract → composed execute | Make a large capability set usable without loading it all into context | Requires reliable discovery and code generation. [[sources/kody-hq--kody#search]] |
| Compact direct API dispatch alongside execute | Avoid sandbox execution for a single registered HTTP/API operation; compare against two-tool and explicit-tool paths | Three tools are actually registered at this pin; latency/quality advantage is not measured here. [[sources/kody-hq--kody#mcp-surface]] |
| Broad query → domain overview | Keep exploration navigable before detailed ranking | Different contract from task-ranked search. [[sources/kody-hq--kody#search]] |
| Inline high-confidence signatures/examples | Save a second lookup when enough information is already known | Ambiguous hits still need detail. [[sources/kody-hq--kody#search]] |
| Semantic parity of text/structured tool output | Make host choice of response channel harmless for call details | This is a documented contract; client matrix untested here. [[sources/kody-hq--kody#search]] |
| Bounded guide/file heading and line lookup | Fetch exact context and fail on a missing anchor | Discovery is separate from access. [[sources/kody-hq--kody#search]] |
| Registry from domains + synthesized remote servers | Keep capability implementations and schemas behind one small facade | Cache freshness and caller filtering need verification. [[sources/kody-hq--kody#registry]] |
| Stable code graph + separate params | Reuse workers and make calls easier to audit | Ad hoc dependency resolution is not a lockfile. [[sources/kody-hq--kody#execute-contract]] |
| Static package imports with publication checks | Reuse typed utilities with visible dependencies | Dependents keep old snapshots until republished. [[sources/kody-hq--kody#execute-contract]] |
| ★ Actor, org, attribution and credential as distinct fields | Preserve who authorized, runs, owns and pays across nested work | Inspect every entrypoint before claiming universal coverage. [[sources/kody-hq--kody#request-context]] |
| Trigger enablement instead of implicit owner fallback | Keep passive incoming data from manufacturing permission | Role/enablement revalidation remains load-bearing. [[sources/kody-hq--kody#request-context]] |
| Explicit conversation handle; repeat cheap memory hints | Support concurrent agents and host compaction | Shared personal memory still needs a privacy boundary. [[sources/kody-hq--kody#conversation-identity]] |
| State-placement table | Prevent cursors, secrets, behavior and team knowledge becoming vague memory | Personal-to-team copy requires deliberate consent. [[sources/kody-hq--kody#memory]] |
| Verify related memories before writing | Deduplicate durable facts using model judgment | Documented procedure, not proven enforcement. [[sources/kody-hq--kody#memory]] |
| ★ Opaque credential refs and use-site resolution | Keep package/agent code from receiving plaintext values | Approved APIs can still cause harmful effects. [[sources/kody-hq--kody#credential-resolution]] |
| Host, package, declaration and placement gates | Narrow where and how credentials are sent | Host approval is not operation approval. [[sources/kody-hq--kody#credentials]] |
| Gateway quota before decryption; manual credential redirects | Bound abuse and avoid forwarding auth through redirects | Full gateway audit unperformed. [[sources/kody-hq--kody#fetch-gateway]] |
| No-plaintext negative fixtures across the proxy | Check output and errors, not only happy-path secret lookup | Inspected tests include mocks; unexecuted here. [[sources/kody-hq--kody#credential-tests]] |
| ★ Return a run handle before transport timeout | Let a host resume observation instead of repeating mutations | Early disconnect differs from completed handoff. [[sources/kody-hq--kody#execute-contract]] |
| Claim caller-supplied keys before sandbox work | Single-flight duplicate transport attempts | Retained results are bounded; external partial effects persist. [[sources/kody-hq--kody#execute-replay]] |
| Separate interactive execution and durable retry | Give slow workflows a retry lifecycle rather than extending chat waits | Retry re-executes code and needs idempotent external operations. [[sources/kody-hq--kody#workflow-implementation]] |
| Record enqueued and executed revisions | Explain exactly what code ran after delay or republish | `pinned` refuses old unavailable bundles; it does not retrieve them. [[sources/kody-hq--kody#workflows]] |
| Structured edit/check/publish repair states | Support agents without git/shell while preserving source ownership | Source push and runtime publication remain distinct. [[sources/kody-hq--kody#repo-sessions]] |
| Commit-specific package approval | Let a user approve a reviewable revision without permanent unlock | New changes need new checks/approval. [[sources/kody-hq--kody#repo-sessions]] |
| Machine-local enable, remote disable for shell authority | Make expansion of device access depend on the device operator | Enabled commands carry broad OS-user authority. [[sources/kody-hq--kody#execution-contexts]] |
| Fallback chain + requirements + `ranOn` provenance | Keep execution placement visible and avoid silent inappropriate fallback | Shared-machine operators see data and active credential use. [[sources/kody-hq--kody#execution-contexts]] |
| Real execution heartbeat distinct from origin smoke | Measure the actual owning MCP path | Source architecture describes it; live health was not checked. [[sources/kody-hq--kody#architecture]] |

## Tensions and anti-patterns

- **A tiny MCP surface can hide a large permission surface.** `execute` is explicitly marked potentially destructive and non-idempotent. Tool-count reduction must be paired with inspectable code, scoped capability enforcement and meaningful user approvals. [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#credentials]]
- **Portability shifts the dependency.** State can follow compatible MCP hosts, while runtime/credentials remain dependent on Kody and Cloudflare services. It is portability across clients, not proof of vendor-free migration. [[sources/kody-hq--kody#architecture]]
- **Personal memory and org isolation are different boundaries.** General org-state isolation prose must be read alongside the specific personal-memory design. A personal snippet in an org-bound tool response is not automatically shared team knowledge. [[sources/kody-hq--kody#intent]], [[sources/kody-hq--kody#memory]]
- **Exactly-once language needs a named boundary.** A workflow engine caching a successful step cannot undo a remote mutation before a failed attempt. Reusing an idempotency key is safe observation of a run, not proof an interrupted remote operation never occurred. [[sources/kody-hq--kody#execute-contract]], [[sources/kody-hq--kody#workflows]]

## Open questions and verification record

- TODO: run a two-host portability exercise with synthetic accounts; measure discovery rounds, recovery, memory visibility and output-channel parity.
- TODO: test credential substitution, redirects, response redaction and package-origin stamps with focused negative fixtures in isolation.
- TODO: inspect runtime enforcement behind shared-context opt-in and host-command dual gates; current findings there are documentation-level.
- TODO: measure search/execute token savings and total latency against a static-tool baseline. Interface intent alone supplies no percentage improvement.
- Source/wiki structural checks are recorded in [[log]]. No Kody account, credential, execution context, provider call or live deployment was activated.

## Related article: Code Mode

[[concepts/code-mode-capability-interface]] now includes [[sources/philschmid--code-mode#typed-interface]]. The article supplies an explanatory single-execution-tool sketch; Kody explicitly exposes discovery plus execution. Similar interface goals do not imply identical runtime or permission behavior. [[sources/kody-hq--kody#intent]]

## MCP research connection — 2026-11-04

[[concepts/model-context-protocol]] and [[analyses/mcp-and-extensions]] place Kody’s compact capability facade within the wider protocol/application stack. This adds protocol evidence, not a new live validation or a refresh of the pinned implementation. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]]

## Agent Habitat comparison — 2026-11-06

[[concepts/agent-habitat-architecture]] supplies a separate reference proposal for credential brokerage. Its lesson is narrower than compliance: hiding secret values does not by itself authorize every effect those secrets enable. No equivalence between Kody implementation and Habitat guarantees is asserted. [[sources/lhchavez--managed-agent-environments#credential-authority]]
