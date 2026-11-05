---
domain: projects
type: internal-project
name: designing-apis-for-agents
status: research
owner: Sidney Swift
last-reviewed: 2026-11-04
---

# Designing APIs for Agents

> A growing research hub for APIs that agents can discover, understand, compose, and use reliably across a large business platform.

## Purpose and scope

Study how business capabilities become useful agent-facing interfaces: naming, categorization, permissions, data retrieval, commands, workflows, runtime execution, and failure recovery. Keep uncertain future uses in view without assuming that every internal step deserves its own endpoint.

This is a research group and navigation node. Findings live in the linked concept, artifact, and pattern pages; evidence lives in `sources/`. The hub groups them without becoming a second copy of their claims. It is not a runnable API product or a confirmed pattern.

## Start here

- [[analyses/frontier-and-business-api-design]] — **working draft** cross-system synthesis; read its coverage and review limits.
- [[concepts/agent-api-learning-and-evolution]] — training versus runtime discovery, a controlled experiment, and conditional 1/5/10-year scenarios.

| Research node | Role in this group |
| --- | --- |
| [[concepts/business-platform-api-design]] | Foundation: business naming, reads versus commands, durable operations, modularity, and platform conventions. Nine primary sources captured 2026-11-04; illustrative architecture is labeled as our recommendation. |
| [[concepts/code-mode-capability-interface]] | Agent interface research: typed capability discovery and composition; read the page's implementation and evidence boundaries. |
| [[concepts/agent-control-plane]] | Background execution context: task identity, sessions, hosts, access, and durable work. |
| [[concepts/durable-agent-execution]] | Runtime reliability research: persistence, recovery, and the boundaries of execution guarantees. |
| [[concepts/ubiquitous-language-for-agents]] | Shared domain vocabulary as an input to consistent interface naming. |

## Research tracks

These are questions to investigate, not settled findings. Extend the existing foundation pages where the subject, mechanism, and role overlap; create a new node only when the distinction earns its own page.

| Track | Questions to investigate | Current home |
| --- | --- | --- |
| Business boundaries and modularity | What should be a reusable capability, a private helper, or a complete workflow? What evidence justifies splitting a service? | [[concepts/business-platform-api-design]] |
| Naming and discovery | How should agents find capabilities among hundreds or thousands of operations? Which names, categories, descriptions, and schemas reduce wrong selections? | [[concepts/ubiquitous-language-for-agents]], [[concepts/code-mode-capability-interface]] |
| Reads, commands, and workflows | How do callers distinguish inspection, refresh, calculation, execution, and approval? When should a command return a resource versus a run? | [[concepts/business-platform-api-design]] |
| Long-running execution | How should agents start, poll, resume, cancel, and inspect partial results? What must survive an agent session ending? | [[concepts/durable-agent-execution]], [[concepts/agent-control-plane]] |
| Permissions and business authority | How do tenant, actor, delegated authority, approval, and queued execution interact? | [[concepts/agent-control-plane]], [[patterns/behavioral/context-is-not-authority]] |
| Failure, retries, and concurrency | How do retries avoid duplicate effects? How are unknown outcomes reconciled? Which preconditions must be rechecked? | [[concepts/business-platform-api-design]], [[patterns/structural/authoritative-recheck-after-notification]] |
| Agent interface surfaces | When should a capability be HTTP, an MCP tool, an SDK method, or a code-composition interface? How much should adapters reshape it? | [[concepts/code-mode-capability-interface]] |
| Evaluation and evolution | How can we measure correct selection, safe execution, recovery, and compatibility across real business tasks? | Open; attach evidence before creating a dedicated concept. |

## Evidence map

### API system case studies

| System | Research node | Evidence class |
| --- | --- | --- |

| Shopify (commerce / agent-facing UCP) | [[artifacts/projects/shopify-api]] | Documentation; no live execution |
| OpenAI (Model/tool protocol and managed runtime) | [[artifacts/projects/openai-agent-api]] | Documentation; no live execution |
| Anthropic (Messages, tool exchange, batches and managed runtime) | [[artifacts/projects/anthropic-agent-api]] | Documentation; no live execution |
| Microsoft (ERP) | [[artifacts/projects/business-central-api]] | Documentation; no live execution |
| SAP (ERP / sales) | [[artifacts/projects/sap-sales-api]] | Documentation; no live execution |
| Salesforce (CRM / business operations) | [[artifacts/projects/salesforce-api]] | Documentation; no live execution |
| Cloudinary (DAM / media) | [[artifacts/projects/cloudinary-api]] | Documentation; no live execution |
| Gusto (Payroll) | [[artifacts/projects/gusto-api]] | Documentation; no live execution |
| ftrack (Production tracking) | [[artifacts/projects/ftrack-api]] | Documentation; no live execution |
| Stripe (Payments) | [[artifacts/projects/stripe-api]] | Documentation; no live execution |

The case studies own findings and source maps. The synthesis links them without replacing their detailed contracts.

### Foundation sources

The source citation pages own version, retrieval, credibility, and anchor details. See the foundation concept for the claims they support.

- **Resource and action conventions:** [[sources/google--aip-121]], [[sources/google--aip-136]].
- **Long-running contracts:** [[sources/google--aip-151]], [[sources/microsoft--async-request-reply]].
- **Business boundaries and read/write models:** [[sources/microsoft--domain-analysis]], [[sources/microsoft--cqrs]].
- **Platform conventions and HTTP semantics:** [[sources/microsoft--web-api-design]], [[sources/ietf--http-semantics]].
- **Retry-safe intent:** [[sources/aws--idempotent-apis]].
- **Agent-facing composition:** [[sources/philschmid--code-mode]], [[sources/kody-hq--kody]]; follow [[concepts/code-mode-capability-interface]] for what was actually inspected.

## Next investigations

Suggested work, not a scheduled commitment:

1. Compare one business capability exposed as HTTP, an MCP tool, and a typed SDK/code interface. Inspect actual schemas and implementations, not just promotional descriptions.
2. Compare a retrieval endpoint, an explicit refresh, and a full workflow against the same business task. Record side effects, freshness, permissions, cost, and results.
3. Trace a long-running operation through duplicate submission, worker restart, provider timeout, permission change, cancellation, and partial success.
4. Examine how a large tool/API catalog supports discovery and selection. Look for evaluations of descriptions, grouping, and capability loading.
5. Build an evidence-backed endpoint review checklist once repeated case studies establish what it needs to catch.

## Adding to this group

- Ingest new evidence through the wiki's existing INGEST operation and source schema; preserve snapshots and registered citation anchors.
- Deduplicate against the current nodes before creating another concept or artifact.
- Add each new node to this hub and the relevant domain/root indexes; link back here from the node.
- Record source version/date, the concrete interface, effects, permissions, lifecycle, failure behavior, and the boundary between documented claims and inspected behavior.
- Extract portable takeaways on the owning page, including counter-examples and open questions. Keep unverified hypotheses labeled.
- Log durable updates in `log.md`. Do not promote a confirmed pattern on documentation agreement alone; the wiki requires two inspected artifacts.

## Open questions

- Which business domain should supply the first concrete agent-facing API case study?
- Which existing platform endpoints should we examine for hidden side effects, ambiguous names, or overlapping responsibilities?
- What task corpus would let us compare interface designs by observed agent behavior?

## Activity

- 2026-11-04 — Created the group from the business-platform API research; linked the existing agent interface, runtime, authority, and vocabulary research. Agent-specific evaluations remain future work.

## Research pass — 2026-11-04

Completed the first comparative documentation pass across nine systems. [[analyses/frontier-and-business-api-design]] records the comparison and limitations; [[concepts/agent-api-learning-and-evolution]] owns the training and horizon questions. Next work is controlled task evaluation and deeper lifecycle/permission verification, not a claim that agent usability has been established. Reuse [[_schemas/api-case-study]] when adding another system.

## Shopify addition — 2026-11-04

Added [[artifacts/projects/shopify-api]] as the tenth API case study, with sixteen official documentation captures. It connects established Admin/business contracts to negotiated agent discovery, cart/checkout phases, browser/server tools and current developer context. [[patterns/composition/negotiated-capability-intersection]] captures the new proposed mechanism; [[analyses/frontier-and-business-api-design]] incorporates its comparison. Auth/example discrepancies and untested runtime behavior remain explicit on the artifact page.

## Related documentation research — 2026-11-05

[[projects/writing-amazing-developer-docs/README]] studies how developers and agents discover, learn, implement and recover using published documentation. [[concepts/developer-documentation-design]] owns the writing and maintenance findings.
