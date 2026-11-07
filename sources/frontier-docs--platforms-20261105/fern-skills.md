# Capture: fern-skills

Canonical URL: https://buildwithfern.com/learn/docs/ai-features/host-skills
Resolved URL: https://buildwithfern.com/learn/docs/ai-features/host-skills
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

> This page is for Docs.

> For clean Markdown content of this page, append .md to this URL. For the complete documentation index, see https://buildwithfern.com/learn/llms.txt.

# Custom skills for your site

> Serve author-supplied agent skills from your Fern docs site and configure the Install skills button.

Fern Docs sites can serve your own [Agent Skills](https://www.skills.sh) so your users can discover and install them with the [skills CLI](https://www.skills.sh). You can also add an "Install skills" button to your docs UI that opens a modal with the install command and your skill list.

#### Lay out the bundle

Place your skills in your `fern/` folder under `.well-known/agent-skills/` (the current v0.2.0 spec) or `.well-known/skills/` (the legacy v0.1.0 layout). Both are supported and can coexist. Each skill is a subdirectory holding at least a `SKILL.md`, with optional supporting files alongside it.

#### Write each SKILL.md

Each `SKILL.md` needs YAML frontmatter with `name` and `description`, following the [Agent Skills spec](https://agentskills.io):

**`fern/.well-known/agent-skills/plant-care/SKILL.md`**

```markdown title="fern/.well-known/agent-skills/plant-care/SKILL.md"
---
name: plant-care
description: Guide for diagnosing and treating common plant diseases.
---

# Plant Care

When diagnosing a plant issue, check for...
```

#### Add the discovery manifest

The `index.json` at the root of the skills directory is required. It enumerates every skill so clients can discover them in a single request. Each entry points at a single artifact by `url` and `digest`, and its `type` decides what the skills CLI downloads:

* `skill-md`: the `url` is a `SKILL.md`. Only that file is installed, so use this type for single-file skills.
* `archive`: the `url` is a `.tgz` or `.zip` of the whole skill directory. The CLI verifies the digest and extracts every file, so use this type for skills with scripts, references, or other supporting files. Place the archive inside the skills directory next to the skill folder and Fern serves it with the rest of the bundle.

**`fern/.well-known/agent-skills/index.json`**

```json title="fern/.well-known/agent-skills/index.json"
{
  "$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json",
  "skills": [
    {
      "name": "plant-care",
      "type": "skill-md",
      "description": "Guide for diagnosing and treating common plant diseases.",
      "url": "/.well-known/agent-skills/plant-care/SKILL.md",
      "digest": "sha256:c4d5e6f7..."
    },
    {
      "name": "garden-planner",
      "type": "archive",
      "description": "Plan garden layouts and planting schedules.",
      "url": "/.well-known/agent-skills/garden-planner.tgz",
      "digest": "sha256:a1b2c3d4..."
    }
  ]
}
```

The legacy v0.1.0 manifest lists a `files` array per skill instead of `type`, `url`, and `digest`. The CLI fetches `SKILL.md` plus every listed file individually, so a multi-file skill needs no archive but must enumerate each file:

**`fern/.well-known/skills/index.json`**

```json title="fern/.well-known/skills/index.json"
{
  "skills": [
    {
      "name": "garden-planner",
      "description": "Plan garden layouts and planting schedules.",
      "files": ["SKILL.md", "references/api.md"]
    }
  ]
}
```

#### Publish

Fern uploads the bundle during `fern generate --docs` and serves the files as-is — no `docs.yml` configuration is required. `fern check` validates the bundle at upload time, flagging:

* A missing or unparseable `index.json`
* A `SKILL.md` whose `name` isn't kebab-case, exceeds 64 characters, or doesn't match its parent directory name
* A `SKILL.md` with a missing or empty `description` (max 1,024 characters)

Once published, skills are served at:

* `https://your-docs-domain.com/.well-known/agent-skills/index.json` (discovery manifest)
* `https://your-docs-domain.com/.well-known/agent-skills/<skill-name>/SKILL.md` (individual skill)
* `https://your-docs-domain.com/.well-known/agent-skills/<skill-name>/<path>` (any supporting file in the skill directory, or an archive placed in the skills directory)
* `https://your-docs-domain.com/.well-known/skills/index.json` (legacy v0.1.0 manifest)

For sites with a basepath like `/docs`, the endpoints live under that basepath (e.g., `https://example.com/docs/.well-known/agent-skills/index.json`).

#### Install the skills

With the bundle published, anyone can install your skills with:

```bash
npx skills add https://your-docs-domain.com
```

The `https://` scheme is required: a bare domain is treated as a GitHub repository shorthand.

#### Configure the Install skills button

Surface your skills in the docs UI by adding an "Install skills" button to the [page action bar](/learn/docs/configuration/site-level-settings#page-actions-configuration). Set `page-actions.options.skills` in `docs.yml` and the button opens a modal with a copyable install command, the list of available skills, and an optional link to the source repository.

**`docs.yml`**

```yaml docs.yml
page-actions:
  options:
    skills:
      title: Plant API Skills
      description: Skills for working with the Plant Store API.
      repository: https://github.com/your-org/plant-api-skills
      install-command: npx skills add https://your-docs-domain.com
      skills:
        - name: plant-care
          description: Guide for diagnosing and treating common plant diseases.
          url: https://github.com/your-org/plant-api-skills/tree/main/plant-care
        - name: garden-planner
          description: Plan garden layouts and planting schedules.
```

## Install skills properties

Configure the Install skills button under `page-actions.options.skills` in `docs.yml`.

**`page-actions.options.skills`** `object`

Enables the "Install skills" page action and configures the modal it opens. Omit to hide it.

---

**`page-actions.options.skills.title`** `string`

Overrides the modal title.

---

**`page-actions.options.skills.description`** `string`

Overrides the modal description.

---

**`page-actions.options.skills.learn-more-url`** `string`

URL for a "Learn more" link shown alongside the description.

---

**`page-actions.options.skills.repository`** `string`

Source repository URL displayed as a "View source" button in the modal.

---

**`page-actions.options.skills.install-command`** `string or list of strings`

Command(s) shown as a copyable block in the modal. A single string is shown as-is; an array is joined with newlines for multi-step installs. Defaults to `npx skills add https://<your-docs-domain>` when omitted.

---

**`page-actions.options.skills.skills`** `list of objects`

List of skills displayed in the modal. Each entry has a `name` (required), `description` (optional), and `url` (optional link to the skill source). When the site serves a `/.well-known/agent-skills/index.json` or `/.well-known/skills/index.json` manifest, the manifest replaces this list.

---