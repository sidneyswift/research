---
domain: sources
type: # repo | article | paper | tweet | reddit-thread | hn-thread | marketplace-listing | docs-page | video | other
url: # canonical URL
retrieved: # YYYY-MM-DD — when we snapshotted it
snapshot-location: # path inside this wiki (e.g., sources/anthropic--skills/) if cloned, else "link-only"
upstream-commit: # git SHA at time of clone, if a repo
last-reviewed: # YYYY-MM-DD
---

# {source-title}

> **One-line description** of what this source is and why we cite it.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: YYYY-MM-DD
- **Where it lives in this wiki**: relative path or "link-only"
- **Upstream URL**: full URL
- **Upstream identifier**: commit SHA / archive.org link / wayback link / screenshot path

## Anchor map

Every claim that cites this source uses a `#anchor` suffix. Define the anchors here so they're stable. Format: anchor name → what it points at.

- `#root` — the source as a whole
- `#SKILL.md-L1-L20` — first 20 lines of SKILL.md inside the snapshot
- `#manifest` — the plugin manifest file
- `#description-field` — the literal `description:` value
- ...add as needed; pages citing this source must use anchors defined here.

## Why we cite this

What kinds of claims this source supports.

## Popularity signals (if this source provides them)

If this source IS a popularity signal (e.g., a tweet with N likes, a GitHub repo with N stars, a marketplace listing with N installs), capture the values *at time of snapshot* here. Signals decay — always paired with the `retrieved` date.

- **Signal type**: github-stars / tweet-likes / install-count / etc.
- **Value at snapshot**: N
- **As-of**: YYYY-MM-DD

## Related sources

- [[sources/...]] — relationship

## Completeness for social sources

Before extraction, check for expanded note/article text rather than relying on a truncated preview; preserve relevant parent/quote context and every meaning-bearing attachment. Record which were read and which remain unavailable. Keep later linked-page facts in a separately dated capture rather than silently updating the historical post. An author screenshot is attributed evidence, not an independently executed verification.

This applies [[patterns/behavioral/evidence-gated-completion]] to the input boundary: the tibo capture's ordinary `text` field stopped in the third bullet, while `note_tweet.text` exposed fourteen; its attachments also supplied concrete counterexamples absent from the prose. [[sources/poteto--tibo-engineering#capture]] [[sources/poteto--tibo-engineering#auto-pick-counterexamples]]

## Structural verification for GitHub repo sources

For maps with registered `### anchor` headings (or explicit backtick `#anchor` entries) and immutable GitHub `blob/<full-sha>/path#Lx-Ly` links, run `python3 scripts/check-source-citations.py sources/<slug>.md`. It reads pinned Git objects, checks line bounds and registered wikilink targets, and never fetches or edits evidence. Stage new pages or include each with `--page`. It does not establish claim entailment, whole-tree link integrity, runtime correctness, or support every historical source format.

## Versioned protocol and extension collections

Apply [[patterns/quality-bar/revision-bound-review]] and [[patterns/behavioral/context-is-not-authority]] when an evidence collection spans a protocol and host implementations. Record **core revision → extension wire revision/stage → SDK revision → documented host/surface/build → exercised behavior** separately, with an anchor for each. Keep stable/draft and specification/example disagreements explicit. For UI/context channels, record which fields reach the model, host and view; an API field name is not a secrecy guarantee.

Done when the citation map identifies the contract behind each load-bearing claim, records unsupported/unknown fallback and distinguishes documented support from executed acceptance. Motivating evidence: [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]], [[sources/modelcontextprotocol--mcp-apps-docs#messages-context]], [[sources/openai--mcp-extensions#platforms]].

For named document collections with a SHA-256/byte receipt, run `python3 scripts/check-document-captures.py <receipt.json> [...]`. It accepts a capture list or an object with `captures`; entries require `file`, `url`, `sha256`, and `bytes`. It verifies local bytes only, rejects missing/duplicate/escaping paths, and never fetches or assesses semantic support.
