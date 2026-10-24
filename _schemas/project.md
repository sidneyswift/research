---
domain: _schemas
type: project-template
last-reviewed: 2026-10-23
---

# Project artifact template

Use for a runnable system larger than a single skill, plugin, or MCP server. This fills the previously referenced-but-absent project template. Follow [_definition-of-done.md](_definition-of-done.md) and retain the exhaustive portable-idea ledger.

The evidence-class and guarantee-boundary fields below apply [[patterns/behavioral/evidence-gated-completion]] and [[patterns/behavioral/latent-vs-deterministic-split]] to research. The concrete motivating case is [[artifacts/projects/humanlayer]]: prompt review gates differ from runtime ACLs, stored history differs from side-effect replay, local review state differs from shared approval, and a labeled eval matrix can fail to vary the actual model. [[sources/humanlayer--humanlayer#permissions]], [[sources/humanlayer--humanlayer#runtime-boundary]], [[sources/humanlayer--humanlayer#review-watermarks]], [[sources/humanlayer--humanlayer#eval-pipeline]]

## Frontmatter

```yaml
domain: artifacts
subdomain: projects
type: project
name: project-slug
creator: "[[creators/creator-slug]]"
source: "[[sources/creator--source]]"
ecosystem: relevant-ecosystem
status: source-investigated
last-reviewed: YYYY-MM-DD
```

## Attributes

State the unit of study, pinned revision, runnable components, distribution/license, dated attention signals, and what was actually inspected or executed. Count files/areas only from an explicit inventory; do not claim exhaustive coverage of an unbounded repository.

## Relationships

Link creator, source, constituent artifacts, existing concepts, and patterns. Deduplicate before creating a new page. Multiple modules of one project do not automatically supply independent examples.

## Mechanism and themes

Explain the system by responsibilities, data/control flow, authority, lifecycle, and recovery boundaries. Use diagrams only where they clarify an actual relationship.

For load-bearing claims, distinguish **implementation**, **test inspected**, **test executed**, **prompt policy**, **documentation**, and **inference**. State the scope of a guarantee: process, host, transaction, content revision, session, or external effect. Record code-versus-documentation conflicts instead of silently selecting the more attractive account.

## Patterns demonstrated

Link each observed mechanism to a source anchor. Keep new patterns proposed until the wiki has the required independent evidence; do not inflate the example count with related modules.

## What we'd steal

Preserve every useful mechanism observed in the investigated scope; ★-mark priorities. Each entry needs its purpose, source, adaptation/use case, and important limit. A collection of slogans without implementation evidence is not an extraction.

## Tensions and anti-patterns

Include counterexamples, failure modes, bypasses, configuration dependencies, skipped checks, and measurable claims not yet demonstrated. Separate a reasonable design tradeoff from a confirmed defect.

## Open questions and verification record

State remaining evidence gaps and what would settle them. Run the wiki checks; validate new links and registered source anchors, plus pinned path/range integrity. Existing unrelated lint findings remain visible rather than being rewritten away.
