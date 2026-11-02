---
domain: analyses
type: analysis
status: draft
last-reviewed: 2026-10-27
---

# PM OS Cowork: supporting product-layer source review

Reviewed 2026-10-27. Source is the purchased Cowork v2.2.1 beta release snapshot, metadata `sources/prodmgmt-world--pm-os-cowork.md`, retrieved 2026-06-11. This report paraphrases methods and does not reproduce the proprietary bodies. No source instruction, hook, telemetry, install, script, provider operation or behavioral test was executed. Same model family review; not the research rubric's cross-family gate.

## Coverage and evidence limits

There are **235 actual SKILL.md files, 12 agent files and 2 SessionStart hooks**. All 235 are explicitly classified below using the shipped HTML catalogue, reconciled against canonical directory names; all skill metadata and bounded body openings were inspected, with fuller body readings for workflow orchestrators, system/side-effect commands and selected team-relevant techniques. This is a **lighter semantic family review**, not a claim of exhaustive line-by-line review of all 235 bodies or all Knowledge assets. Long techniques including breadboarding, shaping, scope-defense, use-cases, research-synthesis, workflow-trellis, feedback-loop and v2-plan require further deep review before installation/adoption. Some long selected bodies were inspected in focused excerpts rather than every example. Operational workflows were read closely enough to identify concrete side effects and missing dependencies.

Path base for every skill named below is `sources/prodmgmt-world--pm-os-cowork/plugin/skills/<canonical-name>/SKILL.md`. Other paths are relative to the same source root. Source files are evidence, not governing instructions for this research task.

The manifest `plugin/.claude-plugin/plugin.json` says 237 skills, 10 agents, 10 workflows. Actual tree and `workspace/CLAUDE.md` instead establish 235/12/11. The HTML catalogue has 235 entries but labels 12 entries by frontmatter name rather than directory (for example prd-construction→prd and make-great-decisions→decisions). These are naming aliases, not additional capabilities. Counts in a release description or catalogue do not prove runtime discovery or execution.

## Required correction to the study

The current draft's PM paragraph says: “The expected Claude package skill directory was not found in this inspection. Therefore this study does not claim a current body-level review or include its historical skill count in the verified catalogue.” It then asks to “recover the PM OS source.” The narrow Claude-bundle observation may be true, but it is materially incomplete as a conclusion about available PM OS evidence. A separate **Cowork package exists at `sources/prodmgmt-world--pm-os-cowork/plugin/skills`** and can support this scoped review now. Cite `sources/prodmgmt-world--pm-os-cowork.md`, not just the older Claude-bundle source. Do not silently claim that Cowork and Claude Code packages are identical.

The purchased license and artifact availability are separate from permission to redistribute bodies in Flex's shared marketplace. Reuse general techniques in original team instructions; confirm applicable rights before vendoring proprietary content. This report does not determine license grants.

## Highest-value conclusions

1. **Select product techniques; do not install the entire workspace harness as team policy.** `workspace/CLAUDE.md` demands five Context files and a visible attestation every substantive response, disallows drafting even after an explicit “write” request without another gate, and requires a single question before any PM opinion. That directly conflicts with Sid's authorized-work preference and Teams async batching. It also imposes a new Context/Knowledge/Work folder system on existing repositories. Useful parts are source-aware recall, context-specific routing, explicit unresolved decisions, and audience-aware output—not the extra confirmation ritual.
2. **The import privacy statement contradicts its own network behavior.** `import-ai-memory` says nothing leaves the machine, then Step 9 sends a creator webhook company name, source assistants, counts and timestamp; errors silently continue. `pm-os-start` sends company/industry/funding, product/challenges, PM role/team/friction, focus/win and recommendation telemetry after local saves. `pm-os-feedback` sends feedback plus best-effort company/role/product context; `pm-os-testimonial` previews then sends approved text with identity context. These are explicit source instructions, not evidence that any request actually happened. Exclude telemetry from any team adaptation; do not treat local file confirmation as blanket disclosure consent.
3. **Important guards and helpers are missing from the shipped tree.** Neither root nor workspace contains `bin/` or `docs/memory/`; `feedback-config.md`, `plugin/registry/skills.json` and the external-skills updater are also absent. Capture/import/recall/daily-drip/tidy/upgrade/release validators are contracts in prose, not verified included implementations. Arithmetic skills reference absent `scripts/estimate.py`, `scripts/calculate_voi.py`, `scripts/analyze.py`; frontend-slides has STYLE_PRESETS.md but lacks required CSS/templates/animation files and all three scripts. Do not credit these as runnable automation or validated data safeguards.
4. **Draft completeness is not approved readiness.** `prd-draft` fills missing sections with informed assumptions, numeric targets and milestones, then lists significant assumptions/questions at the end. The full `prd` calls it after requirements/stories/acceptance-criteria collection. This can create persuasive proposed scope while important decisions remain open. Adapt by marking uncertain claims inline, recording owner/decision/source, keeping GitHub epic/issue draft state, and requiring explicit readiness transition. A review persona cannot approve on behalf of engineering, legal, customers or business owners.
5. **The product layer helps before and after engineering but does not own shipping.** There is no demonstrated GitHub epic→approved issue→PR lifecycle, parent/submodule commit publication sequence, deployment verification, or Teams message transport. `.mcp.json` includes GitHub but server presence is not a workflow contract or authenticated capability evidence. Slack is not bundled; `slack-signal` consumes pasted text. Adapt channel-neutral evidence synthesis to Teams; preserve timestamps/links and distinguish suggestions, decisions and accepted actions.
6. **Stale-prose control is genuinely addressed, but needs present-state evidence.** `research-recency` distinguishes stable user needs from changing behavior/product/market context and proposes validation; `tidy` compares modified work to Context and asks before updates. Neither mtime nor a well-written memo proves a live release, actual use, cost savings or approved policy. Keep canonical facts with their owner and link supporting evidence rather than replicating project status in another memory silo.

## Orchestrators: inputs, outputs, and adoption advice

All 11 workflow names below resolve to actual canonical directories. Most chain skills, carry outputs forward, and offer saving in dated project Work files. Confirm-between-step behavior permits end-to-end requests, but the separate harness imposes additional gates. Adapt the interaction contract to established user authorization and existing docs placement.

| Workflow | Input → output and important sequencing | Team disposition |
|---|---|---|
| strategy | Company/problem/constraints → strategic crux, Porter competitor analysis, product strategy, constraint choices, value chain. Optional Lenny podcast enrichment. | Reuse selected reasoning; cite current company/source evidence and avoid a mandatory six-document ceremony. |
| opportunity | Business outcome, users, interview evidence → structured intake, OST, optional MECE refinement, four-factor qualitative choice; ost-choose is an explicitly alternative mechanical selector. | Strong upstream discovery method; connect chosen opportunity to one epic, not directly to approved implementation. |
| assumptions | Strategy → desirability/feasibility/viability/usability assumptions, pairwise risk ranking, cheap validation signals. | Reuse assumption→test mapping. Adapt repeated QuickSort questions to bounded async comparison. |
| research | Transcripts → cleanup, JTBD extraction, forces clustering, hypotheses, experiment plans. | Strong evidence chain. Description says tested hypothesis but body only designs experiments; do not claim testing occurred. Preserve raw originals and quote provenance. |
| decisions | Situation → causal map, reversibility, journal, MECE options, recommendation, decision rights. | Useful decision record. Wrapper's DAVCI expansion differs from leaf; use leaf's explicit roles and actual owner confirmation. |
| stakeholder | Known profiles + initiative → power/interest map, risk register, comms frames, meeting prep, hard-conversation script, exec update review. | Reuse audience-aware comms; sensitive motive speculation stays tentative, not canonical fact. Step7 says review performance after meeting but exec-update-review actually edits a draft/deck, so input/output mismatch needs repair. |
| meeting | Profiles and meeting context → possible motives, influence tactics, then post-meeting transcript summary. | Use preparation and summary only as needed; cannot generate actual meeting outcomes from pre-meeting hypotheses. Wrapper expands IDEAS differently from meeting-summary leaf. |
| pm-review | Document + selected lenses → up to7 structured read-only reviews; optionally synthesized convergence/conflicts/actions; save beside source when possible. | Good bounded reviewer contract; remove redundant one-question-per-lens gate for authorized async review. Multiple personas of one model are not independent model families or actual stakeholder approval. |
| coaching | PM situation → alignment-router → one of5 behavioral modes, optionally saved cross-project; separate consent for durable memory. | Optional personal development, not engineering process or performance-review evidence. |
| measure | Intangible→observable metrics→Fermi decomposition→elicited uncertainty ranges→value of information→sampling plan or observations→updated decision model. | Useful measurement design. Missing scripts and untested statistical assumptions prevent treating estimates as achieved outcomes. Do not turn inferred ranges into booked savings. |
| prd | Raw talk/design/research→conflict reconciliation→use cases→basic/Gherkin stories→UI criteria if relevant→draft→2 PRD lenses→optional7 cross-functional lenses→explicitly gated synthesis. | Reuse selected chain and reviewer I/O; preserve unresolved decisions. Overlap with Matt/HumanLayer PRDs should become one chosen artifact contract, not three competing PRDs. |

The reviewer agents are `plugin/agents/{prd-strengths-reviewer,prd-flaws-reviewer,engineering-reviewer,design-reviewer,executive-reviewer,legal-risk-reviewer,ux-research-reviewer,devils-advocate-reviewer,customer-voice-reviewer}.md`. They declare readonly and structured status/scope/findings/open questions/next action. Their output is analysis, not authorization. `pm-workflows.md` allows confirmed workflow output writes; `context-manager.md` and `knowledge-librarian.md` support status/retrieval. Agent frontmatter cannot by itself enforce runtime readonly access.

## System and side-effect skills

| Skill/family | Behavior and dependency | Recommendation |
|---|---|---|
| pm-os-start | Web-enriched onboarding, confirmed Context writes, optional stakeholder/style/project creation, four setup telemetry stages plus import branch. | Do not transplant; use existing owner context. No telemetry in adaptation. |
| import-ai-memory | Paste-back import from up to3 assistants, per-file conflict preview and atomic Context writes; user/project memory helpers; creator telemetry. Missing extraction prompt/helper docs. | Reuse provenance/digest/conflict-preview idea only. Do not claim pasted assistant memory proves current business state. |
| pm-os-capture-memory | Explicit source only, no hidden logs/browser/history harvesting; candidate event preview, confirmation tied to current digest, sensitivity default exclusion; event append and projected decision log; global memory separate. | Strong persistence contract to adapt to existing records. Missing helper implementations mean guards/locking/secret filters are unverified. Import calls append-events with a different argument shape than capture; cannot reconcile without helper. |
| pm-os-daily-drip | Opt-in local context question state machine, no new question when pending/unfiled; skip/snooze/stop. Uses absent state helper; no scheduling/network in body. | Optional concept, not a Teams monitor. Existing context is preferable to repeated intake. |
| pm-os-project | Creates/switches/multi-activates/archives local project folders; nested parent context cascades down; archive moves descendants and prunes active entries. | Do not use to restructure independent engineering repositories. Current command marks first active slug default, but save/capture says ask when multiple; clarify rather than infer. |
| pm-os-tidy + tidy-procedure | Scans modified Work/orphans, proposes moves and Context changes, confirms, uses git mv if tracked; archive/empty deletion only approved; writes tidy state. Missing bin/tidy.sh. | Reuse affected-record reconciliation. Existing docs locations are not orphans simply because upstream taxonomy differs. Procedure's bare mkdir example contains spaces without quoting; fix in any implementation. |
| pm-status | Reads Context, per-active-project recall/cascade, user-memory and files to recommend one next action; graceful fallback for unavailable memory. | Reuse compact evidence-aware resumption. Never infer current deployment from saved prose. |
| pm-help, pm-os-framework, pm-os-skill | Discover actual files and route to matching knowledge/skills, optional podcast lookup. | Good discovery principle, poor portable paths. pm-help still references old commands directories and Cursor-only MCP config despite Cowork package. |
| skill-browser | Opens shipped static235-entry HTML catalogue in host browser; font CDN. | Useful discoverability, not dynamic registry or execution proof. Frontmatter labels differ from canonical directory invocation. |
| pm-os-feedback, pm-os-testimonial | External webhook sends; feedback adds company/role/product/challenge automatically best-effort; testimonial requires preview approval. Missing webhook config. | Exclude from shared engineering adaptation. Feedback's302-as-success rule does not establish durable receipt. |
| pm-os-upgrade | Tool-aware in-place replacement, removes other tool surface in mixed distributions; preserves selected Context/customizations, overwrites custom bin scripts. Cowork explicitly uses UI reupload instead. Missing upgrade helper. | Exclude; respect canonical marketplace and repository rules. |
| frontend-slides | Generates local HTML/previews, opens browser, deletes preview directory; optional PowerPoint extraction/install, optional Vercel publish, PDF via browser install/server; remote fonts. Required supporting files mostly absent. | Use existing slide capability instead. Optional publishing remains separately authorized. No unsupported claim that hosting cannot incur charges. |
| staff-or-intern | Separate planning vs exact-file implementation modes; can write code in implementation mode. | Mode separation useful, but its prescribed assertion of full codebase understanding is unsupported. Use verified scope. |
| vibe-code-leaf-finder | rg + Git history dependency/isolation/stability/testability audit; writes LEAF_REPORT.md; proposes external tests. | Adapt risk decomposition, not blanket permission to skip review or ship. Dynamic/remote consumers and submodule boundaries need explicit handling; no importing pure-consumer label as proof of safety. |

Hooks are in `plugin/hooks/{hooks.json,tidy-reminder.sh,drip-reminder.sh}`. They read local state and emit imperative session-start prompts, rather than automatically performing tidying or collecting answers. Tidy checks orphan/changed files and12-hour threshold; drip defers to tidy and tapers from roughly daily to weekly/fortnightly with pending-answer handling. The prompts force the first user-facing action before substantive work; unsuitable as a team default. No scheduler is thereby provided. `.mcp.json` registers six external servers and uses unpinned npx for Perplexity; no Teams integration is bundled or verified.

## Reusable technique families and substantive cautions

| Family | Typical inputs → outputs; effect profile | Recommendation for our team |
|---|---|---|
| Discovery/research | Transcripts, surveys, tickets, usage evidence → needs, jobs, opportunities, hypotheses, study plans. Primarily prose/data synthesis. | Select interview-insights, research-recency, product-assumptions, work-backwards, workflow-trellis. Synthetic personas/transcripts/roleplay are explicitly simulated evidence and cannot validate demand. |
| Requirements/design | Briefs/screenshots/PRDs → use cases, stories, criteria, flow descriptions/prototypes. Some actual HTML/file generation. | Reuse traceability and state coverage; avoid exhaustive boilerplate when bounded MVP suffices. Preserve draft vs approved. |
| Decisions/prioritization | Decisions/constraints/capacity → options, reversibility, ranking, tradeoffs, owners, scope changes. | Reuse decision-journal, two-way-door, scope-defense principles; estimated days/impact require owner evidence. P0/P1/P2 importance is different from engineering readiness/status. |
| Strategy/vision | Market/company evidence → diagnosis, positioning, constraints, goals, differentiated strategy. | Useful optional discovery layer; not all initiatives need a strategy workbook. Verify mutable competitor/market facts. |
| Measurement | Metrics/data/model assumptions → quantified model, uncertainty, experiment/tracking design or SQL. | Reuse observable outcome/measurement plans. Query generation is not execution; impact models are not realized returns. Rule-of-five concerns a population median interval from random samples, not confidence in mean/ROI or causal effect. |
| Communication | Raw facts/audience/voice → drafts, decks, structured updates and summaries. | Best short-term complement for Teams: status-update, comms-plan, tech-to-business, slack-signal. Keep factual issue/PR links and decision asks; do not auto-send. |
| Meeting/stakeholders | People, meeting goal, constraints → agenda, facilitation, decision-rights/comms plan. | Prefer async outputs where sufficient. Keep hidden motivations as hypotheses and avoid political speculation in durable shared facts. |
| Planning/execution | Brief/tasks/capacity → dependencies, schedule, top priorities, scenarios. | Adapt to GitHub ownership and live dependency state; no second task system or invented dates. |
| Ideation/analysis | Questions/problems → alternatives, issue trees, analogies. | Reuse only when uncertainty warrants. Solutions produced by imagination need validation before issues become ready. |
| Coaching/career | Personal situations/resumes → feedback, practice, development plan. | Outside core team rollout. Simulated peer judgments are not actual feedback; suppress insulting personas and unsupported psychological certainty. |
| Engineering | PRD/code/task → technical brief, planned code edits, risk report. | Supporting techniques only; mature engineering tools provide repo/test/PR contracts. |
| System | Context/workspace/plugin state → onboarding, retrieval, memory, housekeeping, external feedback. | Adapt selected contracts; do not copy harness, folder taxonomy, missing helper guarantees or telemetry. |

Further contradictions worth retaining in the adoption study:

- `decisions` expands DAVCI as Decides/Advises/Vetoes/Contributes/Informed; `davci` explicitly means Decider/**Approver**/Veto/**Consulted**/Informed, with one accountable Decider and distinct optional Approver. This is substantive authority drift. Its default veto deadline and proceed-after-silence text is not automatic team consent policy.
- `meeting` claims IDEAS means Issues/Decisions/Evidence/Actions/Sentiments; `meeting-summary` defines Insights/Decisions/Engagements/Actions/Summary. Choose the actual desired output; do not treat wrapper prose as authoritative evidence of the leaf.
- `risky-assumptions` correctly describes pairwise comparisons but claims23×4.5≈20–30 comparisons. That arithmetic is wrong (about104), and ranking forced choices can be nontransitive. Retain bounded comparison, remove unsupported efficiency guarantee.
- `mckinsey-issue-tree` names historical long skill identifiers in headings while canonical directories use shorter slugs. Resolve actual dependency paths before adapting; do not infer that generated names are installed commands.
- `socratic-thinking` explicitly requests an extended private reasoning stream and indefinite exploration. Exclude this behavior; use concise evidence/rationale/uncertainty summaries instead. Some other leaves request thinking tags; this is not an adoption requirement.
- `prd-draft`'s confidence/completeness posture conflicts with root cautious questioning and downstream explicit approval needs. `research`'s title/description overstates experiment execution. `pm-help` promises current discovery but includes stale commands/MCP paths. Capture actual behavior in the catalogue rather than copying descriptions.
- External `shaping`, `breadboarding`, `breadboard-reflection` identify `rjs/shaping-skills`, and frontend-slides identifies `zarazhangrui/frontend-slides`; assess those upstreams separately before vendoring. External-source attribution does not supply their license review or omitted assets.

## Practical composition

For a profit calculator or similar initiative, use a small product layer: evidence and existing tools→brief-to-problem/workflow-trellis as needed→one measurable decision outcome→a draft epic with assumptions/open decisions→bounded option and decision-rights review→approved scoped issues→existing engineering implementation and PR verification→concise Teams draft anchored in actual results→update the owning docs. No new PM OS workspace, parallel memory log, or automatic message sender is required. Business value is measured after release against a baseline; generating a measurement plan is preparatory work.

## Rubric on the initial draft, PM OS slice

Citation integrity **3**: the quoted paragraph cites only the older source and misses the separate Cowork source. Faithfulness **3**: a narrow missing Claude directory is presented without the available235-body Cowork evidence; do not imply this is a verified unavailable product. Completeness **2**: usable product techniques, telemetry, missing helpers and harness conflicts are absent. Non-genericness **4**: existing readiness/placement guidance is specific but lacks the strongest PM source evidence. Decision usefulness **3**: cannot choose reuse/adapt without these behaviors. Lowest2 blocks this slice under the rubric. After correction it may support a limited source-based recommendation; this review does not grant the cross-family gate or behavioral acceptance.

## Complete canonical catalogue by explicit family

Names below are canonical directories, each resolving to `plugin/skills/<name>/SKILL.md` under the source base above. Categories follow the shipped catalogue for traceability, with the12 label aliases normalized. Every actual body appears exactly once (235 unique names); categories are organizational, not claims that each family should be installed together.

### meetings & facilitation (9)

`1-on-1`, `meeting-agenda`, `meeting`, `meeting-outcomes`, `meeting-prep`, `meeting-summary`, `miro-workshop`, `refinement-session`, `workshop-design`.

### communication, writing & influence (17)

`5-step-story-deck`, `cialdini`, `comms-plan`, `exec-deck`, `exec-update-review`, `frontend-slides`, `leadership-presence`, `presentation-narrative`, `problem-deck`, `pyramid-principle`, `rulebook-for-arguments`, `skimmable-writing`, `slack-signal`, `status-update`, `strategic-deck`, `tech-to-business`, `what-so-what-deck`.

### coaching, self-management & career (27)

`adhd-action-summary`, `adhd-motivation`, `adversarial-roleplay`, `ai-tutor`, `blind-spot-scan`, `career-guidance`, `decision-audit`, `founder-focus`, `life-design-mapping-exercise`, `mindset-shift`, `motivation-journal`, `motivational-interview`, `orchestrate-pm-alignment`, `coaching`, `pm-interview`, `resume`, `resume-skill-gaps`, `situation-retrospective`, `skill-acquisition`, `skill-coach`, `skill-mastery`, `socratic-thinking`, `star-stories`, `superpowers`, `team-perspective-reveal`, `top-5-wins`, `work-sample`.

### design & prototyping (15)

`affordances-signifiers`, `app-design-foundation`, `clickable-prototype`, `cta-copy`, `demo-narrative`, `friction-reduce`, `interface-4-lenses`, `onboarding-redesign`, `pm-to-design`, `product-design-analyzer`, `solution-flaws`, `ui-to-json`, `ux-edge-cases`, `ux-terminology`, `wireframe-sketch`.

### discovery & research (36)

`aha-moment`, `ai-recommendation-canvas`, `assumptions`, `create-empathy-maps`, `critical-decision-method`, `design-critique`, `experiment-design`, `interview-guide`, `interview-insights`, `interview-notes`, `intuition-to-research`, `journey-map`, `jtbd-forces`, `jtbd-jobs`, `jtbd-market-canvas`, `jtbd-transcript-sim`, `mom-test-guide`, `nps-to-cx-plan`, `persona-lens-decision`, `problem-framing-canvas`, `product-assumptions`, `product-hypothesis`, `proto-persona`, `research-brief`, `research-decision`, `research-recency`, `research-synthesis`, `risky-assumptions`, `survey-to-actions`, `tickets-to-improvements`, `transcript-cleanup`, `transcript-insights`, `user-profile`, `v2-plan`, `work-backwards`, `workflow-trellis`.

### ideation & analytical thinking (15)

`brainstorm-genius`, `causal-tree`, `constrained-ideas`, `disruption-what-ifs`, `good-question-brainstormer`, `lateral-thinking`, `mckinsey-issue-tree`, `metaphor-thinking`, `offbeat-questions`, `power-user-shift`, `product-brainstorm`, `startup-ideas`, `tech-sensemaking`, `verbalized-sampling`, `via-negativa`.

### prd, specs & documentation (22)

`breadboard-reflection`, `breadboarding`, `edge-case-balance`, `eng-solution`, `expert-strategy`, `gherkin-stories`, `mrd`, `pm-review`, `prd`, `prd-draft`, `prd-enterprise`, `press-release`, `requirements-from-design`, `requirements-from-talk`, `requirements-reconcile`, `research`, `shape-up`, `shaping`, `ui-acceptance-criteria`, `use-case-map`, `use-cases`, `user-stories`.

### decisions & prioritization (22)

`brief-to-problem`, `bug-triage`, `decision-journal`, `exec-feedback`, `feedback-loop`, `gut-check`, `icp-roleplay`, `decisions`, `mece-tree`, `opportunity`, `ost`, `ost-choose`, `ost-intake`, `ost-prioritize`, `p0-p1-p2`, `problem-first`, `reinforcing-sequence`, `scope-defense`, `structure-problem`, `tradeoff-matrix`, `two-way-door`, `vision-to-quarter`.

### strategy & vision (23)

`business-strategy`, `strategy`, `find-the-strategic-crux`, `flywheel`, `growth-strategy`, `industry-strategy`, `inflection-scan`, `limit-strategy`, `moats`, `netmba-competitor-analysis`, `niche-finder`, `now-next-later`, `parity-vs-differentiation`, `pioneer-migrator-settler`, `positioning`, `product-strategy`, `seven-powers`, `strategy-kernel`, `strategy-review-prep`, `swot-moves`, `value-chain`, `vision-to-okrs`, `winning-position`.

### metrics & measurement (13)

`churn-reduction`, `clarification-chain`, `feature-writeup`, `fermi-decomposition`, `impact-model`, `impact-sizing`, `measure`, `metric-drop`, `rule-of-five`, `sql-from-spec`, `success-metric`, `tracking-schema`, `value-of-information`.

### stakeholders & politics (13)

`corporate-misalignment-finder`, `crisis-comms`, `davci`, `difficult-conversation`, `focal-point-finder`, `hidden-agendas`, `objection-scan`, `office-politics`, `power-map`, `stakeholder`, `stakeholder-map`, `stakeholder-risk`, `toc-thinking`.

### pm os system & operations (15)

`pm-help`, `import-ai-memory`, `pm-os-capture-memory`, `pm-os-daily-drip`, `pm-os-feedback`, `pm-os-framework`, `pm-os-project`, `pm-os-skill`, `pm-os-start`, `pm-os-testimonial`, `pm-os-tidy`, `pm-os-upgrade`, `pm-status`, `skill-browser`, `tidy-procedure`.

### planning & execution (5)

`project-plan`, `scenario-plan`, `task-list-to-plan`, `task-sequence`, `weekly-top-3`.

### code/engineering (3)

`staff-or-intern`, `tech-arch-brief`, `vibe-code-leaf-finder`.


Related: [adoption study](engineering-skill-adoption-study.md) · [full catalogue](engineering-skill-catalogue.md).
