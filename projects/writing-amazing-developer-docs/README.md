---
domain: projects
type: internal-project
name: writing-amazing-developer-docs
status: research
owner: Sidney Swift
last-reviewed: 2026-11-05
---

# Writing amazing developer docs

A growing research node for documentation that helps people and agents complete real development tasks correctly.

## Start here

- [[concepts/developer-documentation-design]] — owning synthesis: audience, information architecture, writing, examples, failure/recovery, navigation, release workflow, automation and agent access. Includes source-backed tensions and an exhaustive portable-ideas ledger.
- [[projects/writing-amazing-developer-docs/page-blueprints]] — practical authoring templates, example rewrites and a review checklist derived from that synthesis; proposed templates, not deployed platform documentation.
- [[projects/designing-apis-for-agents/README]] — related API contracts and platform design research.

## Evidence map

| Collection | What was examined | Boundary |
| --- | --- | --- |
| [[sources/diataxis--documentation-framework#root]] | Six pages: four needs, forms and incremental workflow | Author's framework; no task-performance experiment |
| [[sources/google--developer-documentation#root]] | Eight pages: audience, samples, procedures, headings, links, accessibility, documents, maintenance | Published guidance, not a claim about every Google product |
| [[sources/writethedocs--documentation-practice#root]] | Two pages: docs as code and initial project documentation | Community practice; no quantified causal effect |
| [[sources/gitlab--documentation-engineering#root]] | Six captured pages, targeted sections on topics, tasks, troubleshooting, workflow and checks | Broad style guide captured as context, not exhaustively reviewed |
| [[sources/developer-docs--product-examples#root]] | Thirteen product pages across Stripe, GitHub, Twilio and Cloudflare | Textual mechanisms and documented contracts; no visual review or runtime tests |
| [[sources/cloudflare--docs-for-agents#root]] | One page: scoped Markdown, indexes, schemas, skills and MCP | Published access surfaces; no independent agent-success benchmark |
| [[sources/answerai--llms-txt#root]] | One page: proposal v2 and discovery conventions | Informal proposal, no guaranteed client support |
| [[sources/cummaudo--api-documentation-knowledge#study]] | 2019 mapping paper, 21 selected studies and 34 recommendations | Original research notes and version/hash restoration; no full-paper reproduction |
| [[sources/nam--documentation-use#study]] | CHI 2024 study, four services, over 100,000 users | Selected methods/results/discussion read; observational, one vendor |

Coverage: **37 documentation pages captured plus two paper metadata pages and two original paper-reading notes**. Captures have byte/hash receipts. Capture volume is not a completeness score: section-level reviewed scope and representation limitations are on the source pages. Guessed inaccessible URLs are excluded.

## Product examples to inspect

| Example | Concrete technique worth studying |
| --- | --- |
| Stripe webhooks | Handler setup together with retries, order, duplicates, signature inputs and local diagnostics. [[sources/developer-docs--product-examples#stripe-webhooks]] |
| Stripe errors and versioning | Machine error fields linked to human debugging; separate governing API, account, SDK and webhook versions. [[sources/developer-docs--product-examples#stripe-errors]] [[sources/developer-docs--product-examples#stripe-versioning]] |
| GitHub quickstart | Choice of tool and execution context; initial read-only request and explicit Actions permissions. [[sources/developer-docs--product-examples#github-quickstart]] |
| GitHub troubleshooting | Actual symptoms, including private resources returning 404 and missing paginated data. [[sources/developer-docs--product-examples#github-troubleshooting]] |
| GitHub webhook testing | Separate evidence for delivery, local forwarding and application processing. [[sources/developer-docs--product-examples#github-webhook-testing]] |
| Twilio SMS quickstart | Account/trial/sender/recipient prerequisites before assuming correct code can send. [[sources/developer-docs--product-examples#twilio-sms-quickstart]] |
| Twilio error 21610 | Stable exact-error URL; business state can require recipient action rather than retries. [[sources/developer-docs--product-examples#twilio-error-21610]] |
| Twilio webhook security | Framework-sensitive URL/body/parameter preparation alongside validation guidance. [[sources/developer-docs--product-examples#twilio-webhook-security]] |
| Cloudflare API calls | Shell/quoting/platform differences made explicit. [[sources/developer-docs--product-examples#cloudflare-api-calls]] |
| Cloudflare Workers quickstart | Observe a local response, change it, check the result, then deploy. [[sources/developer-docs--product-examples#cloudflare-workers-quickstart]] |
| Cloudflare Markdown | Alternate representation includes negotiation and cache/metadata concerns. [[sources/developer-docs--product-examples#cloudflare-markdown-agents]] |

These are selected mechanisms, not a vendor ranking or blanket endorsement. Large mixed-context pages can lose prerequisites when a reader extracts only one snippet. No support or conversion gains were measured.

## Next investigations

1. Observe fresh developers completing three real platform integration tasks using current docs; record setup, discovery, correctness and recovery separately.
2. Audit existing Flex docs against those failed steps before redesigning navigation.
3. Test real supported languages/shells from clean environments and verify business results.
4. Compare scoped Markdown retrieval, docs search and ordinary HTML for the same bounded agent tasks.
5. Investigate ownership and release tooling before adding a second independently authored documentation surface.
6. Extend research to internal architecture docs, ADRs and runbooks; current coverage emphasizes product/API integration docs.

## Adding to the group

Use INGEST; deduplicate against the owning concept, capture evidence immutably, register source anchors and add a dated note here and in log.md. Distinguish author guidance, visible documentation behavior, runtime execution and measured developer outcomes. Keep proposed tools and templates labeled.

## Activity

- 2026-11-05 — Initial deep research collection and practical blueprints created; no production docs were replaced, no examples executed and no usability experiment performed.
