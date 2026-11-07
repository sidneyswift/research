# Capture: readme-llms-upgrade

Canonical URL: https://docs.readme.com/main/changelog/upgraded-llms-txt
Resolved URL: https://docs.readme.com/main/changelog/upgraded-llms-txt
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

---
agentTools:
  siteIndex: https://docs.readme.com/llms.txt
  siteSearch: https://docs.readme.com/agentSearch?query=term1%20term2
  projectIndex: https://docs.readme.com/main/llms.txt
  projectSearch: https://docs.readme.com/main/agentSearch?query=term1%20term2
---

# Upgraded LLMs.txt for AI Agents

We’ve upgraded LLMs.txt and the markdown versions of your pages for AI agents. LLMs.txt now mirrors your sidebar with nested pages, markdown pages point agents at your index, and guessed or missing markdown URLs lead back to LLMs.txt to close the loop.

**Docs**

* The `llms.txt` file now groups pages under their sidebar categories, with child pages nested under their parents, and lists API Reference intro pages under a plain API Reference heading.
* LLMs.txt settings now have a single Summarize Index option that links the root llms.txt to per-section and per-category files instead of listing every page.
* Markdown versions of your pages now include `agentTools` front matter that points agents at your llms.txt index.
* Requests for a missing `.md` page now return a markdown 404 that points to llms.txt, and guessed URLs like `/docs.md`, `/reference.md`, or `/docs/<category>.md` redirect to the matching llms.txt. Markdown requests to a project root redirect there too.
* The markdown versions of the API Reference Getting Started and Authentication pages now include your API's servers and security schemes, when your OpenAPI definition is visible to the reader.

**Enterprise**

* Enterprise projects now have a project switcher in the sidebar for jumping between projects in the group, with a quicker link to the enterprise dashboard.
* Enterprise group analytics (Page Views, New Users, Search Terms, and page feedback) can now be exported to CSV.

**AI**

* Every AI Agent edit suggestion (page rewrites, API Reference updates, and Recipe changes) now has its own Apply and Revert controls.
* The AI Agent can now read the content inside Reusable Content blocks when working on a page, while keeping the blocks themselves intact.

**MCP**

* Hidden and deprecated endpoints can now be individually enabled for your MCP server from the MCP routes settings.

**Translations**

* AI-translated guides, custom pages, and API Reference pages can now be re-translated individually with a Re-translate This Page button in the editor footer.
* The translation status on the enterprise Translations page now expands to show progress for each content type during a run, with links to any pages that failed to translate.

<br />

***

### Bugs Eaten (by Owlbert) 🐛

**API Reference**

* The API Explorer now keeps your selected server when you move between API definitions that share the same base URL, including compatible server variable values.

**AI**

* Ask AI analytics now shows the name of the model that answered a question, including when using the recommended model.

**MCP**

* MCP install links on enterprise child project docs now connect to that child project only.
* The `execute-request` tool now accepts server URLs with a trailing slash, and returns the HTTP status for error responses and empty successful responses.

**Docs**

* With Sticky Header on, the landing page header and hero now scroll away together, while other pages keep the header pinned.
* Deep links to a `#heading` now stay on that heading while images above it load, and the table of contents highlights the right section.
* Signed-in admins and editors no longer see a dark flash when the docs load, and an enterprise child project set to light or dark keeps that color scheme.
* Hidden and deleted changelog posts now disappear from the public changelog right away.
* Uploaded header logos now stay sharp, and wide logos on the end user login page stay inside their container.

**Editor**

* Rename and Delete on a category in the editor sidebar now work in Chrome.
* Blank lines between blocks inside a component are now preserved.
* Saving unsaved edits to a new branch no longer triggers a "Leave site?" prompt or gets stuck on "Redirecting…".
* Rebasing a branch more than once on a GitHub-synced project no longer shows conflicts on files the parent version never changed.

**Admin**

* Toggling the global In-App or Email notification setting now preserves your individual preferences for the other channel.

**Translations**

* Glossary terms on translated pages now keep their tooltip.
* Translated pages now keep the source page's SEO/Display image, and removing it from the source clears it on the translation too.
* Structural changes to an OpenAPI definition, like a new endpoint or a renamed enum, now carry over to its translated versions.
* API Reference pages whose definition didn't fully translate now show the "Translation failed" banner.
* Doc Metrics now records page views from admins and editors on translated docs in the language of the page they read.