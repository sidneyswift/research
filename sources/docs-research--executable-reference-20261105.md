---
domain: sources
type: docs-page
url: https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html
retrieved: 2026-11-05
snapshot-location: sources/docs-research--executable-reference-20261105/
last-reviewed: 2026-11-05
---

# Executable documentation and SDK reference

## Snapshot details

New, immutable 2026-11-05 captures of living first-party documentation. Server Markdown retained where provided; otherwise main/article HTML converted to Markdown. Extraction can expose or omit hidden widgets, change code fencing, and omit visual assets. Images were not visually audited; no tool installations or vendor runtimes executed. The exact reviewed sections are below; a full captured reference does not mean every API/version was reviewed. Guessed inaccessible paths are excluded.

| Capture | Canonical URL | SHA-256 |
| --- | --- | --- |
| [rust-doctests.md](docs-research--executable-reference-20261105/rust-doctests.md) | https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html | `5f23a14664c8dbd731a4f85d72bcc963eb2988ed7c1e72b9deed1879cfa02df1` |
| [rust-api-guidelines.md](docs-research--executable-reference-20261105/rust-api-guidelines.md) | https://rust-lang.github.io/api-guidelines/documentation.html | `c9602c9654b1d142c66e9c17d0df7f59911c2c845caac0d5967cd5c87f2ca4f9` |
| [python-doctest.md](docs-research--executable-reference-20261105/python-doctest.md) | https://docs.python.org/3/library/doctest.html | `104a7ba6f80a7920d7e6618813b76d3b6a0e4161266812cdd849e97d714adf9e` |
| [sphinx-doctest.md](docs-research--executable-reference-20261105/sphinx-doctest.md) | https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html | `a8a976803d4060834552fca0990496f0ba3f5270239685c387ed7a3f56450beb` |

Byte receipts: [captures.json](docs-research--executable-reference-20261105/captures.json).

## Anchor map

- `#root` — collection and evidence limits.
- `#rust-tests` — [rust-doctests.md](docs-research--executable-reference-20261105/rust-doctests.md): Passing/failing, preprocessing, hidden portions, attributes ignore/no_run/compile_fail/should_panic and run directories; macro/edition internals not exhaustively reviewed.
- `#reference-semantics` — [rust-api-guidelines.md](docs-research--executable-reference-20261105/rust-api-guidelines.md): Examples explain purpose; qualified per-item examples; Errors/Panics/Safety, error propagation, crosslinks, release notes and hidden implementation details. Full prose read; linked RFCs not followed.
- `#python-context` — [python-doctest.md](docs-research--executable-reference-20261105/python-doctest.md): Execution Context section; module globals and injected globs; simple usage. Broad stdlib API page captured, not exhaustively read.
- `#python-flags` — [python-doctest.md](docs-research--executable-reference-20261105/python-doctest.md): Option Flags (ELLIPSIS, SKIP, exception detail, whitespace) and Warnings (nondeterministic sets/addresses/floats). Advanced object APIs not reviewed.
- `#sphinx-fixtures` — [sphinx-doctest.md](docs-research--executable-reference-20261105/sphinx-doctest.md): Opening mechanics, directives testsetup/testcleanup/hide/trim flags, grouping, conditional skips. Configuration reference captured but not exhaustively read.

## Why we cite this

Extends [[concepts/developer-documentation-design]] and [[projects/writing-amazing-developer-docs/README]] with specific tool mechanisms. Published behavior is distinct from executed examples, usability and outcome measurements. The local synthetic probe on the hub is our experiment, not evidence that these maintainers' examples are broken.

## Popularity and credibility signals

- Signal: first-party tool/project guidance; no popularity ranking or independent effectiveness measurement.
- As-of: 2026-11-05.

## Related sources

- [[sources/google--developer-documentation#sample-code]] — prior maintained-example guidance.
- [[sources/nam--documentation-use#study]] — observational reader-use evidence and limits.

- [[creators/rust]] — creator/maintainer context.

- [[creators/python]] — creator/maintainer context.

- [[creators/sphinx]] — creator/maintainer context.
