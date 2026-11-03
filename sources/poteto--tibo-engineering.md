---
domain: sources
type: article
url: https://x.com/poteto/status/2117043478140276847
retrieved: 2026-11-03
published: 2026-11-01
snapshot-location: sources/poteto--tibo-engineering/
upstream-commit: n/a (author's long-form X post; no game source revision supplied)
last-reviewed: 2026-11-03
---

# Lauren Tan — engineering tibo.dog with agents

> A first-person account of turning observed defects, performance requirements, state transitions, and game outcomes into executable checks during an agent-assisted game build.

## Snapshot details

- **Retrieved:** 2026-11-03, 12:34 UTC.
- **Published:** 2026-11-01 at 23:57:52 UTC; parent announcement at 21:23:49 UTC.
- **Author:** X API user `2832427459`, handle `poteto`, display name `lauren`; linked to the existing [[creators/lauren-tan]] attribution from [[sources/cursor--plugins-pstack#PK01]].
- **Canonical URL / identifier:** https://x.com/poteto/status/2117043478140276847 / `2117043478140276847`.
- **Raw capture:** [post.json](poteto--tibo-engineering/post.json), including `note_tweet.text`, parent announcement, author, media metadata, and metrics. [snapshot.md](poteto--tibo-engineering/snapshot.md) preserves the complete post and parent text.
- **Attachments:** all four images downloaded, visually inspected, and recorded with URLs, sizes and SHA-256 hashes in [assets.json](poteto--tibo-engineering/assets.json).
- **Linked destination:** https://tibo.dog/ and its About page read and captured as raw HTML plus [linked-pages.md](poteto--tibo-engineering/linked-pages.md). No game application, source clone, TLC run, replay server, or benchmark executed.
- **Evidence class:** author report and author-supplied screenshots; independently observed public-page text. Not an implementation audit. A screenshot of a counterexample is not an independently reproduced counterexample.

## Anchor map

- `#root` — complete post, parent announcement and attached images in `snapshot.md`.
- `#capture` — raw `post.json`: `data.text` stops partway through the TLA+ bullet; `data.note_tweet.text` contains all 14 bullets, 1,918 characters. This capture used the latter.
- `#throughput` — `snapshot.md` L13: author's four-day / approximately 1,150-PR report; initial-commit screenshot `HWE8dRMawAE9vMM.png` shows October 28, 2026, 9:07 PM PDT. No PR history supplied.
- `#defect-lints` — `snapshot.md` L14: ask the bot for a lint rule whenever an issue is discovered.
- `#formal-verification` — `snapshot.md` L15: TLA+ for story, cutscenes and systems; system-specific verification skills.
- `#hot-paths` — `snapshot.md` L16: `.hot.ts` identifies frame/tick code and scopes allocation bans.
- `#engine-boundary` — `snapshot.md` L17: three.js renders; simulation, post-processing and audio are custom.
- `#deterministic-replay` — `snapshot.md` L18: input-replayable simulation and server-side high-score replay.
- `#share-and-localize` — `snapshot.md` L19: run-specific OG images from final statistics; ten languages reported at publication.
- `#music-continuity` — `snapshot.md` L20: biome transitions continue the previous melody.
- `#procedural-audio` — `snapshot.md` L21: live synthesized audio, chip voices plus synthwave, songs as text in code.
- `#procedural-art` — `snapshot.md` L22: sprite files, shared palette and build-time atlas packing.
- `#runtime-target` — `snapshot.md` L23: embedded 245px card through fullscreen; a target of 60 fps / 500 enemies / mid-range phone, not a measured benchmark supplied here.
- `#download-budget` — `snapshot.md` L24: first-download budget fails the build; reported current size about 124 KB gzipped. The budget threshold itself is not specified.
- `#headless-tuning` — `snapshot.md` L25: headless bots tune difficulty against target survival rates.
- `#comments` — `snapshot.md` L26: lint bans comments; prefer improved names or a test.
- `#parent` — `snapshot.md` L28–39: launch announcement credits Grok bot and Cursor and links the game.
- `#auto-pick-counterexamples` — `HWE_v_LaMAADmkY.jpg`: close-up labels three failures: timed auto-pick interrupts the level-up lesson; it selects while the player is away and play continues; after reroll it points to a card from the old hand. All are labeled #1191 in the supplied diagram.
- `#statechart-images` — `HWE_xiHasAABpoV.jpg` marks eleven reported story-mode bugs; `HWE_yjgaUAAeSc2.png` diagrams concurrent story, fires, lines, pause, and offer regions. These are author-produced visual explanations, not inspected model files or raw TLC logs.
- `#current-site` — `linked-pages.md`, captured 2026-11-03: game homepage and About page now describe 27 languages, browser/X play, keyboard/touch controls, and the creator. Preserve this separately from the post's earlier ten-language report; no versioned release history inspected.
- `#traction` — `post.json` `public_metrics` and `snapshot.md` L48–59: dated attention signals, not correctness evidence.

## Why we cite this

Primary evidence for the author's engineering choices in [[artifacts/projects/tibo-dog]], with specific examples beyond general advice to test agent-written code. It illustrates an online defect-to-rule loop, filename-scoped constraints, subsystem verification, deterministic outcome recomputation, executable resource budgets and outcome-based tuning. The adaptation and caveats live in the project page, not in this immutable raw capture.

The formal-verification diagrams make the intended class of failure concrete: interleavings of timers, focus, tutorials and changing offers. They support a report that such bugs were found, not a claim that we checked the models, fixes, or code/model correspondence. See [[concepts/verification-model-fidelity]].

## Popularity signals (if this source provides them)

- **Signal type:** X public metrics at capture.
- **Value at snapshot:** 3,712 likes; 167 reposts; 79 quotes; 197 replies; 5,945 bookmarks; 449,046 impressions.
- **As-of:** 2026-11-03, 12:34 UTC. These indicate attention, not productivity, quality, or causal effectiveness.

## Related sources

- [[sources/cursor--plugins-pstack]] — same creator's separately investigated toolkit. Related design choices do not prove the game used a particular pstack version or statechart renderer.
- [[sources/SHL0MS--skill-diffs]] — corpus-scale defect-derived validation; unlike this post, its documented method includes running rules over a historical corpus. Do not collapse the two evidence scopes.
