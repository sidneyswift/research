---
domain: concepts
type: concept
name: developer-documentation-design
creators: [Google, Diátaxis, GitLab, Write the Docs]
sources: [google--developer-documentation, diataxis--documentation-framework, gitlab--documentation-engineering, developer-docs--product-examples, nam--documentation-use, cummaudo--api-documentation-knowledge, cloudflare--docs-for-agents, answerai--llms-txt]
status: active
last-reviewed: 2026-11-05
---

# Developer documentation design

> Help a developer choose an approach, complete a real task, verify its result, and recover when it fails; maintain those instructions with the software they describe.

## What it is

Developer documentation is a product interface with several reading modes: learning, doing, consulting a contract, understanding a design, and diagnosing a problem. Diátaxis separates four underlying needs; GitLab adds explicit troubleshooting topics and allows several topic types on one page. Treat these as tools for deciding what belongs together, rather than a mandatory folder taxonomy. [[sources/diataxis--documentation-framework#overview]] [[sources/gitlab--documentation-engineering#topic-types]]

This page is the owning synthesis and recommendation ledger. [[projects/writing-amazing-developer-docs/README]] is its research navigation hub. Recommendations below are our interpretation of the named evidence, not measured universal rules. No product examples were executed, no docs site was visually usability-tested, and no ranking of vendors is claimed.

## Where it came from

The evidence combines Daniele Procida's Diátaxis framework, Google's technical-writing courses and style guidance, Write the Docs' community practice, GitLab's published documentation workflow, concrete product documentation, and two academic studies. The 2019 mapping study covers 21 selected studies; the 2024 CHI paper analyzes documentation-use logs for four Google cloud services. Neither establishes that following this checklist causes a particular productivity gain. [[sources/diataxis--documentation-framework#root]] [[sources/google--developer-documentation#root]] [[sources/writethedocs--documentation-practice#root]] [[sources/gitlab--documentation-engineering#root]] [[sources/cummaudo--api-documentation-knowledge#study]] [[sources/nam--documentation-use#study]]

## Why it matters

In a business platform, consumers may know HTTP and TypeScript but lack the business rules behind an inventory reservation, payroll approval, asset publication or vendor refresh. Google's audience guidance explicitly distinguishes professional role from proximity to a subject. Write down the domain knowledge a task requires; being an experienced developer does not imply familiarity with your platform. [[sources/google--developer-documentation#audience]] [[concepts/business-platform-api-design]]

A useful target is **independent, correct task completion**. Measure whether readers find the right instructions, choose a supported path, obtain the intended result and recognize failure. This is our proposed operating target, grounded in tutorial observation, runnable sample guidance and the limits of observational usage logs; it is not an established universal metric. [[sources/diataxis--documentation-framework#tutorials]] [[sources/google--developer-documentation#sample-code]] [[sources/nam--documentation-use#study]]

## Evidence & claims

### 1. Design around the reader's task and starting knowledge

Before outlining, specify the reader, their starting state and the intended result. Example authoring brief, **illustrative**: “An integrator who knows REST but is new to our company must refresh a vendor directory in a test tenant and verify which source revision became available.” List required role, account, test data, tools, versions and permissions. Link unfamiliar shared concepts without making the reader tour the entire architecture. [[sources/google--developer-documentation#audience]] [[sources/google--developer-documentation#documents]] [[sources/gitlab--documentation-engineering#tasks]]

Use titles that reveal intent. “Refresh vendor data from Business Central” communicates a task; “Vendor data freshness” names a concept; “Vendor refresh operations” names a reference family. “Overview,” “Advanced,” and “Integration” provide little information when shown alone in search. This is an application of Google's descriptive-title guidance and Diátaxis' problem-oriented how-to guidance. [[sources/google--developer-documentation#headings]] [[sources/diataxis--documentation-framework#how-to]]

Avoid using the organization chart as the only navigation model. A business task may cross identity, data and workflow boundaries. Provide task entry points that link to canonical resource references, while references follow the API's structure. The task/reference distinction is supported by Diátaxis; this dual navigation model is our platform recommendation. [[sources/diataxis--documentation-framework#how-to]] [[sources/diataxis--documentation-framework#reference]]

### 2. Give different reading modes different promises

| Reader need | Page promise | Include | Keep elsewhere |
| --- | --- | --- | --- |
| Learn | Guided, reliable encounter with the system | Fixed path, meaningful small results, observations, bounded setup | Exhaustive alternatives and deep rationale |
| Complete a task | A way to solve a stated real problem | Preconditions, decisions, ordered actions, result, relevant branches | Introductory teaching the audience already knows |
| Look up a contract | Precise description of supported behavior | Parameters, constraints, defaults, results, errors, limitations, examples | Long persuasive or architectural essays |
| Understand | Reasons and relationships | Model, rationale, alternatives, tradeoffs and boundaries | A procedure disguised as an essay |
| Diagnose | Recognizable symptom leading to a safe next action | Exact error, plausible causes, checks, workaround/resolution | A generic “contact support” dead end |

The first four derive from Diátaxis. Troubleshooting is explicitly separated in GitLab's topic system. A page can combine a brief concept introduction and a task without becoming incoherent; separation should protect the reader's focus rather than force a page explosion. [[sources/diataxis--documentation-framework#tutorials]] [[sources/diataxis--documentation-framework#how-to]] [[sources/diataxis--documentation-framework#reference]] [[sources/diataxis--documentation-framework#explanation]] [[sources/gitlab--documentation-engineering#topic-types]] [[sources/gitlab--documentation-engineering#troubleshooting]]

Diátaxis explicitly discourages beginning with empty four-part structures or a wholesale reorganization. Improve a real page incrementally, then let navigation emerge from useful content. This matters when an existing business platform has hundreds of pages: changing labels alone does not repair missing prerequisites or inaccurate examples. [[sources/diataxis--documentation-framework#workflow]]

### 3. Make the first successful task meaningful and observable

A quickstart should demonstrate a small real capability. Diátaxis recommends visible results early and often, a narrative of expected behavior and minimal choices. Avoid beginning with every deployment option, authentication mode and architectural alternative. Select one supported route, state its assumptions and link alternatives. [[sources/diataxis--documentation-framework#tutorials]]

**Our recommended quickstart contract**, adapted from Google's runnable-sample guidance and GitLab's task format:

1. State what will exist at the end and where the exercise runs.
2. List prerequisites before the first command: account, role, environment, runtime and dependency versions, fixture data and credentials setup.
3. Provide a complete runnable example or identify the complete project containing the excerpt.
4. Show expected output and explain which fields vary.
5. Tell the reader how to verify the result in the system of record.
6. Cover the most likely failure at the step where it occurs.
7. Explain cleanup for resources the exercise created and link the next production task.

Items 5 and 7 are our additions for business systems; they prevent a successful HTTP exchange or a leftover test resource from becoming the stopping point. The product-specific verification must be supplied by the owning API contract. [[sources/google--developer-documentation#sample-code]] [[sources/gitlab--documentation-engineering#tasks]] [[concepts/business-platform-api-design]]

Do not promise “five minutes” without observing representative readers from the stated starting point. Track account provisioning and permission approval separately from command execution; excluding that waiting time can hide the real onboarding obstacle. This is a proposed measurement practice, motivated by audience fit and tutorial observation rather than a published timing standard. [[sources/google--developer-documentation#audience]] [[sources/diataxis--documentation-framework#tutorials]]

### 4. Treat examples as maintained educational programs

Google recommends sample code that builds, does its stated job, follows language conventions and remains secure. It explicitly warns that snippets are often less rigorously tested than complete programs, and that a unit test's testing goal differs from a sample's teaching goal. A green unit suite alone does not establish a usable onboarding example. [[sources/google--developer-documentation#sample-code]]

Our sample policy:

- Keep complete examples in runnable projects; extract displayed regions where the toolchain supports it.
- State runtime, SDK version, imports, installation, execution directory, configuration and expected result.
- Distinguish complete programs from fragments and pseudocode.
- Use names that carry domain meaning; add comments for non-obvious reasoning.
- Put essential copy-time qualifications inside comments that travel with the copied code.
- Keep secrets out of source; explain how the example reads them and the permission scope required.
- Document what was simplified and link a production version when the simplification affects reliability.
- Test important variants from a clean environment; prioritize languages and shells the audience actually uses.

The first and last bullets are our maintenance design; the rest apply Google's sample-code criteria. Do not require every possible variant before publishing a useful path. [[sources/google--developer-documentation#sample-code]] [[sources/google--developer-documentation#audience]]

A short example is valuable when it preserves correct behavior. Removing verification or error handling solely to shorten it can teach the wrong integration. Conversely, burying one API call in a whole application obscures the concept. Provide graduated examples: smallest working call, complete task, then production concerns. [[sources/google--developer-documentation#sample-code]]

### 4a. Write steps that remove inference

Use concrete actions, objects and conditions. Google recommends stating the location before the action, introducing a command by what it accomplishes, explaining placeholders and separating the command from its output. Put prerequisites ahead of the procedure, mark optional steps explicitly and make the sequence follow the reader's work. [[sources/google--developer-documentation#procedures]]

Practical authoring recipe, adapted from that guidance:

- **Identify the thing.** “Open the operation record returned by the request” is more precise than “check it.” Keep the same domain noun across the task, reference and UI.
- **State the relevant condition.** “If the operation failed, inspect its documented error field” gives the branch before the action. Supply real field names from the contract.
- **Use an action verb.** Replace “Authentication configuration” as a task heading with “Configure test-tenant authentication.” Keep noun phrases for conceptual sections.
- **Explain replacements.** State what each placeholder represents, where to obtain it and any required format. Preserve the command's actual shell syntax.
- **Show one meaningful action at a time.** Combine trivial adjacent UI actions when useful; split steps that require separate decisions or verification.
- **Make outputs recognizable.** Separate input from output; identify dynamic values and what confirms progress.
- **Give the important fact first.** Open a paragraph with the qualification or result the reader needs; move background after it or link an explanation.
- **Use navigable text.** Describe links and section titles by their destinations. Keep commands and error messages as text that can be copied and searched.

These are applications of the cited guides, not a universal word-count or sentence-length rule. Read the steps from a fresh reader's viewpoint: whenever they must guess a directory, resource, credential, version or success condition, supply that missing fact. [[sources/google--developer-documentation#procedures]] [[sources/google--developer-documentation#headings]] [[sources/google--developer-documentation#links]] [[sources/google--developer-documentation#documents]] [[sources/google--developer-documentation#accessibility]]

### 5. Document runtime semantics beyond request and response shapes

For business workflows, the most consequential questions often concern what the caller may conclude after a response. Pair this documentation research with the owning API-design concept; the table below is our proposed authoring coverage, not a claim every product supports every feature. [[concepts/business-platform-api-design]] [[sources/cummaudo--api-documentation-knowledge#study]]

| Capability | Questions the docs must answer |
| --- | --- |
| Retrieval | Which source is read? How fresh can it be? What do missing, redacted and unauthorized results mean? What are pagination and consistency rules? |
| Command | Which state changes? What authority is required? What validates atomically? What happens on duplicate submission or stale state? |
| Background operation | Does the response mean accepted or complete? How is the operation identified, observed, canceled or resumed? What are terminal states and partial results? |
| Webhook/event | How is authenticity checked? Can events repeat or arrive out of order? When should the handler acknowledge? How does it replay or reconcile missed events? |
| Cross-system workflow | Which system owns each outcome? What if an external effect succeeds but the response is lost? What can be safely retried or compensated? |

Stripe's published webhook documentation is a concrete example of failure semantics alongside handler implementation. GitHub's troubleshooting shows why a status code alone may not identify the cause. Study these as documentation mechanisms; they do not prove a universal retry policy for our platform. [[sources/developer-docs--product-examples#stripe-webhooks]] [[sources/developer-docs--product-examples#github-troubleshooting]]

**Illustrative wording improvement:** replace “Returns the refreshed vendors” with “Accepts a refresh request and returns an operation identifier. Wait for the operation's documented success state, then verify the snapshot is published under that API's freshness contract; follow recovery guidance for failure or cancellation.” Supply the actual states, paths, freshness rules and retry guarantees from the implemented contract. These sentences illustrate precision; they do not describe an existing Flex endpoint. [[concepts/business-platform-api-design]]

Generated OpenAPI or GraphQL reference is useful for shapes and discoverability. It does not automatically explain business intent, prerequisites, safe retries or multi-step workflows. Diátaxis explicitly cautions against treating generated reference as the entire documentation set; the academic taxonomy also includes rationale, domain concepts and support artifacts. [[sources/diataxis--documentation-framework#reference]] [[sources/cummaudo--api-documentation-knowledge#study]]

### 6. Write recovery paths that match the symptom

Use the exact error code/message as searchable text. Then explain what it means, distinguish likely causes, give ordered diagnostic checks and show a concrete resolution or temporary workaround. GitLab distinguishes a workaround from a resolution and recommends tables where multiple causes apply. [[sources/gitlab--documentation-engineering#troubleshooting]]

For each consequential error, our proposed template asks:

- What operation failed, and what might already have happened?
- What evidence separates authentication, authorization, environment, input, conflict and transient failure?
- Is retry supported, and with which identity/key/preconditions?
- Which action is safe next? What should the caller avoid repeating?
- How does the developer verify recovery?
- If escalation is required, what non-secret request/operation identifiers help support?

The unknown-outcome and retry questions come from the API research, not a universal HTTP inference. GitHub's documentation provides a concrete caution: an apparent not-found response can require authentication/permission investigation. Twilio's error pages provide a description/causes/solutions structure. [[concepts/business-platform-api-design]] [[sources/developer-docs--product-examples#github-troubleshooting]] [[sources/developer-docs--product-examples#twilio-error-21610]]

Place a short hazard notice **before** the step that can cause damage, and provide a test path or recovery requirement appropriate to the operation. GitLab explicitly requires a warning for troubleshooting console functions that change data. A separate security section is insufficient if readers arrive directly at the command. [[sources/gitlab--documentation-engineering#troubleshooting]] [[sources/nam--documentation-use#study]]

### 7. Make every entry point intelligible

Readers arrive from search, an exact error, a colleague's deep link, an SDK symbol or an agent tool. The log study finds diverse usage patterns and recommends explicit audiences and product-specific starting recommendations while preserving consistent cross-product structures. Do not assume everyone starts at the homepage or reads prerequisite chapters in order. [[sources/nam--documentation-use#study]]

Our navigation design for a large platform: a shared identity/environment/error/version layer; stable domain reference; task guides that cross domains; product-specific starting routes; exact-error troubleshooting; and migration paths. Test search with the language developers actually use, including business synonyms and error strings. These are recommendations motivated by the study and the domain-vocabulary research, not evaluated search improvements. [[sources/nam--documentation-use#study]] [[concepts/ubiquitous-language-for-agents]]

Use precise descriptive link text and link to the relevant section. Supply a few sentences of context in place when that saves a detour. Google itself allows repeated links for long pages or distinct entry points, so “never repeat anything” is an inaccurate reading of its guidance. [[sources/google--developer-documentation#links]]

Accessibility is part of usable docs: semantic heading order, keyboard-accessible tabs, descriptive links, text equivalents for diagrams, selectable code and meaningful table structure. Do not make a screenshot the only source for a command or crucial state transition. These also make content easier to extract, but improved agent task success still requires testing. [[sources/google--developer-documentation#accessibility]]

### 8. Keep one owner for facts and repeat essential context deliberately

Google recommends updating docs with code, trimming dead material and linking to authoritative shared guidance. The log study recommends exposing important information in multiple documentation types or linking prominently, because readers may consistently use only some types. The practical synthesis is **canonical ownership plus intentional reuse at decision points**. [[sources/google--developer-documentation#maintenance]] [[sources/nam--documentation-use#study]]

Example recommendation: maintain an environment's credential rules once, reuse its short applicable prerequisite in task pages and link the full policy. Reuse a versioned warning component next to a risky operation instead of maintaining three separately edited paragraphs. A self-contained task need not duplicate the whole authentication guide. Component reuse is our implementation suggestion; the cited documents do not mandate a particular renderer. [[sources/google--developer-documentation#links]] [[sources/google--developer-documentation#maintenance]] [[patterns/composition/single-source-multi-surface-distribution]]

Keep decision history distinct from the current contract. Google explicitly describes implemented design docs as archives of decisions rather than half-correct operating guidance. Link an ADR when its rationale is useful; maintain current behavior in the reference and task pages. [[sources/google--developer-documentation#maintenance]]

### 9. Make documentation part of the release process

GitLab publishes ownership, developer technical review, technical-writer review, documentation requirements and code/docs synchronization practices. Its general same-MR recommendation is not universally mandatory, and it documents merge exceptions and follow-up processes. Adopt deliberate rules suited to your release workflow rather than misrepresenting another company's policy. [[sources/gitlab--documentation-engineering#workflow]]

Our proposed platform workflow:

1. Identify affected user tasks and documentation alongside the feature's acceptance criteria.
2. Name the technical owner; ask a reader unfamiliar with the implementation to review the path.
3. Prepare docs while implementing, including error cases and runnable examples.
4. Run mechanical checks and a fresh-environment task walkthrough.
5. Coordinate documentation visibility with the released API/SDK/environment version.
6. After release, inspect failures, search gaps and support cases; repair the authoritative page and reuse the correction.

This combines Google's update-with-code guidance, GitLab's workflow, tutorial observation and the log study's use of telemetry. It is our operating model rather than a copied GitLab mandate. [[sources/google--developer-documentation#maintenance]] [[sources/gitlab--documentation-engineering#workflow]] [[sources/diataxis--documentation-framework#tutorials]] [[sources/nam--documentation-use#study]]

**Version dimensions should be explicit:** documentation edition, API contract version, SDK version, product/environment availability and example's tested version. A publication date alone does not establish which service behavior is documented. This recommendation applies [[patterns/quality-bar/revision-bound-review]] to the version behavior already studied in [[artifacts/projects/shopify-api]] and the newly captured account/API/SDK/webhook distinctions in Stripe. [[sources/developer-docs--product-examples#stripe-versioning]]

For migrations, specify who is affected, old/new behavior, before/after examples, ordering/dependencies, how to verify success, reversal limits and retirement timing. This is a proposed checklist derived from contract precision and coordinated release requirements, not an observed universal template. [[concepts/business-platform-api-design]] [[sources/gitlab--documentation-engineering#workflow]]

### 10. Automate what is mechanical and review what is semantic

GitLab's documented pipeline checks Markdown, relative links/anchors, Mermaid, redirects, builds, ownership metadata and certain generated-page update processes. Its described link jobs skip links requiring network access. A passing link checker therefore cannot be reported as verification that every external link works. [[sources/gitlab--documentation-engineering#testing]]

| Check | Can establish | Cannot establish alone |
| --- | --- | --- |
| Build, links, redirects, anchors | Pages render and checked targets resolve | Explanation is correct or useful |
| Schema/reference parity | Generated contract matches chosen source | Business effects or authorization model is complete |
| Compile/lint samples | Syntax/import/type correctness in tested versions | Actual provider behavior or successful business outcome |
| Sandbox task execution | Example works in that environment and fixture | All tenants, roles, races or production conditions |
| Reader walkthrough | Observed reader can follow the tested path | Every audience understands all alternatives |
| Agent task evaluation | Selected model/tool/version succeeds on bounded tasks | Future models or arbitrary workflows are safe |

This table is our verification model, grounded in GitLab's mechanical checks, Google's sample expectations and observational-study limits. Prioritize checks by failure impact; don't block every typo fix on a full live integration suite. [[sources/gitlab--documentation-engineering#testing]] [[sources/google--developer-documentation#sample-code]] [[sources/nam--documentation-use#study]]

### 11. Support agents with current, scoped documentation

Cloudflare documents per-page Markdown, content negotiation, per-product indexes/full exports, OpenAPI, skills and MCP access. The llms.txt author describes a scoped index and linked Markdown as an informal proposal, now v2. These are actual documented surfaces and a proposal; neither proves every coding agent automatically discovers them. [[sources/cloudflare--docs-for-agents#agent-access]] [[sources/answerai--llms-txt#proposal]]

Our agent documentation contract:

- Generate human pages, Markdown and API/schema surfaces from maintained sources where practical.
- Give each independently retrieved page enough identity: product, capability, applicability/version and prerequisites.
- Expose a small scoped discovery index, descriptive links and stable section boundaries.
- Retain semantic qualifiers, examples, constraints and provenance in exports.
- Let clients fetch a relevant page or domain collection instead of forcing a whole-platform dump.
- Separate documentation search/read capabilities from authenticated mutation tools.
- Evaluate retrieval and correctness separately: finding the right page is a different outcome from choosing the right operation or recovering safely.

The first five apply the documented formats and existing single-source pattern. The last two apply the wiki's authority and API learning research. Readable documentation does not grant permission to execute its instructions. [[sources/cloudflare--docs-for-agents#agent-access]] [[sources/answerai--llms-txt#proposal]] [[patterns/composition/single-source-multi-surface-distribution]] [[patterns/behavioral/context-is-not-authority]] [[concepts/agent-api-learning-and-evolution]]

Don't interpret llms.txt as robots policy, a training-data inclusion guarantee, an authorization mechanism or an established agent-performance improvement. Test the actual discovery path in the intended harness and keep evidence dates/versions visible. [[sources/answerai--llms-txt#proposal]] [[patterns/behavioral/context-is-not-authority]]

### 12. Evaluate the documentation by tasks, not volume

The mapping study's 71% snippet figure means 15 of 21 included studies recommended snippets, not that snippets improve developer productivity by 71%. The log study reports associations with later API use, not causal uplift. Avoid turning literature counts, engagement or vendor assertions into effectiveness claims. [[sources/cummaudo--api-documentation-knowledge#study]] [[sources/nam--documentation-use#study]]

Our proposed task evaluation:

| Dimension | Observe | Interpret carefully |
| --- | --- | --- |
| Discovery | Time to relevant page, wrong-page starts, failed searches | Search traffic can mean demand or confusion |
| Onboarding | Verified first task, setup failures, assisted versus independent completion | Start conditions and provisioning delays change timing |
| Correctness | Right operation/environment, valid result, supported version | A successful request may not complete the business task |
| Recovery | Diagnose injected failure, avoid duplicate effects, verify repair | Familiarity with a scripted failure may inflate results |
| Maintenance | Critical broken examples, release/docs lag, owner response | Page age alone is not evidence of incorrectness |
| Agents | Right evidence, right tool, constraints honored, recoveries | Pin model, harness, tool inventory and source version |

Choose representative novices and experienced integrators, several business tasks and deliberate failure scenarios. Observe where readers hesitate; repair the page and repeat the same bounded task with another reader. For agents, use the same task corpus to compare retrieval paths and record unsupported assumptions. This experiment is proposed, not performed here. [[sources/diataxis--documentation-framework#tutorials]] [[sources/nam--documentation-use#study]] [[concepts/agent-api-learning-and-evolution]]

## Patterns demonstrated

- [[patterns/composition/single-source-multi-surface-distribution]] — apply the existing pattern to canonical facts, reusable examples and human/agent exports; no new inspected-artifact example count claimed. [[sources/google--developer-documentation#maintenance]] [[sources/cloudflare--docs-for-agents#agent-access]]
- [[patterns/quality-bar/revision-bound-review]] — distinguish contract/API/SDK/docs revisions and review the version actually consumed. Application to documentation, not a new implementation validation. [[sources/gitlab--documentation-engineering#workflow]]
- [[patterns/quality-bar/defect-derived-validation]] — proposed application: turn recurring broken-example or drift defects into checks. Existing GitLab checks show mechanical enforcement, but this pass does not prove they were mined from repeated defects. [[sources/gitlab--documentation-engineering#testing]]
- [[patterns/behavioral/context-is-not-authority]] — searchable instructions and executable service access need different authority boundaries. [[sources/cloudflare--docs-for-agents#agent-access]]

## Tensions & counter-arguments

- **Separate needs versus fragmenting pages.** Diátaxis separates purposes; GitLab permits mixed topic types. Preserve a dominant purpose and enough local context; don't force one tiny page per heading. [[sources/diataxis--documentation-framework#overview]] [[sources/gitlab--documentation-engineering#topic-types]]
- **DRY versus discovery.** Central ownership prevents drift; local context protects readers entering mid-flow. Reuse centrally maintained content where decisions occur and link details. [[sources/google--developer-documentation#maintenance]] [[sources/google--developer-documentation#links]] [[sources/nam--documentation-use#study]]
- **Short versus correct.** Google prioritizes correctness over brevity. Keep essential setup and operational qualifications; move optional explanation out of the critical path. [[sources/google--developer-documentation#sample-code]] [[sources/diataxis--documentation-framework#tutorials]]
- **Automated versus understandable.** A generated reference and valid links can coexist with missing rationale or unusable onboarding. Keep semantic and reader review distinct. [[sources/diataxis--documentation-framework#reference]] [[sources/cummaudo--api-documentation-knowledge#study]]
- **Consistent platform navigation versus domain-specific needs.** The log study recommends tailored starting recommendations without inconsistent site organization. [[sources/nam--documentation-use#study]]
- **Comprehensiveness versus maintenance.** Small accurate docs can outperform large stale collections as an engineering judgment; this pass does not quantify the effect. Scope to supported tasks and keep a visible backlog. [[sources/google--developer-documentation#maintenance]] [[sources/diataxis--documentation-framework#workflow]]
- **AI assistance versus technical accountability.** GitLab says authors remain responsible for technical accuracy and requires technical-writer review for its AI-generated documentation. The transferable principle is accountable review; that staffing requirement is GitLab's own policy. [[sources/gitlab--documentation-engineering#workflow]]

## Timeline (append-only)

- 2026-11-05 — Initial deep documentation research: primary frameworks, style/maintenance guides, live product examples, two studies and current agent-access formats. Documentation behavior inspected; no live examples or audience experiment executed. [[sources/google--developer-documentation#root]] [[sources/developer-docs--product-examples#root]]

## Related

- [[projects/writing-amazing-developer-docs/README]] — collection navigation and next investigations.
- [[concepts/business-platform-api-design]] — domain contracts the docs must explain.
- [[projects/designing-apis-for-agents/README]] — business-platform API research.
- [[concepts/agent-api-learning-and-evolution]] — runtime evidence versus model priors.
- [[concepts/ubiquitous-language-for-agents]] — shared business vocabulary.
- [[artifacts/projects/shopify-api]] — existing version/lifecycle reference.
- [[artifacts/projects/eve]] — existing source-inspected documentation distribution example; its prior evidence is not a newly executed check here.

## What we'd steal

★ marks priority; details and qualifications live in the evidence sections above.

- ★ An explicit task, audience and starting-state brief before writing.
- ★ Early visible results and expected-output checkpoints.
- ★ One supported default route, with alternatives linked at relevant decisions.
- ★ Complete maintained sample projects behind short displayed excerpts.
- ★ Copy-time comments for consequential simplifications and constraints.
- ★ Lifecycle, permission, retry and unknown-outcome semantics next to the affected operation.
- ★ Troubleshooting indexed by actual symptoms and exact errors.
- ★ Separate technical, editorial, mechanical and reader checks.
- ★ Documentation change requirements alongside product acceptance criteria.
- ★ A task-based human/agent evaluation corpus.
- Distinct learning, task, reference, explanation and diagnosis purposes.
- Topic composition where it reduces reader detours.
- Verb-led task titles and precise concept titles.
- Knowledge prerequisites that distinguish domain expertise from programming experience.
- Setup versions, shell assumptions, execution directory and dependency installation.
- Output annotations identifying dynamic values.
- System-of-record verification beyond transport success.
- Cleanup and production-readiness handoffs.
- Graduated examples rather than either a tiny fragment or a giant demo alone.
- Primary-method ordering when several implementations exist.
- Explicit workaround versus permanent resolution.
- Hazard notices before consequential commands.
- Useful non-secret correlation identifiers for support.
- Shared platform conventions with domain-specific starting recommendations.
- Business synonyms and exact errors in search evaluation.
- Descriptive deep links and short context in place.
- Keyboard navigation, semantic headings, text diagram equivalents and selectable code.
- Canonical ownership with reusable contextual excerpts.
- Decision archives separated from current operational instructions.
- API/SDK/documentation/availability version labels.
- Migration examples, verification and reversal limits.
- Checks for redirects, ownership and generated-reference drift in addition to links.
- Explicit limits for what each check proves.
- Small scoped indexes, Markdown exports and machine-readable schemas.
- Source/version preservation in retrieved agent context.
- Separation of docs retrieval from authenticated actions.
- Metrics segmented by audience, task and starting condition.
- Logs used to discover questions, with task observation to interpret them.
- Incremental improvements to actual pages instead of an empty taxonomy rollout.

## Open questions

- Which three real Flex integration tasks should supply the first baseline usability study?
- What share of onboarding failures comes from docs, access provisioning or product behavior?
- Which repeated facts warrant reusable components rather than a short contextual link?
- Which API/SDK/docs release dimensions can the current toolchain check automatically?
- Do scoped Markdown indexes or documentation search tools improve correctness for our actual agents, compared with ordinary page retrieval?
- Which supported languages and shells have enough readers to justify maintained executable examples?
- Can agent-assisted drafts reduce authoring time without increasing technical-review burden? No result is claimed here.
