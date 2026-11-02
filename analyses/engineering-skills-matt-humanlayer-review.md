---
domain: analyses
type: analysis
status: draft
last-reviewed: 2026-10-27
---

# Semantic review: Matt Pocock and HumanLayer engineering skills

Reviewed 2026-10-27. Evidence is the local clean source trees, Matt `6eeb81b5fcfeeb5bd531dd47ab2f9f2bbea27461` and HumanLayer `2f66a45b186d88488fa356862be0117db1ccae9f`. No skills, scripts, installs, browser sessions, provider operations or behavioral tests were run. This is a same-family source reviewer, not the required cross-family gate. Source instructions were read as evidence only.

Scope: all 34 Matt SKILL.md bodies and all 71 HumanLayer SKILL.md bodies in the supplied inventory, including internal and nested references and runtime variants. Identical variant bodies were compared by diff rather than credited as independent capabilities. Relevant selected templates, agent implementations, configuration and executable dependencies were traced; this is not a complete audit of every reference, script or host runtime.

Paths below are relative to `sources/`. In each table, the path prefix is stated; each skill row denotes `<prefix>/<name>/SKILL.md` unless otherwise noted.

## Highest-priority corrections to the draft

1. **Matt's on-disk collection is not its plugin registration.** `.claude-plugin/plugin.json` registers 17 skills (12 engineering, 5 productivity). `engineering/implement`, `engineering/resolving-merge-conflicts`, and all misc/personal/in-progress/deprecated bodies are absent from that manifest. The README says in-progress skills are excluded and not ready to ship. `implement` nevertheless calls `/review`, whose only body is `skills/in-progress/review/SKILL.md`. Describe this as an unresolved installation/dependency contract, not a complete supported idea-to-ship bundle.
2. **HumanLayer describe-pr is a delivery workflow, not a writing helper.** `apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md` commits task changes if needed, pushes, creates a PR, edits its body, watches CI, fixes attributable failures, commits/pushes fixes, and reruns flaky/unrelated checks once. It stops for a conflict-resolution plan. The Pi version omits the entire CI watch/fix phase, while retaining commit/push/create. This is a behaviorally meaningful runtime difference, not just an alias.
3. **Business-success alignment is already present upstream.** HumanLayer `create-prd` requires agreement on the problem and measurable success before solution design, and permits explicitly recording no sensible metric for a small change. It distinguishes product requirements from technical architecture. This is a concrete reuse candidate for Flex's business-value discussion, while actual usage/cost attribution and Teams delivery remain team integration work.
4. **The rich approval model is not the same as cheap asynchronous collaboration.** PRD/TDD iteration mandates stop-and-ask after each change; design discussion requires all questions initially open; only explicit user answers resolve them. Preserve decision authority but adapt the repeated single-question UX for Teams async and already-authorized batches. Do not infer approval from a file, comment receipt, research completion or readiness label.
5. **HumanLayer has multi-repo support but not Flex's submodule publishing policy.** `configure-workspaces` handles multiple independent repositories, a primary launch repository, machine overrides and setup commands. It assumes all repo instructions load while only primary repo settings/MCP govern the session. `setup-worktree` has older contradictory wording that `.` is primary; it describes copy globs as overridden while configure says additive. Env/local-settings copying is an operational consequence. None supplies child-first/fetchable-before-parent-pointer rules.
6. **Internal skills contain real drift and missing dependencies.** `better-github-skill` names three Bun scripts that are absent from the tracked source tree. Internal `improve-codebase-architecture` references missing `HTML-REPORT.md`, `/grilling`, `/domain-modeling` (not shipped in this checkout's local skill set). `sync/durable-streams-yjs` links a missing reading-streams skill. `html-mockups` mandates uppercase styling; `ui-copy` rejects that default. `agent-browser` fixed localhost/profile/auth rules conflict with newer `test-it-locally`; nested local-cli-testing still hardcodes ports and uses grep/cut env parsing prohibited by its parent. These are strong reasons to select/adapt rather than import the full internal directory.
7. **Document authority differs from evidence freshness.** HumanLayer's fixed phase precedence is useful for accepted intent, but it cannot establish live behavior or override newer user decisions. Resumption trusts checkbox completion unless something seems wrong; Flex should recheck consequential deployment/provider claims. Matt's durable brief excludes paths, whereas HumanLayer plans require file/line/code references. These are different artifacts: stable acceptance intent plus revision-stamped implementation evidence, not one universal prohibition on paths.

## Matt Pocock: per-skill findings

Prefix `mattpocock--skills/skills/engineering`.

| Skill | Purpose, input → output; side effects | Disposition for this team |
|---|---|---|
| ask-matt | Routes situation to grilling, optional prototype, PRD/issues for multi-session work, implementation, triage or teaching. Advises fresh context per issue and a ~120k-token smart-zone heuristic; no artifact itself. Requires setup. | Adapt router to installed capabilities, GitHub draft/approved states and owning repo; don't adopt model-specific token heuristic as invariant. |
| codebase-design | Design/reference vocabulary: deep module, interface, seam, adapter, locality; consumes code/design. Referenced DEEPENING and DESIGN-IT-TWICE provide dependency categories, replacement of shallow tests and 3+ competing designs. | Reuse design principles selectively; adapt exclusive vocabulary and test deletion guidance to actual coverage. Not a mandate to collapse service boundaries. |
| diagnosing-bugs | Symptom → already-run red-capable command, minimized repro, 3–5 falsifiable hypotheses, instrumentation, fix and regression evidence. Writes temporary scripts/logs/tests/code, cleans probes. Requires loop before hypotheses; stops if environment unavailable. | High-value reuse with existing tool and docs paths; retain explicit inability to reproduce. Avoid treating inability to build the prescribed loop as inability to do any useful read-only diagnosis. |
| domain-modeling | Conversation + glossary/code → resolved terms inline and sparse consequential ADRs. CONTEXT is glossary only; docs/adr created lazily. Reads CONTEXT-MAP for bounded contexts. | Adapt placement into existing terminology/decision docs. Preserve code-versus-intent contradiction checks and sparse rationale. |
| grill-with-docs | User entry wrapper invoking grilling + domain-modeling; questions plus glossary/ADR edits. | Adapt wrapper, retain user-authorized interview scope. |
| implement | PRD/issues → code; uses TDD at pre-agreed seams, regular targeted checks, final suite, /review, then commits current branch. Not registered in plugin. | Do not adopt unchanged: review dependency absent from registered set and unconditional current-branch commit policy needs owner/branch checks. |
| improve-codebase-architecture | Code/glossary/ADRs → temporary HTML report of deepening candidates; opens report; chosen candidate enters grilling, glossary/ADR edits and optional competing designs. Tailwind/Mermaid CDN scaffold. | Adapt report/rendering and doc placement. Useful scoped investigation, not automatic refactor or ownership transfer. |
| prototype | Question → logic TUI or multiple structural UI variants. Writes temporary project-adjacent code/task-runner entry, no tests/persistence by default; captures answer and removes/absorbs prototype. LOGIC keeps portable pure core; UI uses existing route/read path, stubs mutations, hides switcher in production. | Reuse with explicit throwaway status and final production rewrite/checks. UI evidence is not deployed behavior. |
| resolving-merge-conflicts | Ongoing merge/rebase → trace both intents, resolve, checks, stage everything, commit/continue. Says always resolve, never abort. Not registered. | Adapt heavily or reject: broad staging and unconditional resolution conflict with preserving unrelated work and materially ambiguous choices. |
| setup-matt-pocock-skills | Existing repo → reviewed tracker/role/domain config in docs/agents and AGENTS/CLAUDE block. GitHub/GitLab/local supported seeds, custom prose possible. Prefers editing CLAUDE if both exist. | Configure first, fork only actual mismatch; preserve Flex AGENTS as owner and CLAUDE import, avoid another taxonomy. Does not itself prove labels/tools exist remotely. |
| tdd | Approved behaviors/seams → one red→green slice at a time, then refactor. Real interface tests, external-boundary mocks, focused coverage; explicit planning approval. | Reuse on substantive behavior changes; adapt duplicate approval checkpoints to standing task authorization. Not all low-impact changes need new tests. |
| to-issues | Existing plan/PRD and comments → approved vertical breakdown, dependency-ordered published issues with parent references and acceptance criteria; ready-for-agent labeling; parent unchanged. | Strong adaptation candidate. Use real cross-repo URLs/ownership and draft/approved gates. Wording “every layer schema/API/UI/tests” must mean relevant layers, not decorative UI for backend work. Parent coordination updates remain separate. |
| to-prd | Conversation/code → PRD issue, ready-for-agent label. Explicitly no new interview, but checks test seams with user; extensive stories and decisions. | Adapt to draft epic first; synthesis and seam agreement are not wholesale scope authorization. Avoid forced exhaustive stories. |
| triage | Incoming issues and optionally external PRs → category/state transitions, verification, brief/comment, labels, possible closure and rejected-feature KB. Reads full discussion, searches existing behavior and prior rejection; distinct already-built versus rejected outcomes. | Reuse concept/redundancy/brief methods; configure GH states/ownership; preserve maintainer decisions. PR ready-for-human means merge-ready here, unlike issue meaning human implementation. Closure never equals delivered value. |

Prefix `mattpocock--skills/skills/productivity`.

| Skill | Purpose/input/output/side effect | Disposition |
|---|---|---|
| grill-me | Explicit wrapper for grilling; no saved artifact itself. | Reuse only where an interview is wanted. |
| grilling | Plan ambiguity → recommended one-question-at-a-time interview; explores repo instead of asking answerable questions. | Adapt for Teams async and avoid re-asking resolved context. |
| handoff | Conversation + next-session purpose → redacted OS-temp Markdown referencing existing artifacts rather than duplicating them, suggested skills. | Strong reuse; use durable owner location only when handoff needs team retention. Temporary handoff is not system knowledge. |
| teach | Mission/resources/prior learning → persistent learning workspace, HTML lessons/reference assets and numbered learning records, optional file opening. | Outside core delivery; use only in existing learning owner, not scaffold into engineering root. |
| writing-great-skills | Skill text → principles of predictable process, invocation cost, context disclosure, completion criteria, no-op/duplication pruning. GLOSSARY reference defines vocabulary. | Reuse as authoring review, validate harness-specific disable-model-invocation semantics and benchmark pruning claims rather than assuming them. |

Prefix `mattpocock--skills/skills/misc` (not registered in plugin).

| Skill | Purpose/input/output/side effect | Disposition |
|---|---|---|
| git-guardrails-claude-code | Scope choice → copied executable Bash PreToolUse hook + merged Claude settings; tests blocked push. Script reads JSON with jq and matches command regexes. | Optional adaptation, not a security boundary: lexical matcher is not shell parsing; blocks all pushes, can misclassify/miss syntactic variants. Never replace actual permission system. |
| migrate-to-shoehorn | Test assertions → installed @total-typescript/shoehorn dependency and migrated fromPartial/fromAny/fromExact test data, typecheck. | Narrow opt-in only where team uses that library; not generic requirement or production-code pattern. |
| scaffold-exercises | Course plan → ai-hero exercise/problem/solution/explainer folders, lint and commit. | Exclude from shared engineering MVP; highly course-specific. |
| setup-pre-commit | Existing package-manager config → Husky/lint-staged/Prettier dependencies/config, hook running formatting/typecheck/tests, then commit. | Configure existing checks instead of installing redundant hooks; broad staging and full-test-per-commit cost need adaptation. |

Prefix `mattpocock--skills/skills/personal`.

| Skill | Purpose/input/output/side effect | Disposition |
|---|---|---|
| edit-article | Article → agreed section ordering then prose edits, maximum 240 characters per paragraph. | Personal writing choice, not engineering policy. |
| obsidian-vault | Search/create/link notes at hardcoded /mnt/d/Obsidian Vault/AI Research, flat title-case wiki. | Do not copy location/taxonomy. Use existing owner/index. |

Prefix `mattpocock--skills/skills/in-progress` (README explicitly says not ready to ship).

| Skill | Purpose/input/output/side effect | Disposition |
|---|---|---|
| decision-mapping | Loose idea → compact dependency map of Research/Prototype/Discuss tickets; bootstrap stops before solving, resume resolves one and updates consequences. | Concept useful for unresolved discovery, but prefer GitHub epic/issue structure. Refers to nonexistent spelling /domain-modelling; 100K-session size is heuristic. |
| review | Fixed ref + spec/standards → parallel independent Standards and Spec reports, no fixing. Uses three-dot committed diff and stops on empty diff. | Reuse two axes after adaptation; advertised WIP coverage does not include unstaged edits in HEAD comparison. Missing fixed-point input and unregistered dependency matter. |
| writing-beats | Raw material → user-chosen sequential beats in article; rereads before each write, stops per choice. | Optional authoring method, not delivery. |
| writing-fragments | Interview → silently appended raw fragments, reread/preserve user edits, no structure. | Optional ideation only; fragments are not decisions/approved scope. |
| writing-shape | Read-only source pile → separate collaboratively shaped article, paragraph-by-paragraph updates. | Optional authoring; not a system-doc refresh workflow by itself. |

Prefix `mattpocock--skills/skills/deprecated` (README: no longer used).

| Skill | Purpose/input/output/side effect | Disposition |
|---|---|---|
| design-an-interface | Requirements → 3+ alternative interfaces, comparison, no implementation. | Reuse current codebase-design/DESIGN-IT-TWICE instead of duplicate entry. |
| qa | Conversational bug reports → immediate gh issues without prior review, optional split/dependencies, reproduction mandatory, no file paths. | Do not install as default. Triage supersedes much of job; publishing behavior needs explicit scope. |
| request-refactor-plan | Detailed interview + code/tests → GitHub issue with tiny working commits, decisions/scope. | Preserve tiny verified increments concept; use current planning path. |
| ubiquitous-language | Conversation → UBIQUITOUS_LANGUAGE.md glossary/relationships/ambiguities, updates on rerun. | Superseded by domain-modeling; don't create competing glossary. |

## HumanLayer published RPI families

Prefix `humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills`. All bodies are task-environment recipes, usually explicit-invocation descriptions; presence in source is not proof a standalone host has agents/hooks/artifact storage.

| Skill/family | Input → output and behavior | Recommendation |
|---|---|---|
| create-research-questions / iterate-research-questions | Ticket/user pointers → numbered current-state questions; writes/revises same task artifact; specialized research agents; preserves exact URLs/packages/paths; frontend prompts include design system. | Adapt query-plan method, retain source pointers and keep proposed solution out of factual investigation. |
| create-research / iterate-research | Questions/current research → source-referenced technical narrative and testing map. Avoids ticket/design contamination, no unsolicited improvement/root cause. Create has one additional gap pass; iterate permits external research only when asked. | Strong method reuse; adapt host roles and existing docs placement; current-state facts remain revision-stamped. Research template status complete can coexist with open questions, so qualify completeness. |
| create-design-discussion / iterate-design-discussion | Research/request → current/desired state, alternatives, recommended but initially OPEN design questions; explicit user feedback resolves; patches original artifact. | Strong decision-authority model; adapt iteration to asynchronous review and newer decision precedence. |
| create-prd / iterate-prd | Product inputs → problem, success lever, solution/mockups, scope; product-only interview, only resolved decisions flushed, final whole-solution review; iterate explicitly stops after each change. | High-value adaptation for draft epic and measurable outcome; avoid excessive question cadence for authorized batches. |
| create-tdd / iterate-tdd | Available product context (PRD optional) → Technical Design Document, first cross-system design then program shape, separate sign-off gates, diagrams/contracts; updates PRD if technical choice changes product. | Adapt for consequential architecture choices. TDD here is not test-driven development. Keep known facts, proposed design and accepted decisions explicit. |
| create-structure-outline / iterate-structure-outline | Research and decisions → independently verifiable vertical phases with concise structural deltas/checklists. Treat follow-up as document edits, not implicit implementation. | Strong reuse of phase contracts; map phases to GH issues and repo ownership instead of parallel task tracker. Relevant layer qualification is explicit here. |
| create-plan / iterate-plan | Outline/feedback → detailed code examples and runnable checks, optional manual criteria, same-path revision. Disabled workspace configuration can trigger git checkout -b even in planning. | Use only when detail earns cost; decouple branch mutation from documentation and preserve current branch/user work. |
| implement-outline | Outline/companions → per-phase delegated code, automated checks, human confirmation, commits, updated outline. Multiple phases can be expressly authorized. | Adapt runtime and verification, not direct copy. Conflicting implementer names, old filename patterns and document precedence require resolution. |
| implement-plan | Plan → delegated phase implementation, orchestration checks, manual confirmation and commits. Resumes checked items as trusted unless suspicious. | Adapt evidence freshness and standing authorization. No deployment proof from checked boxes. |
| iterate-implementation | Feedback + code/diff/history/artifacts → fixes/tests/lint; unstarted phase delegates; may add logs and ask reproduction. | Useful aftercare model, preserve scope and repository data-access limits. |
| ci-commit | Session changes → logical planned commits, explicit file staging, avoids rpi/dummy files. Text says execute upon confirmation yet also never stop for feedback. | Adapt to actual authorization; correct stale rpi exclusion to current task artifact ownership. |
| configure-workspaces | Repo evidence → approved shared/local JSON, validation of repo/remotes, gitignore local config, optional staging shared config. Supports multi-repo primary, setup and additive copy globs. | Reference model only for this runtime; Flex already has canonical submodule ownership and must retain it. |
| setup-worktree | Task/config → branches/worktrees, copies matching local/env files, runs setup commands. Disabled mode still creates branch. | Host-specific; use existing Codex/canonical checkout facilities. Fix primary/copy merge semantics contradiction first. |
| describe-pr | Task/diff → commit/push/create/update PR, structural description/session trailer, CI watch/fix/rerun. | Do not expose as harmless writing skill. Adapt explicit publication scope, verification summary and no unrequested CI mutation. |
| review-artifact-comments | Artifact + MCP comments/user direction → document edits and optionally replies/resolve/delete; asks unless already instructed. | Reuse distinction between applying feedback and resolving comments. Teams/GH adapters need explicit author/decision provenance and messaging authorization. |

Runtime evidence: `apps/riptide-daemon/src/plugins/bundled-rpi-plugin.ts` embeds RPI skill bodies and references; specialized agents live in daemon source, not the RPI plugin directory: `apps/riptide-daemon/src/agents/claudecode/agents/{outline-implementer-agent,implementer-agent}.ts`. Outline agent inherits model and enforces human-confirmed manual validation; plan agent hardcodes sonnet and still describes `thoughts/shared/plans/` while skills use `.humanlayer/tasks/`. Thus copying Markdown is insufficient.

Pi prefix `humanlayer--humanlayer/apps/riptide-pi-extension/skills`: create/iterate research questions, research, design discussion, PRD, structure outline, implement-plan, implement-outline and iterate-implementation bodies are identical to corresponding RPI files. `create-tech-design` / `iterate-tech-design` rename create/iterate-tdd and their reference filenames. `describe-pr` retains publication but lacks Claude's CI step. `show-me` is identical to the HumanLayer-plugin body. These account for all 17 Pi SKILL.md files.

HumanLayer plugin prefix `humanlayer--humanlayer/apps/riptide-humanlayer-claude-plugin/skills`:

| Skill | Input/output/side effects | Recommendation |
|---|---|---|
| show-me | Current topic → smallest useful pseudocode/tree/Mermaid/diff/HTML; optional task HTML file, no prescribed publishing. | Reuse visual communication method; adapt viewer and artifact placement. |
| orchestrate | Job → HumanLayer CLI references for login/host/tasks/sessions/auto-advance/PR/artifact operations. Can launch worktrees/sessions, upload/copy/move/delete synced artifacts. Defaults to prod without flag. | Runtime-specific, not shared generic engineering workflow. launch-task reference explicitly offers freeform/oneshot, so RPI is not one mandatory sequence. |
| teleport | Current task/host choice → commit/push, remote provisioning/install/login, approved secret-file copying, daemon, new session and handoff; must wait for actual launch state, not just saved ID. | Exclude from initial adoption; broad remote operational authority. Reuse handoff + launch evidence distinction only. |

## HumanLayer internal skills

Prefix `humanlayer--humanlayer/.claude/skills` (29 bodies including nested local-cli-testing).

| Skill | Purpose/input/output/side effects | Recommendation |
|---|---|---|
| agent-browser | Browser task → snapshot/action/resnapshot, captures, extracts, submits forms, persistent sessions; CLI/Chrome installs, optional policies, state files. | Prefer existing browser capability; adapt isolation and credential behavior. Read auth reference: it contradicts body's claim session-name excludes cookies. Not a tested browser contract. |
| chrome-devtools-cli | Browser task → direct persistent CLI automation, screenshots/network/performance traces; referenced global installation prerequisite. | Existing browser tooling first; do not introduce alternate runtime by default. |
| asd-ste100 | Dense text → rule-annotated before/after rewrite, preserves qualifiers, explicitly not certified full STE dictionary compliance. | Reuse clarity method selectively for operational text, not all voice. |
| better-github-skill | PR state/review conversation/CI failures → intended compact reports through Bun scripts; explicitly read-only threads. | Valuable capability distinction, but scripts pr-snapshot.ts, pr-threads.ts, ci-failures.ts absent from tracked checkout. Use available GH connector/CLI or implement verified equivalent, don't claim ready reuse. |
| bump-version | Named HumanLayer package → synchronized base versions, commit/derive/verify/push; post-merge beta/prod workflows in private release repo. | Exclude: release mechanism and policies are owner-specific, external publication. |
| calldiff | Refs/entrypoints → structural call graph diff/reach/tree, global latest install if missing. | Optional tool trial on controlled repo; tool output is static structure, not observed runtime. |
| codebase-design | Matt vocabulary body with formatting-only differences. | Count shared method once; same adaptation notes. |
| effect-program-design | Effect v4 feature/refactor → typed deep services/errors/config/resources/test patterns; checks installed versions, local conventions first; many topic references. | Stack-specific opt-in; preserve real-seam tests and capture-before-narrow errors, not mandatory stack migration. |
| grill-me | Inline one-question interview, recommended answer and codebase exploration. | Same interview method as Matt, not independent innovation; adapt async. |
| grind-design-discussion | Existing design → verifies assumptions/patterns, adds options/questions, updates research, cannot resolve questions or change resolved decisions/scope. | Strong candidate for autonomous useful work while awaiting decisions. Adapt roles/paths, keep approvals separate. |
| grind-research | Existing research → deeper code/web evidence, corrections, resolved gaps; splits >1000-line docs autonomously. | Good freshness method, but route splits to existing owner/index and avoid automatic taxonomy changes. |
| html-demo-video-guidelines | Product footage/voice → prescriptive HTML-motion demo + vertical cut; particular person's taste and voice-clone settings, keeps feedback in skill. | Exclude from engineering baseline; specific creator/media workflow, not reusable team policy. |
| html-mockups | UI request → single self-contained HTML task artifact, Poimandres monospace/uppercase style. | Reuse self-contained artifact constraint; replace branding and conflict with ui-copy. |
| improve-codebase-architecture | Matt workflow plus recent-change hotspots to scope scanning; report then selected design/doc changes. | Useful scoped freshness improvement; missing local HTML scaffold and grilling/domain skills prevent clean standalone reuse. |
| improve-writing | Prose critique → preserve writer's specificity/voice, remove symmetry/summary taps, personal essay examples. | Optional writing reference, do not imitate author or import as corporate voice. |
| merge-resolve-conflicts | Fetch/default-branch merge + per-conflict analysis and user resolution approval; asks commit/push at end; dirty work prompts stash/commit. | Adapt informed merge plan, selected repo and preserve-user-work behavior. More conservative than Matt conflict body; don't install competing defaults. |
| migrate-orpc-to-effect | Eligible single procedure → equivalent Effect base/auth/contract, new .effect.ts/router update, original deletion; typecheck/quality, CI tests only. | Highly local migration pattern. Inconsistent with generic bounded-concurrency policy (example unbounded), and no-local-tests rule needs current infra verification. |
| narrow-react-prop-types | Production call sites → stricter real prop contract; updates variants/tests/stories and consumer typechecks, removes impossible fallbacks. | Strong scoped adaptation; verify all actual consumers before declaring a state unsupported. |
| no-use-effect | React effect → derived state/query/event/key/useMountEffect replacements, typechecks/tests. | Reuse unnecessary-effect diagnostic, not absolute ban: bundled React article explicitly allows effects for external synchronization. Mounted-only replacement can alter reactive semantics. |
| react-doctor | React diff → latest CLI scan, regression fixes; full mode fetches mutable external playbook and edits working tree, no commit. | Optional version-pinned controlled evaluation, not guaranteed stable behavior from source revision. |
| rebase-drizzle-migration | Diverged migrations → checkout upstream, migrate DB, delete branch artifacts/restore journal, user DB reset, regenerate/apply checks. | Do not reuse wholesale; destructive/local DB assumptions, current schema authority and data preservation must be verified per owner. |
| show-me-the-components | React topic → concise component/hook/package ownership tree. | Reuse as view inside broader show-me, not extra overlapping skill. |
| storybook | UI component/story work → Pure/ShellDemo/Wired taxonomy, real production components, no providers/wired stories, deletes mockups, local ports. | Adapt production-realism principle, not mandatory naming/composition/deletion policy. |
| stripe-billing-verification | Local webhook/lifecycle task → Stripe forwarding/events/Test Clock objects, logs and DB/provider inspection; public endpoint setup human-confirmed. | Opt-in domain test recipe. Reference explicitly distinguishes intake acknowledgement from billing effects and test mode from real environment. |
| subagent-orchestrator | Complex task → delegates all nontrivial research/bash to named agents, avoids overlap. | Adapt proportional delegation to available host; not independent runtime or universally efficient policy. |
| sync/durable-streams-yjs | CRDT integration → DurableStreamsProvider lifecycle/streams/auth patterns, peer deps and binary framing, target v0.2.1. | Narrow reference; missing linked reading-streams skill, useEffect example conflicts with local ban, verify installed library. |
| test-it-locally | Riptide changed behavior → inspect/sync devstack (containers/migrations/seeds), tmux app, isolated browser/profile, sandbox login, exact flow + stored state, tasks/sessions via CLI. | Excellent verification-method example; cannot transplant services/credentials/ports/provider writes. |
| test-it-locally/references/local-cli-testing | Local CLI login → task/artifact/session writes and SQL inspection, bypass-mode sample. | Nested reference, not independent general capability; fixed routes/env parsing drift from parent. |
| ui-copy | Existing/new user-visible strings → humane actionable copy, glossary/status maps; mechanical fixes versus judgment, no bulk voice rewrites. | Reuse minimal-defect editing and user-outcome framing; replace HumanLayer glossary and metrics vocabulary. |

## Contradictions and dependency evidence worth retaining

- Matt setup says configure tracker names, but to-prd literally names ready-for-agent; label mapping must actually be honored, not assumed.
- Matt codebase-design deletion test says disappearing complexity indicates pass-through; improve-codebase-architecture's wording about deletion “concentrating” is less precise. Test the decision, don't turn language into a metric.
- Matt review compares `<fixed-point>...HEAD`, then implement calls review before committing. Uncommitted implementation can therefore be invisible to the called reviewer. This is a concrete integration bug candidate in source instructions, not behavioral-test proof.
- HumanLayer create/iterate artifacts preserve same-path edits rather than append history; this directly fits avoiding stale prose. Keep accepted rationale in existing decisions rather than treating task transcripts as permanent system truth.
- HumanLayer create-plan and iterate-plan can mutate branch under disabled worktrees; setup-worktree can copy .env* and run arbitrary configured setup. These are real side effects even though filenames sound preparatory.
- HumanLayer implement-outline matches `*-structure-outline.md` / `*-research.md` whereas creators write `NN-structure-outline-DESCRIPTION.md` / `NN-research-DESCRIPTION.md`; its examples also use older date names. Resolve discovery convention before porting.
- RPI PR template still includes PR Walkthrough alpha placeholder, whereas describe-pr forbids adding walkthrough artifacts; strip unavailable links rather than inventing them. It also forbids verification checklists; Flex reviewer-useful validation should remain available in appropriate PR format.
- RPI ci-commit excludes old rpi/ while phase implementations exclude .humanlayer/tasks (symlink another repo). Generic exclusion name is insufficient; resolve owning Git root before staging.
- HumanLayer local architecture copy carries Matt semantics but omits supporting local dependencies. Bundling a skill means following references and runtime, not copying its name.
- HumanLayer `orchestrate/references/launch-task.md` explicitly supports GitHub ticket filenames and multi-repo saved projects, beyond the RPI README's Linear-only description. README alone understates source capability.
- HumanLayer `orchestrate/references/managing-artifacts-and-files.md` says move = hash-verified copy then tombstone; deletion removes files on every host. This is not a local file-organizing helper.

## Draft rubric (scored only for reviewed Matt/HumanLayer claims and shared synthesis)

| Dimension | Score | Evidence and repair |
|---|---:|---|
| Citation integrity | 3 | Exact span: “Sources: [[artifacts/plugins/mattpocock-skills]], [[sources/mattpocock--skills]]. Direct bodies…” and equivalent HumanLayer paragraph. These are real roots but do not meet rubric's non-obvious-claim anchor requirement. Add specific source anchors per load-bearing claim; extend anchor map for new registration/variant findings. |
| Faithfulness | 4 | Core interpretations match bodies, and draft candidly limits coverage/testing. Qualify “The central path … implementation and review” with manifest absence and uncommitted-diff flaw. “PR description” undersells commit/push/CI side effects. |
| Completeness | 3 | Exact span: “The repository also includes internal development skills and a Pi extension; those are not additional independent RPI workflow stages.” Correct but omits meaningful Pi describe-pr CI delta, internal stale/missing dependency evidence, business-success requirements and multi-repo configuration. Add these material counterexamples. |
| Non-genericness | 5 | Concrete readiness labels, document precedence, domain glossary, vertical slices and test scenarios are specific and useful. |
| Decision usefulness | 4 | Candidate adaptation plan is credible; elevate existing HumanLayer success-metric and grind-review contracts, clarify availability before first trial, specify GH draft/approved owner and Teams async boundaries. |

Lowest score 3: not a pass. Same-family review cannot satisfy cross-family gate even after corrections. No behavioral benefit claims should be added until representative evaluations run.

## Recommended smallest composition to evaluate

Use one clarification method; draft GitHub epic with scope and success evidence; HumanLayer-style factual research and open decision review where warranted; Matt-style approved vertical issues; existing implementation/review capabilities with working-tree-aware diff; targeted verification of actual observable behavior; GH-linked Teams update only when publishing is authorized; update existing owner docs and progress log. Retain separate approval, implementation, merge, deployment and business-outcome states. Do not add new global workspace scaffolding, parallel tracker, automatic remote infrastructure or mandatory interview on small fixes.


Related: [adoption study](engineering-skill-adoption-study.md) · [full catalogue](engineering-skill-catalogue.md).
