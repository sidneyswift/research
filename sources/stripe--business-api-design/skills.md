# Agent skills

Canonical URL: https://docs.stripe.com/skills.md
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

# Skills for agents

Install instructions that help AI agents create more accurate Stripe integrations.

[Agent skills](https://agentskills.io/home) give AI coding agents reusable guidance for building Stripe integrations. Stripe-maintained skills provide the newest product and API guidance based on the latest recommended practices.

## Install skills with a plugin (Recommended)

[Agent plugins](https://docs.stripe.com/agents/plugin.md) for Stripe automatically configure the Stripe MCP server, install our skills, and make sure they’re up-to-date. You get our latest capabilities without configuration or maintenance.

```bash
npm install -g @stripe/cli@latest
stripe agent setup
```

This command automatically detects which agents you use, and runs the applicable commands.

## Manually install agent skills 

Alternatively, run the following command to install Stripe skills manually. You also needs to regularly update the skills to get the latest versions.

```bash
npx skills add https://docs.stripe.com
```

> Manually installed skills don’t auto-update. Run `npx skills update -y` to get the latest versions.

To access live Stripe account data, also [set up the Stripe MCP](https://docs.stripe.com/mcp.md#manual) server. Together, Stripe MCP and skills provide capabilities similar to the plugin, but you must configure and maintain them separately. Vendor-specific plugin features, such as lifecycle hooks, aren’t available.

## Skills index

See the [index of Stripe skills](https://docs.stripe.com/.well-known/skills/index.json.md).

If `npx skills` isn’t available: You can use curl to fetch the index of available skills, what they do, and their files from `https://docs.stripe.com/.well-known/skills/index.json`. To download a skill and its related files, use curl to download them from `https://docs.stripe.com/.well-known/skills/<filepath>`.

## See also

- [Plugin for agents](https://docs.stripe.com/agents/plugin.md)
- [Stripe MCP](https://docs.stripe.com/mcp.md)

