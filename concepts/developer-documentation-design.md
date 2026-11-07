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

This page is the owning synthesis and recommendation ledger. [[projects/writing-amazing-developer-docs/README]] is its research navigation hub. Recommendations below are our interpretation of the named evidence, not measured universal rules. No vendor product examples were executed, no docs site was visually usability-tested, and no ranking of vendors is claimed. A separate local synthetic doctest probe was executed; its narrow scope is recorded below.

## Where it came from

The evidence combines Daniele Procida's Diátaxis framework, Google's technical-writing courses and style guidance, Write the Docs' community practice, GitLab's published documentation workflow, concrete product documentation, and an expanding empirical literature. The initial two-study pass is extended below with five additional papers, including two 2026 preprints. The 2019 mapping study covers 21 selected studies; the 2024 CHI paper analyzes documentation-use logs for four Google cloud services. Neither establishes that following this checklist causes a particular productivity gain. [[sources/diataxis--documentation-framework#root]] [[sources/google--developer-documentation#root]] [[sources/writethedocs--documentation-practice#root]] [[sources/gitlab--documentation-engineering#root]] [[sources/cummaudo--api-documentation-knowledge#study]] [[sources/nam--documentation-use#study]]

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

### 13. Separate current architecture, decisions and proposed changes

An architecture account should let a reader distinguish **what exists**, **why a choice was made**, **what is proposed**, and **what was actually implemented or deployed**. GDS treats acceptance and implementation separately and says an ADR does not replace the architecture description. Nygard's original purpose is preserving the context and consequences behind a significant choice for future maintainers. A merged decision record is evidence of agreement in a particular process, not evidence the running system conforms. [[sources/docs-research--architecture-20261105#gds-adr]] [[sources/docs-research--architecture-20261105#nygard-adr]]

Do not prescribe universal ADR immutability. AWS makes accepted/rejected records immutable and uses supersession. GDS allows clarifications and discovered consequences, permits changing an unimplemented decision with agreement, and asks for a new ADR when changing a decision that has already been implemented. Choose and document a local amendment policy; preserve the previous rationale and replacement links. GDS's page has an overdue review date, so these are the captured published rules, not a claim of freshly audited GDS practice. [[sources/docs-research--architecture-20261105#aws-adr]] [[sources/docs-research--architecture-20261105#gds-adr]]

Our minimum internal bundle is a service entry point, a current architecture brief, selected runtime scenarios, a decision log and operational links. Scale it to the system's complexity. A small utility need not carry every arc42 section; the template is a coverage aid for constraints, quality goals, risks, boundaries and terminology. Keep one owner for each current fact and link historical rationale where needed. [[sources/docs-research--architecture-20261105#arc42-overview]] [[sources/docs-research--architecture-20261105#backstage-publishing]]

### 14. Make each diagram answer a question

C4 distinguishes context, containers, components, code, dynamic behavior and deployment. Its author recommends that many teams can stop at context and container views; this is guidance, not a measured proportion of teams. C4's container means an application/data store, not specifically Docker. Do not mistake a logical container view for environment-specific deployment topology; C4 places clustering, replication and failover in deployment views. [[sources/docs-research--architecture-20261105#c4-diagrams]] [[sources/docs-research--architecture-20261105#c4-context]] [[sources/docs-research--architecture-20261105#c4-container]]

Use a small number of representative business events to connect components through time. C4 recommends dynamic views sparingly; arc42 includes critical interfaces, startup/shutdown and exception scenarios. For a background workflow, a scenario such as external timeout or worker recovery can reveal a boundary a static “worker” box cannot explain. That scenario selection is our application of the frameworks, not verification of a specific runtime. [[sources/docs-research--architecture-20261105#c4-dynamic]] [[sources/docs-research--architecture-20261105#arc42-runtime]]

Give each view a title, scope, level, defined visual vocabulary and labeled directed relationships. Map business partners and meaningful inputs/outputs to technical interfaces. A context table may communicate this better than an image. C4 supplies legibility checks; arc42 explicitly separates business meaning from transport. [[sources/docs-research--architecture-20261105#c4-checklist]] [[sources/docs-research--architecture-20261105#arc42-context]]

Accessibility requires more than labeling an image “architecture diagram.” W3C's complex-image guidance provides a short identifying alternative plus a detailed textual account of essential relationships where needed. Its `aria-describedby` example warns that complex structure may be flattened to a single paragraph. Tables also need real header/data associations, which can be lost in conversion. Review the rendered and exported representations for preserved meaning; no visual or assistive-technology audit was executed in this pass. [[sources/docs-research--discovery-governance-20261105#accessible-diagrams]] [[sources/docs-research--discovery-governance-20261105#accessible-tables]]

### 15. Operational documentation coordinates people, evidence and authority

Our operational separation is **runbook / current incident record / retrospective**. Google's incident-management chapter uses a live document and explicit roles; its postmortem guidance provides the later reviewed learning record. PagerDuty distinguishes responsibilities during response. Reusable procedure, current observation, hypothesis and retrospective explanation should remain recognizable as different kinds of information. This separation is our synthesis, not an independently tested optimal document architecture. [[sources/docs-research--operations-20261105#google-managing-incidents]] [[sources/docs-research--operations-20261105#google-postmortem]] [[sources/docs-research--operations-20261105#pagerduty-during-incident]]

A runbook should identify the trigger, applicable environment, authorized role, preconditions, expected evidence, consequential actions, stop/escalation conditions and supported recovery. During an incident, record who is coordinating, what is known, which tests/changes were made and their results. Google emphasizes acknowledged handoff; a reader of the procedure does not acquire incident authority merely by possessing the text. These fields are our authoring contract grounded in the cited processes. [[sources/docs-research--operations-20261105#google-managing-incidents]] [[sources/docs-research--operations-20261105#pagerduty-during-incident]] [[patterns/behavioral/context-is-not-authority]]

Keep instructions and contact paths available during an outage of the service being repaired. Mitigation can precede complete diagnosis, and restored service does not establish the underlying cause is corrected. [[sources/docs-research--operations-20261105#google-managing-incidents]] [[sources/docs-research--operations-20261105#google-troubleshooting]]

A checklist can precompute familiar coordination, but diagnosis still needs a system model and discriminating tests. Google frames troubleshooting as iterative hypotheses, inspection and treatment, with attention to side effects and uncertainty. A diagnostic step should state what evidence it obtains and what that result cannot conclude. If the system lacks relevant observability, improving the documentation may require product work rather than more prose. [[sources/docs-research--operations-20261105#google-troubleshooting]]

Practice matters. Google's workbook recommends preparedness and exercises; PagerDuty reports that silently changing policy docs and assuming responders read them did not work for its team. Consequently, our release process for consequential operating instructions includes dissemination and rehearsal, not just publication. Neither source establishes a universal incident-time reduction or staffing model. [[sources/docs-research--operations-20261105#google-incident-response]] [[sources/docs-research--operations-20261105#pagerduty-antipatterns]]

### 16. Migration guides describe the intermediate system

A migration guide should explain the starting state, target, affected dependencies, changed semantics, intermediate states, checks to advance, supported reversal and retirement conditions. This is our authoring model grounded in Kubernetes, Django and Stripe; it is not a claim that every migration is reversible. [[sources/docs-research--operations-20261105#kubernetes-migration]] [[sources/docs-research--operations-20261105#django-upgrade]] [[sources/docs-research--operations-20261105#stripe-upgrade]]

Kubernetes illustrates why a renamed API is insufficient: replacements may change defaults, required fields and validation. Its deprecation policy distinguishes serving an endpoint from decoding stored representations, and supplies warnings/usage signals. Do not project its timelines onto other systems. A converter or updated manifest is evidence of transformation, not equivalent application behavior. [[sources/docs-research--operations-20261105#kubernetes-deprecation-policy]] [[sources/docs-research--operations-20261105#kubernetes-migration]]

Django's version-specific guide makes dependencies, intervening release notes, warning visibility, tests and post-deployment runtime state part of upgrading. Stripe's guide stages old/new webhook handling, controls which route processes effects, monitors before retirement and describes provider-specific retry/reversal behavior. Write down the intermediate states and duplicated-work constraints, rather than presenting only the desired final configuration. Neither guide was executed here. [[sources/docs-research--operations-20261105#django-upgrade]] [[sources/docs-research--operations-20261105#stripe-upgrade]]

### 17. Expand SDK reference beyond signatures

Rust's API guidelines add error, panic and safety considerations; unsafe-call documentation identifies invariants the caller must uphold. They also explain that an example may need to demonstrate why to use an item, rather than merely syntax, and allow linking an applicable example instead of mechanically duplicating one on every symbol. These are Rust guidelines, not universal mandates for every language. [[sources/docs-research--executable-reference-20261105#reference-semantics]]

Our transferable reference questions are: what does the operation mean; what can fail; what state can change before failure; what must the caller guarantee; and which supported usage demonstrates its purpose? Hide irrelevant implementation details while preserving constraints that affect correct use. Document release changes where the consumer will look. This extends the earlier HTTP-focused contract model to libraries without pretending HTTP errors, exceptions and Rust panics are interchangeable. [[sources/docs-research--executable-reference-20261105#reference-semantics]] [[concepts/business-platform-api-design]]

### 18. Audit what documentation tests actually exercise

The statement “all examples pass” needs a denominator and a test mode. Rustdoc distinguishes normal execution, compilation-only `no_run`, skipped `ignore`, expected panic and expected compile failure. It preprocesses examples and can hide setup lines in rendered documentation. An example compiling, being executed and asserting its promised result are different claims. [[sources/docs-research--executable-reference-20261105#rust-tests]]

Python doctest may run with module globals or injected context. Sphinx supports hidden setup/cleanup, groups and conditional skips; presentation can omit test flags. These are useful mechanisms, not defects by themselves. Review whether the reader can obtain the required context and whether skipping an unavailable dependency leaves an important path untested. Python's output flags also alter what a match proves: broad ellipses can match too much, while unstable ordering/addresses make exact text brittle. [[sources/docs-research--executable-reference-20261105#python-context]] [[sources/docs-research--executable-reference-20261105#python-flags]] [[sources/docs-research--executable-reference-20261105#sphinx-fixtures]]

We executed a bounded **synthetic local probe**, not a vendor audit. An injected-context fragment passed; the same fragment without that context failed; the complete context-bearing example passed. Separately, an output check using a broad ellipsis accepted an intentionally failed-job string, while an exact expected-success output check rejected it. This demonstrates the mechanics in Python 3.12.4; it does not measure how often real docs suffer these problems or the impact on developers/agents. Reproduction, script hash and results: [[projects/writing-amazing-developer-docs/experiments/README]]. The documented tool mechanisms above supply context; the probe result is our own measured artifact.

Our recommended report separates total runnable examples, selected examples, compiled examples, executed examples, skipped examples and explicit outcome assertions. For external integrations, record fixture/mocked/live scope separately. Test a copied fragment with its promised setup, not solely the expanded program used internally. This coverage policy is proposed; we did not audit an actual documentation site's coverage. [[sources/docs-research--executable-reference-20261105#rust-tests]] [[sources/docs-research--executable-reference-20261105#sphinx-fixtures]]

### 19. Treat discovery as a delivery pipeline

Backstage demonstrates code-local authorship with shared catalog discovery and a build/publish/serve pipeline. A source merge can succeed before a particular revision is built, published or served. TechDocs supports separate cross-cutting documentation entities as well as service-linked docs; central discovery does not require a single central authoring repository. This is a documented architecture, not a Backstage deployment tested here. [[sources/docs-research--architecture-20261105#backstage-publishing]] [[sources/docs-research--architecture-20261105#backstage-architecture]]

Search adds another stage. Algolia's documentation separates URL selection, content-hierarchy extraction, record inspection, recurring crawls and the frontend. Docusaurus filters results by version/language; missing or inconsistent indexed facets can produce no results even when pages exist. A content problem and an indexing/filter problem need different fixes. Its captured configuration is version-specific; no search engine was installed or benchmarked. [[sources/docs-research--discovery-governance-20261105#search-index]] [[sources/docs-research--discovery-governance-20261105#search-filters]]

Read the Docs distinguishes `latest` development docs from `stable`, and offers notifications about applicability. Hidden versions remain accessible by URL; privacy is separate. Changing an active version's slug can remove old artifacts and require a rebuild/redirect. Thus a documentation lifecycle includes access policy, version routing and compatibility of old links, not just a visible version selector. These are Read the Docs' published behaviors, not assertions about all hosting systems. [[sources/docs-research--discovery-governance-20261105#rtd-lifecycle]]

Our platform verification chain is source revision → built artifact → published version → served page → indexed record → query context → retrieved passage → task outcome. Record the boundary actually checked. Documentation search permissions must be enforced by the chosen system; hiding navigation or adding ownership metadata is insufficient. Backstage explicitly separates owner metadata from runtime authorization. [[sources/docs-research--architecture-20261105#backstage-catalog]] [[sources/docs-research--discovery-governance-20261105#rtd-lifecycle]] [[patterns/behavioral/context-is-not-authority]]

### 20. Reuse includes applicability and localization

GitHub's documentation describes long Markdown reusables, short variables, task-oriented grouping and version-dependent rendering. Its reason for Markdown includes localization segmentation and reduced translation churn. This gives a concrete implementation behind the earlier “canonical fact plus local context” recommendation; it does not establish that every team needs GitHub's Liquid/YAML setup. [[sources/docs-research--discovery-governance-20261105#reuse]]

A reused instruction should carry the right version, role, environment and consequence when rendered into a task. A correct source fragment can still be assembled into an inapplicable page. Preview and review the rendered combinations that matter, including exported Markdown and translated variants, rather than approving only the fragment in isolation. This is our proposed assembly check, grounded in conditional reuse and the observed semantic risks of conversion. [[sources/docs-research--discovery-governance-20261105#reuse]] [[sources/docs-research--discovery-governance-20261105#accessible-tables]]

GitHub's writing guidance also makes progressive disclosure concrete: start with initial context and conclusions, prioritize the core task, use meaningful subheadings and keep optional depth later. Avoid interpreting a publisher's numeric style limits as measured universal optima. The goal is preserving what the reader needs to act while reducing irrelevant decisions. [[sources/docs-research--discovery-governance-20261105#content-design]]

### 21. Reconnect concepts and examples to the task

Robillard's 2009 article reports 80 analyzed survey responses and 12 exploratory interviews at Microsoft, with a low survey response rate and retrospective accounts. Its examples include composition/resource-lifecycle gaps: a small working call did not tell a developer how to continue a multi-call task. This motivates separate criteria for an example being runnable, current, recommended and sufficient for the intended task. It does not establish population prevalence or that an architecture-first reading order works best. [[sources/docs-research--empirical-20261105#robillard-learning]]

Meng and colleagues observed 11 developers working on shipping-API tasks. Readers struggled to predict where concepts, samples, recipes and references held the needed information; samples that omitted shared code to avoid redundancy could impede copy/adapt use. That is distinct from a clearly explained credential placeholder. The study is small, single-API and qualitative, with language and observation limitations, so it does not validate a universal navigation taxonomy or fixed developer learning styles. [[sources/docs-research--empirical-20261105#meng-information-seeking]]

This qualifies the first pass: separate deep explanation from procedure **while reconnecting necessary concepts where the reader needs them**. Provide task-language entry points, map domain terms to actual symbols, and offer complete examples assembled from maintained code. Include a return task in usability tests: can a developer find a fact again after leaving the page? These are proposed applications of the observed breakdowns, not experimentally established fixes in this research. [[sources/docs-research--empirical-20261105#meng-information-seeking]] [[sources/docs-research--empirical-20261105#robillard-learning]]

A later 2020 study by Meng and colleagues randomly assigned22participants to a bundled documentation redesign or control for five shipping-API tasks. The authors found better task accuracy under their18-subtask measure, but no statistically significant overall task-time difference; perceived documentation quality also did not differ significantly. A secondary outside-document viewing-time measure improved, but it is a rough planning/action proxy rather than end-to-end speed. Authentication was preconfigured; the small sample, one API, basic tasks and jointly changed structure/concepts/examples/search limit generalization and prevent attributing the effect to one technique. [[sources/docs-research--empirical-20261105#meng-intervention]]

This adds intervention evidence while qualifying the goal: fewer errors, faster completion, less reading and higher satisfaction are different outcomes. Define correctness at the business-task level, separate assisted from independent completion, record setup excluded from the test and retain failed/partial attempts. Do not optimize page dwell or user ratings as substitutes for accurate work. These are our proposed evaluation practices informed by the study, not a promised effect size. [[sources/docs-research--empirical-20261105#meng-intervention]]

### 22. Evaluate documentation changes, abstention and actual evidence use

DoGBench's version-pinned 2026 preprint studies repository-triggered documentation updates and abstention cases using task-specific criteria rather than textual similarity alone. Its failure analysis includes missing prerequisites, incorrect defaults/scope/lifecycle and stopping after an initially plausible surface. A real symbol or an accurate sentence can still produce an inadequate task guide. The portable question is “what changed for the reader, and which surfaces now owe an update?” rather than “how much documentation did the agent write?” [[sources/docs-research--empirical-20261105#dogbench]]

Keep its limits explicit: model-generated criteria/scoring have human validation on subsets; one-run performance, abstention labels, critical-defect caps and maintainer judgments are study-design choices. The paper, author HTML and landing-page leaderboard differ in evaluated scope and denominators. This wiki does not combine them into a single success percentage or claim an independent benchmark replication. A correct no-op can be valuable; absence of prior documentation does not prove a change should remain undocumented. [[sources/docs-research--empirical-20261105#dogbench]] [[sources/docs-research--empirical-20261105#restoration]]

Gao and Chen's separate 2026 preprint examines recorded local coding-agent documentation interactions and repository changes. It distinguishes observation populations and explicitly limits visibility into browser docs, docstrings, preloaded context and model knowledge. Its LLM-disambiguated category labels lack human validation. A small observed API-reference share cannot establish agents ignore API docs, and file reads cannot establish comprehension or successful use. It does not experimentally compare HTML, Markdown, llms.txt or executable examples. [[sources/docs-research--empirical-20261105#agent-traces]]

Our proposed agent evaluation records exposure, retrieved version, selected evidence, constraints applied, action, validation and outcome separately, with task-specific critical requirements and correct abstention. A human review should distinguish technical correctness, missing task coverage and editorial preferences. Run the same bounded task from the same starting state when comparing documentation variants; do not count a page visit, a plausible answer or a green build as the final result. [[sources/docs-research--empirical-20261105#dogbench]] [[sources/docs-research--empirical-20261105#agent-traces]] [[concepts/agent-api-learning-and-evolution]]


### 23. Mintlify supplies a concrete agent-documentation case study

[[artifacts/projects/mintlify]] owns the detailed case study: discovery indexes and headers, representation-aware Markdown, capability skills, search/section retrieval, an assistant, authoring agents and feedback. The transferable design is a connected content lifecycle with explicit consumer, applicability and authority boundaries—not merely another text export. [[sources/mintlify--agent-documentation-docs#overview]] [[sources/mintlify--agent-documentation-docs#markdown]]

Its large-index work makes discovery coverage concrete: semantically split child indexes replace a cutoff that omitted pages. Its URL benchmark principally measures source-location efficiency; high URL accuracy is not evidence of correct integration. The pinned public data permit aggregate inspection, while missing claimed proxy logs limit cause-decomposition reproduction. Detailed methods and limitations stay on the case study rather than creating a parallel vendor-results catalog here. [[sources/mintlify--agent-docs-research#scaling-index]] [[sources/mintlify--docs-url-discovery-bench#grading]] [[sources/mintlify--docs-url-discovery-bench#reproducibility-gap]]

The case also sharpens authority: a docs search server can contain a feedback-writing tool; inline visibility is different from restricted page access; privileged REST keys and user-authenticated retrieval do not have interchangeable filtering guarantees. Generated capability summaries add synthesis latency, and different authoring/assistant/editor instruction surfaces require different configuration. These are documented contracts, not runtime tests. [[sources/mintlify--agent-documentation-docs#search-mcp]] [[sources/mintlify--agent-documentation-docs#visibility]] [[sources/mintlify--agent-documentation-docs#api-search]] [[sources/mintlify--agent-documentation-docs#skill]] [[sources/mintlify--agent-documentation-docs#agent-customize]]

Traffic, technical readiness, suggested-change acceptance and heuristic savings are separate proxies. Mintlify's quality guidance itself recommends interpreting metrics alongside feedback and observed task walkthroughs. Use these mechanisms to form testable hypotheses for the platform, keeping actual task success as a separate outcome. [[sources/mintlify--agent-docs-research#midyear-traffic]] [[sources/mintlify--agent-documentation-docs#quality-guide]] [[sources/mintlify--agent-documentation-docs#savings]]

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

- 2026-11-05 — Second pass broadened to internal architecture/ADRs, operational documentation, migration, SDK reference/testing, search/versioning/reuse/accessibility and five additional empirical papers; local synthetic probe executed. No vendor runtime or human/agent task experiment performed. [[sources/docs-research--empirical-20261105#root]]

## Related

- [[artifacts/projects/mintlify]] — concrete agent-documentation platform, vendor research and selected benchmark source/data.

- [[projects/writing-amazing-developer-docs/platform-documentation-system]] — proposed ownership, delivery and evaluation model for a large platform.
- [[projects/writing-amazing-developer-docs/experiments/README]] — executed synthetic probe with exact runtime and result.

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

## Second-pass portable additions

The sections above own the evidence and qualifications for this additional steal ledger.

- ★ Current architecture, proposal, accepted decision and deployed result as distinct states.
- ★ Explicit local ADR amendment/supersession policy; accepted does not imply implemented.
- ★ Scoped diagrams with a question, level, vocabulary and labeled relationships.
- ★ Representative failure/operations scenarios alongside static structure.
- ★ Runbooks, live incident records and retrospectives with separate jobs/owners.
- ★ Diagnostic steps that state their evidence, uncertainty and stop/escalation branch.
- ★ Role-specific authority and acknowledged handoff.
- ★ Migration intermediate states, mixed-version behavior and retirement gates.
- ★ Compiled/executed/skipped/asserted example counts reported separately.
- ★ Test context versus reader-promised setup audited explicitly.
- ★ Source/build/publish/serve/index/retrieve/use checked as distinct boundaries.
- ★ Correct documentation no-op decisions and cross-surface obligation checks.
- One significant decision per ADR, with tradeoffs and replacement links.
- Architecture constraints, risks, debt and quality goals alongside components.
- Business input/output meaning mapped to transport/API realization.
- Logical component views separated from environment topology.
- Accessible detailed diagram descriptions and semantic table headers.
- Preservation of meaning across rendered, translated and agent-readable surfaces.
- A service scaffold that includes its documentation/catalog entry.
- Code-local owners with central discovery and cross-cutting guides.
- Ownership metadata separated from runtime authorization.
- Prepared incident channels and a record of actions, tests and results.
- Rehearsal and dissemination after consequential policy changes.
- Mitigation distinguished from diagnosis and permanent correction.
- Retrospective follow-ups assigned and distributed, not merely written.
- Changed defaults/validation/required fields in migrations, not only renamed endpoints.
- Warning visibility, dependency compatibility and retained runtime state checked during upgrades.
- Provider-specific rollback/replay rules kept attached to their contract.
- SDK errors/panics/caller invariants treated as first-class reference semantics.
- Examples explaining purpose and composition, not only syntax.
- Explicit hidden fixtures, conditional skips and weak matcher limits.
- Stable semantic assertions instead of brittle incidental output where appropriate.
- Language/version-aware search facets and inspected extracted records.
- Hidden versus private content treated as different controls.
- Version-slug/redirect/artifact lifecycle included in documentation release planning.
- Reusables carry version/context and are reviewed after assembly.
- Task-language routes reconnect concepts to relevant symbols and decisions.
- Find-it-again tasks supplement first-discovery tests.
- Runnable/current/recommended/task-suitable properties tracked separately.
- Critical omissions distinguished from editorial preferences in reviews.
- Agent exposure, reading, action and verified result counted separately.
- Version-specific benchmark denominators and unvalidated classification limits preserved.

## Mintlify portable additions

The exhaustive vendor-specific ledger lives on [[artifacts/projects/mintlify]], keeping one owner for its details. Highest-priority applications here are semantic discovery coverage, content-representation verification, narrow retrieval/feedback/authoring authority, explicit summary freshness, and task-based evidence beyond traffic/readiness/acceptance proxies. [[sources/mintlify--agent-documentation-docs#llms]] [[sources/mintlify--agent-documentation-docs#visibility]] [[sources/mintlify--agent-documentation-docs#skill]] [[sources/mintlify--agent-documentation-docs#quality-guide]]

## Open questions

- Which three real Flex integration tasks should supply the first baseline usability study?
- What share of onboarding failures comes from docs, access provisioning or product behavior?
- Which repeated facts warrant reusable components rather than a short contextual link?
- Which API/SDK/docs release dimensions can the current toolchain check automatically?
- Do scoped Markdown indexes or documentation search tools improve correctness for our actual agents, compared with ordinary page retrieval?
- Which supported languages and shells have enough readers to justify maintained executable examples?
- Can agent-assisted drafts reduce authoring time without increasing technical-review burden? No result is claimed here.

## Frontier documentation interfaces — 2026-11-05

[[concepts/agent-documentation-interfaces]] specializes the delivery/interaction boundary: source retrieval versus synthesized answers versus API execution; version fallback and retrieval-triggered indexing; browser-local tool lifecycle; novel/internal API task evaluation. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--webmcp-20261105#root]] [[sources/frontier-docs--empirical-20261105#root]]

The owned findings preserve source-specific controls and uncertainty; no universal context budget or future training-data guarantee is inferred. See [[artifacts/projects/dokimi]] for the documented evaluator, and [[artifacts/projects/webmcp]] for the dated browser contract.

## Vercel Schedules — 2026-11-06

[[artifacts/projects/vercel-schedules]] preserves source drift between a launch example, product configuration, skill guidance and framework envelopes rather than blending them into a fictional contract. The capture records 8/16/64 KB scope differences and a source-path/build-output-path conflict. [[sources/vercel--schedules-docs#documentation-conflicts]]
