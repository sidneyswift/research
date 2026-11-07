# Capture: sphinx-doctest

Canonical URL: https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html
Resolved URL: https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

[![logo](https://www.sphinx-doc.org/en/master/_static/sphinx-logo.svg) Sphinx](https://www.sphinx-doc.org/en/master/index.html)

[Source Code](https://github.com/sphinx-doc/sphinx)

### Navigation

- [Documentation](https://www.sphinx-doc.org/en/master/index.html) »
- [Using Sphinx](https://www.sphinx-doc.org/en/master/usage/index.html) »
- [Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html) »
- [`sphinx.ext.doctest` – Test snippets in the documentation]()

### On this page

- `sphinx.ext.doctest` – Test snippets in the documentation
  - [Directives](#directives)
    - [`.. testsetup::`](#directive-testsetup)
      - [`:skipif:`](#directive-option-testsetup-skipif)
    - [`.. testcleanup::`](#directive-testcleanup)
      - [`:skipif:`](#directive-option-testcleanup-skipif)
    - [`.. doctest::`](#directive-doctest)
      - [`:hide:`](#directive-option-doctest-hide)
      - [`:options:`](#directive-option-doctest-options)
      - [`:pyversion:`](#directive-option-doctest-pyversion)
      - [`:trim-doctest-flags:`](#directive-option-doctest-trim-doctest-flags)
      - [`:no-trim-doctest-flags:`](#directive-option-doctest-no-trim-doctest-flags)
      - [`:skipif:`](#directive-option-doctest-skipif)
    - [`.. testcode::`](#directive-testcode)
      - [`:hide:`](#directive-option-testcode-hide)
      - [`:trim-doctest-flags:`](#directive-option-testcode-trim-doctest-flags)
      - [`:no-trim-doctest-flags:`](#directive-option-testcode-no-trim-doctest-flags)
      - [`:skipif:`](#directive-option-testcode-skipif)
    - [`.. testoutput::`](#directive-testoutput)
      - [`:hide:`](#directive-option-testoutput-hide)
      - [`:options:`](#directive-option-testoutput-options)
      - [`:trim-doctest-flags:`](#directive-option-testoutput-trim-doctest-flags)
      - [`:no-trim-doctest-flags:`](#directive-option-testoutput-no-trim-doctest-flags)
      - [`:skipif:`](#directive-option-testoutput-skipif)
  - [Skipping tests conditionally](#skipping-tests-conditionally)
  - [Configuration](#configuration)
    - [`doctest_default_flags`](#confval-doctest_default_flags)
    - [`doctest_show_successes`](#confval-doctest_show_successes)
    - [`doctest_path`](#confval-doctest_path)
    - [`doctest_global_setup`](#confval-doctest_global_setup)
    - [`doctest_global_cleanup`](#confval-doctest_global_cleanup)
    - [`doctest_test_doctest_blocks`](#confval-doctest_test_doctest_blocks)
    - [`doctest_fail_fast`](#confval-doctest_fail_fast)

The Basics

- [Installing Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
- [Getting started](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
- [Build your first project](https://www.sphinx-doc.org/en/master/tutorial/index.html)

User guide

- [Using Sphinx](https://www.sphinx-doc.org/en/master/usage/index.html)
  - [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
  - [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)
  - [Cross-references](https://www.sphinx-doc.org/en/master/usage/referencing.html)
  - [Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html)
  - [Builders](https://www.sphinx-doc.org/en/master/usage/builders/index.html)
  - [Domains](https://www.sphinx-doc.org/en/master/usage/domains/index.html)
  - [Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
    - [`sphinx.ext.apidoc` – Generate API documentation from Python packages](https://www.sphinx-doc.org/en/master/usage/extensions/apidoc.html)
    - [`sphinx.ext.autodoc` – Include documentation from docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
    - [`sphinx.ext.autosectionlabel` – Allow referencing sections by their title](https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html)
    - [`sphinx.ext.autosummary` – Generate autodoc summaries](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
    - [`sphinx.ext.coverage` – Collect doc coverage stats](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html)
    - `sphinx.ext.doctest` – Test snippets in the documentation
    - [`sphinx.ext.duration` – Measure durations of Sphinx processing](https://www.sphinx-doc.org/en/master/usage/extensions/duration.html)
    - [`sphinx.ext.extlinks` – Markup to shorten external links](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html)
    - [`sphinx.ext.githubpages` – Publish HTML docs in GitHub Pages](https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html)
    - [`sphinx.ext.graphviz` – Add Graphviz graphs](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html)
    - [`sphinx.ext.ifconfig` – Include content based on configuration](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html)
    - [`sphinx.ext.imgconverter` – A reference image converter using Imagemagick](https://www.sphinx-doc.org/en/master/usage/extensions/imgconverter.html)
    - [`sphinx.ext.inheritance_diagram` – Include inheritance diagrams](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html)
    - [`sphinx.ext.intersphinx` – Link to other projects’ documentation](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
    - [`sphinx.ext.linkcode` – Add external links to source code](https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html)
    - [Math support for HTML outputs in Sphinx](https://www.sphinx-doc.org/en/master/usage/extensions/math.html)
    - [`sphinx.ext.napoleon` – Support for NumPy and Google style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
    - [`sphinx.ext.todo` – Support for todo items](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
    - [`sphinx.ext.viewcode` – Add links to highlighted source code](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
  - [HTML theming](https://www.sphinx-doc.org/en/master/usage/theming.html)
  - [Internationalization](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
  - [Sphinx Web Support](https://www.sphinx-doc.org/en/master/usage/advanced/websupport/index.html)
- [Extending Sphinx](https://www.sphinx-doc.org/en/master/development/index.html)
- [Sphinx API](https://www.sphinx-doc.org/en/master/extdev/index.html)
- [LaTeX customization](https://www.sphinx-doc.org/en/master/latex.html)

Community

- [Get support](https://www.sphinx-doc.org/en/master/support.html)
- [Contribute to Sphinx](https://www.sphinx-doc.org/en/master/internals/index.html)
- [Sphinx FAQ](https://www.sphinx-doc.org/en/master/faq.html)
- [Sphinx authors](https://www.sphinx-doc.org/en/master/authors.html)

Reference

- [Command-line tools](https://www.sphinx-doc.org/en/master/man/index.html)
- [Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html)
- [Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
  - [`sphinx.ext.apidoc` – Generate API documentation from Python packages](https://www.sphinx-doc.org/en/master/usage/extensions/apidoc.html)
  - [`sphinx.ext.autodoc` – Include documentation from docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
  - [`sphinx.ext.autosectionlabel` – Allow referencing sections by their title](https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html)
  - [`sphinx.ext.autosummary` – Generate autodoc summaries](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
  - [`sphinx.ext.coverage` – Collect doc coverage stats](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html)
  - `sphinx.ext.doctest` – Test snippets in the documentation
  - [`sphinx.ext.duration` – Measure durations of Sphinx processing](https://www.sphinx-doc.org/en/master/usage/extensions/duration.html)
  - [`sphinx.ext.extlinks` – Markup to shorten external links](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html)
  - [`sphinx.ext.githubpages` – Publish HTML docs in GitHub Pages](https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html)
  - [`sphinx.ext.graphviz` – Add Graphviz graphs](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html)
  - [`sphinx.ext.ifconfig` – Include content based on configuration](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html)
  - [`sphinx.ext.imgconverter` – A reference image converter using Imagemagick](https://www.sphinx-doc.org/en/master/usage/extensions/imgconverter.html)
  - [`sphinx.ext.inheritance_diagram` – Include inheritance diagrams](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html)
  - [`sphinx.ext.intersphinx` – Link to other projects’ documentation](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
  - [`sphinx.ext.linkcode` – Add external links to source code](https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html)
  - [Math support for HTML outputs in Sphinx](https://www.sphinx-doc.org/en/master/usage/extensions/math.html)
  - [`sphinx.ext.napoleon` – Support for NumPy and Google style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
  - [`sphinx.ext.todo` – Support for todo items](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
  - [`sphinx.ext.viewcode` – Add links to highlighted source code](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
- [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
- [Glossary](https://www.sphinx-doc.org/en/master/glossary.html)
- [Changelog](https://www.sphinx-doc.org/en/master/changes/index.html)
- [Projects using Sphinx](https://www.sphinx-doc.org/en/master/examples.html)

# `sphinx.ext.doctest` – Test snippets in the documentation ¶

It is often helpful to include snippets of code in your documentation and demonstrate the results of executing them. But it is important to ensure that the documentation stays up-to-date with the code.

This extension allows you to test such code snippets in the documentation in a natural way. If you mark the code blocks as shown here, the `doctest` builder will collect them and run them as doctest tests.

Within each document, you can assign each snippet to a *group*. Each group consists of:

- zero or more *setup code* blocks (e.g. importing the module to test)
- one or more *test* blocks

When building the docs with the `doctest` builder, groups are collected for each document and run one after the other, first executing setup code blocks, then the test blocks in the order they appear in the file.

There are two kinds of test blocks:

- *doctest-style* blocks mimic interactive sessions by interleaving Python code (including the interpreter prompt) and output.
- *code-output-style* blocks consist of an ordinary piece of Python code, and optionally, a piece of output for that code.

## Directives ¶

The *group* argument below is interpreted as follows: if it is empty, the block is assigned to the group named `default`. If it is `*`, the block is assigned to all groups (including the `default` group). Otherwise, it must be a comma-separated list of group names.

<dl><dt>.. testsetup::[group]<a href="#directive-testsetup" title="Link to this definition">¶</a></dt>
<dd>

A setup code block. This code is not shown in the output for other builders, but executed before the doctests of the group(s) it belongs to.

Options

<dl><dt>:skipif:condition(text)<a href="#directive-option-testsetup-skipif" title="Link to this definition">¶</a></dt>
<dd>

Skip the directive if the python expression *condition* is True. See <a href="#doctest-skipif">skipping tests conditionally</a>.

</dd></dl></dd>
</dl><dl><dt>.. testcleanup::[group]<a href="#directive-testcleanup" title="Link to this definition">¶</a></dt>
<dd>

A cleanup code block. This code is not shown in the output for other builders, but executed after the doctests of the group(s) it belongs to.

Added in version 1.1.

Options

<dl><dt>:skipif:condition(text)<a href="#directive-option-testcleanup-skipif" title="Link to this definition">¶</a></dt>
<dd>

Skip the directive if the python expression *condition* is True. See <a href="#doctest-skipif">skipping tests conditionally</a>.

</dd></dl></dd>
</dl><dl><dt>.. doctest::[group]<a href="#directive-doctest" title="Link to this definition">¶</a></dt>
<dd>

A doctest-style code block. You can use standard <a href="https://docs.python.org/3/library/doctest.html#module-doctest" title="(in Python v3.15)"><code>doctest</code></a> flags for controlling how actual output is compared with what you give as output. The default set of flags is specified by the <a href="#confval-doctest_default_flags"><code>doctest_default_flags</code></a> configuration variable.

Options

<dl><dt>:hide:<a href="#directive-option-doctest-hide" title="Link to this definition">¶</a></dt>
<dd>

Hide the doctest block in other builders. By default it is shown as a highlighted doctest block.

</dd></dl><dl><dt>:options:doctest flags(comma separated list)<a href="#directive-option-doctest-options" title="Link to this definition">¶</a></dt>
<dd>

A comma-separated list of doctest flags that apply to each example in the tests. (You still can give explicit flags per example, with doctest comments, but they will show up in other builders too.)

Alternatively, you can give inline doctest options, like in doctest:

```
>>> datetime.date.now()
datetime.date(2008, 1, 1)

```

They will be respected when the test is run, but by default will be stripped from presentation output. You can prevent stripping using the option <a href="#directive-option-doctest-no-trim-doctest-flags" title="doctest:no-trim-doctest-flags directive:option"><code>doctest:no-trim-doctest-flags</code></a>.

</dd></dl><dl><dt>:pyversion:(text)<a href="#directive-option-doctest-pyversion" title="Link to this definition">¶</a></dt>
<dd>

Specify the required Python version for the example to be tested. For instance, in the following case the example will be tested only for Python versions greater than 3.15:

```
.. doctest::
   :pyversion: > 3.15

```

The following operands are supported:

- <code>~=</code>: Compatible release clause
- <code>==</code>: Version matching clause
- <code>!=</code>: Version exclusion clause
- <code>&lt;=</code>, <code>&gt;=</code>: Inclusive ordered comparison clause
- <code>&lt;</code>, <code>&gt;</code>: Exclusive ordered comparison clause
- <code>===</code>: Arbitrary equality clause.

<code>pyversion</code> option is followed <a href="https://peps.python.org/pep-0440/#version-specifiers">**PEP-440: Version Specifiers**</a>.

Added in version 1.6.

Changed in version 1.7: Supported PEP-440 operands and notations

</dd></dl><dl><dt>:trim-doctest-flags:<a href="#directive-option-doctest-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dt>:no-trim-doctest-flags:<a href="#directive-option-doctest-no-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dd>

Whether to trim remove doctest flags (comments looking like <code># doctest: FLAG, ...</code>) at the ends of lines and <code>&lt;BLANKLINE&gt;</code> markers individually. Default is <code>trim-doctest-flags</code>.

Note that like with standard doctests, you have to use <code>&lt;BLANKLINE&gt;</code> to signal a blank line in the expected output. The <code>&lt;BLANKLINE&gt;</code> is removed when building presentation output (HTML, LaTeX etc.).

</dd></dl><dl><dt>:skipif:condition(text)<a href="#directive-option-doctest-skipif" title="Link to this definition">¶</a></dt>
<dd>

Skip the directive if the python expression *condition* is True. See <a href="#doctest-skipif">skipping tests conditionally</a>.

</dd></dl></dd>
</dl><dl><dt>.. testcode::[group]<a href="#directive-testcode" title="Link to this definition">¶</a></dt>
<dd>

A code block for a code-output-style test.

Options

<dl><dt>:hide:<a href="#directive-option-testcode-hide" title="Link to this definition">¶</a></dt>
<dd>

Hide the code block in other builders. By default it is shown as a highlighted code block.

</dd></dl><dl><dt>:trim-doctest-flags:<a href="#directive-option-testcode-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dt>:no-trim-doctest-flags:<a href="#directive-option-testcode-no-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dd>

Whether to trim remove doctest flags (comments looking like <code># doctest: FLAG, ...</code>) at the ends of lines and <code>&lt;BLANKLINE&gt;</code> markers individually. Default is <code>trim-doctest-flags</code>.

</dd></dl><dl><dt>:skipif:condition(text)<a href="#directive-option-testcode-skipif" title="Link to this definition">¶</a></dt>
<dd>

Skip the directive if the python expression *condition* is True. See <a href="#doctest-skipif">skipping tests conditionally</a>.

</dd></dl>

Note

Code in a <code>testcode</code> block is always executed all at once, no matter how many statements it contains. Therefore, output will *not* be generated for bare expressions – use <code>print</code>. Example:

```
.. testcode::

   1+1         # this will give no output!
   print(2+2)  # this will give output

.. testoutput::

   4

```

Also, please be aware that since the doctest module does not support mixing regular output and an exception message in the same snippet, this applies to testcode/testoutput as well.

</dd></dl><dl><dt>.. testoutput::[group]<a href="#directive-testoutput" title="Link to this definition">¶</a></dt>
<dd>

The corresponding output, or the exception message, for the last <a href="#directive-testcode" title="testcode directive"><code>testcode</code></a> block.

<dl><dt>:hide:<a href="#directive-option-testoutput-hide" title="Link to this definition">¶</a></dt>
<dd>

Hide the doctest block in other builders. By default it is shown as a highlighted doctest block.

</dd></dl><dl><dt>:options:doctest flags(comma separated list)<a href="#directive-option-testoutput-options" title="Link to this definition">¶</a></dt>
<dd>

A comma-separated list of doctest flags.

</dd></dl><dl><dt>:trim-doctest-flags:<a href="#directive-option-testoutput-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dt>:no-trim-doctest-flags:<a href="#directive-option-testoutput-no-trim-doctest-flags" title="Link to this definition">¶</a></dt>
<dd>

Whether to trim remove doctest flags (comments looking like <code># doctest: FLAG, ...</code>) at the ends of lines and <code>&lt;BLANKLINE&gt;</code> markers individually. Default is <code>trim-doctest-flags</code>.

</dd></dl><dl><dt>:skipif:condition(text)<a href="#directive-option-testoutput-skipif" title="Link to this definition">¶</a></dt>
<dd>

Skip the directive if the python expression *condition* is True. See <a href="#doctest-skipif">skipping tests conditionally</a>.

</dd></dl>

Example:

```
.. testcode::

   print('Output     text.')

.. testoutput::
   :hide:
   :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

   Output text.

```

</dd></dl>

The following is an example for the usage of the directives. The test via [`doctest`](#directive-doctest "doctest directive") and the test via [`testcode`](#directive-testcode "testcode directive") and [`testoutput`](#directive-testoutput "testoutput directive") are equivalent.

```
The parrot module
=================

.. testsetup:: *

   import parrot

The parrot module is a module about parrots.

Doctest example:

.. doctest::

   >>> parrot.voom(3000)
   This parrot wouldn't voom if you put 3000 volts through it!

Test-Output example:

.. testcode::

   parrot.voom(3000)

This would output:

.. testoutput::

   This parrot wouldn't voom if you put 3000 volts through it!

```

## Skipping tests conditionally ¶

`skipif`, a string option, can be used to skip directives conditionally. This may be useful e.g. when a different set of tests should be run depending on the environment (hardware, network/VPN, optional dependencies or different versions of dependencies). The `skipif` option is supported by all of the doctest directives. Below are typical use cases for `skipif` when used for different directives:

- [`testsetup`](#directive-testsetup "testsetup directive") and [`testcleanup`](#directive-testcleanup "testcleanup directive")
  - conditionally skip test setup and/or cleanup
  - customize setup/cleanup code per environment
- [`doctest`](#directive-doctest "doctest directive")
  - conditionally skip both a test and its output verification
- [`testcode`](#directive-testcode "testcode directive")
  - conditionally skip a test
  - customize test code per environment
- [`testoutput`](#directive-testoutput "testoutput directive")
  - conditionally skip output assertion for a skipped test
  - expect different output depending on the environment

The value of the `skipif` option is evaluated as a Python expression. If the result is a true value, the directive is omitted from the test run just as if it wasn’t present in the file at all.

Instead of repeating an expression, the [`doctest_global_setup`](#confval-doctest_global_setup) configuration option can be used to assign it to a variable which can then be used instead.

Here’s an example which skips some tests if Pandas is not installed:

conf.py [¶](#id1 "Link to this code")

```
extensions = ['sphinx.ext.doctest']
doctest_global_setup = '''
try:
    import pandas as pd
except ImportError:
    pd = None
'''

```

contents.rst [¶](#id2 "Link to this code")

```
.. testsetup::
   :skipif: pd is None

   data = pd.Series([42])

.. doctest::
   :skipif: pd is None

   >>> data.iloc[0]
   42

.. testcode::
   :skipif: pd is None

   print(data.iloc[-1])

.. testoutput::
   :skipif: pd is None

   42

```

## Configuration ¶

The doctest extension uses the following configuration values:

<dl><dt>doctest_default_flags<a href="#confval-doctest_default_flags" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>int</code></dd>
<dt>Default:</dt>
<dd><code>ELLIPSIS | IGNORE_EXCEPTION_DETAIL | DONT_ACCEPT_TRUE_FOR_1</code></dd>
</dl>

By default, these options are enabled:

- <code>ELLIPSIS</code>, allowing you to put ellipses in the expected output that match anything in the actual output;
- <code>IGNORE_EXCEPTION_DETAIL</code>, causing everything following the leftmost colon and any module information in the exception name to be ignored;
- <code>DONT_ACCEPT_TRUE_FOR_1</code>, rejecting “True” in the output where “1” is given – the default behavior of accepting this substitution is a relic of pre-Python 2.2 times.

Added in version 1.5.

</dd></dl><dl><dt>doctest_show_successes<a href="#confval-doctest_show_successes" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>bool</code></dd>
<dt>Default:</dt>
<dd><code>True</code></dd>
</dl>

Controls whether successes are reported.

For a project with many doctests, it may be useful to set this to <code>False</code> to only highlight failures.

Added in version 7.2.

</dd></dl><dl><dt>doctest_path<a href="#confval-doctest_path" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>Sequence[str]</code></dd>
<dt>Default:</dt>
<dd><code>()</code></dd>
</dl>

A list of directories that will be added to <a href="https://docs.python.org/3/library/sys.html#sys.path" title="(in Python v3.15)"><code>sys.path</code></a> when the doctest builder is used. (Make sure it contains absolute paths.)

</dd></dl><dl><dt>doctest_global_setup<a href="#confval-doctest_global_setup" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>str</code></dd>
<dt>Default:</dt>
<dd><code>''</code></dd>
</dl>

Python code that is treated like it were put in a <code>testsetup</code> directive for *every* file that is tested, and for every group. You can use this to e.g. import modules you will always need in your doctests.

Added in version 0.6.

</dd></dl><dl><dt>doctest_global_cleanup<a href="#confval-doctest_global_cleanup" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>str</code></dd>
<dt>Default:</dt>
<dd><code>''</code></dd>
</dl>

Python code that is treated like it were put in a <code>testcleanup</code> directive for *every* file that is tested, and for every group. You can use this to e.g. remove any temporary files that the tests leave behind.

Added in version 1.1.

</dd></dl><dl><dt>doctest_test_doctest_blocks<a href="#confval-doctest_test_doctest_blocks" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>str</code></dd>
<dt>Default:</dt>
<dd><code>'default'</code></dd>
</dl>

If this is a nonempty string, standard reStructuredText doctest blocks will be tested too. They will be assigned to the group name given.

reStructuredText doctest blocks are simply doctests put into a paragraph of their own, like so:

```
Some documentation text.

>>> print(1)
1

Some more documentation text.

```

(Note that no special <code>::</code> is used to introduce a doctest block; docutils recognizes them from the leading <code>&gt;&gt;&gt;</code>. Also, no additional indentation is used, though it doesn’t hurt.)

If this value is left at its default value, the above snippet is interpreted by the doctest builder exactly like the following:

```
Some documentation text.

.. doctest::

   >>> print(1)
   1

Some more documentation text.

```

This feature makes it easy for you to test doctests in docstrings included with the <a href="https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc" title="sphinx.ext.autodoc: Include documentation from docstrings."><code>autodoc</code></a> extension without marking them up with a special directive.

Note though that you can’t have blank lines in reStructuredText doctest blocks. They will be interpreted as one block ending and another one starting. Also, removal of <code>&lt;BLANKLINE&gt;</code> and <code># doctest:</code> options only works in <a href="#directive-doctest" title="doctest directive"><code>doctest</code></a> blocks, though you may set <a href="https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-trim_doctest_flags"><code>trim_doctest_flags</code></a> to achieve that in all code blocks with Python console content.

</dd></dl><dl><dt>doctest_fail_fast<a href="#confval-doctest_fail_fast" title="Link to this definition">¶</a></dt>
<dd><dl><dt>Type:</dt>
<dd><code>bool</code></dd>
<dt>Default:</dt>
<dd><code>False</code></dd>
</dl>

Exit when the first failure is encountered.

Added in version 9.0.

</dd></dl>

[Previous`sphinx.ext.coverage` – Collect doc coverage stats](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html) [Next`sphinx.ext.duration` – Measure durations of Sphinx processing](https://www.sphinx-doc.org/en/master/usage/extensions/duration.html)

© Copyright 2007-2026, the Sphinx developers. Created using [Sphinx](https://www.sphinx-doc.org/) 9.3.0.