# Documentation topic types (CTRT) | GitLab Docs

Source: https://docs.gitlab.com/development/documentation/topic_types/
Final URL: https://docs.gitlab.com/development/documentation/topic_types/
Retrieved: 2026-11-05
Capture: main-content text extracted from HTML; no UI interaction or code execution.

/
#
Documentation topic types (CTRT)
Each topic on a page should be one of the following topic types:
Concept
Task
Reference
Troubleshooting
Even if a page is short, the page usually starts with a concept and then
includes a task or reference topic.
The tech writing team sometimes uses the acronym
CTRT
to refer to the topic types.
The acronym refers to the first letter of each topic type.
For an overview, see
Editing for style and topic type
.
##
Other page and topic types
In addition to the four primary topic types, you can use the following:
Page type:
Tutorial
Page type:
Get started
Page type:
Top-level
Page type:
Prompt example
Topic type:
Related topics
Page or topic type:
Glossaries
##
Pages and topics to avoid
You should avoid:
Pages that are exclusively links to other pages. The only exceptions are
top-level pages that aid with navigation.
Topics that have one or two sentences only. In these cases:
Incorporate the information in another topic.
If the sentence links to another page, use a
Related topics
link instead.
##
Topic title guidelines
In general, for topic titles:
Be clear and direct. Make every word count.
Use fewer than 70 characters when possible. The
markdownlint
rule:
line-length
(MD013)
Use articles and prepositions.
Follow
capitalization
guidelines.
Do not repeat text from earlier topic titles. For example, if the page is about merge requests,
instead of
Troubleshooting merge requests
, use only
Troubleshooting
.
Review the specific guidance for the topic type. For example, do not use
Overview
or
Introduction
for
concept topic titles
.
Avoid using hyphens to separate information.
For example, instead of
Internal analytics - Architecture
, use
Internal analytics architecture
or
Architecture of internal analytics
.
See also
guidelines for heading levels in Markdown
.
##
Related topics
If inline links are not sufficient, you can create a section called
Related topics
and include an unordered list of related topics. This topic should be above the Troubleshooting section.
The link text should be brief and scannable.
Use topic titles (not complete sentences) and do not end them with periods.
markdown
## Related topics
-
[
CI/CD variables
](
link-to-topic.md
)
- [
Environment variables
](
link-to-topic.md
)
Was this page helpful?
Yes
No
