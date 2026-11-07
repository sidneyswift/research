# Capture: context7-search-contract

Canonical URL: https://context7.com/docs/api-reference/search/search-documentation-in-one-request
Resolved URL: https://context7.com/docs/api-reference/search/search-documentation-in-one-request
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

> ## Documentation index
> Fetch the complete documentation index at: https://context7.com/docs/llms.txt
> Ask it with GET https://context7.com/docs/ask?q=<keywords or question>. Short keywords rank best.
> Use these to discover all available pages before exploring further.
> Feature requests: https://context7.com/docs/resources/feature-requests.md lists what users asked for and how to vote for a request or add one.
> Page rating: `GET https://context7.com/docs/feedback?path=/docs/api-reference/search/search-documentation-in-one-request&helpful={true|false}&comment={comment}` records whether this page helped. The `comment` (URL-encoded, at most 500 characters) says what helped, or what was missing or wrong; a `helpful=false` rating needs it. It is anonymous and needs no key. Comments hold no code, secrets or personal data.

# Search documentation in one request

> Select up to four relevant Context7 libraries, retrieve their documentation in parallel, deduplicate and globally rerank the evidence, and return one bounded response. Optional library, version, and language values improve routing and ranking.

`GET /v3/search`

## OpenAPI

````yaml https://context7.com/openapi.json get /v3/search
openapi: 3.0.0
info:
  title: Context7 Public API
  description: The Context7 Public API provides programmatic access to library
    documentation and search functionality. Get up-to-date documentation and
    code examples for any library.
  version: 2.0.0
  contact:
    name: Context7 Support
    url: https://context7.com
    email: support@context7.com
servers:
  - url: https://context7.com/api
    description: Production server
tags:
  - name: Search
    description: Search for libraries in the Context7 database
  - name: Context
    description: Retrieve documentation context for queries
  - name: Ask
    description: Answer questions from a website registered with Context7 Ask
  - name: Refresh
    description: Refresh existing libraries to fetch latest documentation
  - name: Policies
    description: Manage teamspace access policies and filters
  - name: Add Library
    description: Submit new libraries for documentation processing
  - name: Metrics
    description: Retrieve usage metrics for libraries
  - name: Usage
    description: See member and teamspace API usage
  - name: Teamspaces
    description: Teamspaces the caller is a member of. The management API
      (`/v2/teamspaces/*`) accepts a Context7 API key, which reaches only its
      own teamspace and can make changes or read personal data only when it was
      created with write access (other keys can only read and get 403
      `write_access_required` on writes and on personal data), or an OAuth token
      issued for the Context7 Admin MCP server
      (`https://admin.mcp.context7.com/mcp`), which reaches every teamspace of
      the user. A browser session is not accepted.
  - name: Teamspace Admin
    description: Members, invitations, rules, library policies and requests, usage
      and the spending limit of a teamspace. Every API key can read rules,
      policies, usage and the spending limit. Changes, and reading members,
      invitations, the invite link and library requests (they name people), need
      an API key created with **Write access** ticked (other keys get 403
      `write_access_required`), or the Context7 Admin MCP sign-in.
  - name: Teamspace Libraries
    description: "A teamspace's libraries: its private sources and the libraries it
      has claimed. Add, refresh, configure, version, claim and remove them, and
      read their parse state and usage. A library id `/owner/repo` is two path
      segments. Every API key can read. Changes need an API key created with
      **Write access** ticked (other keys get 403 `write_access_required`), or
      the Context7 Admin MCP sign-in."
  - name: Docs7 Sites
    description: 'Docs7 documentation sites of a teamspace: settings, custom
      domains, deployments, previews and the Docs7 agents. Any member can read;
      owners and admins can change; developers can add a site, publish one added
      for the agents only, and rebuild. Sites deployed with the `docs7 deploy`
      CLI have `source: "local"`; operations marked GitHub-only answer 404 for
      them. Every API key can read, except feature requests and the GitHub
      account behind a build (personal data). Changes, and those reads, need an
      API key created with **Write access** ticked (other keys get 403
      `write_access_required`), or the Context7 Admin MCP sign-in.'
  - name: Docs7 Analytics
    description: "Traffic of one Docs7 site: visitors, AI crawlers, searches,
      assistant questions and page feedback. Docs7 Free reads the last 7 days,
      Docs7 Pro the last 90. Every API key can read the visitor, crawler and
      path reports. Searches, questions, conversations, feedback and the raw
      records (`explore`) are personal data and need an API key created with
      **Write access** ticked, or the Context7 Admin MCP sign-in."
  - name: Ask Sites
    description: "Manage a teamspace's Context7 Ask sites: add, verify, remove, and
      read their analytics and question log. Every API key can read the sites.
      Changes, and reading the analytics and question log (visitor questions),
      need an API key created with **Write access** ticked (other keys get 403
      `write_access_required`), or the Context7 Admin MCP sign-in."
paths:
  /v3/search:
    get:
      summary: Search documentation in one request
      description: Select up to four relevant Context7 libraries, retrieve their
        documentation in parallel, deduplicate and globally rerank the evidence,
        and return one bounded response. Optional library, version, and language
        values improve routing and ranking.
      operationId: searchDocumentation
      tags:
        - Search
      parameters:
        - $ref: "#/components/parameters/SearchQueryParam"
        - $ref: "#/components/parameters/TypeParam"
        - name: library
          in: query
          description: Optional library hints. Repeat for up to four values; each may be a
            fuzzy product name such as `next.js` or an exact Context7 ID such as
            `/vercel/next.js`. An exact ID that is not indexed, or has no
            documentation to serve, is searched by its product name instead. A
            version-like tag (/vercel/next.js@15) is resolved like the version
            parameter for that library, including when the ID is searched by its
            product name.
          required: false
          style: form
          explode: true
          schema:
            type: array
            maxItems: 4
            items:
              type: string
              minLength: 1
              maxLength: 120
          example:
            - next.js
            - react
        - name: version
          in: query
          description: "Optional version preference. `latest` (any case) is the same as no
            version. Without a library value, the version applies when the
            question names one product; when it names several, the version is
            ignored. With one library, verified matching documentation is
            preferred; if unavailable, the newest stable release of the
            requested line when it is newer than the request (v2.3.1 for 2.0.0;
            below 1.0, the same minor) or else current documentation is
            returned, and the response says so (X-Context7-Search-Status:
            partial with reason versionUnverified, X-Context7-Search-Version,
            and the version field of JSON responses). A prerelease tag serves
            only a request for that prerelease. With multiple libraries, the
            version is a preference and each returned library reports what it
            served. A version-like tag on a library value (/vercel/next.js@15)
            is the same request scoped to that library. A version that is not
            indexed for a public GitHub library is queued for indexing in the
            background, so a later request for it can be answered."
          required: false
          schema:
            type: string
            pattern: ^([Ll][Aa][Tt][Ee][Ss][Tt]|[Vv]?[0-9]+([._][0-9]+){0,2}([-+][a-zA-Z0-9.-]+)?)$
          example: "15.2"
        - name: language
          in: query
          description: Optional programming-language preference used for library
            selection, retrieval, and reranking. This is a soft preference and
            does not exclude language-neutral documentation.
          required: false
          schema:
            type: string
            minLength: 1
            maxLength: 40
          example: TypeScript
        - name: context
          in: query
          description: Optional. `broad` appends more sections of the best-matching
            documentation pages, up to about 3,500 extra tokens, after the
            ranked results. How-to, migration, troubleshooting, and overview
            questions get these sections without it; use it when a question
            needs several facts but reads as a single-fact question.
          required: false
          schema:
            type: string
            enum:
              - broad
          example: broad
      responses:
        "200":
          description: Bounded documentation evidence from the selected libraries
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                $ref: "#/components/schemas/SearchContextResponse"
          headers:
            X-Context7-Search-Status:
              description: Present with value partial when successful results are returned
                after an operational search failure or reranker fallback, or
                when no returned library serves the requested version. This is
                not a relevance score.
              schema:
                type: string
                enum:
                  - partial
            X-Context7-Search-Reason:
              description: "Reason for partial results. Present with X-Context7-Search-Status.
                partialSearchFailure: an operational failure or reranker
                fallback. versionUnverified: no returned library has
                documentation indexed for the requested version, so the newest
                stable release of that line or current documentation is served.
                When at least one returned library serves the requested version,
                the search is complete; X-Context7-Search-Version and the
                version field still report each library that fell back."
              schema:
                type: string
                enum:
                  - partialSearchFailure
                  - versionUnverified
            X-Context7-Search-Version:
              description: "Present when a version was requested. The worst outcome across
                returned libraries: verified or unverified. The JSON version
                field carries the per-library detail."
              schema:
                type: string
                enum:
                  - verified
                  - unverified
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "402":
          $ref: "#/components/responses/SpendingLimitError"
        "404":
          description: No documentation matched the question or library hints
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: no_documentation_found
                message: No documentation library matched the request. Check the library hint or
                  name.
        "429":
          $ref: "#/components/responses/RateLimitError"
        "503":
          description: Documentation search could not be completed
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: search_failed
                message: The documentation search could not be completed.
      security:
        - {}
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: "Get your API key at
        [context7.com/dashboard](https://context7.com/dashboard). Treat your API
        key like a password and store it securely. Every key can read the
        management API (`/v2/teamspaces/*`), except personal data: member and
        invitation emails, library requesters, visitor questions, Docs7 reader
        searches, conversations, feedback and feature requests, and the GitHub
        account behind a build. To read those or make changes there, the key
        must be created with **Write access** ticked; other keys get 403
        `write_access_required`."
  parameters:
    SearchQueryParam:
      name: query
      in: query
      description: The question or task to search documentation for. Long questions
        and pasted error output are accepted.
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 2000
      example: How do I write optimistic updates with TanStack Query v5?
    TypeParam:
      name: type
      in: query
      description: Response format type
      required: false
      schema:
        type: string
        enum:
          - json
          - txt
        default: txt
      example: json
  schemas:
    CodeSnippet:
      type: object
      description: A code snippet from library documentation
      properties:
        codeTitle:
          type: string
          description: Title of the code snippet
        codeDescription:
          type: string
          description: Description of what the code does
        codeLanguage:
          type: string
          description: Primary programming language
        codeTokens:
          type: integer
          description: Token count for the snippet
        codeId:
          type: string
          description: URL to source location
        pageTitle:
          type: string
          description: Title of the documentation page
        codeList:
          type: array
          description: Code examples in different languages
          items:
            $ref: "#/components/schemas/CodeExample"
        isDynamic:
          type: boolean
          description: Whether this snippet was recovered from the dynamic source-code
            index instead of the primary docs index
        sourceFile:
          type: string
          description: Repo-relative source file path for dynamic snippets
      required:
        - codeTitle
        - codeDescription
        - codeLanguage
        - codeTokens
        - codeId
        - pageTitle
        - codeList
    CodeExample:
      type: object
      description: A single code example
      properties:
        language:
          type: string
          description: Programming language
        code:
          type: string
          description: The actual code content
      required:
        - language
        - code
    InfoSnippet:
      type: object
      description: A documentation snippet
      properties:
        pageId:
          type: string
          description: URL to source page
        breadcrumb:
          type: string
          description: Navigation breadcrumb path
        content:
          type: string
          description: The documentation content
        contentTokens:
          type: integer
          description: Token count for the content
      required:
        - content
        - contentTokens
    ContextCodeSnippet:
      allOf:
        - $ref: "#/components/schemas/CodeSnippet"
        - type: object
          properties:
            rank:
              type: integer
              minimum: 1
              description: 1-based position in the text response, shared by codeSnippets and
                infoSnippets. Sort both lists together by rank to read the
                snippets in the order the text response gives them (the
                selection model's relevance order when it ranked them).
              example: 1
          required:
            - rank
    ContextInfoSnippet:
      allOf:
        - $ref: "#/components/schemas/InfoSnippet"
        - type: object
          properties:
            rank:
              type: integer
              minimum: 1
              description: 1-based position in the text response, shared by codeSnippets and
                infoSnippets. Sort both lists together by rank to read the
                snippets in the order the text response gives them (the
                selection model's relevance order when it ranked them).
              example: 1
          required:
            - rank
    SearchCodeSnippet:
      allOf:
        - $ref: "#/components/schemas/CodeSnippet"
        - type: object
          properties:
            libraryId:
              type: string
              description: Context7 library ID that produced this snippet
            rank:
              type: integer
              minimum: 1
              description: 1-based position in the reranked order shared by codeSnippets and
                infoSnippets. Sort both lists together by rank to read the
                evidence in the order the text response gives it.
              example: 1
          required:
            - libraryId
            - rank
    SearchInfoSnippet:
      allOf:
        - $ref: "#/components/schemas/InfoSnippet"
        - type: object
          properties:
            libraryId:
              type: string
              description: Context7 library ID that produced this snippet
            rank:
              type: integer
              minimum: 1
              description: 1-based position in the reranked order shared by codeSnippets and
                infoSnippets. Sort both lists together by rank to read the
                evidence in the order the text response gives it.
              example: 1
          required:
            - libraryId
            - rank
    SearchContextResponse:
      allOf:
        - $ref: "#/components/schemas/ContextResponse"
        - type: object
          properties:
            codeSnippets:
              type: array
              description: Relevant code snippets with their selected library
              items:
                $ref: "#/components/schemas/SearchCodeSnippet"
            infoSnippets:
              type: array
              description: Relevant documentation snippets with their selected library
              items:
                $ref: "#/components/schemas/SearchInfoSnippet"
            rules:
              type: object
              description: Optional global rules and library-scoped guidelines
              properties:
                global:
                  type: array
                  description: Global team rules that apply to every returned library
                  items:
                    type: string
                libraries:
                  type: array
                  description: Rules scoped to a specific returned library
                  items:
                    type: object
                    properties:
                      libraryId:
                        type: string
                      libraryOwn:
                        type: array
                        items:
                          type: string
                      libraryTeam:
                        type: array
                        items:
                          type: string
                    required:
                      - libraryId
                      - libraryOwn
                      - libraryTeam
            version:
              type: object
              description: Present when a version was requested by the version parameter or a
                version-like library tag. Says what each returned library
                served.
              required:
                - status
                - libraries
              properties:
                requested:
                  type: string
                  description: The version parameter, when given.
                  example: "15"
                status:
                  type: string
                  enum:
                    - verified
                    - unverified
                  description: Worst outcome across the returned libraries.
                libraries:
                  type: array
                  items:
                    type: object
                    required:
                      - libraryId
                      - requested
                      - served
                      - status
                    properties:
                      libraryId:
                        type: string
                        description: The library id as it appears on the returned snippets, including
                          the served tag when one was matched.
                        example: /vercel/next.js/v15.1.11
                      requested:
                        type: string
                        description: The version requested for this library.
                        example: "15"
                      served:
                        type: string
                        nullable: true
                        description: "The indexed tag served: the matching tag or, when unverified, the
                          newest stable release of the requested line that is
                          newer than the request. The requested version when the
                          source id pins it. Null when current documentation was
                          served instead."
                        example: v15.1.11
                      status:
                        type: string
                        enum:
                          - verified
                          - unverified
    ContextResponse:
      type: object
      description: Documentation context response
      properties:
        codeSnippets:
          type: array
          description: Relevant code snippets
          items:
            $ref: "#/components/schemas/ContextCodeSnippet"
        infoSnippets:
          type: array
          description: Relevant documentation snippets
          items:
            $ref: "#/components/schemas/ContextInfoSnippet"
        rules:
          type: object
          description: Optional library-specific rules and guidelines
          properties:
            global:
              type: array
              description: Global team rules
              items:
                type: string
            libraryOwn:
              type: array
              description: Rules defined by the library owner
              items:
                type: string
            libraryTeam:
              type: array
              description: Library-specific rules from the team
              items:
                type: string
        version:
          type: object
          description: Present only when the library ID names a version that is not
            indexed. Says what was served instead, with the fields of each entry
            of the Search API's `version.libraries`. The text response states
            the same in a leading version note when the status is unverified.
          required:
            - libraryId
            - requested
            - served
            - status
          properties:
            libraryId:
              type: string
              description: The library id served, including the served tag when one was
                matched.
              example: /vercel/next.js/v15.1.11
            requested:
              type: string
              description: The version named by the library ID.
              example: v15.0.0
            served:
              type: string
              nullable: true
              description: "The indexed tag served: the matching tag or, when unverified, the
                newest stable release of the requested line that is newer than
                the request. Null when current documentation was served
                instead."
              example: v15.1.11
            status:
              type: string
              enum:
                - verified
                - unverified
              description: verified when the served tag matches the requested version (`15`
                served by v15.1.11); unverified when another release or current
                documentation was served.
          example:
            libraryId: /vercel/next.js/v15.1.11
            requested: v15.0.0
            served: v15.1.11
            status: unverified
      required:
        - codeSnippets
        - infoSnippets
    Error:
      type: object
      description: Standard error response
      properties:
        error:
          type: string
          description: Error code identifier
        message:
          type: string
          description: Human-readable error message
      required:
        - error
        - message
  responses:
    BadRequestError:
      description: Bad Request - Invalid input parameters
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          examples:
            validationError:
              summary: Validation error
              value:
                error: validation_error
                message: Library name is required
            invalidLibraryId:
              summary: Invalid library ID format
              value:
                error: invalid_library_id
                message: "Invalid library ID format. Expected: `/owner/repo` for GitHub
                  repositories, or `/<source>/<id>` for other sources (the URL
                  path of the library on context7.com)"
    UnauthorizedError:
      description: Unauthorized - Invalid or missing API key
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: invalid_api_key
            message: Invalid API key. Please check your API key. API keys should start with
              'ctx7sk' prefix.
    SpendingLimitError:
      description: Payment Required - the teamspace's configured monthly spending
        limit has been reached. A teamspace owner or admin can raise the limit
        in billing settings, or the cap will reset at the start of the next
        billing month.
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: spending_limit_exceeded
            message: Monthly spending limit of $5.00 reached for this teamspace. An owner or
              admin can raise the limit at
              https://context7.com/dashboard/billing, or the cap will reset at
              the start of next month.
    RateLimitError:
      description: Too Many Requests - Rate limit exceeded
      headers:
        Retry-After:
          description: Seconds until rate limit resets
          schema:
            type: integer
        RateLimit-Limit:
          description: Request limit
          schema:
            type: integer
        RateLimit-Remaining:
          description: Remaining requests
          schema:
            type: integer
        RateLimit-Reset:
          description: Unix timestamp when limit resets
          schema:
            type: integer
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: rate_limit_exceeded
            message: Rate limit exceeded. Please try again later.
````
