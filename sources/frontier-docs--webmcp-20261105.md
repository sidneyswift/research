---
domain: sources
type: docs-page
url: https://webmachinelearning.github.io/webmcp/
retrieved: 2026-11-05
snapshot-location: sources/frontier-docs--webmcp-20261105/
last-reviewed: 2026-11-05
---

# WebMCP: draft, browser documentation and testing contracts

## Snapshot details

Eleven captures/notes retrieved2026-11-05; file URLs, byte counts, representations and SHA-256 values live in [captures.json](frontier-docs--webmcp-20261105/captures.json). Ten are returned textual documents or HTML converted to Markdown; the Edge entry is original notes from a rendered first-party article because direct retrieval returnedHTTP403. The complete Edge article is not preserved. No repository clone was created; raw GitHub documents are immutable local captures of living URLs, not commit-pinned upstream repositories.

The draft is dated2026-11-02. Chrome overview/imperative/declarative/tool-security/best-practices pages display respective last updates2026-10-07/10-16/09-25/09-01/10-30. Agent-security is published2026-06-09; Edge announcement2026-09-21. Playwright's methods are marked addedv1.64; current installation/release compatibility was not executed.

Reviewed scope: draft status, introduction, API dictionaries, execution/registration signals, origin gates and security recommendations; explainer background/goals/lifecycle/best-practices/alternatives; complete bounded Chrome guides; declarative proposal motivation/attributes/schema/response design; Playwright WebMCP reference; Edge's WebMCP subsection. This is not an exhaustive algorithm-conformance review. Captures do not preserve interactive demos, rendered visual states, linked source projects or every image. API descriptions/examples are evidence of published design, not runtime acceptance. Instructions to install, enable flags, register origin trials or submit feedback were treated as source content; none was executed.

## Anchor map

- `#root` — collection and receipt above; reviewed scope and evidence limits.
- `#draft-status` — [spec.md](frontier-docs--webmcp-20261105/spec.md), title/status: Draft Community Group Report2026-11-02; neither W3C Standard nor Standards Track.
- `#current-imperative-contract` — [spec.md](frontier-docs--webmcp-20261105/spec.md), sections4.1–4.2: Document extension, ModelContext, schemas, annotations, registration/execution signals and returned tool identity.
- `#origin-gates` — [spec.md](frontier-docs--webmcp-20261105/spec.md), sections4.4/6.3.4: tools policy, exposedTo, fromOrigins; permissions versus residual agent risks.
- `#browser-vs-backend` — [explainer.md](frontier-docs--webmcp-20261105/explainer.md), Background and Motivation, Goals & Non-Goals, Alternatives Considered; browser-local design complements remote MCP.
- `#tool-lifecycle` — [chrome-imperative.md](frontier-docs--webmcp-20261105/chrome-imperative.md), registration/unregistration/cancellation/discovery/execution/events: version-specific guidance, navigation result and argument representation.
- `#declarative-chrome` — [chrome-declarative.md](frontier-docs--webmcp-20261105/chrome-declarative.md), registration, fields, submission, visual states; Chrome-documented behavior rather than current CG normative coverage.
- `#declarative-proposal` — [declarative-explainer.md](frontier-docs--webmcp-20261105/declarative-explainer.md), motivation/form attributes/schema synthesis/response options; separate proposal status confirmed by explainer's Future Exploration section.
- `#browser-availability` — [chrome-overview.md](frontier-docs--webmcp-20261105/chrome-overview.md), Get started/Limitations/Permissions policy: origin trial fromChrome149, local flag, contextual discovery; no browser executed.
- `#edge-preview` — [edge-preview-notes.md](frontier-docs--webmcp-20261105/edge-preview-notes.md), original notes from WebMCP subsection under Ready for testing; not a preserved full article or independently tested Edge build.
- `#tool-author-security` — [chrome-tool-security.md](frontier-docs--webmcp-20261105/chrome-tool-security.md), hints, origin exposure, suggested character budgets, consent discussions; preliminary recommendations, not universal hard limits.
- `#agent-security` — [chrome-agent-security.md](frontier-docs--webmcp-20261105/chrome-agent-security.md), authenticated sessions, malicious metadata/output and deterministic/probabilistic defense layers; guidance rather than measured protection.
- `#design-practices` — [chrome-best-practices.md](frontier-docs--webmcp-20261105/chrome-best-practices.md), architecture constraints, strategy/naming, input, reliability, stale work and evals; publisher advice, not an executed experiment.
- `#playwright-testing` — [playwright-webmcp.md](frontier-docs--webmcp-20261105/playwright-webmcp.md), class introduction/tools/callTool: frame scope, experimental setup, result/error distinctions, v1.64 method markers.
- `#documentation-drift` — comparative anchor: spec/Chrome imperative use document.modelContext and Hint-suffixed annotations; Playwright introduction uses navigator.modelContext and lists differently named annotations. Chrome tool-security links requestUserInteraction, absent from captured current draft/imperative guide. Explainer excludes declarative from current specification while Chrome documents it. These are publication disagreements; runtime compatibility remains untested.

## Why we cite this

Primary evidence for [[artifacts/projects/webmcp]], extending [[concepts/developer-documentation-design]] from retrieved knowledge to page-local callable capabilities. Interpret through [[patterns/quality-bar/revision-bound-review]] and [[patterns/behavioral/context-is-not-authority]]; published support, implementation access and executed behavior differ.

## Popularity and credibility signals

As-of2026-11-05: community-group document editors identify Google/Microsoft affiliations; Chrome and Edge publish first-party guidance; Playwright publishes a testing interface. These establish institutional participation and documented tooling, not adoption counts, effectiveness or cross-browser universality. No stars/install counts measured.

## Related sources

- [[sources/mintlify--agent-documentation-docs]] — existing vendor WebMCP namespace differs from this current draft; preserve historical capture.
- [[sources/modelcontextprotocol--mcp-core-and-extensions-docs]] — remote MCP's core/extension contracts are a separate layer.
