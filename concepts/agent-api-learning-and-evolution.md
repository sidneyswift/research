---
domain: concepts
type: concept
name: agent-api-learning-and-evolution
creators:
  - "[[creators/timo-schick]]"
  - "[[creators/berkeley-function-calling]]"
  - "[[creators/openai]]"
  - "[[creators/anthropic]]"
sources:
  - "[[sources/schick--toolformer]]"
  - "[[sources/berkeley--function-calling-evaluation]]"
  - "[[sources/openai--agent-api-design]]"
  - "[[sources/anthropic--agent-api-design]]"
status: emerging
last-reviewed: 2026-11-04
---

# Agent API learning and evolution

> **One-line:** Design for agents that can learn an interface from current descriptions and feedback; do not make safe operation depend on a model having memorized a vendor's API during training.

## What it is

Agent API competence can come from several mechanisms: prior learned conventions, explicit tool-use training, current tool documentation supplied at runtime, and feedback from attempted execution. They are different levers with different evidence. Toolformer supplies a narrow research example of training API selection and argument construction; BFCL evaluates function use given documentation; current OpenAI and Anthropic tool protocols explicitly send definitions and return correlated outputs. The portable design question is therefore which semantics must remain stable and enforceable, and which interface details can be discovered and learned on demand. [[sources/schick--toolformer#abstract]], [[sources/berkeley--function-calling-evaluation#methodology]], [[sources/openai--agent-api-design#function-loop]], [[sources/anthropic--agent-api-design#tool-lifecycle]]

This is a research framing, not a claim about the exact training recipe of any current vendor model. It does not establish that all agents are trained on the public web, which vendor API versions they saw, or what fraction of future training data will describe frontier systems. Agent applications also differ in the models, tools, permissions and runtimes they combine. [[sources/openai--agent-api-design#agent-surfaces]], [[sources/anthropic--agent-api-design#managed-runtime]]

## Where it came from

- **2023 research example:** Schick and colleagues' Toolformer abstract describes training a model to select APIs, decide when to call them, generate arguments, and incorporate returned results. The listed tools are a calculator, Q&A system, search engines, translation and calendar. This is author-reported evidence of an explicit tool-learning mechanism, not evidence of successful ERP/payroll transfer or ten-year trends. [[sources/schick--toolformer#abstract]]
- **Historical evaluation methodology:** the captured BFCL methodology supplies function documentation, tests selection among several functions, tests abstention when none fits, and distinguishes AST matching from executable checking. We use the methodology, not its historical model rankings as current performance evidence. [[sources/berkeley--function-calling-evaluation#methodology]]
- **2026 provider contracts:** OpenAI and Anthropic document tool schemas, descriptions, result correlation, runtime ownership, and compatibility limits. These make interface use partly a runtime protocol, not solely a recalled fact from pretraining. [[sources/openai--agent-api-design#tool-design]], [[sources/anthropic--agent-api-design#tool-definitions]], [[sources/anthropic--agent-api-design#tool-lifecycle]]

## Why it matters

If we attribute every failure to missing training data, we may wait for a future model instead of fixing ambiguous capability names, missing descriptions, wrong permissions, weak errors or an unobservable workflow. If we attribute every failure to API design, we may miss a model's planning, selection or tool-use limitations. The sources support evaluating these separately: BFCL decomposes selection/call structure/execution, while OpenAI distinguishes protocol compatibility from changeable model behavior. Our design implication is to improve the interface and the agent together, while measuring which intervention actually helps. [[sources/berkeley--function-calling-evaluation#methodology]], [[sources/openai--agent-api-design#compatibility]]

## Evidence & claims

### Shopify runtime-context evidence — 2026-11-04

[[artifacts/projects/shopify-api]] adds an established business platform that explicitly gives coding agents current docs, schemas and validation access; UCP profile negotiation also makes versioned supported capabilities inspectable at runtime. This supports the runtime-context mechanism, not proof of learning in model weights or improved task success. [[sources/shopify--agent-commerce-api-design#toolkit]], [[sources/shopify--agent-commerce-api-design#profiles]]

### Four mechanisms that should not be collapsed into “trained on the web”

| Mechanism | What the captured evidence supports | What it does not establish | API-design implication — our synthesis |
| --- | --- | --- | --- |
| Prior learned conventions | OpenAI states that callable definitions are injected in a syntax the model has been trained on | Exposure to a named business API, its current version, or the provenance/proportions of general training data | Familiar conventions may help, but current contracts must still be available |
| Explicit tool-use learning | Toolformer describes training which API/when/arguments/result incorporation from a small demonstration seed | Enterprise permission competence, universal transfer, or the recipes of current frontier models | Treat tool competence as trainable behavior; do not infer it from language fluency alone |
| Runtime documentation and schema loading | Both providers accept tool definitions; OpenAI documents namespace/deferred discovery and Anthropic detailed behavioral descriptions | That any arbitrary documentation will be sufficient, or that retrieval can fix all reasoning failures | Publish precise, bounded, versioned callable descriptions and expose the relevant subset |
| Execution feedback and evaluation | Both tool protocols return outputs linked to calls; BFCL has executable checks and relevance tests | Automatic weight updates from an ordinary tool result or safe trial-and-error on production systems | Return actionable typed outcomes and test recovery in controlled environments |

Sources for the four rows, respectively: [[sources/openai--agent-api-design#tool-design]], [[sources/schick--toolformer#abstract]], [[sources/openai--agent-api-design#tool-design]] and [[sources/anthropic--agent-api-design#tool-definitions]], [[sources/openai--agent-api-design#function-loop]] and [[sources/anthropic--agent-api-design#tool-lifecycle]] and [[sources/berkeley--function-calling-evaluation#methodology]].

Runtime context use is not the same thing as persistent training. A model can use returned error information in the current interaction without its weights changing; the captured tool protocols document continuation, not online model updating. We should specify whether an experiment changes model weights, prompts/descriptions, retrieved context, runtime policy, or application code before claiming that the agent “learned.” This is a scope distinction inferred from the documented mechanisms. [[sources/openai--agent-api-design#function-loop]], [[sources/anthropic--agent-api-design#tool-lifecycle]], [[sources/schick--toolformer#abstract]]

### What is likely to remain a platform responsibility

The current provider contracts distinguish context from execution authority: strict schemas constrain shape, application tools execute outside model generation, and managed permission/review controls do not erase environment restrictions or custom-tool responsibility. Our conclusion is that better future selection does not justify moving business authorization, invariants or durable-effect recording into a model's implicit understanding. That conclusion is an engineering inference, not a claim that model capabilities cannot improve. [[sources/openai--agent-api-design#strict-schema]], [[sources/openai--agent-api-design#review-boundary]], [[sources/anthropic--agent-api-design#strict-tools]], [[sources/anthropic--agent-api-design#managed-permissions]]

We should also preserve separately inspectable completion levels: model output, tool result, runtime/session state and business outcome. Anthropic documents an idle session with an open workflow; OpenAI distinguishes response, conversation, managed session and sandbox. Training on more examples of these protocols does not make their meanings interchangeable. [[sources/anthropic--agent-api-design#managed-session-operations]], [[sources/openai--agent-api-design#agent-surfaces]]

### What can evolve without replacing the business contract

Both providers already allow distinct model-facing surfaces above underlying actions: OpenAI offers namespaces and deferred discovery; Anthropic recommends grouping related actions into fewer well-described tools. They do not prescribe one universally optimal granularity. Our inference is that discovery catalogs, descriptions, adapters and grouped tools can evolve faster than business capabilities, while preserving action-specific checks and provenance. The right grouping should be evaluated on tasks, not deduced from vendor age or an assumed training corpus. [[sources/openai--agent-api-design#tool-design]], [[sources/anthropic--agent-api-design#tool-definitions]], [[sources/anthropic--agent-api-design#managed-permissions]]

### One-, five-, and ten-year scenarios

**Baseline: 2026-11-04. These are conditional research scenarios, not forecasts, commitments or claims about future training data.** The evidence establishes mechanisms available now; the following hypotheses ask how their relative value might change.

| Horizon | Conditional scenario / hypothesis | Alternative that could also occur | Evidence that would test it |
| --- | --- | --- | --- |
| **2027-11-04 — one year** | If tool-use training and current-schema discovery improve, an unfamiliar well-described API may become easier to use without vendor-specific memorization | Tool selection may improve while multi-step recovery, domain ambiguity or stale context remains the dominant failure | Freeze business tasks; compare current and later model snapshots on familiar versus deliberately renamed/unseen interfaces, with and without current docs; separately score selection, arguments, effects and recovery |
| **2031-11-04 — five years** | If runtime discovery and managed execution become more interoperable, reusable business capabilities may serve several agent surfaces through adapters | Provider-specific state/tool contracts may diverge, or domain-specific workflows may continue to outperform generic adapters | Repeat the same task suite across providers and interface forms; measure adapter maintenance, outcome correctness, permission failures and recovery effort, not just call syntax |
| **2036-11-04 — ten years** | If agents can negotiate or generate much of their own interface glue, human-authored route names may matter less for some integrations while explicit effects, authority and observable outcomes remain central | Familiar APIs may persist because compatibility, regulation, operational cost or integration ecosystems outweigh autonomous adaptation | Evaluate migration and failure cases over real version histories; test whether generated adapters preserve invariants, access boundaries, idempotency and audit trails under changed schemas |

The first scenario is motivated by the existence of explicit tool-use training and current-definition loading; the second by today's multiple runtime ownership models and catalog surfaces; the third extrapolates those mechanisms and tests the inference against current authority/completion boundaries. None is a documented prediction by the cited authors. [[sources/schick--toolformer#abstract]], [[sources/openai--agent-api-design#tool-design]], [[sources/openai--agent-api-design#agent-surfaces]], [[sources/anthropic--agent-api-design#managed-runtime]], [[sources/anthropic--agent-api-design#managed-permissions]]

### Proposed evaluation design for this research group

Use a frozen, bounded task suite on safe synthetic/test systems. BFCL's documented separation of function selection, structural matching, abstention and execution is a starting point, not a complete enterprise validation method. The business extensions below are proposed work, not completed experiments. [[sources/berkeley--function-calling-evaluation#methodology]]

| Factor to vary | What the comparison isolates |
| --- | --- |
| Familiar resource/action names versus systematically renamed equivalents | Dependence on naming familiarity; not proof that the original API appeared in training |
| No docs versus supplied current schemas/descriptions versus retrieved relevant subset | Value and cost of runtime interface knowledge |
| Separate actions versus grouped domain tools versus an orchestration operation | Selection/composition burden versus coherent business intent |
| New versus pinned model snapshot with unchanged API/task inputs | Model drift independent of protocol evolution |
| Valid schema but invalid business precondition | Shape correctness versus safe effect execution |
| Missing tool, ambiguous request, stale revision or insufficient authority | Abstention/clarification behavior instead of forced tool calling |
| Duplicate submission, worker restart, lost response and partial provider failure | Recovery behavior and real effect accounting, beyond AST correctness |

Score the outcome at several levels: selected capability; correct argument structure; semantically correct inputs; correct authorized state transition; abstention when necessary; recoverable partial failure; and evidence of the final business outcome. Also record calls, latency, token use and human intervention. These are proposed enterprise additions to the narrower captured evaluation. Do not label a successful parsed call as a successful business workflow. [[sources/berkeley--function-calling-evaluation#methodology]], [[sources/openai--agent-api-design#structured-output-limits]], [[sources/anthropic--agent-api-design#managed-session-operations]]

If a model performs better on a popular API, naming, documentation quality, tool-specific post-training or task difficulty could explain the result. Without access to training data and controlled attribution experiments, do not claim that web exposure caused the improvement. BFCL's historical blog itself discusses contamination concerns and separates different evaluation methods; it does not provide the causal study we need. [[sources/berkeley--function-calling-evaluation#methodology]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — more fluent use of a schema is not broader permission; provider review/runtime distinctions remain relevant. [[sources/openai--agent-api-design#review-boundary]], [[sources/anthropic--agent-api-design#managed-permissions]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — trained selection and argument proposal coexist with code-enforced constraints, execution and observed outcomes. [[sources/openai--agent-api-design#function-loop]], [[sources/anthropic--agent-api-design#tool-lifecycle]]
- [[patterns/quality-bar/defect-derived-validation]] — proposed enterprise evaluations should add checks for failures actually observed in repeated case studies. BFCL supplies a decomposition example, not proof that its original categories cover every enterprise failure. [[sources/berkeley--function-calling-evaluation#methodology]]
- Candidate: **runtime-learnable interfaces above stable effect contracts**. Supported as a synthesis direction by current descriptions/catalogs; not promoted to a confirmed implementation pattern or empirically demonstrated superiority claim.

## Tensions & counter-arguments

- **Familiarity can still matter.** A model trained on a known protocol may have useful priors; this does not settle unfamiliar-vendor transfer or justify hiding current schemas. OpenAI explicitly acknowledges learned function-definition syntax. [[sources/openai--agent-api-design#tool-design]]
- **More documentation is not always better context.** OpenAI recommends limiting initially available tools and evaluating deferred discovery; Anthropic recommends carefully scoped behavioral descriptions. Neither supports dumping an entire ERP manual into every turn. [[sources/openai--agent-api-design#tool-design]], [[sources/anthropic--agent-api-design#tool-definitions]]
- **Specialization may beat generic adaptation.** Toolformer establishes a particular training approach on particular tools, while BFCL describes narrow function-use evaluation. Neither demonstrates that general agents will replace domain-specific integration engineering. [[sources/schick--toolformer#abstract]], [[sources/berkeley--function-calling-evaluation#methodology]]
- **Evaluation success can be narrower than deployment safety.** AST matching and even executable GET-style calls do not settle authorization, irreversible effects, reconciliation or long-running workflows. The captured historical BFCL methodology's own REST category emphasizes GET requests and checks executable outputs. [[sources/berkeley--function-calling-evaluation#methodology]]
- **Protocols and behavior drift separately.** Future model changes may improve one task and regress another without any endpoint changing. OpenAI's compatibility guidance explicitly separates model prompting behavior from API stability. [[sources/openai--agent-api-design#compatibility]]
- **Forecast uncertainty grows with horizon.** The dates above organize experiments and strategic questions; no cited source establishes the projected adoption pace, corpus mixture or economic feasibility.

## Timeline (append-only)

- 2023-02-09 — Toolformer v1 submitted; abstract describes explicit training for API selection, argument generation and result incorporation. [[sources/schick--toolformer#abstract]]
- 2026-11-04 — Captured historical BFCL methodology and current provider contracts; separated observed mechanisms from 2027/2031/2036 research scenarios. [[sources/berkeley--function-calling-evaluation#methodology]], [[sources/openai--agent-api-design#root]], [[sources/anthropic--agent-api-design#root]]

## Related

- [[projects/designing-apis-for-agents/README]] — owning research hub and future work.
- [[analyses/frontier-and-business-api-design]] — broader frontier/business comparison; read its status and review boundary.
- [[concepts/business-platform-api-design]] — stable business intent, operations and invariants.
- [[concepts/code-mode-capability-interface]] — current definitions and programmable composition.
- [[concepts/imitation-vs-correctness-eval]] — output resemblance and real correctness are separate axes.
- [[artifacts/projects/openai-agent-api]], [[artifacts/projects/anthropic-agent-api]] — the inspected provider-documentation case studies.

## What we'd steal

- ★ Treat corpus familiarity as a hypothesis, not an architectural dependency.
- ★ Make current capabilities understandable from their published definitions; test unfamiliar names and versions.
- ★ Keep protocol compatibility, model behavior and runtime/effect guarantees as separate contracts.
- ★ Preserve deterministic business authority and invariants even as agents improve at selection and planning.
- Record whether “learning” means weight changes, prompt/schema changes, retrieval, interaction feedback or application fixes.
- Distinguish a tool proposal, application execution, runtime state and verified business outcome.
- Supply effect-aware descriptions: purpose, when not to use, inputs, output meaning and failure behavior.
- Defer large catalogs and evaluate the relevant initial subset rather than assuming a fixed optimal tool count.
- Compare action-level and workflow-level tools on the same task corpus; do not decide granularity from vendor age.
- Bind trusted known context where appropriate instead of asking a model to reconstruct it.
- Test valid-shaped but semantically wrong calls, not only malformed JSON.
- Include missing-tool and insufficient-authority tasks where abstention or clarification is the correct outcome.
- Track partial results and recovery under lost responses, retries and runtime restarts.
- Use stable task IDs and frozen model/API/document versions for longitudinal comparisons.
- Evaluate new model snapshots against existing business tasks before migration.
- Use structural checks and executable outcome checks together; do not equate either alone with a business safety audit.
- Record latency, calls, token cost and human intervention alongside correctness.
- Keep historical leaderboard methodology separate from current rankings and causal training claims.
- Frame 1/5/10-year views as conditional scenarios with tests and disconfirming evidence.
- Revisit the research when new measured results arrive; do not update forecast confidence solely because more documentation was published.

## Open questions

- On our target business tasks, how much failure comes from discovery, argument construction, domain ambiguity, planning, permissions or recovery?
- Does current-document retrieval reduce the performance gap between familiar and unfamiliar interfaces?
- When do grouped tools outperform explicit actions without hiding effect-specific authority?
- Which observed integration defects should extend the function-calling evaluation categories?
- What evidence would justify changing the 2027/2031/2036 scenarios rather than merely restating them?
- Can we obtain enough controlled evidence about model training or adaptation to attribute any familiarity advantage causally?

## Verification boundary

This page synthesizes captured source text and inspected provider documentation pages. The Toolformer **abstract** is the evidence used; the full captured PDF was not analyzed for additional experimental claims. BFCL is a historical methodology source, not a current leaderboard assessment. No training, fine-tuning, agent benchmark, live API request or enterprise failure-injection experiment was run for this page.
