---
domain: analyses
type: reference
status: draft
last-reviewed: 2026-10-27
---

# Engineering and product skill catalogue

Source inventory, not proof of runtime behavior. Read the [study](engineering-skill-adoption-study.md) and its detailed reviews for semantic findings. Each entry links the actual local body; open-repository descriptions and headings are attributed excerpts. Purchased-package bodies are not reproduced. Source revisions and hashes are in [the inventory](engineering-skill-inventory.json).

281 repository paths plus 235 purchased-package paths. Counts include aliases, internal skills and runtime variants; they are not 516 independent capabilities. Test fixtures, Anthropic template and Pstack generated harness copy excluded.

## mattpocock--skills

34 skill paths at `6eeb81b5fcfeeb5bd531dd47ab2f9f2bbea27461`.

### design-an-interface

[Read source](../sources/mattpocock--skills/skills/deprecated/design-an-interface/SKILL.md) · deprecated · 94 lines

Source description: Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice".

Section preview: Workflow; 1. Gather Requirements; 2. Generate Designs (Parallel Sub-Agents); 3. Present Designs; 4. Compare Designs; 5. Synthesize; Evaluation Criteria; Anti-Patterns

### qa

[Read source](../sources/mattpocock--skills/skills/deprecated/qa/SKILL.md) · deprecated · 130 lines

Source description: Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".

Section preview: For each issue the user raises; 1. Listen and lightly clarify; 2. Explore the codebase in the background; 3. Assess scope: single issue or breakdown?; 4. File the GitHub issue(s); What happened; What I expected; Steps to reproduce; Additional context; Parent issue; What's wrong; What I expected …

### request-refactor-plan

[Read source](../sources/mattpocock--skills/skills/deprecated/request-refactor-plan/SKILL.md) · deprecated · 68 lines

Source description: Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refactor, create a refactoring RFC, or break a refactor into safe incremental steps.

Section preview: Problem Statement; Solution; Commits; Decision Document; Testing Decisions; Out of Scope; Further Notes (optional)

### ubiquitous-language

[Read source](../sources/mattpocock--skills/skills/deprecated/ubiquitous-language/SKILL.md) · deprecated · 93 lines

Source description: Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE.md. Use when user wants to define domain terms, build a glossary, harden terminology, create a ubiquitous language, or mentions "domain model" or "DDD".

Section preview: Process; Output Format; Order lifecycle; People; Relationships; Example dialogue; Flagged ambiguities; Rules; Example dialogue; Re-running

### ask-matt

[Read source](../sources/mattpocock--skills/skills/engineering/ask-matt/SKILL.md) · published skill source · 61 lines

Source description: Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.

Section preview: The main flow: idea → ship; Context hygiene; On-ramps; Codebase health; Crossing sessions; Standalone; Precondition

### codebase-design

[Read source](../sources/mattpocock--skills/skills/engineering/codebase-design/SKILL.md) · published skill source · 114 lines

Source description: Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.

Section preview: Glossary; Deep vs shallow; Principles; Designing for testability; Relationships; Rejected framings; Going deeper

### diagnosing-bugs

[Read source](../sources/mattpocock--skills/skills/engineering/diagnosing-bugs/SKILL.md) · published skill source · 134 lines

Source description: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.

Section preview: Phase 1 — Build a feedback loop; Ways to construct one — try them in roughly this order; Tighten the loop; Non-deterministic bugs; When you genuinely cannot build a loop; Completion criterion — a tight loop that goes red; Phase 2 — Reproduce + minimise; Minimise; Phase 3 — Hypothesise; Phase 4 — Instrument; Phase 5 — Fix + regression test; Phase 6 — Cleanup + post-mortem

### domain-modeling

[Read source](../sources/mattpocock--skills/skills/engineering/domain-modeling/SKILL.md) · published skill source · 74 lines

Source description: Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model.

Section preview: File structure; During the session; Challenge against the glossary; Sharpen fuzzy language; Discuss concrete scenarios; Cross-reference with code; Update CONTEXT.md inline; Offer ADRs sparingly

### grill-with-docs

[Read source](../sources/mattpocock--skills/skills/engineering/grill-with-docs/SKILL.md) · published skill source · 7 lines

Source description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.

### implement

[Read source](../sources/mattpocock--skills/skills/engineering/implement/SKILL.md) · published skill source · 15 lines

Source description: Implement a piece of work based on a PRD or set of issues.

### improve-codebase-architecture

[Read source](../sources/mattpocock--skills/skills/engineering/improve-codebase-architecture/SKILL.md) · published skill source · 66 lines

Source description: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.

Section preview: Process; 1. Explore; 2. Present candidates as an HTML report; 3. Grilling loop

### prototype

[Read source](../sources/mattpocock--skills/skills/engineering/prototype/SKILL.md) · published skill source · 31 lines

Source description: Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.

Section preview: Pick a branch; Rules that apply to both; When done

### resolving-merge-conflicts

[Read source](../sources/mattpocock--skills/skills/engineering/resolving-merge-conflicts/SKILL.md) · published skill source · 14 lines

Source description: Use when you need to resolve an in-progress git merge/rebase conflict.

### setup-matt-pocock-skills

[Read source](../sources/mattpocock--skills/skills/engineering/setup-matt-pocock-skills/SKILL.md) · published skill source · 127 lines

Source description: Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.

Section preview: Process; 1. Explore; 2. Present findings and ask; 3. Confirm and edit; 4. Write; Agent skills; Issue tracker; Triage labels; Domain docs; 5. Done

### tdd

[Read source](../sources/mattpocock--skills/skills/engineering/tdd/SKILL.md) · published skill source · 108 lines

Source description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.

Section preview: Philosophy; Anti-Pattern: Horizontal Slices; Workflow; 1. Planning; 2. Tracer Bullet; 3. Incremental Loop; 4. Refactor; Checklist Per Cycle

### to-issues

[Read source](../sources/mattpocock--skills/skills/engineering/to-issues/SKILL.md) · published skill source · 84 lines

Source description: Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices.

Section preview: Process; 1. Gather context; 2. Explore the codebase (optional); 3. Draft vertical slices; 4. Quiz the user; 5. Publish the issues to the issue tracker; Parent; What to build; Acceptance criteria; Blocked by

### to-prd

[Read source](../sources/mattpocock--skills/skills/engineering/to-prd/SKILL.md) · published skill source · 75 lines

Source description: Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.

Section preview: Process; Problem Statement; Solution; User Stories; Implementation Decisions; Testing Decisions; Out of Scope; Further Notes

### triage

[Read source](../sources/mattpocock--skills/skills/engineering/triage/SKILL.md) · published skill source · 112 lines

Source description: Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.

Section preview: Reference docs; Roles; Invocation; Show what needs attention; Triage a specific issue or PR; Quick state override; Needs-info template; Triage Notes; Resuming a previous session

### decision-mapping

[Read source](../sources/mattpocock--skills/skills/in-progress/decision-mapping/SKILL.md) · in progress · 84 lines

Source description: Turn a loose idea into a sequenced map of investigation tickets, then drive them to resolution one at a time.

Section preview: The Decision Map; Structure; 1: Relational Or Non-Relational Database?; Question; Answer; Ticket Types; Fog of war; Invocation; Bootstrap; Resume; Parallelism; Skipping The Decision Map

### review

[Read source](../sources/mattpocock--skills/skills/in-progress/review/SKILL.md) · in progress · 69 lines

Source description: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".

Section preview: Process; 1. Pin the fixed point; 2. Identify the spec source; 3. Identify the standards sources; 4. Spawn both sub-agents in parallel; 5. Aggregate; Why two axes

### writing-beats

[Read source](../sources/mattpocock--skills/skills/in-progress/writing-beats/SKILL.md) · in progress · 52 lines

Source description: Shape an article as a journey of beats, choose-your-own-adventure style. The user picks a starting beat from the raw material, you write only that beat, then offer options for where to pivot next, beat by beat, until the article reaches a natural end. Use when the user has raw material and wants to assemble it as a narrative rather than an argument.

Section preview: What is a beat; Writing one beat; Ending the journey; Writing rhythm

### writing-fragments

[Read source](../sources/mattpocock--skills/skills/in-progress/writing-fragments/SKILL.md) · in progress · 75 lines

Source description: Grilling session that mines the user for fragments — heterogeneous nuggets of writing (claims, vignettes, sharp sentences, half-thoughts) — and appends them to a single document as raw material for a future article. Use when the user wants to develop ideas before imposing structure, or mentions "fragments", "ideate", or "raw material" for writing.

Section preview: What is a fragment; File format; Writing rhythm

### writing-shape

[Read source](../sources/mattpocock--skills/skills/in-progress/writing-shape/SKILL.md) · in progress · 64 lines

Source description: Take a markdown file of raw material and shape it into an article through a conversational session — drafting candidate openings, growing the piece paragraph by paragraph, arguing about format (lists, tables, callouts, quotes) at each step. Use when the user has a pile of notes, fragments, or a rough draft and wants help turning it into something publishable.

Section preview: The loop; Conversational feel; Pulling from the pile; Format arguments to actually have; Writing rhythm; Out of scope

### git-guardrails-claude-code

[Read source](../sources/mattpocock--skills/skills/misc/git-guardrails-claude-code/SKILL.md) · published skill source · 95 lines

Source description: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.

Section preview: What Gets Blocked; Steps; 1. Ask scope; 2. Copy the hook script; 3. Add hook to settings; 4. Ask about customization; 5. Verify

### migrate-to-shoehorn

[Read source](../sources/mattpocock--skills/skills/misc/migrate-to-shoehorn/SKILL.md) · published skill source · 118 lines

Source description: Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.

Section preview: Why shoehorn?; Install; Migration patterns; Large objects with few needed properties; `as Type` → `fromPartial()`; `as unknown as Type` → `fromAny()`; When to use each; Workflow

### scaffold-exercises

[Read source](../sources/mattpocock--skills/skills/misc/scaffold-exercises/SKILL.md) · published skill source · 106 lines

Source description: Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.

Section preview: Directory naming; Exercise variants; Required files; Workflow; Lint rules summary; Moving/renaming exercises; Example: stubbing from a plan

### setup-pre-commit

[Read source](../sources/mattpocock--skills/skills/misc/setup-pre-commit/SKILL.md) · published skill source · 91 lines

Source description: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.

Section preview: What This Sets Up; Steps; 1. Detect package manager; 2. Install dependencies; 3. Initialize Husky; 4. Create `.husky/pre-commit`; 5. Create `.lintstagedrc`; 6. Create `.prettierrc` (if missing); 7. Verify; 8. Commit; Notes

### edit-article

[Read source](../sources/mattpocock--skills/skills/personal/edit-article/SKILL.md) · published skill source · 15 lines

Source description: Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.

### obsidian-vault

[Read source](../sources/mattpocock--skills/skills/personal/obsidian-vault/SKILL.md) · published skill source · 59 lines

Source description: Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian.

Section preview: Vault location; Naming conventions; Linking; Workflows; Search for notes; Create a new note; Find related notes; Find index notes

### grill-me

[Read source](../sources/mattpocock--skills/skills/productivity/grill-me/SKILL.md) · published skill source · 7 lines

Source description: A relentless interview to sharpen a plan or design.

### grilling

[Read source](../sources/mattpocock--skills/skills/productivity/grilling/SKILL.md) · published skill source · 10 lines

Source description: Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.

### handoff

[Read source](../sources/mattpocock--skills/skills/productivity/handoff/SKILL.md) · published skill source · 16 lines

Source description: Compact the current conversation into a handoff document for another agent to pick up.

### teach

[Read source](../sources/mattpocock--skills/skills/productivity/teach/SKILL.md) · published skill source · 140 lines

Source description: Teach the user a new skill or concept, within this workspace.

Section preview: Teaching Workspace; Philosophy; Fluency vs Storage Strength; Lessons; Assets; The Mission; Zone Of Proximal Development; Knowledge; Skills; Acquiring Wisdom; Reference Documents; `NOTES.md`

### writing-great-skills

[Read source](../sources/mattpocock--skills/skills/productivity/writing-great-skills/SKILL.md) · published skill source · 82 lines

Source description: Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.

Section preview: Invocation; Writing the description; Information hierarchy; When to split; Pruning; Leading words; Failure modes


## every--compound-engineering-plugin

39 skill paths at `3e77a7bd8450fef7270f8b46c0f1865fd7125741`.

### coding-tutor

[Read source](../sources/every--compound-engineering-plugin/plugins/coding-tutor/skills/coding-tutor/SKILL.md) · published skill source · 214 lines

Source description: Personalized coding tutorials that build on your existing knowledge and use your actual codebase for examples. Creates a persistent learning trail that compounds over time using the power of AI, spaced repetition and quizes.

Section preview: Welcome New Learners; Setup: Ensure Tutorials Repo Exists; First Step: Know Your Learner; Teaching Philosophy; Tutorial Creation; Q&A; Quiz History; Tutorial Writing Style; The Living Tutorial; What Makes Great Teaching; Quiz Mode; Quiz - DD-MM-YYYY

### ce-agent-native-architecture

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-agent-native-architecture/SKILL.md) · published skill source · 87 lines

Source description: Build applications where agents are first-class citizens. Use this skill when designing autonomous agents, creating MCP tools, implementing self-modifying systems, or building apps where features are outcomes achieved by agents operating in a loop.

Section preview: Agent-Native Architecture; What aspect of agent-native architecture do you need help with?; Reference Files

### ce-agent-native-audit

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-agent-native-audit/SKILL.md) · published skill source · 278 lines

Source description: Run comprehensive agent-native architecture review with scored principles

Section preview: Core Principles to Audit; Workflow; Step 1: Load the Agent-Native Skill; Step 2: Launch Parallel Sub-Agents; Action Parity Audit; User Actions Found; Score: X/Y (percentage%); Missing Agent Tools; Recommendations; Tools as Primitives Audit; Tool Analysis; Score: X/Y (percentage%) …

### ce-brainstorm

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-brainstorm/SKILL.md) · published skill source · 271 lines

Source description: Explore requirements and approaches through collaborative dialogue, then write a right-sized requirements document. Use when the user says "let''s brainstorm", "what should we build", or "help me think through X", presents a vague or ambitious feature request, or seems unsure about scope or direction -- even without explicitly asking to brainstorm.

Section preview: Core Principles; Interaction Rules; Output Guidance; Feature Description; Execution Flow; Phase 0: Resume, Assess, and Route; Phase 1: Understand the Idea; Phase 2: Explore Approaches; Phase 2.5: Synthesis Summary; Phase 3: Capture the Requirements; Phase 4: Handoff

### ce-clean-gone-branches

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-clean-gone-branches/SKILL.md) · published skill source · 63 lines

Source description: Clean up local branches whose remote tracking branch is gone. Use when the user says "clean up branches", "delete gone branches", "prune local branches", "clean gone", or wants to remove stale local branches that no longer exist on the remote. Also handles removing associated worktrees for branches that have them.

Section preview: Workflow; Step 1: Discover gone branches; Step 2: Present branches and ask for confirmation; Step 3: Delete confirmed branches

### ce-code-review

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-code-review/SKILL.md) · published skill source · 898 lines

Source description: Structured code review using tiered persona agents, confidence-gated findings, and a merge/dedup pipeline. Use when reviewing code changes before creating a PR.

Section preview: When to Use; Argument Parsing; Quick Review Short-Circuit; Mode Detection; Autofix mode rules; Report-only mode rules; Headless mode rules; Interactive mode rules; Severity Scale; Action Routing; Reviewers; Review Scope …

### ce-commit-push-pr

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-commit-push-pr/SKILL.md) · published skill source · 135 lines

Source description: Commit, push, and open a PR with an adaptive, value-first description that scales in depth with the change. Use when the user says "commit and PR", "ship this", "create a PR", or "open a pull request". Also handles description-only flows ("write a PR description", "rewrite the PR body", "describe this PR") without committing or pushing.

Section preview: Mode; Context; Context fallback; Step 1: Resolve branch and PR state; Step 2: Determine conventions; Step 3: Commit and push; Step 4: Compose the PR title and body; Step 5: Apply and report; Applying via gh

### ce-commit

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-commit/SKILL.md) · published skill source · 105 lines

Source description: Create a git commit with a clear, value-communicating message. Use when the user says "commit", "commit this", "save my changes", "create a commit", or wants to commit staged or unstaged work. Produces well-structured commit messages that follow repo conventions when they exist, and defaults to conventional commit format otherwise.

Section preview: Context; Context fallback; Workflow; Step 1: Gather context; Step 2: Determine commit message convention; Step 3: Consider logical commits; Step 4: Stage and commit; Step 5: Confirm

### ce-compound-refresh

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-compound-refresh/SKILL.md) · published skill source · 634 lines

Source description: Refresh stale learning and pattern docs under docs/solutions/ by reviewing them against the current codebase, then updating, consolidating, or deleting drifted ones. Use when the user asks to "refresh my learnings", "audit docs/solutions/", "clean up stale learnings", or "consolidate overlapping docs", or when ce-compound flags an older doc as superseded. Do not trigger for general refactor, debugging, or code-review work unless the user has explicitly pointed at docs/solutions/.

Section preview: Mode Detection; Headless mode rules; Interaction Principles; Refresh Order; Maintenance Model; Core Rules; Scope Selection; Phase 0: Assess and Route; Route by Scope; Broad Scope Triage; Phase 1: Investigate Candidate Learnings; Drift Classification: Update vs Replace …

### ce-compound

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-compound/SKILL.md) · published skill source · 583 lines

Source description: Document a recently solved problem to compound your team's knowledge

Section preview: Purpose; Usage; Mode Detection; Pre-resolved context; Support Files; Execution Strategy; Full Mode; Phase 0.5: Auto Memory Scan; Supplementary notes from auto memory; Phase 1: Research; Phase 2: Assembly & Write; Phase 2.5: Selective Refresh Check …

### ce-debug

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-debug/SKILL.md) · published skill source · 252 lines

Source description: Systematically find root causes and fix bugs. Use when debugging errors, investigating test failures, reproducing bugs from issue trackers (GitHub, Linear, Jira), or when stuck on a problem after failed fix attempts. Also use when the user says ''debug this'', ''why is this failing'', ''fix this bug'', ''trace this error'', or pastes stack traces, error messages, or issue references.

Section preview: Core Principles; Execution Flow; Phase 0: Triage; Phase 1: Investigate; Phase 2: Root Cause; Phase 3: Fix; Phase 4: Handoff; Debug Summary

### ce-demo-reel

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-demo-reel/SKILL.md) · published skill source · 184 lines

Source description: Capture a visual demo reel (GIF, terminal recording, screenshots) for PR descriptions. Use when shipping UI changes, CLI features, or any work with observable behavior that benefits from visual proof. Also use when asked to add a demo, record a GIF, screenshot a feature, show what changed visually, create a demo reel, capture evidence, add proof to a PR, or create a before/after comparison.

Section preview: Never Record Secrets; Arguments; Step 0: Discover Capture Target; Step 1: Exercise the Feature; Step 2: Detect Project Type; Step 3: Assess Change Type; Step 4: Tool Preflight; Step 5: Create Run Directory; Step 6: Recommend Tier and Ask User; Step 7: Execute Selected Tier; Step 8: Upload and Approval; Output

### ce-dhh-rails-style

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-dhh-rails-style/SKILL.md) · published skill source · 186 lines

Source description: This skill should be used when writing Ruby and Rails code in DHH's distinctive 37signals style. It applies when writing Ruby code, Rails applications, creating models, controllers, or any Ruby file. Triggers on Ruby/Rails code generation, refactoring requests, code review, or when the user mentions DHH, 37signals, Basecamp, HEY, or Campfire style. Embodies REST purity, fat models, thin controllers, Current attributes, Hotwire patterns, and the "clarity over cleverness" philosophy.

Section preview: Core Philosophy; Naming Conventions; REST Mapping; Ruby Syntax Preferences; Key Patterns; Domain Knowledge

### ce-doc-review

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-doc-review/SKILL.md) · published skill source · 221 lines

Source description: Review requirements or plan documents using parallel persona agents that surface role-specific issues. Use when a requirements document or plan document exists and the user wants to improve it.

Section preview: Interactive mode rules; Phase 0: Detect Mode; Phase 1: Get and Analyze Document; Classify Document Type; Select Conditional Personas; Phase 2: Announce and Dispatch Personas; Announce the Review Team; Build Agent List; Dispatch; Decision primer; Phases 3-5: Synthesis, Presentation, and Next Action; Included References …

### ce-dogfood-beta

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-dogfood-beta/SKILL.md) · published skill source · 187 lines

Source description: [BETA] Dogfood the active branch end-to-end as a QA engineer. Diffs the branch against main, builds an exhaustive browser test matrix of every change (full user journeys, not just features), drives the app with agent-browser, then auto-fixes issues, adds regression tests, and commits each fix until the matrix is green. Use when you want a hands-off 'test everything we just built and make it actually work' pass before shipping.

Section preview: Use `agent-browser` Only For Browser Automation; Prerequisites; Reusing Compound-Engineering Skills; Workflow; Phase 0: Scope and Get on the Right Branch; Resumability (stop and return at any point); Phase 1: Analyze Changes; Phase 2: Map the Flows, Then Build the Matrix; Phase 3: Detect Port and Start the Dev Server; Phase 4: Execute the Matrix; Phase 5: Fix Loop (Autonomous); Phase 6: Write the Report Artifact

### ce-frontend-design

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-frontend-design/SKILL.md) · published skill source · 258 lines

Source description: Build web interfaces with genuine design quality, not AI slop. Use for any frontend work - landing pages, web apps, dashboards, admin panels, components, interactive experiences. Activates for both greenfield builds and modifications to existing applications. Detects existing design systems and respects them. Covers composition, typography, color, motion, and copy. Verifies results via screenshots before declaring done.

Section preview: Authority Hierarchy; Workflow; Layer 0: Context Detection; What to Look For; Mode Classification; Asking the User; Layer 1: Pre-Build Planning; Layer 2: Design Guidance Core; Typography; Color & Theme; Composition; Motion …

### ce-gemini-imagegen

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-gemini-imagegen/SKILL.md) · published skill source · 237 lines

Source description: This skill should be used when generating and editing images using the Gemini API (Nano Banana Pro). It applies when creating images from text prompts, editing existing images, applying style transfers, generating logos with text, creating stickers, product mockups, or any image generation/manipulation task. Supports text-to-image, image editing, multi-turn refinement, and composition from multiple reference images.

Section preview: Default Model; Quick Reference; Default Settings; Available Aspect Ratios; Available Resolutions; Core API Pattern; Custom Resolution & Aspect Ratio; Resolution Examples; Aspect Ratio Examples; Editing Images; Multi-Turn Refinement; Prompting Best Practices …

### ce-ideate

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-ideate/SKILL.md) · published skill source · 400 lines

Source description: Generate and critically evaluate grounded ideas about a topic. Use when asking what to improve, requesting idea generation, exploring surprising directions, or wanting the AI to proactively suggest strong options before brainstorming one in depth. Triggers on phrases like 'what should I improve', 'give me ideas', 'ideate on X', 'surprise me', 'what would you change', or any request for AI-generated suggestions rather than refining the user's own idea.

Section preview: Interaction Method; Focus Hint; Core Principles; Execution Flow; Phase 0: Resume and Scope; Phase 1: Mode-Aware Grounding; Phase 1.5: Topic-Surface Decomposition; Phase 2: Divergent Ideation

### ce-optimize

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-optimize/SKILL.md) · published skill source · 659 lines

Source description: Run metric-driven iterative optimization loops -- define a measurable goal, run parallel experiments, measure each against hard gates or LLM-as-judge scores, keep improvements, and converge on the best solution. Use when optimizing clustering quality, search relevance, build performance, prompt quality, or any measurable outcome that benefits from systematic experimentation.

Section preview: Interaction Method; Input; Optimization Spec Schema; Experiment Log Schema; Quick Start; Persistence Discipline; Core Rules; Mandatory Disk Checkpoints; File Locations (all under `.context/compound-engineering/ce-optimize/<spec-name>/`); On Resume; Phase 0: Setup; 0.1 Determine Input Type …

### ce-plan

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-plan/SKILL.md) · published skill source · 767 lines

Source description: Create structured plans for multi-step tasks -- software features, research workflows, events, study plans, or any goal that benefits from breakdown. Also deepens existing plans with interactive sub-agent review. Use when the user says 'plan this', 'create a plan', 'how should we build', 'break this down', or when a brainstorm doc is ready for planning. Use 'deepen the plan' or 'deepening pass' for the deepening flow. For exploratory requests, prefer ce-brainstorm first.

Section preview: Interaction Method; Feature Description; Core Principles; Plan Quality Bar; Workflow; Phase 0: Resume, Source, and Scope; Phase 1: Gather Context; Phase 2: Resolve Planning Questions; Phase 3: Structure the Plan; Phase 4: Write the Plan; Phase 5: Final Review, Write File, and Handoff

### ce-polish-beta

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-polish-beta/SKILL.md) · published skill source · 89 lines

Source description: [BETA] Start the dev server, open the feature in a browser, and iterate on improvements together.

Section preview: Phase 0: Get on the right branch; Phase 1: Start the dev server; 1.1 Check for `.claude/launch.json`; 1.2 Auto-detect (when no launch.json); 1.3 Start the server; 1.4 Open in browser; Phase 2: Iterate; References

### ce-product-pulse

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-product-pulse/SKILL.md) · published skill source · 180 lines

Source description: Generate a time-windowed pulse report on what users experienced and how the product performed - usage, quality, errors, signals worth investigating. Use when the user says 'run a pulse', 'show me the pulse', 'how are we doing', 'weekly recap', 'launch-day check', or passes a time window like '24h' or '7d'. Configures via .compound-engineering/config.local.yaml and saves reports to docs/pulse-reports/.

Section preview: Interaction Method; Lookback Window; Core Principles; Execution Flow; Phase 0: Route by Config State; Phase 1: First-Run Interview; Phase 2: Run the Pulse; Phase 3: Routine Hook; What This Skill Does Not Do; Learn More

### ce-proof

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-proof/SKILL.md) · published skill source · 404 lines

Source description: Run human-in-the-loop review loops over markdown via Proof (proofeditor.ai) — share, view, comment on, edit, and sync collaborative docs. Use when the user says "view this in proof", "share to proof", "HITL this doc", or wants a shared markdown review surface for a spec, plan, or draft, including handoffs from ce-brainstorm, ce-ideate, or ce-plan. Do not trigger on "proof" meaning evidence, math proofs, proof-of-concept, or "proofread this".

Section preview: Identity and Attribution; Human-in-the-Loop Review Mode; Web API (Primary for Sharing); Create a Shared Document; Read a Shared Document; Edit a Shared Document; Edit Strategy: Avoid Whole-Doc Rewrite; Known Limitations (Web API); Local Bridge (macOS App); Key Endpoints; Presence Statuses; Workflow: Review a Shared Document …

### ce-release-notes

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-release-notes/SKILL.md) · published skill source · 155 lines

Source description: Summarize recent compound-engineering plugin releases, or answer a specific question about a past release with a version citation. Use when the user types `/ce-release-notes` or asks "what changed in compound-engineering recently?" or "what happened to `<skill-name>`?".

Section preview: Phase 1 — Parse Arguments; Phase 2 — Fetch Releases (Summary Mode); Phase 3 — Render Summary; v{version} ({published_at_human}); Phase 5 — Fetch Releases (Query Mode); Phase 6 — Confidence Judgment; Phase 7 — PR Enrichment (Confident Match Only); Phase 8 — Synthesize Narrative (Match Found); Phase 9 — No Match

### ce-report-bug

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-report-bug/SKILL.md) · published skill source · 157 lines

Source description: Report a bug in the compound-engineering plugin

Section preview: Step 1: Gather Bug Information; Step 2: Collect Environment Information; Step 3: Format the Bug Report; Bug Description; Environment; What Happened; Expected Behavior; Steps to Reproduce; Error Messages; Additional Context; Step 4: Create GitHub Issue; Step 5: Confirm Submission …

### ce-resolve-pr-feedback

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-resolve-pr-feedback/SKILL.md) · published skill source · 49 lines

Source description: Resolve PR review feedback by evaluating validity and fixing issues in parallel. Use when addressing PR review comments, resolving review threads, or fixing code review feedback.

Section preview: Security; Mode Detection; Scripts; Success Criteria

### ce-riffrec-feedback-analysis

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-riffrec-feedback-analysis/SKILL.md) · published skill source · 36 lines

Source description: Riffrec product-feedback workflow. ALWAYS load when the user posts a `riffrec-*.zip`, a bundle with `session.json` + `events.json` + `recording.webm` + `voice.webm`, a video/audio recording for product feedback, or asks how to capture and share Riffrec sessions. Routes between setup, quick bug report, and extensive analysis.

Section preview: Choose the path; Common rules; Analyzer entrypoint

### ce-sessions

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-sessions/SKILL.md) · published skill source · 216 lines

Source description: Search and ask questions about coding agent session history across Claude Code, Codex, and Cursor. Use when asking what was worked on, what was tried before, how a problem was investigated across sessions, what happened recently, or any question about past agent sessions. Also use when the user references prior sessions, previous attempts, or past investigations — even without saying 'sessions' explicitly.

Section preview: Usage; Pre-resolved context; Note: 2026; Guardrails; Execution; Step 1 — Determine scan window; Step 2 — Discover sessions and extract metadata; Step 3 — Filter and rank; Step 4 — Set up scratch space; Step 5 — Extract per-session content (file-mediated); Step 6 — Dispatch synthesis subagent; Step 7 — Return findings …

### ce-setup

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-setup/SKILL.md) · published skill source · 164 lines

Source description: Diagnose and configure compound-engineering environment. Checks CLI dependencies, plugin version, and repo-local config. Offers guided installation for missing tools. Use when troubleshooting missing tools, verifying setup, or before onboarding.

Section preview: Interaction Method; Phase 1: Diagnose; Step 1: Determine Plugin Version; Step 2: Run the Health Check Script; Step 3: Evaluate Results; Phase 2: Fix; Step 4: Resolve Repo-Local CE Issues; Step 5: Bootstrap Project Config; Step 6: Offer Installation; Step 7: Install Selected Dependencies; Step 8: Summary

### ce-simplify-code

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-simplify-code/SKILL.md) · published skill source · 88 lines

Source description: Simplify and refine recently changed code for clarity, reuse, quality, and efficiency while preserving behavior.

Section preview: Step 1: Identify scope; Step 2: Launch 3 review agents in parallel; Agent 1: Code Reuse Reviewer; Agent 2: Code Quality Reviewer; Agent 3: Efficiency Reviewer; Step 3: Fix issues; Step 4: Verify behavior is preserved; Step 5: Summarize

### ce-slack-research

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-slack-research/SKILL.md) · published skill source · 41 lines

Source description: Search Slack for interpreted organizational context -- decisions, constraints, and discussion arcs -- and produce a synthesized research digest with cross-cutting analysis. Use when the user says 'search slack for', 'what did we discuss about', 'slack context for', or 'what does the team think about'. Differs from slack:find-discussions, which returns raw message results without synthesis.

Section preview: Usage; Examples; Execution

### ce-strategy

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-strategy/SKILL.md) · published skill source · 97 lines

Source description: Create or maintain STRATEGY.md - the product's target problem, approach, users, key metrics, and tracks of work. Use when starting a new product, updating direction, or when prompts like 'write our strategy', 'update the roadmap', 'what are we working on', or 'set up the strategy doc' come up. Also triggers when ce-ideate, ce-brainstorm, or ce-plan need upstream grounding and no strategy doc exists yet.

Section preview: Interaction Method; Focus Hint; Core Principles; Execution Flow; Phase 0: Route by File State; Phase 1: First-Run Interview; Phase 2: Update Run; Phase 3: Downstream Handoff; What This Skill Does Not Do; Learn More

### ce-test-browser

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-test-browser/SKILL.md) · published skill source · 358 lines

Source description: Run browser tests on pages affected by current PR or branch

Section preview: Use `agent-browser` Only For Browser Automation; Prerequisites; Setup; Workflow; 1. Verify Installation; 2. Ask Browser Mode; 3. Determine Test Scope; 4. Map Files to Routes; 5. Detect and Claim a Free Port; 6. Start Dev Server if Not Running, Then Verify; 7. Test Each Affected Page; 8. Human Verification (When Required) …

### ce-test-xcode

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-test-xcode/SKILL.md) · published skill source · 208 lines

Source description: Build and test iOS apps on simulator using XcodeBuildMCP. Use after making iOS code changes, before creating a PR, or when verifying app behavior and checking for crashes on simulator.

Section preview: Prerequisites; Workflow; 0. Verify XcodeBuildMCP is Available; 1. Discover Project and Scheme; 2. Boot Simulator; 3. Build the App; 4. Install and Launch; 5. Test Key Screens; 6. Human Verification (When Required); 7. Handle Failures; 8. Test Summary; Xcode Test Results …

### ce-update

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-update/SKILL.md) · published skill source · 95 lines

Section preview: Step 1: Probe versions; Step 2: Apply decision logic; Handle failure cases; Compare versions

### ce-work-beta

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-work-beta/SKILL.md) · published skill source · 442 lines

Source description: [BETA] Execute work with external delegate support. Same as ce-work but includes experimental Codex delegation mode for token-conserving code implementation.

Section preview: Introduction; Input Document; Argument Parsing; Settings Resolution Chain; Execution Workflow; Phase 0: Input Triage; Phase 1: Quick Start; Phase 2: Execute; Phase 3-4: Quality Check and Finishing Work; Codex Delegation Mode; Key Principles; Start Fast, Execute Faster …

### ce-work

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-work/SKILL.md) · published skill source · 369 lines

Source description: Execute work efficiently while maintaining quality and finishing features

Section preview: Introduction; Input Document; Execution Workflow; Phase 0: Input Triage; Phase 1: Quick Start; Phase 2: Execute; Phase 3-4: Quality Check and Finishing Work; Key Principles; Start Fast, Execute Faster; The Plan is Your Guide; Test As You Go; Quality is Built In …

### ce-worktree

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/ce-worktree/SKILL.md) · published skill source · 80 lines

Source description: Create an isolated git worktree for parallel feature work or PR review. Use when starting work that should not disturb the current checkout, or when `ce-work` or `ce-code-review` offers a worktree option.

Section preview: Creating a worktree; Other worktree operations; Dev tool trust behavior; When to create a worktree; Integration; Troubleshooting

### lfg

[Read source](../sources/every--compound-engineering-plugin/plugins/compound-engineering/skills/lfg/SKILL.md) · published skill source · 112 lines

Source description: Run the full autonomous engineering pipeline end-to-end (plan, work, code review, test, commit, push, open PR, watch CI, fix CI failures until green). Use only when the user explicitly requests hands-off execution of a software task and provides a feature description; do not auto-route casual conversation here.


## humanlayer--humanlayer

71 skill paths at `2f66a45b186d88488fa356862be0117db1ccae9f`.

### agent-browser

[Read source](../sources/humanlayer--humanlayer/.claude/skills/agent-browser/SKILL.md) · repository development skill · 614 lines

Source description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction.

Section preview: Core Workflow; Command Chaining; Session Management; Before starting any browser task; Session naming convention; When you hit an auth screen; Essential Commands; Common Patterns; Form Submission; Data Extraction; Parallel Sessions; Connect to Existing Chrome …

### asd-ste100

[Read source](../sources/humanlayer--humanlayer/.claude/skills/asd-ste100/SKILL.md) · repository development skill · 80 lines

Source description: Rewrites ambiguous English into ASD-STE100 style — one meaning per word, active voice, simple tense, short sentences. Use when agent output is hard to parse; triggers: simplify this, STE100 rewrite.

Section preview: When to Use This Skill; Source and Scope; Core Rewrite Rules; Process; Output Format; Boundaries; Additional Resources

### better-github-skill

[Read source](../sources/humanlayer--humanlayer/.claude/skills/better-github-skill/SKILL.md) · repository development skill · 58 lines

Source description: Use for 1) inspecting PR state, 2) reading review threads, or 3) debugging CI failures. Otherwise use the gh CLI.

Section preview: Scripts; Gotchas (each one burned real sessions repeatedly)

### bump-version

[Read source](../sources/humanlayer--humanlayer/.claude/skills/bump-version/SKILL.md) · repository development skill · 53 lines

Source description: Bump the base version of one or more packages (riptide-native, cli, linear-cli, rpi-plugin) on a PR - updates every synced file, verifies, commits, pushes. Use when cutting a release or asked to bump versions.

Section preview: 1. Bump the named packages; 2. Verify, commit, push; 3. After merge: ship riptide beta + prod together; Edge cases

### calldiff

[Read source](../sources/humanlayer--humanlayer/.claude/skills/calldiff/SKILL.md) · repository development skill · 124 lines

Source description: Diff call stacks across git commits for agentic code review (22 languages). Run `calldiff --help` for usage details.

Section preview: Presenting output; Arguments; Options; Examples; Arguments; Options; Examples; Arguments; Options; Examples

### chrome-devtools-cli

[Read source](../sources/humanlayer--humanlayer/.claude/skills/chrome-devtools-cli/SKILL.md) · repository development skill · 132 lines

Source description: Use this to skill to write shell scripts or run shell commands to automate tasks in the browser or otherwise use Chrome DevTools via CLI.

Section preview: Setup; AI Workflow; Command Usage; Input Automation (<uid> from snapshot); Navigation; Emulation; Performance; Network; Debugging & Inspection; Service Management

### codebase-design

[Read source](../sources/humanlayer--humanlayer/.claude/skills/codebase-design/SKILL.md) · repository development skill · 114 lines

Source description: Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.

Section preview: Glossary; Deep vs shallow; Principles; Designing for testability; Relationships; Rejected framings; Going deeper

### effect-program-design

[Read source](../sources/humanlayer--humanlayer/.claude/skills/effect-program-design/SKILL.md) · repository development skill · 138 lines

Section preview: Source rule; References; The creed; Core defaults; Testing defaults; Review checklist

### grill-me

[Read source](../sources/humanlayer--humanlayer/.claude/skills/grill-me/SKILL.md) · repository development skill · 9 lines

Source description: Interview the user relentlessly about a plan or design to establish a shared understanding. use this any time the user says "grill me

### grind-design-discussion

[Read source](../sources/humanlayer--humanlayer/.claude/skills/grind-design-discussion/SKILL.md) · repository development skill · 89 lines

Source description: autonomous review pass on design discussion document. Use when you want to grind on a design doc without user feedback - surfaces questions, vets assumptions, verifies patterns.

Section preview: Steps; Subagents; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation

### grind-research

[Read source](../sources/humanlayer--humanlayer/.claude/skills/grind-research/SKILL.md) · repository development skill · 129 lines

Source description: autonomous deep-dive pass on research document. Use when you want to grind on a research doc without user feedback - digs deeper, vets claims, adds detail.

Section preview: Steps; Research Guidelines; Cloud Permalinks; Markdown Formatting; Installation; Important notes:

### html-demo-video-guidelines

[Read source](../sources/humanlayer--humanlayer/.claude/skills/html-demo-video-guidelines/SKILL.md) · repository development skill · 63 lines

Section preview: Do; Don't; Vertical (9:16) cuts

### html-mockups

[Read source](../sources/humanlayer--humanlayer/.claude/skills/html-mockups/SKILL.md) · repository development skill · 383 lines

Source description: if the user asks for an html mockup for ui components or screens

Section preview: Output Location; Design System: Poimandres Theme; Color Palette; Typography; Button Styling; Semantic Button Patterns; Component Patterns; Layout Patterns; Icon Styling; Annotation Pattern (for mockup notes); HTML Template; Guidelines …

### improve-codebase-architecture

[Read source](../sources/humanlayer--humanlayer/.claude/skills/improve-codebase-architecture/SKILL.md) · repository development skill · 71 lines

Source description: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.

Section preview: Process; 1. Explore; 2. Present candidates as an HTML report; 3. Grilling loop

### improve-writing

[Read source](../sources/humanlayer--humanlayer/.claude/skills/improve-writing/SKILL.md) · repository development skill · 75 lines

Source description: use when the user complains that prose writing is bad - do not use for code

Section preview: The one that mattered most; How the AI tell actually shows up; The RL section, as a worked example; The verifying-quality rewrite, as a worked example; Rules of thumb

### merge-resolve-conflicts

[Read source](../sources/humanlayer--humanlayer/.claude/skills/merge-resolve-conflicts/SKILL.md) · repository development skill · 51 lines

Source description: Use to merge in main and resolve open merge conflicts.

Section preview: Step 1: Orientation; Step 2: Action; Conflict Resolution Procedure

### migrate-orpc-to-effect

[Read source](../sources/humanlayer--humanlayer/.claude/skills/migrate-orpc-to-effect/SKILL.md) · repository development skill · 539 lines

Source description: Migrate a single oRPC procedure from classic async handler to Effect-backed implementation. Use when converting procedures one at a time to maintain incremental, reviewable changes.

Section preview: When to Use; Available Effect Services; Prerequisites; Migration Workflow; 1. Identify the procedure to migrate; 2. Determine the Effect base; 3. Create the Effect procedure file; 4. Write the Effect procedure; 5. Key transformation patterns; 6. Add billing middleware if needed; 7. Update the router; 8. Delete the original file …

### narrow-react-prop-types

[Read source](../sources/humanlayer--humanlayer/.claude/skills/narrow-react-prop-types/SKILL.md) · repository development skill · 166 lines

Source description: narrow React component prop types to match live code paths

Section preview: Core Requirements; Workflow; 1. Identify the suspect component; 2. Find every live usage; 3. Derive the real types from the live code paths; 4. Tighten the public prop type; 5. Derive and extract types where possible; 6. Tighten internal child props too; 7. Remove fallback logic for unsupported states; 8. Update all variants that share the prop type; 9. Let tests and stories adapt to live code; 10. Validate the change …

### no-use-effect

[Read source](../sources/humanlayer--humanlayer/.claude/skills/no-use-effect/SKILL.md) · repository development skill · 229 lines

Section preview: Quick Reference; When to Use This Skill; Workflow; 1. Identify the useEffect; 2. Apply the Correct Replacement Pattern; 3. Verify; The Escape Hatch: useMountEffect; Replacement Patterns; Rule 1: Derive state, do not sync it; Rule 2: Use data-fetching libraries; Rule 3: Event handlers, not effects; Rule 4: useMountEffect for one-time external sync …

### react-doctor

[Read source](../sources/humanlayer--humanlayer/.claude/skills/react-doctor/SKILL.md) · repository development skill · 51 lines

Source description: Use when finishing a feature, fixing a bug, before committing React code, or when the user types `/doctor`, asks to scan, triage, or clean up React diagnostics. Covers lint, accessibility, bundle size, architecture. Includes a regression check and a full local-triage workflow that fetches the canonical playbook.

Section preview: After making React code changes:; For general cleanup or code improvement:; /doctor — full local triage workflow; Configuring or explaining rules; Command

### rebase-drizzle-migration

[Read source](../sources/humanlayer--humanlayer/.claude/skills/rebase-drizzle-migration/SKILL.md) · repository development skill · 224 lines

Source description: fix drizzle migrations after rebasing onto upstream/main when migrations diverged

Section preview: Agent Workflow; Diagnosis Phase; The Problem (Explain to User); Fix Process; Step 1: Checkout upstream/main; Step 2: Apply migrations to database; Step 3: Switch back to feature branch; Step 4: Clean up migration artifacts; Step 5: Verify clean state; Step 6: reseet database state; Step 7: Regenerate migration; Step 8: Apply migration locally …

### show-me-the-components

[Read source](../sources/humanlayer--humanlayer/.claude/skills/show-me-the-components/SKILL.md) · repository development skill · 15 lines

Source description: Show how a react component tree is structured

### storybook

[Read source](../sources/humanlayer--humanlayer/.claude/skills/storybook/SKILL.md) · repository development skill · 159 lines

Section preview: Component Taxonomy; Pure/Wired Production Pattern; Anti-Pattern: Mock-ups; Story Patterns; 1. Pure Story — Static Args (Default); 2. ShellDemo — Inline Wrapper for Interactivity; 3. ShellDemo — Companion File for Complex Composition; 4. ShellDemo — Page Layout Composition (Rare); ShellDemo Nav Group; Quick Checklist; Locations; Running Storybook

### stripe-billing-verification

[Read source](../sources/humanlayer--humanlayer/.claude/skills/stripe-billing-verification/SKILL.md) · repository development skill · 198 lines

Source description: Run Stripe webhook smoke tests and billing lifecycle simulations for stripe

Section preview: Task; Quick Reference; Workflow; Secret Rules; Captured Output and Dev Logs; Smoke-Test Procedure; Test Clock Workflow; Safe Automation Guidance; Troubleshooting; Invalid signature; `stripe listen --print-secret` succeeded, but forwarding does not happen; Need daemon or API errors after the trigger …

### subagent-orchestrator

[Read source](../sources/humanlayer--humanlayer/.claude/skills/subagent-orchestrator/SKILL.md) · repository development skill · 18 lines

Source description: orchestrate sub-agents to accomplish complex long-horizon tasks without losing coherency by delegating to sub-agents

### durable-streams-yjs

[Read source](../sources/humanlayer--humanlayer/.claude/skills/sync/durable-streams-yjs/SKILL.md) · repository development skill · 174 lines

Source description: Yjs CRDT sync over durable streams with @durable-streams/y-durable-streams. DurableStreamsProvider setup, document stream and awareness stream config, transport modes (SSE vs long-poll), provider lifecycle (connect, disconnect, destroy), synced/status/error events, lib0 VarUint8Array framing, awareness heartbeat. Requires yjs, y-protocols, lib0 peer dependencies. Load when integrating Yjs collaborative editing with durable streams.

Section preview: Setup; Core Patterns; Document-only sync (no presence); Manual connect/disconnect; Dynamic auth headers; Common Mistakes; HIGH Forgetting peer dependencies for Yjs; HIGH Using application/json content type for Yjs streams; HIGH Not calling destroy() on cleanup; See also; Version

### test-it-locally

[Read source](../sources/humanlayer--humanlayer/.claude/skills/test-it-locally/SKILL.md) · repository development skill · 186 lines

Source description: Test Riptide changes against the local devstack through the UI, HumanLayer CLI, and database. Use for local verification, agent-browser checks, local task or session creation, and devstack setup.

Section preview: Workflow; Devstack; agent-browser; Local CLI testing; Durable Streams Testing

### local-cli-testing

[Read source](../sources/humanlayer--humanlayer/.claude/skills/test-it-locally/references/local-cli-testing/SKILL.md) · repository development skill · 101 lines

Source description: Guide local HumanLayer CLI login and create local test tasks and sessions

Section preview: Login (Interactive); Create Task; Upload Artifact; Launch Session; Inspect Results; Troubleshooting

### ui-copy

[Read source](../sources/humanlayer--humanlayer/.claude/skills/ui-copy/SKILL.md) · repository development skill · 168 lines

Section preview: Changing a string that already ships; Mechanics; Session status labels; Shapes; Glossary; Rewrites

### orchestrate

[Read source](../sources/humanlayer--humanlayer/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/SKILL.md) · published skill source · 25 lines

Source description: Toolbox for driving HumanLayer from the CLI - log in, pick a host, launch tasks in their own worktrees, launch sessions, list tasks and their PRs, and copy, move, or upload task artifacts.

### show-me

[Read source](../sources/humanlayer--humanlayer/apps/riptide-humanlayer-claude-plugin/skills/show-me/SKILL.md) · published skill source · 123 lines

Source description: Help the user understand the current topic visually with concise diagrams, code-shape sketches, and focused HTML artifacts.

### teleport

[Read source](../sources/humanlayer--humanlayer/apps/riptide-humanlayer-claude-plugin/skills/teleport/SKILL.md) · published skill source · 199 lines

Source description: Move the current task to a new HumanLayer session on another host (sandbox, cloud VM, or a machine you can SSH into).

Section preview: 1. Gather context, then ask once; 2. Saved defaults; 3. Save the work; 4. Prepare the host; 5. Start the daemon; 6. Launch the remote session; 7. Finish; When something fails

### create-design-discussion

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-design-discussion/SKILL.md) · Pi runtime variant · 134 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps to follow after receiving the user's request; Cloud Permalinks; Markdown Formatting; Installation; Document Precedence

### create-prd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-prd/SKILL.md) · Pi runtime variant · 156 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: How the conversation works (read this before you start); Working from whatever inputs exist; Design system for mockups; Markdown formatting; HTML mockups

### create-research-questions

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-research-questions/SKILL.md) · Pi runtime variant · 115 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps to follow after receiving the user's request; Output Format; Cloud Permalinks

### create-research

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-research/SKILL.md) · Pi runtime variant · 299 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: CRITICAL: YOUR ONLY JOB IS TO DOCUMENT AND EXPLAIN THE CODEBASE AS IT EXISTS TODAY; Initial Setup:; Steps to follow after receiving the research query:; Document Style and Format; Headers state the takeaway, not the topic or the question; Writing and citation style; Visual structure — show the shape of the code, don't just describe it; Code References section; Testing patterns; Important notes:; Response; Cloud Permalinks …

### create-structure-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-structure-outline/SKILL.md) · Pi runtime variant · 182 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Steps; Output Document; Work with the user to iterate on the design; Cloud Permalinks; Markdown Formatting; Installation; Phase changes should be concise but clear; Phase Validation Design; Document Precedence

### create-tech-design

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/create-tech-design/SKILL.md) · Pi runtime variant · 286 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: How the conversation works (read this before you start); Working from whatever inputs exist; Markdown formatting; System Design representations; HTML artifacts for complex concepts; Program Design views; HTML artifacts for complex concepts

### describe-pr

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/describe-pr/SKILL.md) · Pi runtime variant · 61 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Workflow

### implement-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/implement-outline/SKILL.md) · Pi runtime variant · 134 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Getting Started; Workflow; 1. Launch Implementer Agent; 2. Report to Human; Phase [N] Complete; 3. Wait for Human Confirmation; 4. Commit the Changes; 5. Repeat for Next Phase; Special Instructions; Resuming Work; Handling Issues; Multiple Phases …

### implement-plan

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/implement-plan/SKILL.md) · Pi runtime variant · 125 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Workflow; 0. Locate Plan File; 1. Launch Implementer Agent; 2. Review Output; 3. Perform Automated Checks; 4. Report to Human; Phase [N] Implementation Summary; 5. Wait for Human Confirmation; 6. Commit the changes; 7. Repeat for Next Phase; Special Instructions; Resuming Work …

### iterate-design-discussion

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-design-discussion/SKILL.md) · Pi runtime variant · 114 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Steps; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation

### iterate-implementation

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-implementation/SKILL.md) · Pi runtime variant · 87 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps; Cloud Permalinks; Markdown Formatting; Installation; When Iteration is Complete

### iterate-prd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-prd/SKILL.md) · Pi runtime variant · 182 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Continue Grilling Mode; Steps; Document Precedence; HTML Mockups; Cloud Permalinks; Markdown Formatting; Installation

### iterate-research-questions

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-research-questions/SKILL.md) · Pi runtime variant · 84 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Steps; Research Question Guidelines; Cloud Permalinks

### iterate-research

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-research/SKILL.md) · Pi runtime variant · 228 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Setup:; Steps; Research Guidelines; Document Style and Format; Headers state the takeaway, not the topic or the question; Visual structure — show the shape of the code, don't just describe it; Cloud Permalinks; Markdown Formatting; Installation; Important notes:

### iterate-structure-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-structure-outline/SKILL.md) · Pi runtime variant · 153 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Initial Check; Steps; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation; Phase changes should be concise but clear; Phase Validation Design

### iterate-tech-design

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/iterate-tech-design/SKILL.md) · Pi runtime variant · 284 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Continue Grilling Mode; Steps; Document Precedence; Mermaid Diagrams; HTML Diagrams; Program Design Views; Referencing the PRD; Cloud Permalinks; Markdown Formatting; Installation

### show-me

[Read source](../sources/humanlayer--humanlayer/apps/riptide-pi-extension/skills/show-me/SKILL.md) · Pi runtime variant · 123 lines

Source description: Help the user understand the current topic visually with concise diagrams, code-shape sketches, and focused HTML artifacts.

### ci-commit

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/ci-commit/SKILL.md) · published skill source · 35 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Process:; Remember:

### configure-workspaces

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/configure-workspaces/SKILL.md) · published skill source · 292 lines

Source description: Propose and generate workspace configuration files (.humanlayer/workspace.json and .humanlayer/workspace.local.json) for a repository

Section preview: Purpose; Steps to follow; Step 0: Select the repository; Step 1: Read the project; Step 2: Build the proposal; Step 3: Validate the proposal; Step 4: Write the approved config; Step 5: Confirm and summarize; Key concepts for this skill; Template variables; Repo precedence rules; copyGlobs semantics …

### create-design-discussion

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md) · published skill source · 134 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps to follow after receiving the user's request; Cloud Permalinks; Markdown Formatting; Installation; Document Precedence

### create-plan

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-plan/SKILL.md) · published skill source · 104 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps; Plan Writing Guidelines; Document Precedence; Output; Cloud Permalinks; Markdown Formatting; Installation; Validation Design

### create-prd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md) · published skill source · 156 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: How the conversation works (read this before you start); Working from whatever inputs exist; Design system for mockups; Markdown formatting; HTML mockups

### create-research-questions

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md) · published skill source · 115 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps to follow after receiving the user's request; Output Format; Cloud Permalinks

### create-research

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md) · published skill source · 299 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: CRITICAL: YOUR ONLY JOB IS TO DOCUMENT AND EXPLAIN THE CODEBASE AS IT EXISTS TODAY; Initial Setup:; Steps to follow after receiving the research query:; Document Style and Format; Headers state the takeaway, not the topic or the question; Writing and citation style; Visual structure — show the shape of the code, don't just describe it; Code References section; Testing patterns; Important notes:; Response; Cloud Permalinks …

### create-structure-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md) · published skill source · 182 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Steps; Output Document; Work with the user to iterate on the design; Cloud Permalinks; Markdown Formatting; Installation; Phase changes should be concise but clear; Phase Validation Design; Document Precedence

### create-tdd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md) · published skill source · 286 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: How the conversation works (read this before you start); Working from whatever inputs exist; Markdown formatting; System Design representations; HTML artifacts for complex concepts; Program Design views; HTML artifacts for complex concepts

### describe-pr

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md) · published skill source · 80 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Workflow

### implement-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md) · published skill source · 134 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Getting Started; Workflow; 1. Launch Implementer Agent; 2. Report to Human; Phase [N] Complete; 3. Wait for Human Confirmation; 4. Commit the Changes; 5. Repeat for Next Phase; Special Instructions; Resuming Work; Handling Issues; Multiple Phases …

### implement-plan

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/implement-plan/SKILL.md) · published skill source · 125 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Workflow; 0. Locate Plan File; 1. Launch Implementer Agent; 2. Review Output; 3. Perform Automated Checks; 4. Report to Human; Phase [N] Implementation Summary; 5. Wait for Human Confirmation; 6. Commit the changes; 7. Repeat for Next Phase; Special Instructions; Resuming Work …

### iterate-design-discussion

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-design-discussion/SKILL.md) · published skill source · 114 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Steps; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation

### iterate-implementation

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-implementation/SKILL.md) · published skill source · 87 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps; Cloud Permalinks; Markdown Formatting; Installation; When Iteration is Complete

### iterate-plan

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-plan/SKILL.md) · published skill source · 107 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Steps; Plan Writing Guidelines; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation; Validation Design

### iterate-prd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-prd/SKILL.md) · published skill source · 182 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Continue Grilling Mode; Steps; Document Precedence; HTML Mockups; Cloud Permalinks; Markdown Formatting; Installation

### iterate-research-questions

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-research-questions/SKILL.md) · published skill source · 84 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Steps; Research Question Guidelines; Cloud Permalinks

### iterate-research

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-research/SKILL.md) · published skill source · 228 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Setup:; Steps; Research Guidelines; Document Style and Format; Headers state the takeaway, not the topic or the question; Visual structure — show the shape of the code, don't just describe it; Cloud Permalinks; Markdown Formatting; Installation; Important notes:

### iterate-structure-outline

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-structure-outline/SKILL.md) · published skill source · 153 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input; Initial Check; Steps; Document Precedence; Cloud Permalinks; Markdown Formatting; Installation; Phase changes should be concise but clear; Phase Validation Design

### iterate-tdd

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/iterate-tdd/SKILL.md) · published skill source · 284 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Initial Check; Continue Grilling Mode; Steps; Document Precedence; Mermaid Diagrams; HTML Diagrams; Program Design Views; Referencing the PRD; Cloud Permalinks; Markdown Formatting; Installation

### review-artifact-comments

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/review-artifact-comments/SKILL.md) · published skill source · 71 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: Input Format; Note: comment block format:; Workflow; Example; Important Notes

### setup-worktree

[Read source](../sources/humanlayer--humanlayer/apps/riptide-rpi-claude-plugin/skills/setup-worktree/SKILL.md) · published skill source · 201 lines

Source description: Only use when the user explicitly invokes this skill by name.

Section preview: steps to follow; Step 0: Check if worktree setup should be skipped; Step 1 Get required information


## cursor--plugins-pstack

61 skill paths at `9580c23696ac8d7abed0c166f2f9918800afb819`.

### reproduce-and-fix-issues

[Read source](../sources/cursor--plugins-pstack/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md) · automation skill · 310 lines

Source description: Reproduce triaged Slack bugs through a configured app-control adapter, verify existing fixes, and open a bounded draft pull request only after before-and-after proof. Use only from the configured Benny repro automation.

Section preview: Hard safety rules; 1. Freeze source coordinates; 2. Wait for the triage contract; 3. Apply ownership and fix-artifact gates; Someone is explicitly fixing it; A fix artifact already exists; 4. Open an optional operations thread; 5. Load and check the control adapter; 6. Study the report; 7. Reproduce; 8. Capture and review evidence; 9. Report the repro outcome …

### setup-benny

[Read source](../sources/cursor--plugins-pstack/pstack/automations/benny/skills/setup-benny/SKILL.md) · automation skill · 266 lines

Source description: Configure Benny and prepare its triage and repro automations. Use when installing Benny or changing its Slack, tracker, repository, routing, control, model, or budget settings.

Section preview: 1. Copy the pack and enable shared pstack skills; 2. Adapt the configuration; 3. Fill the required choices; 4. Check integration capabilities; 5. Prepare the routing map; 6. Verify the control adapter; 7. Prepare the live automations; First-time creation; Existing automations; Creation boundary; 8. Test thread safety

### triage-issue-reports

[Read source](../sources/cursor--plugins-pstack/pstack/automations/benny/skills/triage-issue-reports/SKILL.md) · automation skill · 240 lines

Source description: Triage Slack issue reports with one thread-only verdict, evidence review, cause-aware routing, tracker dedupe, and fail-closed ticket creation. Use only from the configured Benny triage automation.

Section preview: Hard safety rules; 1. Freeze source coordinates; 2. Read the whole report; 3. Trace cause before routing; 4. Classify; Bug; Performance; Feature request; Question or feedback; Reroute; 5. Apply configured routing; 6. Use the issue-tracker adapter …

### architect

[Read source](../sources/cursor--plugins-pstack/pstack/skills/architect/SKILL.md) · published skill source · 79 lines

Source description: Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape.

Section preview: Start; Phase A: Ground the problem; Phase B: Sketch; Phase C: Agree (opt-in); Phase D: Implement against the sketch; Phase E: Scrap when the architecture is wrong; Outputs

### arena

[Read source](../sources/cursor--plugins-pstack/pstack/skills/arena/SKILL.md) · published skill source · 48 lines

Source description: Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape.

Section preview: Phase A: Frame; Phase B: Fan out; Phase C: Cross-judge; Phase D: Pick a base; Phase E: Graft; Phase F: Verify; Outputs

### automate-me

[Read source](../sources/cursor--plugins-pstack/pstack/skills/automate-me/SKILL.md) · published skill source · 104 lines

Source description: Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via create-skill + unslop, optionally pulling fresh evidence from recent transcripts.

Section preview: Flow; 0. Check for an existing skill; 1. Mine their history; 2. Ask the user directly; 3. Cluster findings; 4. Draft the skill; 5. Iterate on prose; 6. Land it; Guardrails; Evaluation; When not to use

### benchmark-checklist

[Read source](../sources/cursor--plugins-pstack/pstack/skills/benchmark-checklist/SKILL.md) · published skill source · 39 lines

Source description: Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark or report a speedup or regression you measured.

Section preview: Before you run anything; The questions; Report; Other perf material

### blast-radius

[Read source](../sources/cursor--plugins-pstack/pstack/skills/blast-radius/SKILL.md) · published skill source · 50 lines

Source description: Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing a small diff you don't trust.

Section preview: Don't trust your own writeup; How sure are you; Steps; What to hand back

### bro

[Read source](../sources/cursor--plugins-pstack/pstack/skills/bro/SKILL.md) · published skill source · 7 lines

Source description: Restate the last message in plain human language, with no jargon.

### correct

[Read source](../sources/cursor--plugins-pstack/pstack/skills/correct/SKILL.md) · published skill source · 32 lines

Source description: Find the mistakes agents keep repeating in this repo and make each one impossible. Try architecture first, then types, then a lint whose error names the fix, then a test, and write docs last. Prove each check fails on a real past mistake. Repeat this each time the operator corrects you. Use for /correct.

Section preview: Find the mistake classes; Fix each class at the highest level that works; Fix and prove; Keep the rule table

### create-formal-verification-skill

[Read source](../sources/cursor--plugins-pstack/pstack/skills/create-formal-verification-skill/SKILL.md) · published skill source · 43 lines

Source description: Generate a project-local skill that formally verifies the code where a bug costs the most and tests reach the least, in any language, with whichever verification tool fits. Use for /create-formal-verification-skill, \"model-check this race\", \"prove this invariant\", or when concurrency, retries, state machines, parsers, or unsafe code need more than tests.

Section preview: Choose the target from the code; Let the question choose the tool; What makes it good; Generate the verify skill; Prove it before you hand off; Hand off

### create-verification-skill

[Read source](../sources/cursor--plugins-pstack/pstack/skills/create-verification-skill/SKILL.md) · published skill source · 44 lines

Source description: Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control skill for this repo\", or when a project has no scripted way to prove UI/CLI/service behavior.

Section preview: 1. Interview the repo, not the user; 2. Generate the skill; 3. Seed the feature map; 4. Prove the generated skill before handing it over; 5. Offer the maintenance loop

### figure-it-out

[Read source](../sources/cursor--plugins-pstack/pstack/skills/figure-it-out/SKILL.md) · published skill source · 52 lines

Source description: Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions. Use for /figure-it-out or 'figure it out'.

Section preview: Start; Phase A: Frame; Phase B: Design the workflow; Phase C: Run the loop; Phase D: Keep the audit trail; Phase E: Verify and hand back

### how

[Read source](../sources/cursor--plugins-pstack/pstack/skills/how/SKILL.md) · published skill source · 36 lines

Source description: Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation.

Section preview: 1. Assess complexity; 2. Explore (complex only); 3. Synthesize (complex only); 4. Present; Output format

### in-your-own-words

[Read source](../sources/cursor--plugins-pstack/pstack/skills/in-your-own-words/SKILL.md) · published skill source · 7 lines

Source description: Restate in your own words what you think the user's goals are and what problem they're trying to solve. Use for /in-your-own-words.

### interrogate

[Read source](../sources/cursor--plugins-pstack/pstack/skills/interrogate/SKILL.md) · published skill source · 74 lines

Source description: Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple LLM reviewers challenge changes from independent angles.

Section preview: Step 1, Scope; Step 2, Intent; Step 3, Spawn Reviewers; Step 4, Synthesize; Step 5, Lead Judgment; Output Format; Intent; Reviewers; Act On; Consider; Noted; Dismissed …

### ketchup-video

[Read source](../sources/cursor--plugins-pstack/pstack/skills/ketchup-video/SKILL.md) · published skill source · 23 lines

Source description: Catch the user up like /ketchup, with a short silent video of slides for what happened and the waiting calls as text under it. Use for /ketchup-video.

Section preview: Slides; Render

### ketchup

[Read source](../sources/cursor--plugins-pstack/pstack/skills/ketchup/SKILL.md) · published skill source · 43 lines

Source description: Catch the user up on what changed in this chat since their last message, in plain words and small visuals. List every item waiting on them with what they need to decide it from the reply alone. Use for /ketchup.

Section preview: Gather what changed; Write the reply; Visuals

### maintain-formal-verification-skill

[Read source](../sources/cursor--plugins-pstack/pstack/skills/maintain-formal-verification-skill/SKILL.md) · published skill source · 58 lines

Source description: Bring a project's formal verification back in line with the code after the code changes: find the commits that touched verified code, update the model, harness, or properties to describe the code as it is now, rerun, and say whether each failure is drift in the verification or a bug in the code. Use for /maintain-formal-verification-skill, \"is the model still true to the code\", or after merges and refactors that touched verified code without rechecking it.

Section preview: Outcomes; Edit scope; Pass; Report

### maintain-verification-skill

[Read source](../sources/cursor--plugins-pstack/pstack/skills/maintain-verification-skill/SKILL.md) · published skill source · 39 lines

Source description: Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. Use for /maintain-verification-skill or \"audit the verify skill\".

Section preview: Outcomes; Edit scope; Pass

### make-bot-ui

[Read source](../sources/cursor--plugins-pstack/pstack/skills/make-bot-ui/SKILL.md) · published skill source · 115 lines

Section preview: Create the webhook routine; Copy the URL and the sender key; Request the sender key; Host the page on this computer; Put the page on the tailnet; Handle the webhook wake

### no-comments

[Read source](../sources/cursor--plugins-pstack/pstack/skills/no-comments/SKILL.md) · published skill source · 24 lines

Source description: Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints.

Section preview: Scope; Steps

### poteto-help

[Read source](../sources/cursor--plugins-pstack/pstack/skills/poteto-help/SKILL.md) · published skill source · 163 lines

Source description: Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task. Type /poteto-help with a question.

Section preview: Find out what they need; Get set up; Start a task with `/poteto-mode`; Pick a skill; Playbooks and principles; Fix a run that went wrong; Make pstack my own; Reply

### poteto-mode

[Read source](../sources/cursor--plugins-pstack/pstack/skills/poteto-mode/SKILL.md) · published skill source · 149 lines

Source description: poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work in this style.

Section preview: Non-negotiables; Principles; Autonomy; Subagents; Writing the reply; Comments; Playbooks

### principle-attack-the-premise

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-attack-the-premise/SKILL.md) · published skill source · 21 lines

Source description: Apply when two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it.

### principle-boundary-discipline

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-boundary-discipline/SKILL.md) · published skill source · 34 lines

Source description: Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions.

### principle-build-the-lever

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-build-the-lever/SKILL.md) · published skill source · 23 lines

Source description: Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun.

### principle-encode-lessons-in-structure

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) · published skill source · 11 lines

Source description: Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text.

### principle-exhaust-the-design-space

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-exhaust-the-design-space/SKILL.md) · published skill source · 9 lines

Source description: Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing.

### principle-experience-first

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-experience-first/SKILL.md) · published skill source · 19 lines

Source description: Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones.

### principle-explain-the-number

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-explain-the-number/SKILL.md) · published skill source · 17 lines

Source description: Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think.

### principle-fix-root-causes

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-fix-root-causes/SKILL.md) · published skill source · 21 lines

Source description: Apply when debugging. Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate.

### principle-foundational-thinking

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-foundational-thinking/SKILL.md) · published skill source · 21 lines

Source description: Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious.

### principle-guard-the-context-window

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-guard-the-context-window/SKILL.md) · published skill source · 12 lines

Source description: Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads.

### principle-laziness-protocol

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-laziness-protocol/SKILL.md) · published skill source · 10 lines

Source description: Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem.

### principle-make-operations-idempotent

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-make-operations-idempotent/SKILL.md) · published skill source · 22 lines

Source description: Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs.

### principle-migrate-callers-then-delete-legacy-apis

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) · published skill source · 14 lines

Source description: Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers.

### principle-minimize-reader-load

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-minimize-reader-load/SKILL.md) · published skill source · 18 lines

Source description: Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.

### principle-model-the-domain

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-model-the-domain/SKILL.md) · published skill source · 24 lines

Source description: Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files.

### principle-never-block-on-the-human

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-never-block-on-the-human/SKILL.md) · published skill source · 15 lines

Source description: Apply when tempted to ask 'should I do X?' on reversible work.

### principle-outcome-oriented-execution

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-outcome-oriented-execution/SKILL.md) · published skill source · 21 lines

Source description: Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code.

### principle-prove-it-works

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-prove-it-works/SKILL.md) · published skill source · 22 lines

Source description: Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.

Section preview: Script the check when you can

### principle-redesign-from-first-principles

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-redesign-from-first-principles/SKILL.md) · published skill source · 16 lines

Source description: Apply when integrating a new requirement into an existing design.

### principle-separate-before-serializing-shared-state

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md) · published skill source · 16 lines

Source description: Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant.

### principle-sequence-verifiable-units

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-sequence-verifiable-units/SKILL.md) · published skill source · 17 lines

Source description: Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer.

### principle-subtract-before-you-add

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-subtract-before-you-add/SKILL.md) · published skill source · 18 lines

Source description: Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base.

### principle-test-behavior-not-implementation

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) · published skill source · 20 lines

Source description: Apply when you write, change, or keep a test. Assert what the code's users can observe, so that the test fails when that behavior breaks and keeps passing when only the internals change.

### principle-type-system-discipline

[Read source](../sources/cursor--plugins-pstack/pstack/skills/principle-type-system-discipline/SKILL.md) · published skill source · 13 lines

Source description: Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, exhaust variants, derive from authoritative schemas.

### recall

[Read source](../sources/cursor--plugins-pstack/pstack/skills/recall/SKILL.md) · published skill source · 35 lines

Source description: Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. Use for 'recall my work on X', 'catch me up', 'what have I been working on', 'where did I leave off', before starting or resuming work.

Section preview: Output contract

### reflect

[Read source](../sources/cursor--plugins-pstack/pstack/skills/reflect/SKILL.md) · published skill source · 69 lines

Source description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.

Section preview: 1. Locate the active transcript; 2. Spawn three reviewers in parallel; 3. Synthesize; 4. Structural enforcement check; 5. Apply; 6. Summarize for the user

### setup-pstack

[Read source](../sources/cursor--plugins-pstack/pstack/skills/setup-pstack/SKILL.md) · published skill source · 78 lines

Source description: Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, "configure pstack models", "pstack budget", or changing pstack's model choices.

Section preview: Steps; 1. Detect available models; 2. Load current state; 3. Budget, map, and confirm; 4. Validate; 5. Write the rule; 6. Confirm; 7. Offer a verification skill (optional); 8. Offer a formal verification skill (optional)

### sharpen

[Read source](../sources/cursor--plugins-pstack/pstack/skills/sharpen/SKILL.md) · published skill source · 16 lines

Source description: Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen.

### show-me-your-work

[Read source](../sources/cursor--plugins-pstack/pstack/skills/show-me-your-work/SKILL.md) · published skill source · 82 lines

Source description: Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for /show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away.

Section preview: The format; Logging a row; Where it lives; Rules; Audit the log against the transcript; Cross-model review of the trail; Reviewing the trail; Composing this skill

### statechart

[Read source](../sources/cursor--plugins-pstack/pstack/skills/statechart/SKILL.md) · published skill source · 36 lines

Source description: Draw how any system moves between states, such as a product flow, a protocol, or a service, as a Mermaid statechart from a TLA+ model. Each bug is a numbered path with blue borders to a state that breaks a rule. Use for /statechart, to show a bug as a path through states, or to turn an agreed chart into a TLA+ skeleton.

Section preview: Pick the direction; Spec to chart; Chart to spec; Hand off

### swarm

[Read source](../sources/cursor--plugins-pstack/pstack/skills/swarm/SKILL.md) · published skill source · 41 lines

Source description: Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration.

Section preview: Start; Phase A: Frame; Phase B: Fan out; Phase C: Aggregate; Phase D: Report

### tdd

[Read source](../sources/cursor--plugins-pstack/pstack/skills/tdd/SKILL.md) · published skill source · 42 lines

Source description: Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is unclear, expensive, integration-heavy, or not requested.

Section preview: Workflow; If a Failing Test Is Impractical; Guardrails; Final Response

### teach

[Read source](../sources/cursor--plugins-pstack/pstack/skills/teach/SKILL.md) · published skill source · 21 lines

Source description: Explain a body of work plainly so a person actually understands it. Runs the `how` and `why` skills and weaves what they find into one clear explanation. Use for 'teach me this', 'help me really understand X', 'explain this change or subsystem to me'.

### technical-writing

[Read source](../sources/cursor--plugins-pstack/pstack/skills/technical-writing/SKILL.md) · published skill source · 106 lines

Source description: Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for /technical-writing or when writing or reviewing docs, RFCs, readmes, PR descriptions, or commit messages.

Section preview: Vary the rhythm; Pick the mode first (Diátaxis); Write sentences to the reader (Google developer style); Make statements load one at a time (STE rules); Leave no sentence open to two readings (Global English); Voice and repo specifics; Worked example

### typescript-best-practices

[Read source](../sources/cursor--plugins-pstack/pstack/skills/typescript-best-practices/SKILL.md) · published skill source · 31 lines

Source description: TypeScript best practices. Use when reading or editing any .ts or .tsx file.

### unslop

[Read source](../sources/cursor--plugins-pstack/pstack/skills/unslop/SKILL.md) · published skill source · 62 lines

Source description: Cut AI tells from any writing.

Section preview: Patterns to detect and fix; Content; Language; Style; Communication artifacts; Filler; Jargon; Plain speech

### why

[Read source](../sources/cursor--plugins-pstack/pstack/skills/why/SKILL.md) · published skill source · 98 lines

Source description: Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence category (source control, issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking, product analytics warehouse) in parallel, then returns a cited read on decisions and tradeoffs. Use how for runtime behavior.

Section preview: Operating Posture; Step 1. Understand the Target and the Question; Step 2. Establish the Code Anchor; Step 3. Spawn Parallel Investigators; Discovery; Investigator roster, one per available evidence category; When to skip an investigator; Step 4. Synthesize; Step 5. Present; Output Format; Common Failure Modes to Avoid


## garrytan--gstack

59 skill paths at `c7ae63201ab193a7dc7fb7e0d81238645111ffac`.

### gstack router

[Read source](../sources/garrytan--gstack/SKILL.md) · published skill source · 992 lines

Source description: Fast headless browser for QA testing and site dogfooding. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last); Plan Status Footer …

### autoplan

[Read source](../sources/garrytan--gstack/autoplan/SKILL.md) · published skill source · 1823 lines

Source description: Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### benchmark-models

[Read source](../sources/garrytan--gstack/benchmark-models/SKILL.md) · published skill source · 631 lines

Source description: Cross-model benchmark for gstack skills. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last); Plan Status Footer …

### benchmark

[Read source](../sources/garrytan--gstack/benchmark/SKILL.md) · published skill source · 756 lines

Source description: Performance regression detection using the browse daemon. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last); Plan Status Footer …

### browse

[Read source](../sources/garrytan--gstack/browse/SKILL.md) · published skill source · 993 lines

Source description: Fast headless browser for QA testing and site dogfooding. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last); Plan Status Footer …

### hackernews-frontpage

[Read source](../sources/garrytan--gstack/browser-skills/hackernews-frontpage/SKILL.md) · published skill source · 52 lines

Source description: Scrape the Hacker News front page (titles, points, comment counts).

Section preview: Usage; How it works; Why this is the reference skill

### canary

[Read source](../sources/garrytan--gstack/canary/SKILL.md) · published skill source · 1023 lines

Source description: Post-deploy canary monitoring. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### careful

[Read source](../sources/garrytan--gstack/careful/SKILL.md) · published skill source · 67 lines

Source description: Safety guardrails for destructive commands. (gstack)

Section preview: When to invoke this skill; What's protected; Safe exceptions; How it works

### codex

[Read source](../sources/garrytan--gstack/codex/SKILL.md) · published skill source · 1567 lines

Source description: OpenAI Codex CLI wrapper — three modes. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### context-restore

[Read source](../sources/garrytan--gstack/context-restore/SKILL.md) · published skill source · 881 lines

Source description: Restore working context saved earlier by /context-save. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### context-save

[Read source](../sources/garrytan--gstack/context-save/SKILL.md) · published skill source · 999 lines

Source description: Save working context. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### cso

[Read source](../sources/garrytan--gstack/cso/SKILL.md) · published skill source · 1256 lines

Source description: Chief Security Officer mode. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### design-consultation

[Read source](../sources/garrytan--gstack/design-consultation/SKILL.md) · published skill source · 1201 lines

Source description: Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview... (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### design-html

[Read source](../sources/garrytan--gstack/design-html/SKILL.md) · published skill source · 1482 lines

Source description: Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### design-review

[Read source](../sources/garrytan--gstack/design-review/SKILL.md) · published skill source · 1965 lines

Source description: Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### design-shotgun

[Read source](../sources/garrytan--gstack/design-shotgun/SKILL.md) · published skill source · 1344 lines

Source description: Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### devex-review

[Read source](../sources/garrytan--gstack/devex-review/SKILL.md) · published skill source · 1276 lines

Source description: Live developer experience audit. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### diagram

[Read source](../sources/garrytan--gstack/diagram/SKILL.md) · published skill source · 894 lines

Source description: Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### document-generate

[Read source](../sources/garrytan--gstack/document-generate/SKILL.md) · published skill source · 1223 lines

Source description: Generate missing documentation from scratch for a feature, module, or entire project. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### document-release

[Read source](../sources/garrytan--gstack/document-release/SKILL.md) · published skill source · 932 lines

Source description: Post-ship documentation update. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### freeze

[Read source](../sources/garrytan--gstack/freeze/SKILL.md) · published skill source · 91 lines

Source description: Restrict file edits to a specific directory for the session. (gstack)

Section preview: When to invoke this skill; Setup; How it works; Notes

### gstack-upgrade

[Read source](../sources/garrytan--gstack/gstack-upgrade/SKILL.md) · published skill source · 284 lines

Source description: Upgrade gstack to the latest version.

Section preview: When to invoke this skill; Inline upgrade flow; Step 1: Ask the user (or auto-upgrade); Step 2: Detect install type; Step 3: Save old version; Step 4: Upgrade; Step 4.5: Handle local vendored copy; Step 4.75: Run version migrations; Step 5: Write marker + clear cache; Step 6: Show What's New; Step 7: Continue; Standalone usage

### guard

[Read source](../sources/garrytan--gstack/guard/SKILL.md) · published skill source · 90 lines

Source description: Full safety mode: destructive command warnings + directory-scoped edits. (gstack)

Section preview: When to invoke this skill; Setup; What's protected

### health

[Read source](../sources/garrytan--gstack/health/SKILL.md) · published skill source · 1047 lines

Source description: Code quality dashboard. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### investigate

[Read source](../sources/garrytan--gstack/investigate/SKILL.md) · published skill source · 1045 lines

Source description: Systematic debugging with root cause investigation. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ios-clean

[Read source](../sources/garrytan--gstack/ios-clean/SKILL.md) · published skill source · 846 lines

Source description: Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ios-design-review

[Read source](../sources/garrytan--gstack/ios-design-review/SKILL.md) · published skill source · 848 lines

Source description: Visual design audit for iOS apps on real hardware. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ios-fix

[Read source](../sources/garrytan--gstack/ios-fix/SKILL.md) · published skill source · 844 lines

Source description: Autonomous iOS bug fixer. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ios-qa

[Read source](../sources/garrytan--gstack/ios-qa/SKILL.md) · published skill source · 964 lines

Source description: Live-device iOS QA for SwiftUI apps. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ios-sync

[Read source](../sources/garrytan--gstack/ios-sync/SKILL.md) · published skill source · 837 lines

Source description: Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### land-and-deploy

[Read source](../sources/garrytan--gstack/land-and-deploy/SKILL.md) · published skill source · 1889 lines

Source description: Land and deploy workflow. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### landing-report

[Read source](../sources/garrytan--gstack/landing-report/SKILL.md) · published skill source · 907 lines

Source description: Read-only queue dashboard for workspace-aware ship. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### learn

[Read source](../sources/garrytan--gstack/learn/SKILL.md) · published skill source · 924 lines

Source description: Manage project learnings.

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### make-pdf

[Read source](../sources/garrytan--gstack/make-pdf/SKILL.md) · published skill source · 758 lines

Source description: Turn any markdown file into a publication-quality PDF. (gstack)

Section preview: When to invoke this skill; Preamble (run first); MAKE-PDF SETUP (run this check BEFORE any make-pdf command); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last) …

### office-hours

[Read source](../sources/garrytan--gstack/office-hours/SKILL.md) · published skill source · 1668 lines

Source description: YC Office Hours — two modes. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### open-gstack-browser

[Read source](../sources/garrytan--gstack/open-gstack-browser/SKILL.md) · published skill source · 987 lines

Source description: Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### gstack-openclaw-ceo-review

[Read source](../sources/garrytan--gstack/openclaw/skills/gstack-openclaw-ceo-review/SKILL.md) · OpenClaw runtime variant · 191 lines

Source description: Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the plan.

Section preview: Philosophy; Prime Directives; Cognitive Patterns... How Great CEOs Think; Step 0: Nuclear Scope Challenge + Mode Selection; 0A. Premise Challenge; 0B. Existing Code Leverage; 0C. Dream State Mapping; 0C-bis. Implementation Alternatives (MANDATORY); 0D. Mode-Specific Analysis; 0E. Temporal Interrogation; 0F. Mode Selection; Review Sections (11 sections, after scope and mode are agreed) …

### gstack-openclaw-investigate

[Read source](../sources/garrytan--gstack/openclaw/skills/gstack-openclaw-investigate/SKILL.md) · OpenClaw runtime variant · 134 lines

Source description: Use when asked to debug, fix a bug, investigate an error, or do root cause analysis, and when users report errors, stack traces, unexpected behavior, or say something stopped working.

Section preview: Iron Law; Phase 1: Root Cause Investigation; Phase 2: Pattern Analysis; Phase 3: Hypothesis Testing; Phase 4: Implementation; Phase 5: Verification & Report; Important Rules

### gstack-openclaw-office-hours

[Read source](../sources/garrytan--gstack/openclaw/skills/gstack-openclaw-office-hours/SKILL.md) · OpenClaw runtime variant · 373 lines

Source description: Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is written.

Section preview: Phase 1: Context Gathering; Phase 2A: Startup Mode — YC Product Diagnostic; Operating Principles; Response Posture; Anti-Sycophancy Rules; Pushback Patterns; The Six Forcing Questions; Phase 2B: Builder Mode — Design Partner; Operating Principles; Response Posture; Questions (generative, not interrogative); Phase 3: Premise Challenge …

### gstack-openclaw-retro

[Read source](../sources/garrytan--gstack/openclaw/skills/gstack-openclaw-retro/SKILL.md) · OpenClaw runtime variant · 299 lines

Source description: Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking. Team-aware with per-person contributions, praise, and growth areas. Use when asked for weekly retro, what shipped this week, or engineering retrospective.

Section preview: Arguments; Instructions; Step 1: Gather Raw Data; Step 2: Compute Metrics; Step 3: Commit Time Distribution; Step 4: Work Session Detection; Step 5: Commit Type Breakdown; Step 6: Hotspot Analysis; Step 7: PR Size Distribution; Step 8: Focus Score + Ship of the Week; Step 9: Team Member Analysis; Step 10: Week-over-Week Trends (if window >= 14d) …

### pair-agent

[Read source](../sources/garrytan--gstack/pair-agent/SKILL.md) · published skill source · 1043 lines

Source description: Pair a remote AI agent with your browser. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### plan-ceo-review

[Read source](../sources/garrytan--gstack/plan-ceo-review/SKILL.md) · published skill source · 1447 lines

Source description: CEO/founder-mode plan review. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### plan-design-review

[Read source](../sources/garrytan--gstack/plan-design-review/SKILL.md) · published skill source · 1468 lines

Source description: Designer's eye plan review — interactive, like CEO and Eng review. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### plan-devex-review

[Read source](../sources/garrytan--gstack/plan-devex-review/SKILL.md) · published skill source · 1431 lines

Source description: Interactive developer experience plan review. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### plan-eng-review

[Read source](../sources/garrytan--gstack/plan-eng-review/SKILL.md) · published skill source · 1003 lines

Source description: Eng manager-mode plan review. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### plan-tune

[Read source](../sources/garrytan--gstack/plan-tune/SKILL.md) · published skill source · 1384 lines

Source description: Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### qa-only

[Read source](../sources/garrytan--gstack/qa-only/SKILL.md) · published skill source · 1227 lines

Source description: Report-only QA testing. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### qa

[Read source](../sources/garrytan--gstack/qa/SKILL.md) · published skill source · 1655 lines

Source description: Systematically QA test a web application and fix bugs found. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### retro

[Read source](../sources/garrytan--gstack/retro/SKILL.md) · published skill source · 1783 lines

Source description: Weekly engineering retrospective. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### review

[Read source](../sources/garrytan--gstack/review/SKILL.md) · published skill source · 1823 lines

Source description: Pre-landing PR review. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### scrape

[Read source](../sources/garrytan--gstack/scrape/SKILL.md) · published skill source · 920 lines

Source description: Pull data from a web page. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### setup-browser-cookies

[Read source](../sources/garrytan--gstack/setup-browser-cookies/SKILL.md) · published skill source · 603 lines

Source description: Import cookies from your real Chromium browser into the headless browse session. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; Artifacts Sync (skill start); Model-Specific Behavioral Patch (claude); Voice; Completion Status Protocol; Operational Self-Improvement; Telemetry (run last); Plan Status Footer …

### setup-deploy

[Read source](../sources/garrytan--gstack/setup-deploy/SKILL.md) · published skill source · 952 lines

Source description: Configure deployment settings for /land-and-deploy.

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### setup-gbrain

[Read source](../sources/garrytan--gstack/setup-gbrain/SKILL.md) · published skill source · 1806 lines

Source description: Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### ship

[Read source](../sources/garrytan--gstack/ship/SKILL.md) · published skill source · 1331 lines

Source description: Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### skillify

[Read source](../sources/garrytan--gstack/skillify/SKILL.md) · published skill source · 1201 lines

Source description: Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### spec

[Read source](../sources/garrytan--gstack/spec/SKILL.md) · published skill source · 2301 lines

Source description: Turn vague intent into a precise, executable spec in five phases. (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### sync-gbrain

[Read source](../sources/garrytan--gstack/sync-gbrain/SKILL.md) · published skill source · 1203 lines

Source description: Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack)

Section preview: When to invoke this skill; Preamble (run first); Plan Mode Safe Operations; Skill Invocation During Plan Mode; Skill routing; AskUserQuestion Format; Tool resolution (read first); When AskUserQuestion is unavailable or a call fails; Format; Handling 5+ options — split, never drop; Self-check before emitting; Artifacts Sync (skill start) …

### unfreeze

[Read source](../sources/garrytan--gstack/unfreeze/SKILL.md) · published skill source · 48 lines

Source description: Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack)

Section preview: When to invoke this skill; Clear the boundary


## anthropic--skills

17 skill paths at `690f15cac7f7b4c055c5ab109c79ed9259934081`.

### algorithmic-art

[Read source](../sources/anthropic--skills/skills/algorithmic-art/SKILL.md) · published skill source · 405 lines

Source description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

Section preview: ALGORITHMIC PHILOSOPHY CREATION; THE CRITICAL UNDERSTANDING; HOW TO GENERATE AN ALGORITHMIC PHILOSOPHY; PHILOSOPHY EXAMPLES; ESSENTIAL PRINCIPLES; DEDUCING THE CONCEPTUAL SEED; P5.JS IMPLEMENTATION; ⚠️ STEP 0: READ THE TEMPLATE FIRST ⚠️; TECHNICAL REQUIREMENTS; CRAFTSMANSHIP REQUIREMENTS; OUTPUT FORMAT; INTERACTIVE ARTIFACT CREATION …

### brand-guidelines

[Read source](../sources/anthropic--skills/skills/brand-guidelines/SKILL.md) · published skill source · 73 lines

Source description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

Section preview: Overview; Brand Guidelines; Colors; Typography; Features; Smart Font Application; Text Styling; Shape and Accent Colors; Technical Details; Font Management; Color Application

### canvas-design

[Read source](../sources/anthropic--skills/skills/canvas-design/SKILL.md) · published skill source · 130 lines

Source description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

Section preview: DESIGN PHILOSOPHY CREATION; THE CRITICAL UNDERSTANDING; HOW TO GENERATE A VISUAL PHILOSOPHY; PHILOSOPHY EXAMPLES; ESSENTIAL PRINCIPLES; DEDUCING THE SUBTLE REFERENCE; CANVAS CREATION; FINAL STEP; MULTI-PAGE OPTION

### claude-api

[Read source](../sources/anthropic--skills/skills/claude-api/SKILL.md) · published skill source · 324 lines

Source description: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

Section preview: Before You Start; Output Requirement; Defaults; Subcommands; Language Detection; Language-Specific Feature Support; Which Surface Should I Use?; Decision Tree; Should I Build an Agent?; Architecture; Current Models (cached: 2026-04-15); Thinking & Effort (Quick Reference) …

### doc-coauthoring

[Read source](../sources/anthropic--skills/skills/doc-coauthoring/SKILL.md) · published skill source · 375 lines

Source description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

Section preview: When to Offer This Workflow; Stage 1: Context Gathering; Initial Questions; Info Dumping; Stage 2: Refinement & Structure; Step 1: Clarifying Questions; Step 2: Brainstorming; Step 3: Curation; Step 4: Gap Check; Step 5: Drafting; Step 6: Iterative Refinement; Quality Checking …

### docx

[Read source](../sources/anthropic--skills/skills/docx/SKILL.md) · published skill source · 590 lines

Source description: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

Section preview: Overview; Quick Reference; Converting .doc to .docx; Reading Content; Converting to Images; Accepting Tracked Changes; Creating New Documents; Setup; Validation; Page Size; Styles (Override Built-in Headings); Lists (NEVER use unicode bullets) …

### frontend-design

[Read source](../sources/anthropic--skills/skills/frontend-design/SKILL.md) · published skill source · 42 lines

Source description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

Section preview: Design Thinking; Frontend Aesthetics Guidelines

### internal-comms

[Read source](../sources/anthropic--skills/skills/internal-comms/SKILL.md) · published skill source · 32 lines

Source description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

Section preview: When to use this skill; How to use this skill; Keywords

### mcp-builder

[Read source](../sources/anthropic--skills/skills/mcp-builder/SKILL.md) · published skill source · 236 lines

Source description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

Section preview: Overview; 🚀 High-Level Workflow; Phase 1: Deep Research and Planning; Phase 2: Implementation; Phase 3: Review and Test; Phase 4: Create Evaluations; 📚 Documentation Library; Core MCP Documentation (Load First); SDK Documentation (Load During Phase 1/2); Language-Specific Implementation Guides (Load During Phase 2); Evaluation Guide (Load During Phase 4)

### pdf

[Read source](../sources/anthropic--skills/skills/pdf/SKILL.md) · published skill source · 314 lines

Source description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

Section preview: Overview; Quick Start; Python Libraries; pypdf - Basic Operations; pdfplumber - Text and Table Extraction; reportlab - Create PDFs; Command-Line Tools; pdftotext (poppler-utils); qpdf; pdftk (if available); Common Tasks; Extract Text from Scanned PDFs …

### pptx

[Read source](../sources/anthropic--skills/skills/pptx/SKILL.md) · published skill source · 232 lines

Source description: Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

Section preview: Quick Reference; Reading Content; Editing Workflow; Creating from Scratch; Design Ideas; Before Starting; Color Palettes; For Each Slide; Typography; Spacing; Avoid (Common Mistakes); QA (Required) …

### skill-creator

[Read source](../sources/anthropic--skills/skills/skill-creator/SKILL.md) · published skill source · 485 lines

Source description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

Section preview: Communicating with the user; Creating a skill; Capture Intent; Interview and Research; Write the SKILL.md; Skill Writing Guide; Report structure; Executive summary; Key findings; Recommendations; Commit message format; Writing Style …

### slack-gif-creator

[Read source](../sources/anthropic--skills/skills/slack-gif-creator/SKILL.md) · published skill source · 254 lines

Source description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

Section preview: Slack Requirements; Core Workflow; Drawing Graphics; Working with User-Uploaded Images; Drawing from Scratch; Making Graphics Look Good; Available Utilities; GIFBuilder (`core.gif_builder`); Validators (`core.validators`); Easing Functions (`core.easing`); Frame Helpers (`core.frame_composer`); Animation Concepts …

### theme-factory

[Read source](../sources/anthropic--skills/skills/theme-factory/SKILL.md) · published skill source · 59 lines

Source description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

Section preview: Purpose; Usage Instructions; Themes Available; Theme Details; Application Process; Create your Own Theme

### web-artifacts-builder

[Read source](../sources/anthropic--skills/skills/web-artifacts-builder/SKILL.md) · published skill source · 74 lines

Source description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

Section preview: Design & Style Guidelines; Quick Start; Step 1: Initialize Project; Step 2: Develop Your Artifact; Step 3: Bundle to Single HTML File; Step 4: Share Artifact with User; Step 5: Testing/Visualizing the Artifact (Optional); Reference

### webapp-testing

[Read source](../sources/anthropic--skills/skills/webapp-testing/SKILL.md) · published skill source · 96 lines

Source description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

Section preview: Decision Tree: Choosing Your Approach; Example: Using with_server.py; Reconnaissance-Then-Action Pattern; Common Pitfall; Best Practices; Reference Files

### xlsx

[Read source](../sources/anthropic--skills/skills/xlsx/SKILL.md) · published skill source · 292 lines

Source description: Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

Section preview: All Excel files; Professional Font; Zero Formula Errors; Preserve Existing Templates (when updating templates); Financial models; Color Coding Standards; Number Formatting Standards; Formula Construction Rules; Overview; Important Requirements; Reading and analyzing data; Data analysis with pandas …


## prodmgmt-world--pm-os-cowork

235 skill paths at `package 2.2.1`.

### 1-on-1

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/1-on-1/SKILL.md) · purchased package; analyze rather than redistribute · 380 lines

### 5-step-story-deck

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/5-step-story-deck/SKILL.md) · purchased package; analyze rather than redistribute · 82 lines

### adhd-action-summary

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/adhd-action-summary/SKILL.md) · purchased package; analyze rather than redistribute · 72 lines

### adhd-motivation

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/adhd-motivation/SKILL.md) · purchased package; analyze rather than redistribute · 75 lines

### adversarial-roleplay

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/adversarial-roleplay/SKILL.md) · purchased package; analyze rather than redistribute · 137 lines

### affordances-signifiers

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/affordances-signifiers/SKILL.md) · purchased package; analyze rather than redistribute · 51 lines

### aha-moment

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/aha-moment/SKILL.md) · purchased package; analyze rather than redistribute · 80 lines

### ai-recommendation-canvas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ai-recommendation-canvas/SKILL.md) · purchased package; analyze rather than redistribute · 73 lines

### ai-tutor

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ai-tutor/SKILL.md) · purchased package; analyze rather than redistribute · 92 lines

### app-design-foundation

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/app-design-foundation/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### assumptions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/assumptions/SKILL.md) · purchased package; analyze rather than redistribute · 58 lines

### blind-spot-scan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/blind-spot-scan/SKILL.md) · purchased package; analyze rather than redistribute · 165 lines

### brainstorm-genius

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/brainstorm-genius/SKILL.md) · purchased package; analyze rather than redistribute · 153 lines

### breadboard-reflection

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/breadboard-reflection/SKILL.md) · purchased package; analyze rather than redistribute · 210 lines

### breadboarding

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/breadboarding/SKILL.md) · purchased package; analyze rather than redistribute · 1657 lines

### brief-to-problem

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/brief-to-problem/SKILL.md) · purchased package; analyze rather than redistribute · 442 lines

### bug-triage

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/bug-triage/SKILL.md) · purchased package; analyze rather than redistribute · 71 lines

### business-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/business-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 52 lines

### career-guidance

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/career-guidance/SKILL.md) · purchased package; analyze rather than redistribute · 75 lines

### causal-tree

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/causal-tree/SKILL.md) · purchased package; analyze rather than redistribute · 72 lines

### churn-reduction

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/churn-reduction/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### cialdini

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/cialdini/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### clarification-chain

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/clarification-chain/SKILL.md) · purchased package; analyze rather than redistribute · 176 lines

### clickable-prototype

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/clickable-prototype/SKILL.md) · purchased package; analyze rather than redistribute · 65 lines

### coaching

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/coaching/SKILL.md) · purchased package; analyze rather than redistribute · 60 lines

### comms-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/comms-plan/SKILL.md) · purchased package; analyze rather than redistribute · 71 lines

### constrained-ideas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/constrained-ideas/SKILL.md) · purchased package; analyze rather than redistribute · 114 lines

### corporate-misalignment-finder

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/corporate-misalignment-finder/SKILL.md) · purchased package; analyze rather than redistribute · 208 lines

### create-empathy-maps

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/create-empathy-maps/SKILL.md) · purchased package; analyze rather than redistribute · 69 lines

### crisis-comms

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/crisis-comms/SKILL.md) · purchased package; analyze rather than redistribute · 74 lines

### critical-decision-method

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/critical-decision-method/SKILL.md) · purchased package; analyze rather than redistribute · 120 lines

### cta-copy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/cta-copy/SKILL.md) · purchased package; analyze rather than redistribute · 60 lines

### davci

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/davci/SKILL.md) · purchased package; analyze rather than redistribute · 153 lines

### decision-audit

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/decision-audit/SKILL.md) · purchased package; analyze rather than redistribute · 139 lines

### decision-journal

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/decision-journal/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### decisions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/decisions/SKILL.md) · purchased package; analyze rather than redistribute · 91 lines

### demo-narrative

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/demo-narrative/SKILL.md) · purchased package; analyze rather than redistribute · 527 lines

### design-critique

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/design-critique/SKILL.md) · purchased package; analyze rather than redistribute · 65 lines

### difficult-conversation

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/difficult-conversation/SKILL.md) · purchased package; analyze rather than redistribute · 58 lines

### disruption-what-ifs

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/disruption-what-ifs/SKILL.md) · purchased package; analyze rather than redistribute · 74 lines

### edge-case-balance

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/edge-case-balance/SKILL.md) · purchased package; analyze rather than redistribute · 80 lines

### eng-solution

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/eng-solution/SKILL.md) · purchased package; analyze rather than redistribute · 36 lines

### exec-deck

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/exec-deck/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### exec-feedback

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/exec-feedback/SKILL.md) · purchased package; analyze rather than redistribute · 205 lines

### exec-update-review

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/exec-update-review/SKILL.md) · purchased package; analyze rather than redistribute · 56 lines

### experiment-design

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/experiment-design/SKILL.md) · purchased package; analyze rather than redistribute · 111 lines

### expert-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/expert-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 102 lines

### feature-writeup

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/feature-writeup/SKILL.md) · purchased package; analyze rather than redistribute · 68 lines

### feedback-loop

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/feedback-loop/SKILL.md) · purchased package; analyze rather than redistribute · 485 lines

### fermi-decomposition

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/fermi-decomposition/SKILL.md) · purchased package; analyze rather than redistribute · 198 lines

### find-the-strategic-crux

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/find-the-strategic-crux/SKILL.md) · purchased package; analyze rather than redistribute · 77 lines

### flywheel

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/flywheel/SKILL.md) · purchased package; analyze rather than redistribute · 76 lines

### focal-point-finder

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/focal-point-finder/SKILL.md) · purchased package; analyze rather than redistribute · 205 lines

### founder-focus

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/founder-focus/SKILL.md) · purchased package; analyze rather than redistribute · 54 lines

### friction-reduce

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/friction-reduce/SKILL.md) · purchased package; analyze rather than redistribute · 551 lines

### frontend-slides

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/frontend-slides/SKILL.md) · purchased package; analyze rather than redistribute · 325 lines

### gherkin-stories

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/gherkin-stories/SKILL.md) · purchased package; analyze rather than redistribute · 118 lines

### good-question-brainstormer

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/good-question-brainstormer/SKILL.md) · purchased package; analyze rather than redistribute · 99 lines

### growth-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/growth-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### gut-check

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/gut-check/SKILL.md) · purchased package; analyze rather than redistribute · 114 lines

### hidden-agendas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/hidden-agendas/SKILL.md) · purchased package; analyze rather than redistribute · 70 lines

### icp-roleplay

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/icp-roleplay/SKILL.md) · purchased package; analyze rather than redistribute · 67 lines

### impact-model

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/impact-model/SKILL.md) · purchased package; analyze rather than redistribute · 86 lines

### impact-sizing

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/impact-sizing/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### import-ai-memory

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/import-ai-memory/SKILL.md) · purchased package; analyze rather than redistribute · 156 lines

### industry-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/industry-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### inflection-scan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/inflection-scan/SKILL.md) · purchased package; analyze rather than redistribute · 86 lines

### interface-4-lenses

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/interface-4-lenses/SKILL.md) · purchased package; analyze rather than redistribute · 44 lines

### interview-guide

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/interview-guide/SKILL.md) · purchased package; analyze rather than redistribute · 110 lines

### interview-insights

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/interview-insights/SKILL.md) · purchased package; analyze rather than redistribute · 87 lines

### interview-notes

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/interview-notes/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### intuition-to-research

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/intuition-to-research/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### journey-map

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/journey-map/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### jtbd-forces

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/jtbd-forces/SKILL.md) · purchased package; analyze rather than redistribute · 87 lines

### jtbd-jobs

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/jtbd-jobs/SKILL.md) · purchased package; analyze rather than redistribute · 69 lines

### jtbd-market-canvas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/jtbd-market-canvas/SKILL.md) · purchased package; analyze rather than redistribute · 81 lines

### jtbd-transcript-sim

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/jtbd-transcript-sim/SKILL.md) · purchased package; analyze rather than redistribute · 86 lines

### lateral-thinking

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/lateral-thinking/SKILL.md) · purchased package; analyze rather than redistribute · 68 lines

### leadership-presence

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/leadership-presence/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### life-design-mapping-exercise

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/life-design-mapping-exercise/SKILL.md) · purchased package; analyze rather than redistribute · 67 lines

### limit-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/limit-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 82 lines

### mckinsey-issue-tree

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/mckinsey-issue-tree/SKILL.md) · purchased package; analyze rather than redistribute · 350 lines

### measure

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/measure/SKILL.md) · purchased package; analyze rather than redistribute · 117 lines

### mece-tree

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/mece-tree/SKILL.md) · purchased package; analyze rather than redistribute · 71 lines

### meeting

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/meeting/SKILL.md) · purchased package; analyze rather than redistribute · 53 lines

### meeting-agenda

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/meeting-agenda/SKILL.md) · purchased package; analyze rather than redistribute · 46 lines

### meeting-outcomes

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/meeting-outcomes/SKILL.md) · purchased package; analyze rather than redistribute · 114 lines

### meeting-prep

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/meeting-prep/SKILL.md) · purchased package; analyze rather than redistribute · 72 lines

### meeting-summary

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/meeting-summary/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### metaphor-thinking

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/metaphor-thinking/SKILL.md) · purchased package; analyze rather than redistribute · 55 lines

### metric-drop

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/metric-drop/SKILL.md) · purchased package; analyze rather than redistribute · 181 lines

### mindset-shift

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/mindset-shift/SKILL.md) · purchased package; analyze rather than redistribute · 50 lines

### miro-workshop

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/miro-workshop/SKILL.md) · purchased package; analyze rather than redistribute · 126 lines

### moats

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/moats/SKILL.md) · purchased package; analyze rather than redistribute · 77 lines

### mom-test-guide

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/mom-test-guide/SKILL.md) · purchased package; analyze rather than redistribute · 61 lines

### motivation-journal

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/motivation-journal/SKILL.md) · purchased package; analyze rather than redistribute · 61 lines

### motivational-interview

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/motivational-interview/SKILL.md) · purchased package; analyze rather than redistribute · 172 lines

### mrd

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/mrd/SKILL.md) · purchased package; analyze rather than redistribute · 195 lines

### netmba-competitor-analysis

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/netmba-competitor-analysis/SKILL.md) · purchased package; analyze rather than redistribute · 117 lines

### niche-finder

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/niche-finder/SKILL.md) · purchased package; analyze rather than redistribute · 51 lines

### now-next-later

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/now-next-later/SKILL.md) · purchased package; analyze rather than redistribute · 58 lines

### nps-to-cx-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/nps-to-cx-plan/SKILL.md) · purchased package; analyze rather than redistribute · 86 lines

### objection-scan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/objection-scan/SKILL.md) · purchased package; analyze rather than redistribute · 101 lines

### offbeat-questions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/offbeat-questions/SKILL.md) · purchased package; analyze rather than redistribute · 59 lines

### office-politics

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/office-politics/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### onboarding-redesign

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/onboarding-redesign/SKILL.md) · purchased package; analyze rather than redistribute · 81 lines

### opportunity

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/opportunity/SKILL.md) · purchased package; analyze rather than redistribute · 75 lines

### orchestrate-pm-alignment

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/orchestrate-pm-alignment/SKILL.md) · purchased package; analyze rather than redistribute · 112 lines

### ost

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ost/SKILL.md) · purchased package; analyze rather than redistribute · 101 lines

### ost-choose

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ost-choose/SKILL.md) · purchased package; analyze rather than redistribute · 156 lines

### ost-intake

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ost-intake/SKILL.md) · purchased package; analyze rather than redistribute · 122 lines

### ost-prioritize

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ost-prioritize/SKILL.md) · purchased package; analyze rather than redistribute · 154 lines

### p0-p1-p2

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/p0-p1-p2/SKILL.md) · purchased package; analyze rather than redistribute · 289 lines

### parity-vs-differentiation

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/parity-vs-differentiation/SKILL.md) · purchased package; analyze rather than redistribute · 238 lines

### persona-lens-decision

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/persona-lens-decision/SKILL.md) · purchased package; analyze rather than redistribute · 77 lines

### pioneer-migrator-settler

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pioneer-migrator-settler/SKILL.md) · purchased package; analyze rather than redistribute · 85 lines

### pm-help

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-help/SKILL.md) · purchased package; analyze rather than redistribute · 97 lines

### pm-interview

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-interview/SKILL.md) · purchased package; analyze rather than redistribute · 459 lines

### pm-os-capture-memory

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-capture-memory/SKILL.md) · purchased package; analyze rather than redistribute · 163 lines

### pm-os-daily-drip

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-daily-drip/SKILL.md) · purchased package; analyze rather than redistribute · 103 lines

### pm-os-feedback

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-feedback/SKILL.md) · purchased package; analyze rather than redistribute · 71 lines

### pm-os-framework

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-framework/SKILL.md) · purchased package; analyze rather than redistribute · 47 lines

### pm-os-project

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-project/SKILL.md) · purchased package; analyze rather than redistribute · 178 lines

### pm-os-skill

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-skill/SKILL.md) · purchased package; analyze rather than redistribute · 31 lines

### pm-os-start

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-start/SKILL.md) · purchased package; analyze rather than redistribute · 469 lines

### pm-os-testimonial

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-testimonial/SKILL.md) · purchased package; analyze rather than redistribute · 101 lines

### pm-os-tidy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-tidy/SKILL.md) · purchased package; analyze rather than redistribute · 46 lines

### pm-os-upgrade

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-os-upgrade/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### pm-review

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-review/SKILL.md) · purchased package; analyze rather than redistribute · 292 lines

### pm-status

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-status/SKILL.md) · purchased package; analyze rather than redistribute · 46 lines

### pm-to-design

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pm-to-design/SKILL.md) · purchased package; analyze rather than redistribute · 159 lines

### positioning

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/positioning/SKILL.md) · purchased package; analyze rather than redistribute · 91 lines

### power-map

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/power-map/SKILL.md) · purchased package; analyze rather than redistribute · 75 lines

### power-user-shift

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/power-user-shift/SKILL.md) · purchased package; analyze rather than redistribute · 104 lines

### prd

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/prd/SKILL.md) · purchased package; analyze rather than redistribute · 251 lines

### prd-draft

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/prd-draft/SKILL.md) · purchased package; analyze rather than redistribute · 79 lines

### prd-enterprise

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/prd-enterprise/SKILL.md) · purchased package; analyze rather than redistribute · 80 lines

### presentation-narrative

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/presentation-narrative/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### press-release

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/press-release/SKILL.md) · purchased package; analyze rather than redistribute · 180 lines

### problem-deck

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/problem-deck/SKILL.md) · purchased package; analyze rather than redistribute · 77 lines

### problem-first

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/problem-first/SKILL.md) · purchased package; analyze rather than redistribute · 201 lines

### problem-framing-canvas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/problem-framing-canvas/SKILL.md) · purchased package; analyze rather than redistribute · 134 lines

### product-assumptions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/product-assumptions/SKILL.md) · purchased package; analyze rather than redistribute · 71 lines

### product-brainstorm

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/product-brainstorm/SKILL.md) · purchased package; analyze rather than redistribute · 62 lines

### product-design-analyzer

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/product-design-analyzer/SKILL.md) · purchased package; analyze rather than redistribute · 51 lines

### product-hypothesis

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/product-hypothesis/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### product-strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/product-strategy/SKILL.md) · purchased package; analyze rather than redistribute · 113 lines

### project-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/project-plan/SKILL.md) · purchased package; analyze rather than redistribute · 91 lines

### proto-persona

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/proto-persona/SKILL.md) · purchased package; analyze rather than redistribute · 146 lines

### pyramid-principle

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/pyramid-principle/SKILL.md) · purchased package; analyze rather than redistribute · 66 lines

### refinement-session

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/refinement-session/SKILL.md) · purchased package; analyze rather than redistribute · 114 lines

### reinforcing-sequence

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/reinforcing-sequence/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### requirements-from-design

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/requirements-from-design/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### requirements-from-talk

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/requirements-from-talk/SKILL.md) · purchased package; analyze rather than redistribute · 75 lines

### requirements-reconcile

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/requirements-reconcile/SKILL.md) · purchased package; analyze rather than redistribute · 358 lines

### research

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/research/SKILL.md) · purchased package; analyze rather than redistribute · 84 lines

### research-brief

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/research-brief/SKILL.md) · purchased package; analyze rather than redistribute · 61 lines

### research-decision

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/research-decision/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### research-recency

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/research-recency/SKILL.md) · purchased package; analyze rather than redistribute · 275 lines

### research-synthesis

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/research-synthesis/SKILL.md) · purchased package; analyze rather than redistribute · 485 lines

### resume

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/resume/SKILL.md) · purchased package; analyze rather than redistribute · 289 lines

### resume-skill-gaps

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/resume-skill-gaps/SKILL.md) · purchased package; analyze rather than redistribute · 123 lines

### risky-assumptions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/risky-assumptions/SKILL.md) · purchased package; analyze rather than redistribute · 117 lines

### rule-of-five

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/rule-of-five/SKILL.md) · purchased package; analyze rather than redistribute · 239 lines

### rulebook-for-arguments

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/rulebook-for-arguments/SKILL.md) · purchased package; analyze rather than redistribute · 468 lines

### scenario-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/scenario-plan/SKILL.md) · purchased package; analyze rather than redistribute · 125 lines

### scope-defense

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/scope-defense/SKILL.md) · purchased package; analyze rather than redistribute · 956 lines

### seven-powers

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/seven-powers/SKILL.md) · purchased package; analyze rather than redistribute · 195 lines

### shape-up

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/shape-up/SKILL.md) · purchased package; analyze rather than redistribute · 55 lines

### shaping

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/shaping/SKILL.md) · purchased package; analyze rather than redistribute · 596 lines

### situation-retrospective

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/situation-retrospective/SKILL.md) · purchased package; analyze rather than redistribute · 113 lines

### skill-acquisition

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/skill-acquisition/SKILL.md) · purchased package; analyze rather than redistribute · 82 lines

### skill-browser

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/skill-browser/SKILL.md) · purchased package; analyze rather than redistribute · 49 lines

### skill-coach

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/skill-coach/SKILL.md) · purchased package; analyze rather than redistribute · 30 lines

### skill-mastery

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/skill-mastery/SKILL.md) · purchased package; analyze rather than redistribute · 91 lines

### skimmable-writing

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/skimmable-writing/SKILL.md) · purchased package; analyze rather than redistribute · 95 lines

### slack-signal

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/slack-signal/SKILL.md) · purchased package; analyze rather than redistribute · 218 lines

### socratic-thinking

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/socratic-thinking/SKILL.md) · purchased package; analyze rather than redistribute · 116 lines

### solution-flaws

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/solution-flaws/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### sql-from-spec

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/sql-from-spec/SKILL.md) · purchased package; analyze rather than redistribute · 69 lines

### staff-or-intern

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/staff-or-intern/SKILL.md) · purchased package; analyze rather than redistribute · 99 lines

### stakeholder

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/stakeholder/SKILL.md) · purchased package; analyze rather than redistribute · 115 lines

### stakeholder-map

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/stakeholder-map/SKILL.md) · purchased package; analyze rather than redistribute · 78 lines

### stakeholder-risk

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/stakeholder-risk/SKILL.md) · purchased package; analyze rather than redistribute · 58 lines

### star-stories

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/star-stories/SKILL.md) · purchased package; analyze rather than redistribute · 62 lines

### startup-ideas

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/startup-ideas/SKILL.md) · purchased package; analyze rather than redistribute · 54 lines

### status-update

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/status-update/SKILL.md) · purchased package; analyze rather than redistribute · 412 lines

### strategic-deck

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/strategic-deck/SKILL.md) · purchased package; analyze rather than redistribute · 98 lines

### strategy

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/strategy/SKILL.md) · purchased package; analyze rather than redistribute · 87 lines

### strategy-kernel

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/strategy-kernel/SKILL.md) · purchased package; analyze rather than redistribute · 171 lines

### strategy-review-prep

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/strategy-review-prep/SKILL.md) · purchased package; analyze rather than redistribute · 66 lines

### structure-problem

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/structure-problem/SKILL.md) · purchased package; analyze rather than redistribute · 70 lines

### success-metric

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/success-metric/SKILL.md) · purchased package; analyze rather than redistribute · 191 lines

### superpowers

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/superpowers/SKILL.md) · purchased package; analyze rather than redistribute · 96 lines

### survey-to-actions

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/survey-to-actions/SKILL.md) · purchased package; analyze rather than redistribute · 85 lines

### swot-moves

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/swot-moves/SKILL.md) · purchased package; analyze rather than redistribute · 97 lines

### task-list-to-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/task-list-to-plan/SKILL.md) · purchased package; analyze rather than redistribute · 80 lines

### task-sequence

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/task-sequence/SKILL.md) · purchased package; analyze rather than redistribute · 102 lines

### team-perspective-reveal

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/team-perspective-reveal/SKILL.md) · purchased package; analyze rather than redistribute · 116 lines

### tech-arch-brief

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tech-arch-brief/SKILL.md) · purchased package; analyze rather than redistribute · 90 lines

### tech-sensemaking

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tech-sensemaking/SKILL.md) · purchased package; analyze rather than redistribute · 150 lines

### tech-to-business

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tech-to-business/SKILL.md) · purchased package; analyze rather than redistribute · 102 lines

### tickets-to-improvements

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tickets-to-improvements/SKILL.md) · purchased package; analyze rather than redistribute · 62 lines

### tidy-procedure

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tidy-procedure/SKILL.md) · purchased package; analyze rather than redistribute · 160 lines

### toc-thinking

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/toc-thinking/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### top-5-wins

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/top-5-wins/SKILL.md) · purchased package; analyze rather than redistribute · 56 lines

### tracking-schema

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tracking-schema/SKILL.md) · purchased package; analyze rather than redistribute · 65 lines

### tradeoff-matrix

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/tradeoff-matrix/SKILL.md) · purchased package; analyze rather than redistribute · 76 lines

### transcript-cleanup

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/transcript-cleanup/SKILL.md) · purchased package; analyze rather than redistribute · 50 lines

### transcript-insights

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/transcript-insights/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### two-way-door

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/two-way-door/SKILL.md) · purchased package; analyze rather than redistribute · 60 lines

### ui-acceptance-criteria

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ui-acceptance-criteria/SKILL.md) · purchased package; analyze rather than redistribute · 113 lines

### ui-to-json

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ui-to-json/SKILL.md) · purchased package; analyze rather than redistribute · 80 lines

### use-case-map

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/use-case-map/SKILL.md) · purchased package; analyze rather than redistribute · 70 lines

### use-cases

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/use-cases/SKILL.md) · purchased package; analyze rather than redistribute · 809 lines

### user-profile

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/user-profile/SKILL.md) · purchased package; analyze rather than redistribute · 188 lines

### user-stories

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/user-stories/SKILL.md) · purchased package; analyze rather than redistribute · 56 lines

### ux-edge-cases

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ux-edge-cases/SKILL.md) · purchased package; analyze rather than redistribute · 67 lines

### ux-terminology

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/ux-terminology/SKILL.md) · purchased package; analyze rather than redistribute · 63 lines

### v2-plan

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/v2-plan/SKILL.md) · purchased package; analyze rather than redistribute · 648 lines

### value-chain

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/value-chain/SKILL.md) · purchased package; analyze rather than redistribute · 83 lines

### value-of-information

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/value-of-information/SKILL.md) · purchased package; analyze rather than redistribute · 239 lines

### verbalized-sampling

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/verbalized-sampling/SKILL.md) · purchased package; analyze rather than redistribute · 156 lines

### via-negativa

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/via-negativa/SKILL.md) · purchased package; analyze rather than redistribute · 77 lines

### vibe-code-leaf-finder

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/vibe-code-leaf-finder/SKILL.md) · purchased package; analyze rather than redistribute · 126 lines

### vision-to-okrs

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/vision-to-okrs/SKILL.md) · purchased package; analyze rather than redistribute · 79 lines

### vision-to-quarter

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/vision-to-quarter/SKILL.md) · purchased package; analyze rather than redistribute · 895 lines

### weekly-top-3

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/weekly-top-3/SKILL.md) · purchased package; analyze rather than redistribute · 401 lines

### what-so-what-deck

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/what-so-what-deck/SKILL.md) · purchased package; analyze rather than redistribute · 59 lines

### winning-position

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/winning-position/SKILL.md) · purchased package; analyze rather than redistribute · 64 lines

### wireframe-sketch

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/wireframe-sketch/SKILL.md) · purchased package; analyze rather than redistribute · 61 lines

### work-backwards

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/work-backwards/SKILL.md) · purchased package; analyze rather than redistribute · 114 lines

### work-sample

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/work-sample/SKILL.md) · purchased package; analyze rather than redistribute · 377 lines

### workflow-trellis

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/workflow-trellis/SKILL.md) · purchased package; analyze rather than redistribute · 466 lines

### workshop-design

[Read source](../sources/prodmgmt-world--pm-os-cowork/plugin/skills/workshop-design/SKILL.md) · purchased package; analyze rather than redistribute · 176 lines
