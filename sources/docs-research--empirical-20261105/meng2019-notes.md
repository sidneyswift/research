# How Developers Use API Documentation: An Observation Study

Source type: paper
Authors: Michael Meng; Stephanie Steinhardt; Andreas Schubert
Publication/version: Communication Design Quarterly, online first January29,2019; DOI10.1145/3274995.3274999
Source URL: https://www.mangold-international.com/_Resources/Persistent/a/7/1/2/a712bdd99343412abc60642ea624ae047ef00b27/Meng_et_al_How-Developers-Use-API-Documentation_2019.pdf
Version identifier: Published article PDF bearing author copyright; online-first2019, observation spring2016
Retrieved/read: 2026-11-05
Local PDF SHA-256: 16da25c48f22200b5cd561f8293bd5c7597e0194f21bfcd15aaa847e5d88cb3f
Local PDF bytes: 709856
Local PDF pages: 11

This file is original research notes and bibliographic metadata. It is not a reproduction or immutable snapshot of the complete paper. Full PDFs and extracted text were read locally under /tmp and are not preserved in Git. To restore, download the source URL and verify the PDF hash; copyright/redistribution rights must be checked before republishing it.

## Reviewed scope

Read methods/materials/participants/procedure, quantitative and qualitative results, obstacles, threats, implications and conclusion; PDF pages2–9 (printed1–8). Tables and prose used for the reported counts; no claim to evaluate the provider's current website. Hosted by Mangold International, but the evidence is the original article rather than a vendor case study.

## Methods and evidence strength

11volunteer developers from3organizations (6e-commerce software,3digital publishing,2universityIT),10men/1woman, all native German speakers, mean9years developer experience. None knew the selected shipcloud REST API. They performed5provider-designed, medium-difficulty shipping tasks such as label creation, returns, pickup slots and special delivery addresses using HTTP requests through curl or Postman.3participants completed3rather than5tasks. Screencasts/audio and eye tracking supported qualitative observation; eye tracking was not analyzed quantitatively at detailed regions because data quality varied. Task instructions German, documentation English. The study is exploratory: smallsample, single API, self-selection and observation effects; no randomized documentation comparison or causal productivity effect.

## Findings supported by this article

- Developers differed in working strategy, including opportunistic adaptation and systematic hypothesis/checking. These categories did not map simply to years of programming experience, domain background or interest in conceptual pages. Avoid turning them into fixed personas or learning-style diagnoses.
- The reference and examples were used from initial unfamiliarity, not only after a tutorial phase. Developers also needed domain concepts but did not consistently seek them in a separate concept section.
- Participants had difficulty predicting which category held an answer. Samples versus Recipes was unclear; inconsistent within-page navigation made previously noticed information difficult to relocate. No site search forced page-search behavior that failed across multiple pages.
- Code samples that replaced shared code with references/placeholders avoided redundant authoring but interrupted copy/adapt use. This concerns omitted code or references to another sample, not a ban on environment-specific credential placeholders.
- Relevant e-commerce knowledge appeared associated with faster task completion; the design cannot isolate it from other participant differences.
- The authors recommend task-linked concepts and explicit concept-to-code connections. A return-shipment task illustrates the missing mapping: a developer had to infer whether return shipment was a new resource or a parameter on an existing one.

## Portable ideas — our interpretation

Test documentation with actual tasks, including relocating previously encountered information. Make reusable examples complete in their presented form even if generated from a shared source. Use task vocabulary as a discovery route alongside reference categories. Place short essential domain explanations in the task and, where needed, code comments. Maintain explicit text-to-symbol correspondence; do not rely on color alone. Treat an API reference as an onboarding surface too. Provide search and stable navigation rather than imposing a linear reading sequence.

## Tension to preserve

This observed study recommends integrating essential concepts with tasks and some intentional redundancy; a rigid interpretation of separated documentation types or blanket DRY can conflict with this. These are design hypotheses supported by observed breakdowns, not experimental proof that a specific page layout is superior.

