# Capture: How does it work? | DocSearch by Algolia

Canonical URL: https://docsearch.algolia.com/docs/how-does-it-work/
Resolved URL: https://docsearch.algolia.com/docs/how-does-it-work/
Retrieved: 2026-11-05
Representation: HTML main/article converted to Markdown via markdownify; visual widgets and assets not captured
Content-Type: text/html; charset=UTF-8

---

Version: Stable (v5.x)

On this page

# How does it work?

DocSearch setup has three parts: join the DocSearch program, index your content, and add a frontend package or framework integration.

![How it works](/img/assets/docsearch-how-it-works.png)

## You apply[​](https://docsearch.algolia.com/docs/how-does-it-work/#you-apply "Direct link to You apply")

First, confirm that [your website qualifies](https://docsearch.algolia.com/docs/who-can-apply), then [apply for DocSearch](https://dashboard.algolia.com/users/sign_up?selected_plan=docsearch&utm_source=docsearch.algolia.com&utm_medium=referral&utm_campaign=docsearch&utm_content=apply). The onboarding flow validates your domain against the program requirements.

If automated validation can't determine eligibility, the application might require a manual review.

## Index your content[​](https://docsearch.algolia.com/docs/how-does-it-work/#index-your-content "Direct link to Index your content")

After approval, create a dedicated [crawler](https://www.algolia.com/products/search-and-discovery/crawler/) in your Algolia application. Its [configuration file](https://www.algolia.com/doc/tools/crawler/apis/configuration/) defines which URLs to crawl, which URLs to ignore, and which selectors extract your content hierarchy.

Run a test crawl, review the extracted records, and configure recurring crawls. Use the Crawler interface to adjust the configuration as your website changes.

**With the Crawler, comes [a dedicated interface](https://dashboard.algolia.com/crawler) for you to:**

* Start, schedule and monitor your crawls
* Edit and test your crawler configuration

**With the Algolia application comes access to the dashboard for you to:**

* Browse your index and see how your content is indexed
* Review analytics to understand how search performs
* Trials for other Algolia features
* Team management

## Add DocSearch to your website[​](https://docsearch.algolia.com/docs/how-does-it-work/#add-docsearch-to-your-website "Direct link to Add DocSearch to your website")

Choose a [DocSearch v5 package](https://docsearch.algolia.com/docs/packages/overview) or [supported framework integration](https://docsearch.algolia.com/docs/integrations). Configure it with your application ID, Search API key, and index name. The frontend queries the Algolia index and displays the results.

Crawler versions, record schema versions, and frontend package versions are separate. In particular, crawler `recordVersion: 'v3'` describes the indexed record schema, not the DocSearch UI version. You can upgrade the v5 frontend packages without recreating the crawler. Keep the "Search by Algolia" logo next to your search results.