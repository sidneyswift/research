---
domain: patterns
type: pattern
name: version-as-update-gate
category: quality-bar
status: confirmed
last-reviewed: 2026-06-02
example-count: 2
---

# version-as-update-gate

> A plugin's `version` field is not metadata — it is the **update-delivery trigger**:
> installs are cached by version, so bumping `version` is what ships changes to users.
> Therefore make `version` **owned by release automation**, forbid hand-bumps in feature
> PRs, and let one automated bump per release be the gate that delivers everything merged
> since the last one.

## Longer definition

In a marketplace/plugin world, a consumer's client caches each install **by version** (a
new version → a new cached directory it pulls; see
[[sources/anthropic--plugins-reference#plugin-caching-and-file-resolution]]). So `version`
is load-bearing for *delivery*, not just bookkeeping: change it and users get the update;
don't and they don't. The hazard is that, when many PRs batch between releases, **no
contributor can know the final released version from inside their PR** — so if everyone
hand-bumps, you get version drift, double-bumps, and broken or skipped update delivery. The
pattern removes the human from the version: a pre-commit hook or a release tool (release-please,
semantic-release) owns the field, contributors are explicitly told *not* to touch it, a drift
check fails the build if they did, and the single automated bump at release time is the gate
that ships the accumulated work.

## Mechanism

Two in-wiki realizations, different machinery, same rule:

- **`anthropics/financial-services` — pre-commit hook + CI backstop.** A pre-commit hook
  patch-bumps a changed plugin's `version` **once per branch**; a GitHub Action backstops it;
  `version` is what gates update delivery to installed users
  ([[sources/anthropic--financial-services#scripts-version-bump]]).
- **`compound-engineering` — release-please + linked-versions + a parity validator.** Releases
  are prepared by automation (`release-please` + `semantic-release`); `linked-versions` keeps
  `cli` and `compound-engineering` at the same version. Contributors are *forbidden* to
  hand-bump `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  or `marketplace.json`; `bun run release:validate` fails on version/parity drift; and CI
  validates the **PR title against Conventional Commits** (`feat:`/`fix:`/…) so the tool can
  classify change intent and pick the bump. Past *direct* merges (bypassing the gate) "caused
  version drift requiring multi-PR recovery" — documented in
  `docs/solutions/workflow/release-please-version-drift-recovery.md`
  ([[sources/every--compound-engineering-plugin#release-automation]]).

The shared shape: `version` is automation-owned; manual bumps are an error; a validator
detects drift; one bump per release delivers the batch.

## When to use

- **Published/installable artifacts whose consumers update *by version*** — marketplace
  plugins, npm packages, anything cached per-version. The version literally controls which copy
  is live.
- **Multi-manifest repos** that must keep several version fields in parity (CE's Claude/Cursor/
  Codex manifests; a marketplace catalog mirroring per-plugin versions). A validator is the only
  reliable way to hold parity.
- **When many PRs batch between releases** — the moment a contributor *can't* know the final
  version from inside their PR, hand-bumping is guaranteed to drift.

## When NOT to use

- **Single-author repos nobody installs by version.** If you're the only consumer and there's no
  version-keyed delivery, a hand-bump (or no version at all) is simpler and fine.
- **Pre-release / throwaway artifacts** where "delivery" isn't a concept yet — adding release
  automation before you have users is premature ceremony.
- **When `version` is purely cosmetic** (a label in a README, no cache or client keyed on it).
  Then it isn't a gate and gating it buys nothing.

## Why it works

It separates **"what changed"** (the PR — classified by its Conventional-Commit type) from
**"when it ships"** (the release — a single automated bump). That separation is necessary
because the version is *emergent from the batch*: with N PRs queued, the next version depends on
the highest-severity change among them, which no single PR author can see. Mechanically it works
because installs are **versioned caches**: a marketplace client copies each plugin version into
its own directory and GCs orphaned versions after a grace period
([[sources/anthropic--plugins-reference#plugin-caching-and-file-resolution]]), so an errant manual
bump doesn't just mislabel — it can mis-deliver (ship half-baked state, or fail to ship at all).
Putting the field under automation + a drift check converts "did someone bump the version wrong?"
from a latent production bug into a build failure — the same move
[[patterns/composition/single-source-multi-surface-distribution]] makes for content drift.

## Detection recipe

- **Look for**: a `release-please`/`semantic-release` config or a pre-commit version-bump hook; a
  `release:validate`-style parity check; and `AGENTS.md`/`CONTRIBUTING` text that *explicitly
  forbids* manual version bumps in feature PRs.
- **Confirm with**: the `version` field is demonstrably **not** edited in normal feature PRs, and a
  drift check exists that would fail if it were. Bonus tell: a documented "version drift recovery"
  runbook (CE has one) — proof the team hit the failure and codified the fix.
- **Rule out**: a repo where contributors *do* bump `version` by hand each PR (that's plain manual
  versioning, not this pattern), or where `version` isn't tied to any update-delivery mechanism
  (then it's cosmetic, and gating it is pointless). Distinguishing question: *"If I hand-edit the
  version in a PR, does something fail — and does the bump itself ship anything to a user?"* Yes to
  both → this pattern.

## Examples in this wiki

- [[artifacts/plugins/anthropic-financial-services-marketplace]] — a pre-commit hook patch-bumps a
  changed plugin's `version` once per branch; a CI Action backstops it; `version` gates update
  delivery. — citation: [[sources/anthropic--financial-services#scripts-version-bump]]
- [[artifacts/plugins/compound-engineering]] — release-please + `linked-versions` own all version
  fields across three marketplace manifests; contributors forbidden to hand-bump; `bun run
  release:validate` fails on drift; a `release-please-version-drift-recovery.md` runbook documents
  the failure mode. — citation: [[sources/every--compound-engineering-plugin#release-automation]]

## Counter-examples or anti-pattern

- [[artifacts/plugins/anthropic-skills-marketplace]] — a **demonstration** marketplace where
  `version` is nominal: the consumer is a human studying the format, not a fleet pulling production
  updates keyed on the field. Nothing breaks if a version is hand-set, because no version-keyed
  delivery depends on it. This sharpens the scope: version-as-update-gate earns its keep only when
  (a) consumers update by version *and* (b) PRs batch between releases. Absent either, the
  automation is overhead.
- **The anti-pattern it prevents:** hand-bumping `version` in feature PRs. CE's own history is the
  cautionary tale — direct merges that bypassed the gate "caused version drift requiring multi-PR
  recovery" ([[sources/every--compound-engineering-plugin#release-automation]]). The fix wasn't
  "bump more carefully"; it was "take the field away from humans."

## Related patterns

- [[patterns/composition/single-source-multi-surface-distribution]] — composes-with: CE keeps *three*
  marketplace manifests in version parity; the same validator that catches content drift catches
  version drift. Version-gating is the *delivery* half of single-sourcing.
- [[patterns/structural/marketplace-as-multi-plugin]] — composes-with: a marketplace carries a
  per-plugin version *and* a catalog version; this pattern is how those stay coherent
  (`linked-versions`, parity checks).
- [[patterns/quality-bar/complexity-ratchet]] — instance-of (delivery arm): release automation +
  the drift-recovery runbook are part of the forward-only floor — a documented lesson
  (`release-please-version-drift-recovery.md`) locked so the team can't re-suffer it.

## Open questions

- **Conventional-Commit-driven bumps depend on honest PR titles.** CE validates titles in CI, but
  the *type* (`feat` vs `fix`) is a human judgment that drives the version. How often does a
  mis-typed PR produce a wrong bump, and does the validator catch semantic (not just syntactic)
  misc;classification?
- **`linked-versions` couples unrelated components** (a plugin-only change still bumps the CLI). Is
  the simplicity of one synced version worth shipping no-op version bumps to consumers of the other
  component?
- **Does a third example use a *different* delivery substrate** (e.g., an MCP server versioned by a
  registry rather than a file cache)? Both current examples are file-cached plugin installs; the
  pattern likely generalizes but isn't yet shown outside that substrate.
