---
domain: sources
type: article
url: https://www.philschmid.de/code-mode
retrieved: 2026-11-02
snapshot-location: sources/philschmid--code-mode/snapshot.md
published: 2026-11-01
last-reviewed: 2026-11-02
---

# Why Agents Are Soon Only Going to Have 1 Tool

> Philipp Schmid's explanation of code-based tool orchestration, its runtime interface and tradeoffs.

## Snapshot details

- **Retrieved:** 2026-11-02; **published:** 2026-11-01 (page date).
- **Canonical URL:** https://www.philschmid.de/code-mode
- **Version stamp:** publication date; no upstream commit. Captured rendered article text, code blocks and outbound links in [snapshot.md](philschmid--code-mode/snapshot.md); two explanatory diagrams stored alongside.
- **Capture fidelity:** HTML article converted to Markdown; navigation/footer excluded. Adjacent date/read-time elements concatenate in the capture. Examples preserved as published and never executed; API/model names and isolation claims are not independently validated.

## Anchor map

All line ranges refer to the immutable local [snapshot](philschmid--code-mode/snapshot.md).

### root

Whole article, lines 3–193; headline and publication date at lines 3–5.

### workflow-composition

Lines 7–30: code orchestration, dependent workflows, parallel fan-out and return-schema motivation. Includes the comparison diagram at line 11.

### typed-interface

Lines 32–83: typed bridge, discoverable catalog, selective text/image/audio output and host-side state helpers; illustrative Linear composition. Architecture diagram at line 83.

### runtime-boundaries

Lines 85–93: language runtime versus shell, host-mediated credential/schema/approval handling and state outside prompt history.

### pseudo-example

Lines 95–177: illustrative Gemini API loop, mocked host functions and `node:vm` execution; comment recommends QuickJS or isolated-vm for untrusted code. Not a tested integration or isolation demonstration.

### adoption-claims

Lines 179–185: author-reported Pi, Factory, Codex and framework adoption; Factory accuracy/spend numbers are unsupported here by a captured benchmark report. The link supplied for those numbers is a benchmark homepage, not an experimental protocol.

### caveats

Lines 187–193: universal single-tool adoption remains an open question; existing shell-oriented skills/CLIs may need adaptation.

## Why we cite this

Extends [[concepts/code-mode-capability-interface]] beyond Kody with a concrete interface sketch. Distinguishes model-visible tool count, backend capabilities, context emission and authority. Supports author-attributed architecture arguments, not independently demonstrated ecosystem convergence or performance gains.

## Popularity signals

No view/share/install count captured as of 2026-11-02. Byline/personal-site authorship and dated technical examples are provenance signals, not evidence of popularity. No popularity claim made.

## Related sources

- [[sources/kody-hq--kody#intent]] — independently inspected implementation explicitly credits Cloudflare; two-tool discovery/execution surface rather than a literal universal single tool.
- [[creators/philipp-schmid]] — author.
