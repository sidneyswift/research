# From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation

Source type: paper
Authors: Zhijun Gao; Jing Chen
Publication/version: arXiv2608.20195v1, August20,2026; preprint
Source URL: https://arxiv.org/pdf/2608.20195v1
Version identifier: arXiv2608.20195v1; HTMLhttps://arxiv.org/html/2608.20195v1
Retrieved/read: 2026-11-05
Local PDF SHA-256: a9b97c3f2c5d5692f5f9c629d2bd19f7f47ad0c92e1b18cdb7683dba69ad7ba8
Local PDF bytes: 967907
Local PDF pages: 14

This file is original research notes and bibliographic metadata. It is not a reproduction or immutable snapshot of the complete paper. Full PDFs and extracted text were read locally under /tmp and are not preserved in Git. To restore, download the source URL and verify the PDF hash; copyright/redistribution rights must be checked before republishing it.

## Reviewed scope

Read abstract, study design3.1–3.6, reported distributions/robustness in4, descriptive model5, supported versus unsupported implications6, and threats7. Not an independent replication or validation of released classifier/pipeline. PDF/HTML are version-pinnedv1.

## Methods and observation boundary

Two distinct public corpora are complementary rather than pooled/cross-validation. SWE-chat sample559sessions stratified by agent and length,557parseable,94,813events/3,033documentation interactions. AIDev curated subset becomes33,097PRs with named non-vendored files/690,260file×commit rows. File-path rules identify documentation; LLMclassification disambiguates500paths,27keyword fallback. There is no human reliability validation for those category labels. Process stages and triggers use heuristics and short event windows. Session/repository cluster bootstraps account for dependence; oversampling correction is incomplete for combined length×agentstrata.

Crucial limitation: the instrument chiefly sees repository-local file interactions, not browser access to APIwebsites, inline docstrings, knowledge in model weights or contextfiles automatically preloaded at runtime. Tool-call extraction varies by harness; shell paths need parsing or whole categories disappear. Do not use observed1.3%API-reference interactions to claim agents ignore online API docs or that API documentation is unimportant.

## Findings and interpretation

The reported pooled-event distribution gives60.5%instructionfiles+agentworkingnotes, versus10.6%classical technical docs and1.3%APIreference. Session-equal/agent-weighted alternatives differ; category precision is provisional because LLMlabels were not human-validated. The robust direction is a large local agent-facing/working-document surface, not an exact universal allocation.

Observed consultation does not consistently support a simple read→act→validate pipeline. Unadjusted and stage-adjusted relationships to editing/creation differ. Zero explicit documentation-validation events are zeros under a narrow operational definition, not evidence that agents never validate, never test, or cannot use prose specifications. Consultation is associated with less immediate test/build activity, but the design cannot show that reading docs reduces testing. Documentation may be read at different task stages, or checks may occur beyond the immediate window.

Agent-created notes/plans are a maintenance surface. The study measures volume/change, not long-term staleness, cost, correctness or usefulness. Agent-document interaction is not confined to task orientation. The authors' sticky failure-stage heuristic inflates debugging share; don't repeat it as an exact time budget.

## Unsupported leaps to avoid

No causal evidence here that Markdown,llms.txt,better cross-links, runnable examples, instructionfiles or any proposed documentation format improves correctness. There is no comparative representation experiment. No observedFollow-reference events under their classifier does not imply links have no value. Recovery strategy ranking is explicitly rejected because only11documentation-recovery episodes have observable outcomes and intervals overlap. Between-agent rankings are confounded by extraction coverage and small samples.

## Portable ideas — proposed implications

Measure documentation discovery, actual exposure, interpretation, use and outcome separately. Capture runtime preloads and browser retrieval if studying agentdoc consumption. Keep durable project contracts separate from ephemeral agentnotes, with ownership/expiry appropriate to each. Test executable checks as an intervention rather than assuming their effectiveness. Evaluate humans and agents on concrete tasks; do not substitute an agent's documentation interaction count for successful use.

