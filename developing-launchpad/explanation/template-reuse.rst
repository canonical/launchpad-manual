Template reuse
==============

.. include:: ../includes/important_not_revised.rst

It's wasteful, and generally harmful, to have the same code repeated in
multiple places, even if that code is HTML. A single definition means
that only that definition need ever be changed, and you can't wind up
with two definitions that are subtly different. There are two ways of
avoiding this: fragment views and macros.

Fragment Views
--------------

Fragment views are the preferred method. When working with content
classes, you may want to render a content class in a view for another
class. The HTML you would want to include is usually the default view's
HTML, stripped of its leading and trailing HTML, like ``<html>``, ``<head>``
and body.

So given a default view named ``+index`` , you would create a new view called
``+fragment``, and move the body of the HTML into it.
The ``+index`` TAL would then include ``context/@@+fragment`` to copy the
content in.

You could then reuse ``+fragment`` in other locations where you want to display
that content object.

The ``+fragment`` view can also be viewed in a browser by hand-hacking its URL.
Since it's only meant to be included in other pages, allowing a browser to view
it is not really pure. Providing it this way permits AJAX to reuse it, and
normal users would need to hand-hack URLs to even be aware of it.)

Macros
------

In cases where you're not dealing with a particular content object, it
may make more sense to use a macro. For example, if you're writing a
page that seems to have certain things repeated frequently, you can
define a macro for the repeated code, then use the macro later in the
page.

Single-view Macros
~~~~~~~~~~~~~~~~~~

To refer to the macro ``mymacro`` within the page where you defined it, you can
use ``template/macros/mymacro``.
``template`` refers to the template that is currently being rendered.

Context-wide Macros
~~~~~~~~~~~~~~~~~~~

If you have macros that need to be reused across pages for a given
content object, then you may wish to create a view that holds the
relevant macros for that content object, like ``+macros`` .

You can then refer to it as ``context/@@/+macros/mymacro``. It is rarely a good
idea for one view to refer to the macro of a "normal" view, because that reuse
will not be obvious to the casual observer.

Multi-context Macros
~~~~~~~~~~~~~~~~~~~~

If you wish to reuse macros for views across various context objects,
you'll need to create a reference to the correct Zope Page Template. You
can do this by making a member of the view class which is an instance of
``ViewPageTemplateFile``.

The view class would look like:

::

   class FooView(LaunchpadView):
       bar_macros = ViewPageTemplateFile("../templates/bar-macros.pt")

A reference to the macro ``mymacro`` would look like:

::

   view/bar_macros/macros/mymacro
