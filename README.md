Aptivate Template Tags
======================

A set of template tags for Django we use within aptivate.

Tags
----

### absurl

Gives the absolute URL, including the domain name.  This is useful when putting
URLs in emails.

### menu_item

TODO

### submit_buttons

TODO

Filters
-------

### format_items

Formats the items in a list using the Django Template syntax.

The template_string is used as a template to control the output.
For example, you can render a certain property of each item in the
list using "item.full_name" as your template The `{{ }}` braces will be
added automatically, as they are not legal inside a template tag.

In the context used to render the template, "item" is the current item
and nothing else is available.

### join_last_two

Joins the last two items in a list with the specified separator.
If the list contains zero or one items, nothing is changed.

### if_empty_list

If the list is empty, put the argument in instead.
