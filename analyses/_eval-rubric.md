---
domain: analyses
type: shared-rules
last-reviewed: 2026-06-02
---

# Cross-modal eval — gate for `analyses/` pages

Self-improvement #20. Synthesis pages (`analyses/`) make load-bearing claims across many artifacts, so they carry the most risk of confident-but-wrong synthesis. Before an analysis ships, run it past a **second (and ideally third) model as judge** — the practice that caught the factual errors in gbrain's "book-mirror" (per [[artifacts/plugins/gbrain]], grounded in [[patterns/behavioral/diarization]]: distilled judgment must be *verified*, not just fluent).

This is a process, not an API harness — run it by hand (or via a sub-agent) with whatever models are available. gbrain's own split is the model here: *Opus catches precision errors, GPT catches missing context, DeepSeek catches when something reads as generic.* Use different model families on purpose; same-family judges miss the same things.

## When to run it

- **Required** before any `analyses/` page moves out of draft.
- **Optional** for a pattern page being promoted `proposed → confirmed`, or any page making a strong cross-artifact claim.
- Not needed for routine artifact/source pages (the [page checklist](../_schemas/_definition-of-done.md) is enough there).

## The rubric

Send the draft to each judge model with this instruction: *"Score this research synthesis 1–5 on each dimension. For any score ≤3, quote the exact span and say what's wrong."*

| Dimension | Asks | A 5 looks like |
|---|---|---|
| **Citation integrity** | Does every non-obvious claim cite a real `[[sources/...#anchor]]`, and does the cited span actually support it? | No claim floats free; spot-checked citations hold |
| **Faithfulness** | Does the synthesis match what the sources say, with no overstatement or invented detail? | Hedges where the evidence hedges |
| **Completeness** | Is a contradicting artifact or counter-example missing? | Surfaces the tension, doesn't bury it |
| **Non-genericness** | Could this paragraph have been written without reading our wiki? | Specific to *these* artifacts; no AI-pablum |
| **Decision usefulness** | Does it change what we'd build? | Ends in a concrete "what we'd steal / do" |

## Procedure

1. Draft the analysis (cite as you go).
2. Run `scripts/wiki-doctor.py` first — fix mechanical issues (broken links, missing sections) before spending model judgment.
3. Send the draft to 2–3 judge models from **different families** with the rubric above.
4. Triage: any dimension ≤3 from any judge is a blocker. Quote → verify against the source → fix.
5. Record the pass in the analysis page footer: `eval: <models>, <date>, lowest score <n>` and log a `## [date] query | <analysis>` entry.
6. The most honest extra check (Garry's heuristic): re-read for any spot where *you* hesitated while writing — that hesitation is usually the weakest claim.

## Why a second model, not just a careful re-read

A single model (including the author) shares its own blind spots across draft and review — it will rate its own fluent-but-wrong prose highly. A judge from a different family has *different* failure modes, so disagreement between them is signal. This is the diversity argument behind gbrain's three-model split, applied to our synthesis layer.
