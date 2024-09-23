CSS
===

.. include:: ../includes/important_not_revised.rst

Files
-----

The main files you will care about are:

::

   lib/canonical/launchpad/icing/css/*.scss

This is where Launchpad's styles live, with exception of third-party or
external elements.

There is also a secondary stylesheet with some legacy styles in it. At
any point you can remove styles from this stylesheet you should. Often
styles are in this stylesheet because they are too specific and need to
be made more generic. This style sheet lives here:

::

   lib/canonical/launchpad/icing/style.css

Building
--------

To build the css files run:

::

   make css_combine

If you are dealing with sprites you may also have to run:

::

   make sprite_image

:doc:`More info on sprites <css-sprites>`.

Fonts
-----

The current font sizes are:

.. list-table::
   :header-rows: 0

   * - 10px
     - smallest
   * - 12px
     - body
   * - 14px
     - navigation
   * - 16px
     - h3
   * - 22px
     - h2
   * - 30px
     - h1


Colours
-------

.. list-table::
   :header-rows: 0

   * - Default text
     - ``#333``
   * - Links
     - ``#03a``
   * - Links that only act on current page
     - ``#093``

Base elements
-------------

These are generic elements that will often be used to make up a
component. These are the defaults we set that everything else will build
on. Within this file you should try normalise as many generic elements
as you can (this will take the place of a reset file).

*Examples: generic headings, links, images, forms, generic buttons*

Layout
------

These elements are the main page structure. Usually there should be only
one of each element, and each element should have an ID. If it's a
re-usable component it probably isn't layout. Layouts are really just a
special type of component and generally should follow component rules
(see below).

*Examples: header, footer, sidebar, content and main navigation.*

Components
----------

These elements are the content themselves and usually make up what might
be called a widget (or component). They will almost always be a
collection of elements.

*Examples: content portlets, notification banners, bug lists. Modifiers*

Modifiers are used to change the state or the presentation of something.
Modifier classes should usually live with the class(es) they are
modifying unless they are very generic. They may be generic typography
modifiers (which would live in typography.css) or for a specific
component (which will live in that components .css file). Component
modifiers should be clearly labelled (using a clearly labelled section at
the bottom of the stylesheet may be a good way to do this).

*Examples: a portlet could have a collapsed state which you would
control by applying a "collapse" class. A layout could be one column or
two column which could be controlled by "one-column" and "two-column"
classes.*

Naming scheme
-------------

CSS classes should be separated by hyphens. Abbreviations should be
avoided.

There are no set prefixes or conventions for layout, base elements and
modifiers. Components should use ".component-name" and
".component-name-element-name" where appropriate.

Files
-----

- base.scss

  - typography.scss
  - forms.scss
  - colours.scss

- layout.scss
- modifiers.scss
- components/component_name.scss

ID usage
--------

IDs can be used when there should only be one of something on the page.
It is recommended that IDs are not used for styling. Components, Base
elements and Modifiers should never contain IDs, Layout elements should
usually have IDs (for the base element). IDs can be used (where
appropriate) when required by JavaScript element selection.

CSS compatibility
-----------------

We should use CSS3 where possible. To maintain compatibility with older
browsers we should use conditional statements and separate stylesheets
with overrides for our other classes.

Example:

.. code:: html

   <!--[if IE 6]>
           <link rel="stylesheet" type="text/css" href="ie6.css" />
   <![endif]-->

Curtis thinks this specific example is dubious, and if this is
representative, we need to really understand what users of these old
browser can do on Launchpad. Recent changes to forms only support recent
browsers. Many AJAX operations do not work with IE6 for example, it
making the site look pretty will not help them use Launchpad.
Non-developers need to report bugs and ask questions: Ubuntu users use
their computer to report bugs, Answers could be a desktop app that talks
to Lp's API.

YUI widgets
-----------

YUI widgets should maintain YUI conventions. They should live with the
javascript for the widget. Where possible the CSS written for a YUI
widget should follow our conventions, but only as secondary to YUI
conventions.
