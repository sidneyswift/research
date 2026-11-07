# DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation?

Source type: paper
Authors: Frances Liu; Manny Silva; Paige Calvert; Ayu Adiati; Sarah Sanders
Publication/version: arXiv2609.39909v1, September30,2026; preprint
Source URL: https://arxiv.org/pdf/2609.39909v1
Version identifier: arXiv2609.39909v1; living author HTMLhttps://dogbench.ai/paper inspected separately
Retrieved/read: 2026-11-05
Local PDF SHA-256: 765be71adac1196335e8e534fb4607b9ac6c3e594913cf40e34f1eb9612de5d1
Local PDF bytes: 1987222
Local PDF pages: 28

This file is original research notes and bibliographic metadata. It is not a reproduction or immutable snapshot of the complete paper. Full PDFs and extracted text were read locally under /tmp and are not preserved in Git. To restore, download the source URL and verify the PDF hash; copyright/redistribution rights must be checked before republishing it.

## Reviewed scope

Read PDF main methods/protocol/results/failureanalysis/discussion/limitations and selected appendicesA–B (rubric construction, maintainer calibration and scorer validation). Also read author HTMLhttps://dogbench.ai/paper and landing page to identify surface drift. No benchmark replication or artifact-code audit performed. Page count is local PDF metadata; not an assertion every appendix line was reviewed.

## Task, sample and scoring

292real open-source repository-triggered items:205documentation updates and87abstention/no-change items. Trigger is a code change or reported documentation gap against a pre-change repository. Primary held-out split117items (82update,35abstain).7model+harness lanes each attempt one patch or abstention in isolated, identity-masked, network-restricted environments. Source projects include Helm, Mautic and PostHog. Task-specific criteria assess behavior, completeness, reader actions, placement and repository norms rather than text similarity to the merged human patch. A correct decision and useful delivered patch are distinct outcomes.

Required/conditional/guardrail criteria and P0critical defects have different roles. Avoiding an optional prohibited behavior earns no positive credit. Any P0failure caps patch score at60; that number is the benchmark authors' explicit policy, not an empirically calibrated maintainer-acceptance probability. Composite score is the harmonic mean of delivered patch quality on update items and abstention recall. The maximum reported primary composite47.3/100 does not mean47.3%of humanexpert capability or47.3%tasks successful.

## Findings and failure mechanisms

The separate1,267pre-rerun patch audit allows multiple defect labels per patch. Task-completion gaps45.5%, technical inaccuracies36.6%, conceptual/reference gaps32.5%; these are audit-label rates, not population estimates or necessarily current held-out-run rates. Fabricated content6.1%was narrower than inaccurate descriptions of real interfaces. A scope/default/lifecycle qualifier can be wrong even when the capability exists. Trajectory analysis identifies premature closure, missing decisive evidence and incomplete cross-surface impact investigation as recurrent explanations. These are coded associations/interpretations, not randomized causal mechanism tests.

An absence of matching docs does not establish an intentional exclusion; it may be the actual gap. Conversely, a backend diff or relevant keyword does not establish a reader-facing documentation obligation. The reviewer must trace observable public behavior and affected reader tasks.

## Validation and limitations

Maintainer input covers a subset, with one maintainer per repository/item and different editorial priorities. PDF appendixB reports42maintainer decision items and242criteria on23documentation-change examples; generated rubric overlap is asymmetric, and overlap absence does not establish invalidity. Direct scorer validation covers20items/330criteria, with post-adjudication human reference;93.9%agreement is not blinded inter-human reliability or validation of every benchmark item.

Authors do not execute every documented procedure or provide deterministic sample/link checks. Some abstention labels rest on absence of a related documentation update within90days; this may encode forgotten updates. One sampled run per agent/item says nothing about repeated reliability or best-of-k. No internet reduces contamination but differs from ordinary workflows. Criteria can overlap. Model judges may under-penalize fluent low-information prose. Two authors disclose affiliation with a documentation-agent vendor.

## Version/surface differences — do not merge denominators

The living author HTML's main human-validation summary mentions21completed criterion alignments/priority-weighted recall.892; PDFv1appendix reports23documentation items/242criteria/90.9%coverage. The landing leaderboard includes additional cloud agents with a54.8maximum, while the primary paper reports7reproducible lanes/47.3maximum. Treat these as different surfaces/scopes and use version-pinned PDF claims. No reason for the discrepancy is established here.

## Portable ideas — proposed, not proven interventions

Decide patchversusno-op from changed reader behavior. Build a traceable coverage list before drafting: behavior, prerequisites, action, verification/recovery, qualifiers and affected surfaces. Treat critical wrongness independently from stylistic improvements. Score documentation against reader requirements, not similarity to old prose. Audit all supported surfaces and generated sources. Use independent technical review plus executable checks; a fluent judge score alone is insufficient. Record authoring/evaluation model+harness and version when comparing results.

