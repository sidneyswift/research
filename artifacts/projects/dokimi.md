---
domain: artifacts
subdomain: projects
type: project
name: dokimi
creator: "[[creators/intel]]"
source: "[[sources/frontier-docs--tool-design-evaluation-20261105]]"
ecosystem: agent-context evaluation
status: documentation-investigated
last-reviewed: 2026-11-05
---

# Dokimi

Intel's documentation and agent-context evaluation system is useful here because it asks whether supplied knowledge changes an agent's answers or working result, rather than only whether a page can be found. This study reviewed two current documentation pages, not the repository implementation or a running benchmark. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## Attributes

- **Evidence:** first-party living documentation captured 2026-11-05, with immutable byte/hash receipts.
- **Runnable unit described:** CLI evaluation pipelines, context arms, repository probes and executable tasks. No installation, provider call or Docker execution performed.
- **Signal:** published by Intel; no adoption count or independently validated evaluator reliability established.
- **Scope:** documentation, skills, profiles and repository guidance; this page owns the evaluator mechanisms, while [[concepts/agent-documentation-interfaces]] owns their application to documentation delivery.

## Relationships

[[creators/intel]] publishes the docs. [[artifacts/projects/context7]] is one documented context source. [[artifacts/projects/mintlify]] has a URL-discovery benchmark with a different outcome measure. [[concepts/developer-documentation-design]] owns the broader writing/maintenance discipline. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## What is held constant

The methodology compares the same task and answer model with and without a context layer. It calls for fixed task sets, temperature, available tools, retrieval and judges unless those are the variables being studied. Generated questions, chunk-grounded questions and curated golden questions have different provenance; recording question-set hashes makes accidental set changes visible. A model/provider default change explicitly requires a new baseline. These are documented controls, not source-code guarantees verified here. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

The documented with-docs condition also instructs the model to use the supplied material, while the baseline lacks that retrieved context. Its delta therefore describes that treatment package; it should not automatically be interpreted as the isolated effect of an editorial change. Reuse the same retrieval and prompt when testing two documentation revisions. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## Evaluation and failure accounting

The ordinary rubric and grounded rubric have different dimensions/weights and should not be averaged as one scale. Ground truth belongs to the judge, not the answering agent. Short expected-topic keyword labels are not treated as full answer ground truth. The documentation warns that confident-looking wrong answers to adversarial questions can beat correct terse caution under an ungrounded rubric. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

Trust checks include retrieval-hit coverage, paired question count, unusable/zero-score fraction, variance and optional judge agreement. Inputs that were never measured are explicitly reported as not measured, although they do not block the gate. Thus an overall PASS can coexist with missing checks. The denominator also changes with fallback/judging options; preserve those flags and excluded attempts with any claimed improvement. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

Executable tasks score generated work through tests. Their task content can live in another repository; preserving evaluator code is insufficient to restore the task environment. The published guidance calls for task provenance/license and offline oracle verification. We did not inspect or run those external tasks. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## Exposure is a separate experiment

The arm catalog distinguishes forced skill context, a skill offered for discretionary loading, and selection among a catalog. Repository modes separately investigate path/command existence, guidance budget, actual harness reach and test-graded repository work. Knowing that a file exists is a weaker observation than knowing the harness loaded it, and both are weaker than improved work. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-measurement]]

The novelty analysis describes added, redundant, degraded and still-missing knowledge at the artifact/model pair level. This is a useful way to investigate the user's training-data hypothesis: known material may be redundant for one model while another needs it. These are evaluator-defined probe classifications, not direct inspection of training data or proof that a fact was memorized. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-measurement]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — unmeasured checks and judge scores are separated from executable task outcomes. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]
- [[patterns/quality-bar/revision-bound-review]] — task hashes, model/default changes and preserved baselines bind comparisons to actual revisions; documented methodology only in this study. [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]

## What we'd steal

- ★ Same-task, same-model comparisons across documentation revisions and explicit no-context baseline.
- ★ Separate discovery/selection, context exposure, answer quality and tested work.
- Hold prompts, retrieval, tools and environment constant when isolating an editorial intervention.
- Store question-set hash, source revision, model/provider, judge and flags.
- Distinguish generated, curated and chunk-derived questions.
- Judge against actual answer facts, not keyword lists or rhetorical confidence.
- Preserve missing measurements and retrieval failures in the result accounting.
- Keep grounded and ungrounded scores on separate scales.
- Test optional skill discovery separately from forced context injection.
- Measure startup context cost separately from on-demand knowledge.
- Test stale/wrong/conflicting guidance as well as helpful guidance.
- Restore task/environment content as well as evaluator source.
- Rebaseline after changes to models, judges, defaults or task sets.

## Open questions

- Does a local benchmark's rubric agree with human domain reviewers and actual business outcomes?
- Which selected platform tasks can be checked using deterministic state assertions without a live external write?
- How much apparent improvement comes from retrieval or prompt changes rather than better source documentation?

## Agent documentation research connection

[[concepts/agent-documentation-interfaces]] owns the cross-system delivery, authority and evaluation comparison; this page owns the source-specific mechanisms.
