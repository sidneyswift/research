# Capture: Tables Tutorial | Web Accessibility Initiative (WAI) | W3C

Canonical URL: https://www.w3.org/WAI/tutorials/tables/
Resolved URL: https://www.w3.org/WAI/tutorials/tables/
Retrieved: 2026-11-05
Representation: HTML main/article converted to Markdown via markdownify; visual widgets and assets not captured
Content-Type: text/html; charset=utf-8

---

# Tables Tutorial

in [Tutorials](https://www.w3.org/WAI/tutorials/)

Data tables are used to organize data with a logical relationship in grids. Accessible tables need HTML markup that indicates header cells and data cells and defines their relationship. Assistive technologies use this information to provide context to users.

Header cells must be marked up with `<th>`, and data cells with `<td>` to make tables accessible. For more complex tables, explicit associations may be needed using `scope`, `id`, and `headers` attributes.

This tutorial shows you how to apply appropriate structural markup to tables. It includes the following pages:

* **[Tables with one header![](/WAI/content-images/tutorials/tables/img-simple.png)](https://www.w3.org/WAI/tutorials/tables/one-header/)** for rows or columns: For tables with content that is easy to distinguish, mark up header cells with `<th>` and data cells with `<td>` elements.
* **[Tables with two headers![](/WAI/content-images/tutorials/tables/img-multidir.png)](https://www.w3.org/WAI/tutorials/tables/two-headers/)** have a simple row header and a simple column header: For tables with unclear header directions, define the direction of each header by setting the `scope` attribute to `col` or `row`.
* **[Tables with irregular headers![](/WAI/content-images/tutorials/tables/img-irreg.png)](https://www.w3.org/WAI/tutorials/tables/irregular/)** have header cells that span multiple columns and/or rows: For these tables, define column and row groups and set the range of the header cells using the `colgroup` and `rowgroup` values of the scope attribute.
* **[Tables with multi-level headers![](/WAI/content-images/tutorials/tables/img-multi.png)](https://www.w3.org/WAI/tutorials/tables/multi-level/)** have multiple header cells associated per data cell: For tables that are so complex that header cells can’t be associated in a strictly horizontal or vertical way, use `id` and `headers` attributes to associate header and data cells explicitly.
* **[Caption & Summary![](/WAI/content-images/tutorials/tables/img-caption.png)](https://www.w3.org/WAI/tutorials/tables/caption-summary/):** A caption identifies the overall topic of a table and is useful in most situations. A summary provides orientation or navigation hints in complex tables.

Some document formats other than HTML, such as PDF, provide similar mechanisms to markup table structures. Word processing applications may also provide mechanisms to markup tables. Tables markup is often lost when converting from one format to another, though some programs may provide functionality to assist converting table markup.

Many web authoring tools and content management systems (CMS) provide functions to define header cells during table creation without having to edit the code manually.

 Note

This tutorial provides guidance for creating tables used to display data in a grid. This tutorial does not apply to tables used for layout. As a general rule, tables aren’t meant to be used for layout purposes. Instead, a best practice is to use Cascading Style Sheets (CSS) for visual presentation.

## Why is this important?

Tables without structural markup to differentiate and properly link between header and data cells, create accessibility barriers. Relying on visual cues alone is not sufficient to create an accessible table. With structural markup, headers and data cells can be programmatically determined by software, which means that:

* **People using screen readers** can have the row and column headers read aloud as they navigate through the table. Screen readers speak one cell at a time and reference the associated header cells, so the reader doesn’t lose context.
* **Some people use alternative ways to render the data**, for example by using custom stylesheets to display header cells more prominently. Techniques like this enable them to change text size and colors and display the information as lists rather than grids. The table code needs to be properly structured to allow alternative renderings.

  Related WCAG resources

These tutorials provide best-practice guidance on implementing accessibility in different situations. This page combined the following WCAG success criteria and techniques from different conformance levels:

**Success Criteria:**

* [**1.3.1** Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships)
  (Level A)

 

## Help improve this page

Please share your ideas, suggestions, or comments via e-mail to the publicly-archived list [wai@w3.org](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.) or via GitHub.

[E-mail](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.)[Fork & Edit on GitHub](https://github.com/w3c/wai-website/edit/main/pages/design-develop/tutorials/tables/index.md)[New GitHub Issue](https://github.com/w3c/wai-website/issues/new?template=content-issue.yml&wai-resource-id=wai-tutorials&wai-url=https://www.w3.org/WAI/tutorials/tables/)

 [Back to Top](https://www.w3.org/WAI/tutorials/tables/#top)