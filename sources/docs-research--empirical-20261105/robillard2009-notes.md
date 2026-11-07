# What Makes APIs Hard to Learn? Answers from Developers

Source type: paper
Authors: Martin P. Robillard
Publication/version: IEEE Software 26(6), 27–34, November/December 2009
Source URL: https://www.cs.mcgill.ca/~martin/papers/software2009a.pdf
Version identifier: Published article author-hosted copy; DOI10.1109/MS.2009.193
Retrieved/read: 2026-11-05
Local PDF SHA-256: f2206f981e11caa55442dbdce89b118138924a192d69290dc62e1ee34666b3a6
Local PDF bytes: 919368
Local PDF pages: 9

This file is original research notes and bibliographic metadata. It is not a reproduction or immutable snapshot of the complete paper. Full PDFs and extracted text were read locally under /tmp and are not preserved in Git. To restore, download the source URL and verify the PDF hash; copyright/redistribution rights must be checked before republishing it.

## Reviewed scope

Read article survey/interview methods, results, design-rationale discussion, example-purpose cases, counterintuitive behavior discussion and conclusion. PDF pages2–8 (printed pages27–34); cover and advertising not substantive evidence. This is the 2009 single-author article, not the later 2011 Robillard/DeLine field-study publication.

## Methods and evidence strength

An exploratory 13-question survey invited1,000 randomly selected Microsoft Redmond developers in February/March2009.83responded;3without open-question answers were discarded, leaving80analyzed responses.74reported at least one obstacle.12qualitative interviews recruited from respondents and personal contacts lasted15–45minutes. The low response rate, one company/location and self-report limit prevalence/generalization claims. The author explicitly seeks situations and interpretations rather than generalizable descriptive statistics; the interviews are not a controlled test of documentation interventions.

## Findings supported by this article

- Resource problems accompanied API-structure problems.50of74respondents who reported obstacles mentioned at least one resource obstacle. Do not call this a population incidence or a causal estimate of time lost.
- Knowing relevant high-level design intent helped interviewees choose between alternatives, organize client code and explain behavior. This is need-to-know rationale, not an instruction that every user must learn the entire architecture before using an API.
- Snippets, guided tutorials and complete applications support different information needs. Examples can frustrate when users expect composition, rationale or best practice from a snippet intended only to demonstrate one call. One case involved a developer able to create a connection and issue a command, but unable to infer resource-lifecycle requirements for issuing multiple commands.
- A technically correct low-level reference can still fail when the behavior depends on an unexplained higher-level model. Workflow scheduling, component defaults and derived-API incompatibility provided concrete cases. The answer existed but was not apparent at the entry point.
- Users may infer endorsement and design intent from official examples. Mere execution success does not show a sample represents the current recommended practice; source credibility and obsolescence need attention.

## Portable ideas — our interpretation

Label what an example demonstrates and what it intentionally leaves out. Offer explicit composition examples for multi-call protocols. Connect surprising defaults/lifecycle constraints to the relevant reference entry and task step. Explain choice criteria near alternative APIs. Track whether a sample is runnable, current and recommended as distinct properties. Search and links should lead to the needed rationale without requiring a whole architecture tour.

## Do not conclude

Do not equate missing documentation with poor API design or assume documentation can repair any API structure. Do not transfer2009Microsoft frequencies to all developers, modern web APIs or agents. Do not call interview testimony a measured productivity improvement.

