# Optimizing API Documentation: Some Guidelines and Effects

Source type: paper; original research notes and bibliographic metadata, not a full-paper reproduction.
Authors: Michael Meng; Stephanie M. Steinhardt; Andreas Schubert.
Publication: Proceedings of the 38th ACM International Conference on Design of Communication (SIGDOC ’20), October 3–4, 2020, Denton, Texas, USA; 11 pages.
DOI: https://doi.org/10.1145/3380851.3416759
Source PDF: https://www.mangold-international.com/_Resources/Persistent/0/8/d/1/08d18ee760a218870f3c621043aeae026935e49c/Meng-et-al_Optimizing-API-Documentation_2020.pdf
Retrieved/read: 2026-11-05.
Local PDF SHA-256: 933c0c9eb67dcd7ac678eba60f067529404d5d700927202f95b9e850594264e0
Local PDF bytes: 926768
Local PDF pages: 11.

Full PDF and extracted text are local reading aids in /tmp/docs-empirical-20261105 and are not committed. Restore from the source PDF URL and verify the hash. The PDF states ACM copyright restrictions on server redistribution. This new note supersedes the earlier research report's inaccessible-lead status; it does not rewrite earlier evidence files.

## Access and reviewed scope

The PDF was initially inaccessible through a guessed direct web-open request. A subsequent search returned the original PDF as an indexed result, and opening that result succeeded. Direct curl download also succeeded. Read the abstract, study design/material modifications, participant assignment, procedure, coding, all quantitative results, discussion, limitations and future research (PDF pages 1–10). The original article is the evidence; the hosting vendor's abstract and conference slides were discovery aids, not substitutes for methods/results.

## Study design and task

A comparative intervention study used two recreated documentation versions for the same shipcloud shipping REST API. The control closely mirrored the provider's original structure/content with small presentation adjustments. The optimized version applied a bundle of the authors' earlier documentation guidelines. The changes included a more task-oriented structure, consistent sections/navigation, a short overview and central sample request, integrated domain concepts/terms, graphics/animations mapping business processes to API parameters, text-to-code visual signaling, ready-to-copy examples without omitted shared-code placeholders, and basic site search. These changes were applied together; individual components were not independently randomized.

Twenty-two volunteers participated, 21 men and one woman. Seventeen were recruited through software-company contacts (including employed interns), five from the university; reported roles were ten developers, two team leads and ten students. The authors report random assignment to two groups of eleven using a predefined schedule and participant arrival order. Groups were similar in measured age, programming/REST experience and e-commerce background; this does not establish equivalence on unmeasured variables.

Participants unfamiliar with shipcloud but with practical REST experience completed five predefined shipping tasks, identical in scope to the authors' earlier observation study: choose resources/endpoints/parameters and construct JSON request bodies. No general-purpose programming was required. Postman was already configured with authentication information and request-body format, and a Postman instruction sheet and dashboard were available. Thus the experiment does not test independent credential provisioning or full production onboarding.

Audio/screen recordings and eye tracking were manually coded. Each coding scheme was applied by a single researcher. Task correctness was measured as 18 binary subtasks across the five tasks. An incorrect subtask or one completed only with experimenter assistance scored zero. This captures requested business-relevant request details, not merely successful HTTP responses. Mixed-effects models assessed documentation type with task/participant terms varying by the selected model.

## Results and what they establish

Mean subtask accuracy was 86.35% with optimized documentation and 74.24% for control; the reported model's documentation-type contrast reached p < .05. This is evidence of better accuracy for the bundled redesign in this small experiment, not an expected uplift from any single best practice or a percentage-point promise for another platform.

Overall mean task time was 364 seconds for optimized and 374 for control. The difference was not statistically significant. Do not summarize the paper as demonstrating faster end-to-end task completion.

A secondary analysis split viewing time into documentation versus other windows. The interaction was significant; post-hoc comparison found less time outside documentation in the optimized group (149 versus 189 seconds; p < .05). The within-documentation difference (202 versus 179 seconds) was not significant. The authors treat outside-documentation viewing as a rough proxy for planning/execution. This is not direct measurement of cognitive processing: readers may execute actions while looking at docs, and optimized docs had more content. Outlier filtering removed 3 of 110 overall-time observations and 7 of 220 window-time observations.

Post-test ratings of overall documentation quality, structure and task difficulty did not differ significantly. Thus user ratings and observed task accuracy did not supply the same signal. Anecdotal interview/comments were not formally transcribed/analyzed and should not be treated as another validated effect.

## Limitations and boundaries

Small volunteer sample, substantial student representation, one relatively small REST API and limited initial tasks constrain generalization. Recruitment stopped at 22 because external developers were difficult to obtain. Full production integrations, long-term use, complex ERP/DAM/workflow tasks, different languages and coding agents were not tested. The study reports a joint effect of the complete redesign and specific implementation choices; it cannot identify which guideline helped, which might have been neutral or harmful, or how effects interact with expertise. Basic search was limited, and documentation content amount differed between versions. Single-researcher coding and selected statistical models should be considered when interpreting findings; no independent replication was performed in this research pass.

## Portable implications — our recommendations

Compare complete documentation variants on matched tasks when isolating a single feature is impractical, but report the bundle. Predefine correctness at business-relevant substeps, separate unassisted completion from assisted completion, and record setup excluded by the test. Measure accuracy, total time, task-stage proxies and perceived usability separately. A developer may spend more time reading and still make fewer errors; lower page dwell is not an automatic goal. For future experiments, distinguish full-task timing from where effort moves, and retain failed/partial tasks in the outcome accounting. Replicate before generalizing to a large business platform or agents.
