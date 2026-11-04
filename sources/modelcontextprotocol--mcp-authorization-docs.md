---
domain: sources
type: docs-page
url: https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization
retrieved: 2026-11-04
snapshot-location: sources/modelcontextprotocol--mcp-authorization-docs/
version: MCP 2026-07-28; ext-auth 15ca394e00a66434520b9ade26294999295a43ae; ID-JAG drafts 04 and 06
last-reviewed: 2026-11-04
---

# MCP authorization and enterprise identity — official documentation captures

> Primary evidence for base HTTP authorization, the two stable authorization extensions, their inherited OAuth contracts, and the limits of centralized policy.

## Snapshot details

- **Retrieved:** 2026-11-04. Publication date for the documentation overviews: **n/a (living page)**.
- **Storage:** named, unmodified Markdown/MDX/text responses in `sources/modelcontextprotocol--mcp-authorization-docs/`. `captures.json` maps each filename to its exact URL, revision, byte length, and SHA-256. Captures are immutable; a later refresh gets a new capture.
- **Base protocol revision:** 2026-07-28. Authorization has separate discovery and registration documents; all three were captured.
- **Extension specification pin:** ext-auth `15ca394e00a66434520b9ade26294999295a43ae`, committer date 2026-10-23T16:24:05Z. The two captured specifications are in `specification/stable/*/2026-07-28/`; neither is a draft directory. These are document captures, not a local repo checkout.
- **IETF version distinction:** stable MCP enterprise profile links normative processing sections of ID-JAG **draft-04**, so that exact draft was captured. The current IETF link resolved to **draft-06**, also captured for comparison; do not silently replace the stable profile's dependency with it. RFC 8693 and RFC 7523 are captured separately.
- **Verification boundary:** documentation read; no IdP configuration, account connection, token exchange, SDK execution, or offboarding test.

## Anchor map

### root

The capture collection and `captures.json` receipt.

### base-contract

`core-authorization-2026-07-28.md`, lines 9–80: HTTP scope, optional authorization, stdio credentials, OAuth roles and discovery/registration requirements. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization).

### base-discovery

`auth-discovery-2026-07-28.md`, lines 11–94: protected resource metadata, challenge/well-known discovery, independent authorization servers, metadata issuer matching. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery).

### base-registration

`client-registration-2026-07-28.md`, sections Client ID Metadata Documents, Pre-registration, Dynamic Client Registration, Authorization Server Binding: registration priority, exact metadata identities and issuer-bound credentials. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration).

### base-scopes

`core-authorization-2026-07-28.md`, lines 97–134 and 325–405: challenged scopes, least privilege, runtime insufficient-scope response and step-up authorization. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#scope-selection-strategy).

### base-token-boundaries

`core-authorization-2026-07-28.md`, lines 190–313: response issuer validation, resource indicators, Bearer header on every request, token audience checks, prohibition on token passthrough, refresh-token boundaries. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#resource-parameter-implementation).

### enterprise-overview

`enterprise-overview.md`, sections What it is, How it works, Implementation guide: extension identifier, advertised benefits, per-request client capabilities, account-linking guidance, and the overview's unqualified immediate-revocation claim. [Upstream](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization).

### enterprise-flow

`enterprise-spec-2026-07-28.mdx`, sections 1–4.3: roles, OIDC/SAML identity assertion, RFC 8693 token exchange, ID-JAG audience/resource/client/scope claims, IdP policy. [Pinned specification](https://github.com/modelcontextprotocol/ext-auth/blob/15ca394e00a66434520b9ade26294999295a43ae/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx).

### enterprise-token-and-discovery

`enterprise-spec-2026-07-28.mdx`, sections 5–6, lines 210–254: RFC 7523 JWT bearer grant, client authentication, MCP resource audience restriction, sample 86400-second access token, grant-profile discovery. [Pinned specification](https://github.com/modelcontextprotocol/ext-auth/blob/15ca394e00a66434520b9ade26294999295a43ae/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx#5-access-token-request).

### enterprise-policy-limit

`enterprise-spec-2026-07-28.mdx`, section 7.2, lines 264–270: enterprise visibility covers token issuance and scope policies, **not actual MCP traffic**. [Pinned specification](https://github.com/modelcontextprotocol/ext-auth/blob/15ca394e00a66434520b9ade26294999295a43ae/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx#72-scope-of-enterprise-visibility-and-policy-enforcement).

### client-credentials

`client-credentials-spec-2026-07-28.mdx`, sections Introduction, Client Credentials Flow and Security Considerations: HTTP M2M flow, out-of-band preregistration, recommended JWT client authentication, client-secret alternative, metadata fields and requests. Note metadata lists `client_secret_basic` while prose/examples put the secret in the body. [Pinned specification](https://github.com/modelcontextprotocol/ext-auth/blob/15ca394e00a66434520b9ade26294999295a43ae/specification/stable/oauth-client-credentials/2026-07-28/oauth-client-credentials.mdx).

### credential-providers

`client-credentials-overview.md`, Implementation guide and SDK examples: documents TypeScript `ClientCredentialsProvider` / `PrivateKeyJwtProvider` with `expectedIssuer` and Python `ClientCredentialsOAuthProvider` with `issuer`. These are documentation examples; no installed SDK release or runtime was verified. [Upstream](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials).

### extension-status

`ext-auth-readme.md`: both authorization extensions listed stable; optional/additive/composable, stable revisions keyed to core protocol revisions; governance through extension maintainers and Authorization Interest Group. [Pinned README](https://github.com/modelcontextprotocol/ext-auth/blob/15ca394e00a66434520b9ade26294999295a43ae/README.md).

### support-caveats

`client-support-matrix.md`: community maintained, opt-in, predominantly empty cells, auth-extension support distinguished from core DCR/CIMD. `enterprise-overview.md`, Implementation support: vendor labels and draft-revision caveat, not independently verified product support. [Matrix](https://modelcontextprotocol.io/extensions/client-matrix), [vendor listing](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#implementation-support).

### id-jag-processing

`id-jag-draft-04.txt`, sections 3.1, 4.3.3, 4.4.1, 5, 6, 9: token type, signature/claims, authorization-server audience, authenticated-client continuity, policy reduction of resources/scopes, subject and tenant context, confidential-client recommendation and step-up. [Exact dependency](https://www.ietf.org/archive/id/draft-ietf-oauth-identity-assertion-authz-grant-04.html).

### id-jag-renewal

`id-jag-draft-04.txt`, section 4.4.3, lines 1652–1688: resource AS SHOULD NOT issue refresh token; obtain new ID-JAG or identity assertion through IdP when expired. Does not establish invalidation of issued resource tokens on an IdP policy change. [Exact dependency](https://www.ietf.org/archive/id/draft-ietf-oauth-identity-assertion-authz-grant-04.html#section-4.4.3).

### id-jag-version-drift

`id-jag-draft-06.txt` vs `id-jag-draft-04.txt`: separate revisions captured; draft-06 description preserves independent resource-AS token decisions and revises identity/tenant claims and processing. This collection does not assert wire compatibility across revisions. [Current captured revision](https://www.ietf.org/archive/id/draft-ietf-oauth-identity-assertion-authz-grant-06.html).

### oauth-jwt-purpose

`rfc7523-jwt-profile.txt`, sections 2.1–2.2 and 3: JWT as authorization grant (`assertion`) differs from JWT as client authentication (`client_assertion`); issuer, subject, audience, expiry, signing and replay considerations. Section 6 notes replay protection is not mandated by RFC 7523 alone. [RFC 7523](https://www.rfc-editor.org/rfc/rfc7523.html).

### oauth-token-exchange

`rfc8693-token-exchange.txt`, sections 1–2: cross-domain token exchange, subject/actor and resource/audience semantics; the returned `access_token` field may carry a non-access token and `token_type=N_A`. [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html).

### security

`security-best-practices-2026-07-28.md`, named sections Confused Deputy Problem, Token Passthrough, Server-Side Request Forgery, State Handle Hijacking, Local MCP Server Compromise, OAuth Authorization URL Validation, Mix-Up Attacks, CIMD Trust Policies, Scope Minimization. Evidence for threat classes and recommended mitigations, not proof of a deployed defense. [Upstream](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## Why we cite this

To distinguish user delegation, corporate identity federation and application identity; separate compatibility from authority; and qualify attractive central-policy claims with the actual token and enforcement boundaries.

## Popularity signals (if this source provides them)

- **Signal type:** official specification / governance placement, not a popularity measure.
- **Value:** both auth extensions listed **Stable** in the pinned official ext-auth README.
- **As-of:** 2026-11-04.
- No install count, host adoption count, IdP coverage estimate, or production assurance is inferred.

## Related sources

- [[sources/modelcontextprotocol--mcp-core-and-extensions-docs]] — core/extension architecture and revision context.
- [[concepts/mcp-enterprise-managed-authorization]] — durable authorization analysis derived from this collection.

- [[sources/openai--agent-api-design]] — earlier API research separates tool schemas, approval controls and provider permissions.
- [[sources/shopify--agent-commerce-api-design]] — negotiated capabilities and authorization are distinct contracts.
