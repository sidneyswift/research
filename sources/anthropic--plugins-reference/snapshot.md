# SNAPSHOT — Claude Code "Plugins reference" (code.claude.com)

> Partial verbatim snapshot captured 2026-05-31. Source is a living docs page, so only the
> sections the wiki cites are captured verbatim (caching/file-resolution and the closely
> related env-var + persistent-data sections), plus the page's full heading outline for the
> anchor map. Full page: https://code.claude.com/docs/en/plugins-reference
> Re-fetch and re-snapshot if upstream changes. Extracted via the page DOM (Mintlify docs site).

## Page heading outline (verbatim, as of 2026-05-31)

H2 sections, in order:

```
Plugin components reference   (H3: Skills · Agents · Hooks · MCP servers · LSP servers · Monitors · Themes)
Plugin installation scopes
Skills-directory plugins      (H3: Choose where the plugin loads from · Edit, reload, and disable a skills-directory plugin)
Plugin manifest schema        (H3: Complete schema · Required fields · Unrecognized fields · Metadata fields · Default enablement · Component path fields · Experimental components · User configuration · Channels · Path behavior rules)
Environment variables
Persistent data directory
Plugin caching and file resolution
Path traversal limitations
Share files within a marketplace with symlinks
Plugin directory structure    (H3: Standard plugin layout · File locations reference)
CLI commands reference
Debugging and development tools (H3: Debugging commands · Common issues · Example error messages · Hook troubleshooting · MCP server troubleshooting · Directory structure mistakes)
Distribution and versioning reference (H3: Version management)
See also
```

Top-of-page framing line (verbatim):
> "A **plugin** is a self-contained directory of components that extends Claude Code with
> custom functionality. Plugin components include skills, agents, hooks, MCP servers, LSP
> servers, and monitors."

## Verbatim: "Plugin caching and file resolution"

> Plugins are specified in one of two ways:
>
> * Through `claude --plugin-dir` or `claude --plugin-url`, for the duration of a session.
> * Through a marketplace, installed for future sessions.
>
> For security and verification purposes, Claude Code copies *marketplace* plugins to the
> user's local **plugin cache** (`~/.claude/plugins/cache`) rather than using them in-place.
> Understanding this behavior is important when developing plugins that reference external files.
>
> Each installed version is a separate directory in the cache. When you update or uninstall a
> plugin, the previous version directory is marked as orphaned and removed automatically 7 days
> later. The grace period lets concurrent Claude Code sessions that already loaded the old
> version keep running without errors.
>
> Claude's Glob and Grep tools skip orphaned version directories during searches, so file
> results don't include outdated plugin code.

## Verbatim: "Environment variables" (the file-resolution mechanism)

> Claude Code provides three variables for referencing paths. All are substituted inline
> anywhere they appear in skill content, agent content, hook commands, monitor commands, and
> MCP or LSP server configs. All are also exported as environment variables to hook processes
> and MCP or LSP server subprocesses.
>
> **`${CLAUDE_PLUGIN_ROOT}`**: the absolute path to your plugin's installation directory. Use
> this to reference scripts, binaries, and config files bundled with the plugin. In hook
> commands, use exec form with args so the path is passed as one argument with no quoting. In
> shell-form hooks and monitor commands, wrap it in double quotes, as in `"${CLAUDE_PLUGIN_ROOT}"`.
> This path changes when the plugin updates. The previous version's directory remains on disk
> for about seven days after an update before cleanup, but treat it as ephemeral and do not
> write state here.
>
> When a plugin updates mid-session, hook commands, monitors, MCP servers, and LSP servers keep
> using the paths from the version loaded at session start. New sessions pick up the updated
> paths. This means a plugin can change on disk while a session is still running against the
> old version.
>
> **`${CLAUDE_PROJECT_DIR}`**: the absolute path to the project root (the current working
> directory where Claude Code was launched). Use this to reference files in the user's project.
>
> **`${CLAUDE_PLUGIN_DATA}`**: the absolute path to a persistent per-plugin data directory. See
> Persistent data directory below.

## Verbatim: "Persistent data directory"

> The `${CLAUDE_PLUGIN_DATA}` directory resolves to `~/.claude/plugins/data/{id}/`, where `{id}`
> is the plugin identifier with characters outside `a-z, A-Z, 0-9, _, and -` replaced by `-`.
> For a plugin installed as `formatter@my-marketplace`, the directory is
> `~/.claude/plugins/data/formatter-my-marketplace/`.
>
> A common use is installing language dependencies once and reusing them across sessions and
> plugin updates. Because the data directory outlives any single plugin version, a check for
> directory existence alone cannot detect when an update changes the plugin's dependency
> manifest. The recommended pattern compares the bundled manifest against a copy in the data
> directory and reinstalls when they differ. (The doc gives a `SessionStart` hook example that
> `diff`s `${CLAUDE_PLUGIN_ROOT}/package.json` against `${CLAUDE_PLUGIN_DATA}/package.json` and
> reinstalls `node_modules` when they differ.)
