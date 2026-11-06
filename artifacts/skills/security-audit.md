---
domain: artifacts
type: skill
name: security-audit
creator: "[[creators/cloudflare]]"
source: "[[sources/cloudflare--security-audit-skill]]"
ecosystem: cross-platform
status: active
discovered-via: user-shared GitHub repository
last-reviewed: 2026-11-06
popularity-signals:
  - signal: github-stars
    value: 61558
    as-of: 2026-11-06
    source: "[[sources/cloudflare--security-audit-skill#root]]"
---

# security-audit

> A security-review skill that separates exploration from evidence: account for coverage, independently challenge concrete candidates, and publish only records that satisfy their verdict's contract.

**Judgment:** the most portable contribution is an evidence workflow, not a claim that adding more agents makes an audit trustworthy. Keep incomplete work visible, preserve who checked what, and reverify a materially changed conclusion. The shipped validators enforce portions of that bookkeeping; the host still has to supply execution isolation and enforce the orchestration. [[sources/cloudflare--security-audit-skill#coverage-contract]] [[sources/cloudflare--security-audit-skill#material-reverification]] [[sources/cloudflare--security-audit-skill#execution-boundary]]

## Attributes

- **What it does:** supports focused security guidance and an explicitly requested six-phase audit: reconnaissance → coverage-led hunting → independent candidate validation → structured records → independent record verification → reports. Loading the skill alone does not authorize the full audit or output-file creation. [[sources/cloudflare--security-audit-skill#modes]] [[sources/cloudflare--security-audit-skill#root]]
- **Trigger conditions — literal description:** “Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete workflow only for explicit codebase audit or pen-test requests, full/comprehensive/end-to-end reviews, or requested report artifacts.” [[sources/cloudflare--security-audit-skill#modes]]
- **Routing neighborhood:** overlaps generic code review, security questions, targeted debugging and full audit requests. The body distinguishes guidance from full audit; the latter requires explicit scope/report intent. Compared with [[artifacts/plugins/pstack]], this is a security-specific evidence and coverage procedure, not a general adversarial panel. Compared with [[artifacts/skills/loop-library]], it prescribes one domain workflow rather than choosing a general loop. No local installation, old-route retention test, discoverability test or downstream task-success experiment was performed. [[sources/cloudflare--security-audit-skill#modes]]
- **Bundle:** 22 tracked files total; 20 inside the skill: 15 Markdown files (main entry, three phase guides, ordinary attack classes and ten domain companions), one JSON schema, two dependency-free JavaScript validators and two fixture suites. Skill-directory total: 5,276 lines; `SKILL.md`: 192 lines. Inventory and all-file hashes in the source manifest. [[sources/cloudflare--security-audit-skill#root]]
- **Disclosure:** main entry → phase guides/selected domain blocks → schema and validators. Hunters must receive the exact selected guidance and relevant schema branches, not merely filenames. Roles and workflow become concrete per assignment. [[sources/cloudflare--security-audit-skill#context-selection]]
- **Dependencies:** tool-using agent with parallel-worker support; Node for validators; an independently provided OS-enforced sandbox for any target-controlled execution. The repository does not ship that sandbox, an artifact-promoter executable, a fleet scheduler, database, patch service or installer implementation. [[sources/cloudflare--security-audit-skill#root]] [[sources/cloudflare--security-audit-skill#execution-boundary]]
- **License:** MIT. Source pin `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` (September 14, 2026), inspected November 6. “Active” describes the source artifact, not an installed local skill. [[sources/cloudflare--security-audit-skill#license]] [[sources/cloudflare--security-audit-skill#root]]

## Relationships

- **Creator:** [[creators/cloudflare]].
- **Evidence:** [[sources/cloudflare--security-audit-skill#root]]; full local checkout, committed hashes/ranges/restore registration, and validator-test receipt.
- **Conceptual neighbors:** [[concepts/evidence-calibrated-research]], [[concepts/review-cost-aware-workflows]], [[concepts/completion-contract]], [[concepts/artifact-centered-agent-context]], [[concepts/lifelong-skill-routing]].
- **Runtime contrasts:** [[artifacts/projects/codex]] and [[artifacts/projects/background-agents]] implement harness/runtime mechanisms that a prompt-defined audit must obtain from its host. This is a research comparison, not a declared dependency or tested integration.

## What problem it solves

Security-flavored prose can confuse missing best practices with reachable vulnerabilities, convert deployment unknowns into confident claims, and hide unreviewed paths behind a polished report. Parallel investigators can also duplicate the same root cause or exhaust the budget before anyone checks their conclusions. This skill gives each of those failures a distinct representation and a prescribed handling path. [[sources/cloudflare--security-audit-skill#claim-standard]] [[sources/cloudflare--security-audit-skill#profiles-budget]] [[sources/cloudflare--security-audit-skill#coverage-contract]]

## How it works (mechanism)

### 1. Plan coverage before dispatch

Four reconnaissance roles map product/stack, principals and controls, input-to-sink paths, and offline-validation readiness. The parent produces a compact architecture overview and a coverage ledger. Assignment identity derives from source-referenced surface, boundary, subsystem, attack class and optional lifecycle; it excludes reviewer names, waves, line numbers, verdicts and severity. Canonical references use NFC plus a specified byte-escaping scheme. This stabilizes bookkeeping, not the correctness of the chosen scope. [[sources/cloudflare--security-audit-skill#recon]] [[sources/cloudflare--security-audit-skill#coverage-contract]]

Each unit tracks selected and excluded blocks, starting paths, status, owner, checks, result fingerprints and unresolved facts. `covered` requires owned evidence and no unresolved fact; `blocked` records an actual partial investigation; `deferred` is unassigned and has no live evidence. Reopening an investigated unit archives its attempt, increments the wave and assigns a fresh owner without relabeling the old owner's evidence. [[sources/cloudflare--security-audit-skill#coverage-contract]] [[sources/cloudflare--security-audit-skill#coverage-code]]

### 2. Investigate an invariant, not a checklist flag

A candidate needs a lower-trust principal, accepted input/action, the control that should constrain it, an exact path through that control, and a concrete affected resource/result. Inspect the strongest preventing layer and alternate lifecycle paths. Use the narrowest bounded local check; stop once the assigned invariant is settled. An unexpected boundary becomes a proposed new coverage unit rather than permission to wander into another investigator's assignment. [[sources/cloudflare--security-audit-skill#hunting]] [[sources/cloudflare--security-audit-skill#candidate-gate]]

The parent is the sole writer of shared records. Workers write scratch only; retained artifacts require a detailed parent-side, descriptor-relative, no-follow promotion procedure after all target processes stop. This is a **prescribed integration contract**, not an implementation included in the repository. The validator's path checks do not substitute for it. [[sources/cloudflare--security-audit-skill#execution-boundary]] [[sources/cloudflare--security-audit-skill#promotion]] [[sources/cloudflare--security-audit-skill#coverage-code]]

### 3. Separate coverage criticism from candidate validation

Coverage critics identify missing/reopened units, not findings. In standard/deep mode, a clean post-wave critic is followed by a distinct final-clean critic; accepted new work reopens the loop. Quick mode stops after one hunter wave and one critic, recording accepted gaps as deferred. A declared cap never implies comprehensive coverage. [[sources/cloudflare--security-audit-skill#coverage-critics]]

A fresh verifier attempts to refute every unique candidate, including proposed unresolved leads. It rereads source and independently reproduces decisive checks when safely possible. The verifier receives the claim and necessary evidence, not another verifier's verdict. Same-source prior confirmations still need current checking; unresolved or changed-source prior records are work, not inherited coverage. [[sources/cloudflare--security-audit-skill#independent-validation]] [[sources/cloudflare--security-audit-skill#prior-evidence]]

### 4. Keep four epistemic states distinct

| State | What may be claimed | Where it belongs |
| --- | --- | --- |
| Unvalidated candidate | A claim has not yet received the required independent decision | Coverage ledger only; makes the run incomplete if validation cannot finish |
| `needs_validation` | Reviewed source-grounded lead with a precise decisive unknown and applicable resolution plan | Structured records and a separate lead handoff; no severity |
| `confirmed` | Complete source trace and bounded observed result with conditions, remediation, impact, likelihood and confidence | Structured records and confirmed-findings report |
| `rejected` | The claim was refuted by source, control, prerequisites, behavior or absent meaningful impact | Structured history; not a finding |

This is the skill's prescribed evidence standard. Code can require an `observed_result` string, not establish that the claimed observation happened. Likewise an agent-ID string is not proof of a genuinely independent agent invocation. [[sources/cloudflare--security-audit-skill#verdict-contract]] [[sources/cloudflare--security-audit-skill#findings-code]]

### 5. Bind the last verification to the final claim

Standard/deep profiles use a second fresh verifier on final confirmed and unresolved records; quick combines candidate and record checks into one fresh review. A promotion or material change to root cause, trace, execution input/result, impact or severity triggers another independent verification. If budget or independence is unavailable, remove the disputed record from findings, keep an unresolved ledger candidate and mark the run incomplete. Cosmetic wording/line corrections that do not change evidence are different. [[sources/cloudflare--security-audit-skill#material-reverification]]

Only then derive prose from the records, ledger and retained hardening notes. The presentation layer cannot change a verdict or inflate severity. A clean result may contain zero confirmed findings. Detailed reproductions use the target's native interface, which need not be HTTP. [[sources/cloudflare--security-audit-skill#reporting]]

### 6. Spend budget on conclusions, not just exploration

Quick, standard and deep vary breadth/redundancy, not the confirmation bar. Reserve critic and verifier invocations before assigning hunters; prioritize lower-trust entry points, consequential resources and prior gaps. If candidates exceed reserves, stop hunting, validate deterministically by fingerprint, retain remaining candidates as unresolved work and disclose incomplete status. The suggested reserve is a policy heuristic, not an empirically optimized allocation. [[sources/cloudflare--security-audit-skill#profiles-budget]] [[sources/cloudflare--security-audit-skill#hunting]]

## What is enforced, and what is not

| Layer | Shipped checks or prescribed behavior | Boundary |
| --- | --- | --- |
| Findings validator | Schema subset, mutually exclusive verdict branches, visible prose, sorted unique fingerprints, safe relative path syntax, trace ordering, severity no higher than stated impact | Does not open cited source paths, reproduce an observation, prove impact or inspect other output files |
| Coverage validator | Canonical IDs, collision checks, sorted units, status/evidence invariants, check-owner path union, artifact-path ownership, fresh assignment-owner/archive rules | Does not establish discovery completeness, actual worker identity, artifact-file existence/promotion or correspondence with `findings.json` |
| Input readers | Bounded bytes/depth/cardinality; fatal UTF-8 decoding; no-follow/nonblocking input opening; regular-file checks; bounded escaped diagnostics | Input-file protections are not the complete descriptor-relative scratch-to-artifact promotion protocol |
| Audit orchestration | Scope selection, invocations, budget, critics, fresh verification and material-edit loops | Markdown instructions; no shipped engine mechanically enforces all phases, independence or cross-file run completeness |
| Target execution | Offline, read-only target/tools, scratch-only writes, allowlisted environment, limits, no live systems | Required host capability, not bundled sandbox code; unavailable capability becomes a precise blocker |
| Reporting | Prose derived from final structured records and ledger | Prompt contract; no bundled deterministic report renderer or checker comparing prose to records |

These limits come from the complete tracked-file inventory and the inspected implementations, not from an attempted bypass or a completed security assessment of this repository. [[sources/cloudflare--security-audit-skill#root]] [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#findings-input]] [[sources/cloudflare--security-audit-skill#coverage-code]] [[sources/cloudflare--security-audit-skill#coverage-input]] [[sources/cloudflare--security-audit-skill#reporting]]

## Evidence and testing

Both provided validator suites ran locally: **65 passed, zero failed, zero skipped**, Node v25.9.0 / macOS arm64. Tests include valid producer-shaped records, state/ownership invariants, hostile nesting/size, invisible Unicode, unsafe paths, terminal-control escaping, FIFO/symlink rejection and consistency between duplicated helper rules. This verifies those fixtures on this environment, not full audit quality, vulnerability recall, sandbox enforcement or semantic truth of a generated report. [[sources/cloudflare--security-audit-skill#validator-tests]] [[sources/cloudflare--security-audit-skill#test-execution]]

The README's claim that one pass found roughly half the repeated-run total is an author observation, not a measured false-negative rate: the denominator is discovered bugs, not all real bugs. The linked June article describes a separate fleet harness and an earlier skill, not the implementation shipped at this September pin. [[sources/cloudflare--security-audit-skill#root]] [[sources/cloudflare--security-audit-skill#harness-context]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — named evidence states, incomplete-run outcome and record-level checks before publication. Some gates remain prompt policy. [[sources/cloudflare--security-audit-skill#verdict-contract]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — investigators judge reachability and meaning; JavaScript checks record structure, state and resource bounds. [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#coverage-code]]
- [[patterns/behavioral/context-is-not-authority]] — model/tool descriptions guide interpretation but do not grant action authority; execution requires host-level controls. [[sources/cloudflare--security-audit-skill#ai-authority]]
- [[patterns/composition/resolver-routing-table]] — phase and domain documents loaded for the relevant trust boundary, then exact blocks carried into worker prompts. [[sources/cloudflare--security-audit-skill#context-selection]]
- [[patterns/quality-bar/revision-bound-review]] — a narrower, prompt-prescribed claim-revision analogue: material record changes invalidate prior verification. Not a second implementation of the whole proposed change-publication pattern. [[sources/cloudflare--security-audit-skill#material-reverification]]

## What makes it great

The handoff format carries uncertainty instead of washing it away. It makes a reviewed but blocked lead different from a claim nobody checked, and preserves old ownership when work is reassigned. The same discipline reaches small details: malformed reviewer JSON is rejected rather than silently “repaired,” prose must be visible while exact payload strings remain intact, and diagnostics escape attacker-controlled control characters. Those are unusually concrete ways to prevent evidence quality from degrading between agents and files. [[sources/cloudflare--security-audit-skill#independent-validation]] [[sources/cloudflare--security-audit-skill#coverage-code]] [[sources/cloudflare--security-audit-skill#validator-tests]]

## What we'd steal

Portable research principles below, not an instruction to install the skill or apply a full security-audit pipeline to every task. ★ marks the highest-leverage transfers.

1. **★ Distinguish guidance from execution authorization.** A broadly matching skill can answer a narrow question without launching its full workflow or creating artifacts. [[sources/cloudflare--security-audit-skill#modes]]

2. **Keep host adapters smaller than the workflow.** Map conceptual worker roles onto platform names while preserving ownership and independence; names alone are not isolation. [[sources/cloudflare--security-audit-skill#modes]]

3. **★ Budget verification before exploration.** Reserve critics and candidate checks before launching hunters; explicitly incomplete is better than unverified conclusions. [[sources/cloudflare--security-audit-skill#profiles-budget]]

4. **Let profiles change breadth, not evidence quality.** Quick mode reduces waves and reviewer passes but retains independent review and the same confirmation standard. [[sources/cloudflare--security-audit-skill#profiles-budget]]

5. **Make priority and tie-breaking explicit.** Use boundary consequence and prior gaps to choose work, then stable identity to break ties rather than launch order. [[sources/cloudflare--security-audit-skill#hunting]]

6. **Reconnoiter validation capability early.** Establish what can be tested locally, what controls exist and which observations need an owner before committing to a plan. [[sources/cloudflare--security-audit-skill#recon]]

7. **Keep the overview compact and assignments precise.** Use a small architecture summary while retaining the full block-selection and coverage contract elsewhere. [[sources/cloudflare--security-audit-skill#context-selection]]

8. **Route by actual trust boundary.** Select companions from visible flows and authority, not merely a language, framework name or dependency keyword. [[sources/cloudflare--security-audit-skill#context-selection]]

9. **Pass needed constraints, not filenames.** Copy exact selected methods, validation rules and schema branches into each assignment. Record excluded blocks and reasons. [[sources/cloudflare--security-audit-skill#context-selection]]

10. **★ Give coverage a stable source-derived identity.** Exclude mutable reviewer, wave, line and verdict data; define normalization and byte encoding, then reject collisions. [[sources/cloudflare--security-audit-skill#coverage-contract]]

11. **Separate work identity from root-cause identity.** Coverage IDs identify investigation obligations; finding fingerprints deduplicate the same claim across units and verdicts. [[sources/cloudflare--security-audit-skill#coverage-contract]] [[sources/cloudflare--security-audit-skill#candidate-gate]]

12. **Make coverage states carry evidence obligations.** Distinguish planned, partial/blocked, covered, candidate, deferred and out-of-scope; neither deferral nor absence of findings means reviewed. [[sources/cloudflare--security-audit-skill#coverage-code]]

13. **★ Preserve per-check ownership.** A unit-level reviewed-path list must equal the union of its attributed checks; independently owned evidence can coexist. [[sources/cloudflare--security-audit-skill#coverage-code]]

14. **Archive before reassigning.** Preserve terminal attempts and their provenance; reset live evidence and use a fresh assignment owner on the next wave. [[sources/cloudflare--security-audit-skill#coverage-code]]

15. **Use prior evidence selectively.** Recheck unchanged confirmations; changed source and old gaps remain work. Rejecting one claim does not cover the whole unit. [[sources/cloudflare--security-audit-skill#prior-evidence]]

16. **★ Start from a concrete invariant.** Identify principal, capability, accepted input, constraining control, exact path and affected resource before describing impact. [[sources/cloudflare--security-audit-skill#hunting]]

17. **Seek the strongest preventing control.** A missing redundant layer is hardening if another layer already prevents the claimed failure. [[sources/cloudflare--security-audit-skill#candidate-gate]]

18. **Compare equivalent effects across alternate paths.** Check batch, legacy, retry, cancellation, migration and error behavior against the same invariant. [[sources/cloudflare--security-audit-skill#hunting]]

19. **Constrain investigation depth.** Stop when the assigned invariant is settled; record new boundaries for deliberate assignment rather than widening scope silently. [[sources/cloudflare--security-audit-skill#hunting]]

20. **Re-establish every prerequisite in a chain.** A demonstrated first step does not prove downstream authority or impact; record the missing observation. [[sources/cloudflare--security-audit-skill#attack-classes]]

21. **Validate the smallest meaningful effect.** Use dummy data and a bounded native check. Do not expand a crash into code execution or ordinary work into shared availability impact. [[sources/cloudflare--security-audit-skill#candidate-gate]]

22. **★ Treat unknown external facts as unknown.** Neither absent source configuration nor a reassuring assumption proves deployment behavior; retain an exact owner-observable question. [[sources/cloudflare--security-audit-skill#claim-standard]]

23. **Separate availability from performance.** Require input-to-cost amplification, effective-bound analysis, shared impact and recovery; avoid stress as a substitute for explanation. [[sources/cloudflare--security-audit-skill#availability]]

24. **Follow data through every derived copy.** Trace caches, indexes, exports, queues and restores after revocation or deletion; a tenant column alone is not enforcement. [[sources/cloudflare--security-audit-skill#data-lifecycle]]

25. **Distinguish authorization from action binding.** An action may be permitted for a user yet not intentionally requested by that user. Bind final normalized tool/action arguments to intent. [[sources/cloudflare--security-audit-skill#ai-authority]]

26. **Treat schemas and metadata as inputs, not policy.** Tool shape does not establish resource authorization; authenticated connection identity matters more than self-declared tool names. [[sources/cloudflare--security-audit-skill#ai-authority]] [[sources/cloudflare--security-audit-skill#protocols]]

27. **Compare producer and consumer interpretations.** Trace the same bytes, identity, units or artifact across parser, schema, ABI and release boundaries instead of checking each in isolation. [[sources/cloudflare--security-audit-skill#web-identity]] [[sources/cloudflare--security-audit-skill#native]] [[sources/cloudflare--security-audit-skill#supply-chain]]

28. **Carry policy through lifecycle changes.** Recheck account switches, stale tabs, reloads, restore, queued actions and peer reconnection, not just the happy-path entry. [[sources/cloudflare--security-audit-skill#browser]] [[sources/cloudflare--security-audit-skill#ipc]] [[sources/cloudflare--security-audit-skill#protocols]]

29. **Use one writer for shared synthesis.** Workers return structured results; the parent consolidates them rather than permitting concurrent edits to canonical records. [[sources/cloudflare--security-audit-skill#hunter-result]]

30. **Treat scratch as untrusted after execution ends.** Parent promotion needs confined descriptor-relative access, type/link-count checks, byte bounds and exclusive destinations; stopping the process alone is insufficient. [[sources/cloudflare--security-audit-skill#promotion]]

31. **Make coverage criticism a different job.** A critic proposes source-backed missing work, not unsupported findings; a clean finite ledger still is not exhaustive security proof. [[sources/cloudflare--security-audit-skill#coverage-critics]]

32. **Do not let early stops impersonate completion.** Record why a gap is deferred and which mandatory critic or validation step did not run. [[sources/cloudflare--security-audit-skill#coverage-critics]] [[sources/cloudflare--security-audit-skill#reporting]]

33. **★ Falsify candidates independently.** A verifier that did not invent the claim reconstructs the path and controls; it must also challenge unresolved leads, not just confident claims. [[sources/cloudflare--security-audit-skill#independent-validation]]

34. **Minimize shared reviewer conclusions.** Provide facts and relevant evidence without another verifier's verdict; fresh roles reduce direct anchoring but do not prove statistical independence. [[sources/cloudflare--security-audit-skill#independent-validation]]

35. **Reject malformed judgments instead of rewriting them.** Discard prose-wrapped or malformed results; retry with a fresh verifier if funded, otherwise preserve incomplete work. [[sources/cloudflare--security-audit-skill#independent-validation]]

36. **★ Keep unvalidated, unresolved and refuted distinct.** An unchecked claim is not a reviewed needs-validation lead; a refuted claim is not unresolved simply because it was once plausible. [[sources/cloudflare--security-audit-skill#verdict-contract]] [[sources/cloudflare--security-audit-skill#profiles-budget]]

37. **Preserve rejected claims as evidence.** Retain root-cause fingerprint and refutation so unchanged failed claims do not repeatedly consume attention. [[sources/cloudflare--security-audit-skill#verdict-contract]] [[sources/cloudflare--security-audit-skill#prior-evidence]]

38. **Separate likelihood, impact and certainty.** Only confirmed records receive severity; cap it by demonstrated impact, not the frightening label or reviewer confidence. [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#claim-standard]]

39. **Use verdict-specific fields.** Discriminated branches prohibit confirmation-only execution, remediation and severity fields on unresolved/refuted records. [[sources/cloudflare--security-audit-skill#verdict-contract]]

40. **★ Reverify material replacements.** A reviewer's proposed promotion or changed causal story is a new claim needing fresh verification, not automatically an approved correction. [[sources/cloudflare--security-audit-skill#material-reverification]]

41. **Keep reporting downstream of evidence.** Generate prose from final records without upgrading verdicts, blockers or effects. Empty confirmed output is valid. [[sources/cloudflare--security-audit-skill#reporting]]

42. **Match the reproduction to the product.** A library can use a function call, a parser a fixture and infrastructure a local policy evaluation; do not force everything into an HTTP template. [[sources/cloudflare--security-audit-skill#reporting]]

43. **Fix the last trusted decision point.** Recommend the smallest invariant-restoring change and a regression case; the audit explains remediation without editing the audited source. [[sources/cloudflare--security-audit-skill#claim-standard]]

44. **★ State exactly what validators prove.** Syntax, internal consistency, physical evidence existence, independent observation and exploit truth are different checks. [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#coverage-code]]

45. **Harden the validator input boundary.** Bound bytes, depth, collection size, work and diagnostics; reject unsupported schema keywords and unsafe input-file types instead of silently weakening validation. [[sources/cloudflare--security-audit-skill#findings-input]] [[sources/cloudflare--security-audit-skill#coverage-input]] [[sources/cloudflare--security-audit-skill#findings-code]]

46. **Validate explanatory prose without corrupting fixtures.** Require visible, valid prose but preserve empty/control-containing test payload strings and replacement code when meaningful. Escape diagnostics separately. [[sources/cloudflare--security-audit-skill#validator-tests]]

47. **Test duplicated contracts for drift.** The two standalone validators intentionally test common regexes, limits and path/prose corpora against each other. [[sources/cloudflare--security-audit-skill#validator-tests]]

48. **Measure fixture behavior separately from review quality.** Passing record-validator tests supports those contracts only; measure detection, false positives, coverage gains and human review cost in separate experiments. [[sources/cloudflare--security-audit-skill#test-execution]] [[sources/cloudflare--security-audit-skill#root]]

## Adoption boundaries and open questions

- **No automatic full-workflow adoption:** use the evidence-state distinction and targeted falsification immediately in relevant research; trial the complete audit only with an authorized target, a real execution-isolation/provenance implementation and a bounded acceptance fixture. Do not install another orchestration stack merely because the prompts are detailed.
- **No claim that adversarial agents beat tests or formal checks:** this protocol tries to disprove concrete source-grounded claims and reproduce relevant behavior. It complements [[concepts/review-cost-aware-workflows]]; it does not refute Lauren Tan's warning about abstract nitpicking, and it contains no formal correctness proof. [[sources/cloudflare--security-audit-skill#independent-validation]] [[sources/poteto--verification-over-adversarial-review#verification-first]]
- **What is the cheapest adequate profile?** Compare accepted findings and reviewer minutes at matched total budgets, including repeated single-model sampling. Fresh contexts can still share systematic mistakes. Profile defaults are design choices, not comparative results. [[sources/cloudflare--security-audit-skill#profiles-budget]]
- **Who enforces cross-file consistency and reviewer identity?** The current CLIs validate one document each. An integration would need trusted run/worker receipts and ledger↔findings↔report checks; add them when actually running this workflow, not as speculative research infrastructure. [[sources/cloudflare--security-audit-skill#coverage-code]] [[sources/cloudflare--security-audit-skill#findings-code]]
- **Can all supported hosts implement promotion and isolation?** Portable wording does not make no-follow descriptor operations, constrained environments and process retirement uniformly available. The specified response to a decisive missing capability is a blocker, not permission to execute anyway. [[sources/cloudflare--security-audit-skill#promotion]]
- **What is the true coverage denominator?** A valid, cleanly exhausted ledger measures its declared scope; it cannot prove that recon discovered every relevant boundary. Keep changing-source and deployment assumptions visible. [[sources/cloudflare--security-audit-skill#coverage-critics]]

## Source citations

- Modes, resource accounting and evidence standards: [[sources/cloudflare--security-audit-skill#modes]], [[sources/cloudflare--security-audit-skill#profiles-budget]], [[sources/cloudflare--security-audit-skill#claim-standard]].
- Ownership, coverage, independent decisions and replacement rules: [[sources/cloudflare--security-audit-skill#coverage-contract]], [[sources/cloudflare--security-audit-skill#hunter-result]], [[sources/cloudflare--security-audit-skill#independent-validation]], [[sources/cloudflare--security-audit-skill#material-reverification]].
- Executable checks and observed fixture outcome: [[sources/cloudflare--security-audit-skill#findings-code]], [[sources/cloudflare--security-audit-skill#coverage-code]], [[sources/cloudflare--security-audit-skill#test-execution]].
- Full inventory, pinned domain references and historical context: [[sources/cloudflare--security-audit-skill#root]], [[sources/cloudflare--security-audit-skill#harness-context]].
