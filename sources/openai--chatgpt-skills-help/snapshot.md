<!-- PARTIAL CAPTURE — 2026-06-04. The canonical page https://help.openai.com/en/articles/20001066-skills-in-chatgpt is Cloudflare/Intercom-gated against automated fetch; direct retrieval returned an empty body. Content below was reconstructed from search-engine extraction of that exact article URL (two independent research passes, 2026-06-04, agreeing on all quoted items). Quoted strings matched verbatim across both passes; unquoted text may paraphrase the article. Treat as secondary-fidelity evidence; re-capture from a browser is a TODO. Do not edit. -->

# Skills in ChatGPT (help.openai.com article 20001066) — extracted content

## What skills are

Skills are "reusable, shareable workflows that tell ChatGPT how to do a specific task" so ChatGPT can do that task more consistently. A skill can include instructions, examples, and code. Format: a SKILL.md manifest plus optional `scripts/`, `references/`, `assets/`.

"OpenAI skills follow the Agent Skills open standard, so you can download them from one product and install them in another."

## Availability

Beta in ChatGPT **Business, Enterprise, Edu, Teachers, and Healthcare** plans (Plus/Free not listed). Skills are also supported in Codex and via the OpenAI API (Responses API Skills tool).

During early access, skills are **off by default for Enterprise/Edu**; admins toggle availability per role. (Business default not stated in extracted content.)

## Creation and invocation

- Created in a built-in editor (**Skills > New skill > Create with editor**) or by asking ChatGPT in chat to create a skill (it prompts to install).
- Accessed via **profile icon → Skills**.
- Invocation is automatic: "ChatGPT can automatically use one or more skills when they are helpful" — no manual activation.

## Workspace distribution and admin controls

Members install skills shared with the workspace via **Skills > Shared with you > ••• > Install**.

Workspace admins control five skill permissions in **Workspace settings > Permissions & roles**:

1. **Enable skills** — allow members to create and use skills
2. **Enable skill uploading** — allow members to upload skill files from their computer to the workspace
3. **Share skills** — allow members to share skills with workspace members, groups, or the whole workspace
4. **Publish skills to workspace** — allow members to publish and share skills with the entire workspace
5. **Enable skills installing** — allow members to "install skills for other workspace members so they are used automatically"

The **admin Skills page** is separate from Permissions & roles: "Permissions & roles controls which roles can create, use, upload, share, publish, or install skills. The admin Skills page helps workspace admins review and manage individual skills created in their workspace."

## Adjacent surfaces

ChatGPT for Excel/Google Sheets and PowerPoint "support Skills and apps where available."
