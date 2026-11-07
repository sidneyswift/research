---
domain: sources
type: article
url: https://www.anthropic.com/research/components-of-agent-memory
retrieved: 2026-11-07
snapshot-location: sources/anthropic--components-of-agent-memory/
last-reviewed: 2026-11-07
---

# Anthropic — The components of agent memory

## Snapshot details

- **Preserved:** complete readable body, original HTML, source/link extraction, figure inventory, cover and all fifteen meaning-bearing figures: **20 hashed files**. [Receipt](anthropic--components-of-agent-memory/capture.json); [coverage](anthropic--components-of-agent-memory/coverage.json).
- **Reviewed:** entire article body and all fifteen figures; figures 5, 10 and 11 enlarged to inspect trial counts, error-bar definitions, budget annotation and classification caveats. Numeric tables below follow explicit labels/alt text, not digitization of unlabeled curves.
- **Limits:** findings are author-reported. No model/benchmark run. Linked neuroscience papers, sleep-time paper, Harvey source repo, game video and Duet page were not independently reviewed. CL-Bench external release extraction is title-only. Supporting product contracts are current captured docs, not necessarily the exact harness used in the experiments.
- **Read alongside:** [[sources/anthropic--agent-memory-support]].

## Anchor map

### root

[Full article](anthropic--components-of-agent-memory/snapshot.md), [original HTML](anthropic--components-of-agent-memory/page.html), all fifteen figure images and original alt text. Published November 6, 2026; HTML modified `2026-11-06T21:15:32Z`; captured November 7. Research report, not a controlled public reproduction package.

### layers

Opening and Memory notes; figures 1–2: searchable transcripts, selective notes, compiled representations, injected context. Here memory means cross-session external context; it excludes weight updates, same-session learning and compaction. Neuroscience is an analogy, not evidence of an equivalent mechanism.

### learning-loop

Memory can be a prediction about what the future will need: CL-Bench 1.0 database task, fresh session per question, shared memory directory, correct-answer feedback. Untested hypotheses differ from checked rules retaining how they were established.

### database-results

Figure 3: mean reward, stateless/memory respectively: Opus 5.5 .655/.838; Sonnet 5.5 .644/.833; Opus 5 .564/.828; Opus 4.7 .383/.700; Sonnet 5 .306/.610; Sonnet 4.6 .330/.364. Curves show 30 questions. These are one task, not whole-benchmark aggregate scores.

### salience

Claude has learned to judge salience; figure 4: one Pokemon run per model near 10k steps. Sonnet 3.7: 413 files/225 folders/977,930 characters, one badge; Fable 5: nine topic files plus global.md, two folders/43,406 characters, four badges. Seventeen Sonnet steps created six/deleted nine memory files without gameplay. Model and strategy change together; memory size is not an isolated causal treatment.

### steering

Steering Claude to write memory; figure 5: Sonnet 4.6 stateless .330, memory .364, memory plus read/test instructions .641, each three runs, error bars standard deviation. Reference lines: Opus 5 .828 over 16 runs; Opus 4.7 .700 over three. Failure-only changes in memory gain: Opus 5 −.234 (three runs), Opus 4.7 −.150 (three), Sonnet 4.6 −.020 (one); right-panel error bars are standard error. No universal no-instructions result.

### correction

Dreaming can correct memory; figures 6–8. An incorrect east-side PokeCenter note caused wrong Mt. Moon completion and repeated backtracking. Transcript-backed correction reached Cerulean at action 1935; uncorrected run returned to Pewter. This is an illustrative navigation experiment; transcripts need observation-level interpretation, not blind trust in agent narration.

### wiki-search

Dreaming can build new memory representations; figure 10: Stainless corpus ~350k files/~420M tokens, 25 eval questions, Opus 5, two to 128 sessions. Wiki-only 13→48% graded criteria, search-only 53%, wiki+search 54→61%; reported ~20k fewer online tokens/question with hybrid retrieval. Examples grow 103 pages/766 links to 222 pages/12,893 links.

### compute-budget

Figure 10 explicitly labels its 2M–128M token axis as a budget of 1M/session, NOT measured spend. Online token savings do not establish net savings after construction, maintenance, cache behavior or model pricing.

### task-fit

Figure 11: merger task has 24 questions; on red/orange items requiring multiple documents and/or judgment/arithmetic, wiki 87% versus search 73%. Separate 57-criterion LAB task has no clear wiki advantage. Figure says classes are model-assigned; document counts are incoming links, not unique supported criteria. Do not present 87% as whole LAB accuracy.

### expansion

Figure 12: another LAB corpus, ten documents/115 KB, becomes 68 pages/255 links/203 KB (1.77×). More pages and links can fail to abstract useful structure.

### injection

Dreaming can promote notes up the memory hierarchy; figure 13. Small injected layer, details demoted with links. Wrong notes propagate across sessions; loading is not compliance. Claude Code limit is first 200 lines or 25 KB; current docs clarify whichever comes first and distinguish CLAUDE.md.

### goal-ownership

Dreaming can focus memory on a specific goal; figure 14. A shared summarized contract table lost terms through concurrent overwrites; generated brief met 41/57 facts. Reflection changed instructions, per-contract ownership and verbatim term preservation; rebuilt wiki supported 57/57. Bundled intervention, no isolated concurrency ablation or claim of universal legal correctness.

### repair

Figure 15: second pass repoints nine links from six pages to the existing buyer-form-escrow-agreement page; adds index, instructions-email and escalations pages. 38 entries/225 links become 41/278. Structural repair and semantic correctness are different checks.

### open-questions

Closing questions: value of online memory writing versus attention cost, incremental offline maintenance versus stale knowledge, timing and forms of representation. Links to dynamic dreaming cookbook and knowledge-wiki tutorial; those are separately dated supporting captures.

## Why we cite this

External-memory selection, consolidation, evaluation, adoption and runtime boundaries. Described results and product contracts are not independent replication.

## Popularity signals

Primary Anthropic publication/documentation, captured 2026-11-07. No adoption or popularity count asserted.

## Related sources

- [[sources/anthropic--agent-memory-support]] — dated API, CLI, cookbook and quickstart evidence.
- [[sources/ankrgyl--trace-lake]] — execution history as a substrate for verified learning.
