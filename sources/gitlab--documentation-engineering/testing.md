# Documentation testing | GitLab Docs

Source: https://docs.gitlab.com/development/documentation/testing/
Final URL: https://docs.gitlab.com/development/documentation/testing/
Retrieved: 2026-11-05
Capture: main-content text extracted from HTML; no UI interaction or code execution.

/
#
Documentation testing
GitLab documentation is stored in projects with code, and treated like code.
To maintain standards and quality of documentation, we use processes similar to
those used for code.
Merge requests containing changes to Markdown (
.md
) files run these CI/CD jobs:
docs-lint markdown
: Runs
lint-docs.sh
script.
docs-lint links
: Checks the validity of
relative links
in the documentation suite.
docs-lint mermaid
: Runs
mermaidlint
to check for invalid Mermaid charts.
rubocop-docs
: Checks links to documentation
from
.rb
files
.
eslint-docs
: Checks links to documentation
from
.js
and
.vue
files
.
docs-lint redirects
: Checks for deleted or renamed documentation files without
redirects
.
docs code_quality
: Runs Code Quality to
add Vale warnings and errors into the MR changes tab (diff view)
.
docs hugo_build
: Runs a partial build of the Hugo website using
test-specific configuration
to validate
shortcodes
and filenames.
A few files are generated from scripts. A CI/CD job fails when either the source code files
or the documentation files are updated without following the correct process:
graphql-verify
: Fails when the docs files in
doc/api/graphql/reference
are not updated
with the
update process
.
docs-lint deprecations-and-removals
: Fails when
doc/update/deprecations.md
is
not updated with the
update process
.
For a full list of automated files, see
Automated pages
.
##
Tests in
lint-doc.sh
The
/scripts/lint-doc.sh
script runs these linters:
Vale
: Checks documentation content.
markdownlint
and
rumdl
: Check Markdown structure.
The script also tests for page content problems that these linters cannot test for.
The
docs-lint markdown
job fails if a linter reports errors or if any of these
lint-doc.sh
tests fail:
Curl (
curl
) commands
must use long-form options (
--header
)
instead of short options, like
-h
.
Documentation pages
must contain front matter
indicating ownership of the page.
CHANGELOG.md
must not contain duplicate versions.
Files in the
doc/
directory must not be executable.
Filenames and directories must
:
Use
_index.md
instead of
README.md
Be lowercase.
Image filenames must
specify the version they were added in
.
###
Mermaid chart linting
Mermaid
builds charts and diagrams from code.
The script (
scripts/lint/check_mermaid.mjs
) runs in the
docs-lint mermaid
job for
all merge requests that contain changes to Markdown files. The script returns an
error if any Markdown files return a Mermaid syntax error.
To help debug your Mermaid charts, use the
Mermaid Live Editor
.
##
Tests in
docs-lint links
and other jobs
To check for broken links, merge requests containing changes to Markdown (
.md
) files run these jobs in their
pipelines:
docs-lint links
job in the
gitlab
project. For example:
https://gitlab.com/gitlab-org/gitlab/-/jobs/7065686331
.
docs-lint links
job in the
omnibus-gitlab
project. For example:
https://gitlab.com/gitlab-org/omnibus-gitlab/-/jobs/7065337075
.
docs-lint links
job in the
gitlab-operator
project.
docs:lint markdown
job in the
gitlab-runner
project, which includes link checking. For example:
https://gitlab.com/gitlab-org/gitlab-runner/-/jobs/7056674997
.
check_docs_links
job in the
charts/gitlab
project. For example:
https://gitlab.com/gitlab-org/charts/gitlab/-/jobs/7066011619
.
These jobs check links, including anchor links, and report any problems. Any link that requires a network connection is skipped.
##
Vale Code Quality report
The
docs code_quality
job runs Vale with the
doc/.vale/vale-json.tmpl
template and uploads the output as a
Code Quality
report.
Vale warnings and errors then display in the
merge request changes view
.
Code Quality compares the report from the merge request with the latest report from the target branch.
If GitLab cannot compare the reports, it might show all Vale issues as resolved. To prevent this,
the job runs and generates a report in most pipelines, even when a merge request has no documentation changes.
Vale findings do not fail this job, so it does not block merge requests.
Vale errors still fail the
docs-lint markdown
job.
##
Tests for translated documentation
To ensure quality across all our translated content, we’ve implemented testing for our documentation in
multiple languages. These tests mirror those used for the English version, but run on internationalized
content in the
/doc-locale/
or
/docs-locale/
directories.
###
General translation linting
The
docs-i18n-lint markdown
job runs general linting tests on all translated documentation:
markdownlint
: Checks Markdown structure and formatting.
Vale
: Runs general documentation style rules using the
gitlab_docs
filter.
This job runs when any files in
/doc-locale/
or
/docs-locale/
are modified and provides baseline quality checks
for all translated content.
Project
English Dir
Translation Dir
Linting Jobs
GitLab
/doc
/doc-locale
docs-i18n-lint markdown
docs-i18n-lint japanese-vale
docs-i18n-lint korean-vale
docs-i18n-lint french-vale
GitLab Runner
/docs
/docs-locale
docs:lint i18n markdown
Linux package
/doc
/doc-locale
docs-lint-i18n markdown
docs-lint-i18n content
Charts
/doc
/doc-locale
check_docs_i18n_content
check_docs_i18n_markdown
Operator
/doc
/doc-locale
docs-i18n-lint content
docs-i18n-lint markdown
###
Language-specific translation linting
For languages with specific style requirements, we provide dedicated CI/CD jobs that run
language-specific Vale rules. Each language has its own job that only runs when files
in that language are modified.
####
Japanese language support
The
docs-i18n-lint japanese-vale
job runs Japanese-specific Vale linting:
Script:
scripts/i18n_lint_language_vale.sh
Configuration:
doc-locale/ja-jp/.vale.ini
Vale filter:
locale_rules
Triggers: Only runs when these files change:
doc-locale/ja-jp/**/*.md
- Japanese documentation files
doc-locale/ja-jp/.vale.ini
- Japanese Vale configuration
scripts/i18n_lint_language_vale.sh
- Universal language linting script
The job uses environment variables to configure the universal script:
yaml
variables
:
LANGUAGE_CODE
:
"ja-jp"
LANGUAGE_NAME
:
"Japanese"
####
Korean language support
The
docs-i18n-lint korean-vale
job runs Korean-specific Vale linting:
Script:
scripts/i18n_lint_language_vale.sh
Configuration:
doc-locale/ko-kr/.vale.ini
Vale filter:
locale_rules
Triggers: Only runs when these files change:
doc-locale/ko-kr/**/*.md
- Korean documentation files
doc-locale/ko-kr/.vale.ini
- Korean Vale configuration
scripts/i18n_lint_language_vale.sh
- Universal language linting script
The job uses environment variables to configure the universal script:
yaml
variables
:
LANGUAGE_CODE
:
"ko-kr"
LANGUAGE_NAME
:
"Korean"
####
French language support
The
docs-i18n-lint french-vale
job runs French-specific Vale linting:
Script:
scripts/i18n_lint_language_vale.sh
Configuration:
doc-locale/fr-fr/.vale.ini
Vale filter:
locale_rules
Triggers: Only runs when these files change:
doc-locale/fr-fr/**/*.md
- French documentation files
doc-locale/fr-fr/.vale.ini
- French Vale configuration
scripts/i18n_lint_language_vale.sh
- Universal language linting script
The job uses environment variables to configure the universal script:
yaml
variables
:
LANGUAGE_CODE
:
"fr-fr"
LANGUAGE_NAME
:
"French"
####
Adding new languages
To add language-specific linting for additional languages:
Create language-specific Vale configuration at
doc-locale/LANGUAGE_CODE/.vale.ini
Add a new CI job in
.gitlab/ci/docs.gitlab-ci.yml
:
yaml
docs-i18n-lint LANGUAGE-vale
:
extends
:
-
.default-retry
-
.docs:rules:docs-i18n-lint-LANGUAGE
-
.docs-markdown-lint-image
stage
:
lint
needs
:
[]
variables
:
LANGUAGE_CODE
:
"LANGUAGE_CODE"
# e.g., "fr-fr", "de-de"
LANGUAGE_NAME
:
"LANGUAGE_NAME"
# e.g., "French", "German"
script
:
-
source ./scripts/utils.sh
-
install_gitlab_gem
-
scripts/i18n_lint_language_vale.sh
Add triggering rules in
.gitlab/ci/rules.gitlab-ci.yml
:
yaml
.docs:rules:docs-i18n-lint-LANGUAGE
:
rules
:
-
<<
:
*if-tech-docs-localization
changes
:
-
"doc-locale/LANGUAGE_CODE/**/*.md"
-
"doc-locale/LANGUAGE_CODE/.vale.ini"
-
"scripts/i18n_lint_language_vale.sh"
The universal script approach eliminates code duplication while maintaining language-specific
customization through environment variables.
##
Tests in
docs-i18n-lint links
and other jobs
To check for broken links in translated documentation, merge requests containing changes to
translated Markdown (
.md
) files run these jobs in their pipelines:
docs-i18n-lint links
job in the
gitlab
project. For example:
https://gitlab.com/gitlab-org/gitlab/-/jobs/7065686331
.
docs-i18n-lint links
job in the
omnibus-gitlab
project. For example:
https://gitlab.com/gitlab-org/omnibus-gitlab/-/jobs/7065337075
.
docs-i18n-lint links
job in the
gitlab-operator
project.
docs:lint i18n markdown
job in the
gitlab-runner
project, which includes link checking. For example:
https://gitlab.com/gitlab-org/gitlab-runner/-/jobs/7056674997
.
check_docs_i18n_links
job in the
charts/gitlab
project. For example:
https://gitlab.com/gitlab-org/charts/gitlab/-/jobs/7066011619
.
These jobs check for broken links, including anchor links. Any link that requires a network connection is skipped.
If broken links are found, they are listed in the job log, but the jobs do not fail the pipeline.
The jobs must be started manually, except for the
docs:lint i18n markdown
job in the Runner project.
###
Path verification of orphaned translation files
The
docs-i18n-lint paths
job fails if translated files in
/doc-locale
have no corresponding English source files. The job runs when:
Files in
/doc-locale
are modified
The path verification script changes
When orphaned translation files are detected, localization team members handle the necessary deletions. English fallback content provides coverage until new translations are available.
##
Install documentation linters
To help adhere to the
documentation style guidelines
, and
improve the content added to documentation, install documentation linters and
integrate them with your code editor. At a minimum, install
markdownlint
and
Vale
to match the checks run in build pipelines. Both tools can
integrate with your code editor.
##
Running documentation tests locally
This has the advantage of:
Speeding up the feedback loop. You can know of any problems with the changes in your branch
without waiting for a CI/CD pipeline to run.
Lowering costs. Running tests locally is cheaper than running tests on the cloud
infrastructure GitLab uses.
It’s important to:
Keep the tools up-to-date, and
match the versions used
in our CI/CD pipelines.
Run linters, documentation link tests, and UI link tests the same way they are
run in CI/CD pipelines. It’s important to use same configuration we use in
CI/CD pipelines, which can be different than the default configuration of the tool.
###
Run Vale, markdownlint, or link checks locally
Installation and configuration instructions are available for:
markdownlint
.
Vale
.
Lychee
and UI link checkers.
###
Run
lint-doc.sh
locally
Use a Rake task to run the
lint-doc.sh
tests locally.
Prerequisites:
You have either:
The
required lint tools installed
on your computer.
A working Docker or
containerd
installation, to use an image with these tools pre-installed.
Go to your
gitlab
directory.
Run:
shell
rake lint:markdown
To specify a single file or directory you would like to run lint checks for, run:
shell
MD_DOC_PATH
=
path/to/my_doc.md rake lint:markdown
The output should be similar to:
=> Linting documents at path /path/to/gitlab as <user>...
=> Checking for cURL short options...
=> Checking for CHANGELOG.md duplicate entries...
=> Checking /path/to/gitlab/doc for executable permissions...
=> Checking for new README.md files...
=> Linting markdown style...
=> Linting prose...
✔ 0 errors, 0 warnings and 0 suggestions in 1 file.
✔ Linting passed
##
Update linter configuration
Vale and markdownlint configurations are under source control in each
project, so updates must be committed to each project individually.
The configuration in the
gitlab
project should be treated as the source of truth,
and all updates should first be made there.
On a regular basis, the changes made in
gitlab
project to the Vale and markdownlint configuration should be
synchronized to the other projects. In each of the
supported projects
:
Create a new branch. Add
docs-
to the beginning or
-docs
to the end of the branch name. Some projects use this
convention to limit the jobs that run.
Copy the configuration files from the
gitlab
project. For example, in the root directory of the project, run:
shell
# Copy markdownlint configuration file
cp ../gitlab/.markdownlint-cli2.yaml .
# Remove existing Vale configuration in case some rules have been removed from the GitLab project
rm -r docs/.vale/gitlab
# Copy gitlab_base Vale configuration files for a project with documentation stored in 'docs' directory
cp -r ../gitlab/doc/.vale/gitlab_base docs/.vale
If updating
gitlab-runner
,
gitlab-omnibus
,
charts/gitlab
, or
gitlab-operator
, also copy the
gitlab-docs
Vale configuration from the
gitlab
project. For example, in the root directory of the project, run:
shell
# Copy gitlab-docs Vale configuration files for a project with documentation stored in 'docs' directory
cp -r ../gitlab/doc/.vale/gitlab_docs docs/.vale
Review the diff created for
.markdownlint-cli2.yaml
. For example, run:
shell
git diff .markdownlint-cli2.yaml
Remove any changes that aren’t required. For example,
customRules
is only used in the
gitlab
project.
Review the diffs created for the Vale configuration. For example, run:
shell
git diff docs
Remove unneeded changes to
RelativeLinks.yml
. This rule is specific to each project.
Remove any
.tmpl
files. These files are only used in the
gitlab
project.
Run
markdownlint-cli2
to check for any violations of the new rules. For example:
shell
markdownlint-cli2 docs/**/*.md
Run Vale to check for any violations of the new rules. For example:
shell
vale --minAlertLevel error docs
Commit the changes to the new branch. Some projects require
conventional commits
so check the contributing information for the
project before committing.
Submit a merge request for review.
##
Update linting images
Lint tests run in CI/CD pipelines using images from the
docs-gitlab-com
container registry
.
If a new version of a dependency is released (like a new version of Vale), we
should update the images to use the newer version. Then, we can update the configuration
files in each of our documentation projects to point to the new image.
To update the linting images:
In
docs-gitlab-com
, open a merge request to update
.gitlab-ci.yml
to use the new tooling
version. (
Example MR
)
When merged, start a
Build docker images pipeline (Manual)
scheduled pipeline
.
Go to the pipeline you started, and wait for the relevant
test:image
job to complete,
for example
test:image:docs-lint-markdown
. If the job:
Passes, start the relevant
image:
job, for example,
image:docs-lint-markdown
.
Fails, review the test job log and start troubleshooting the issue. The image configuration
likely needs some manual tweaks to work with the updated dependency.
After the
image:
job passes, check the job’s log for the name of the new image.
(
Example job output
)
Verify that the new image was added to the container registry.
Open merge requests to update each of these configuration files to point to the new image.
For jobs that use
markdownlint
,
vale
, or
lychee
:
gitlab
:
.gitlab/ci/docs.gitlab-ci.yml
,
update the
image
in the
.docs-markdown-lint-image:
section.
scripts/lint-doc.sh
,
update the
registry_url
value in the
run_locally_or_in_container()
section.
gitlab-runner
:
.gitlab/ci/_common.gitlab-ci.yml
,
update the value of the
DOCS_LINT_IMAGE
variable.
omnibus-gitlab
:
gitlab-ci-config/variables.yml
,
update the value of the
DOCS_LINT_IMAGE
variable.
charts/gitlab
:
.gitlab-ci.yml
,
update the value of the
DOCS_LINT_IMAGE
variable.
cloud-native/gitlab-operator
:
.gitlab-ci.yml
update the value of the
DOCS_LINT_IMAGE
variable.
gitlab-development-kit
:
.gitlab-ci.yml
update the value of the
DOCS_LINT_IMAGE
variable.
In each merge request:
Include a small doc update to trigger the job that uses the image.
Check the relevant job output to confirm the updated image was used for the test.
Assign the merge requests to any technical writer to review and merge.
##
Configure pre-push hooks
Git
pre-push hooks
allow Git users to:
Run tests or other processes before pushing a branch.
Avoid pushing a branch if failures occur with these tests.
Lefthook
is a Git hooks manager. It makes configuring,
installing, and removing Git hooks simpler. Configuration for it is available in the
lefthook.yml
file for the
gitlab
project.
To set up Lefthook for documentation linting, see
Pre-commit and pre-push static analysis with Lefthook
.
To show Vale errors on commit or push, see
Show Vale warnings on commit or push
.
##
Disable linting on documentation
Some, but not all, linting can be disabled on documentation files:
Vale tests can be disabled
for all or part of a file.
markdownlint
tests can be disabled
for all or part of a file.
##
Tool versions used in CI/CD pipelines
You should use linter versions that are the same as those used in our CI/CD pipelines for maximum compatibility
with the linting rules we use.
To match the versions of
markdownlint-cli2
and
vale
used in the GitLab projects, refer to:
For projects managed with
mise
, the
.tool-versions
or
mise.toml
file in the project. For example:
The
.tool-versions
file in the
gitlab
project
.
The
mise.toml
file in the
gitlab-operator
project
.
The
versions used (see
variables:
section)
when building the
image:docs-lint-markdown
Docker image containing these tools for CI/CD.
Versions set in these two locations should be the same.
Tool
Version
Command
Additional information
markdownlint-cli2
(with
yarn
)
Latest
yarn global add markdownlint-cli2
None.
markdownlint-cli2
(with
mise
)
Latest
mise use -g markdownlint-cli2
Overridden by project-specific configuration.
markdownlint-cli2
(with
yarn
)
Specific
yarn global add markdownlint-cli2@0.20.0
The
@
indicates a specific version, and this example updates the tool to version
0.20.0
.
markdownlint-cli2
(with
mise
)
Specific
mise install
Installs the version of
markdownlint-cli2
set in the
.tool-versions
or
mise.toml
file in a project.
Vale (with
mise
)
Specific
mise install
Installs the version of Vale set in the
.tool-versions
or
mise.toml
file in a project.
Vale (with
mise
)
Latest
mise use -g vale
Overridden by project-specific configuration.
Vale (other)
Specific
Not applicable.
Binaries can be
directly downloaded
.
Vale (with
brew
)
Latest
brew update && brew upgrade vale
This command is for macOS only.
##
Supported projects
For the specifics of each test run in our CI/CD pipelines, see the configuration for those tests
in the relevant projects:
https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/ci/docs.gitlab-ci.yml
https://gitlab.com/gitlab-org/gitlab-runner/-/blob/main/.gitlab/ci/qa.gitlab-ci.yml
https://gitlab.com/gitlab-org/omnibus-gitlab/-/blob/master/gitlab-ci-config/gitlab-com.yml
https://gitlab.com/gitlab-org/charts/gitlab/-/blob/master/.gitlab/ci/checks.gitlab-ci.yml
https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/blob/master/.gitlab-ci.yml
https://gitlab.com/gitlab-org/cli/-/blob/main/.gitlab-ci.yml
https://gitlab.com/gitlab-org/ops/artifact-registry/-/blob/main/.gitlab/ci/docs.gitlab-ci.yml
https://gitlab.com/gitlab-org/release/patch-release-blogs/-/blob/main/.gitlab/ci/docs.gitlab-ci.yml
We also run some documentation tests in these projects:
GitLab Development Kit:
https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/.gitlab/ci/test.gitlab-ci.yml
GitLab Docs website:
https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/blob/main/.gitlab/ci/lint.gitlab-ci.yml
Gitaly:
https://gitlab.com/gitlab-org/gitaly/-/blob/master/.gitlab-ci.yml
GitLab Duo Plugin for JetBrains:
https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin/-/blob/main/.gitlab-ci.yml
GitLab for VS Code extension:
https://gitlab.com/gitlab-org/gitlab-vscode-extension/-/blob/main/.gitlab-ci.yml
GitLab Plugin for Neovim:
https://gitlab.com/gitlab-org/editor-extensions/gitlab.vim/-/blob/main/.gitlab-ci.yml
GitLab Language Server:
https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp/-/blob/main/.gitlab-ci.yml
GitLab for Visual Studio extension:
https://gitlab.com/gitlab-org/editor-extensions/gitlab-visual-studio-extension/-/blob/main/.gitlab-ci.yml
AI Gateway:
https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/.gitlab/ci/lint.gitlab-ci.yml
Centralized Evaluation Framework CLI:
https://gitlab.com/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/cef-cli/-/blob/main/.gitlab-ci.yml
Centralized Evaluation Framework Service:
https://gitlab.com/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/cef-service/-/blob/main/.gitlab-ci.yml
GitLab Container Registry:
https://gitlab.com/gitlab-org/container-registry/-/blob/master/.gitlab/ci/validate.yml
Was this page helpful?
Yes
No
