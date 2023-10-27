
Using CSS sprites
=================

.. include:: ../includes/important_not_revised.rst

We've introduced CSS sprites into Launchpad. This is a technique that
uses a single image containing all the icons for a website. Icons are
displayed by showing just the required segment of that image using CSS.
If you are interested you can read more about `how CSS sprites improve
website
performance <http://www.websiteoptimization.com/speed/tweak/css-sprites/>`__.
This page will focus on how you can use the Launchpad sprites with ease in your
templates.

You can see what the launchpad image looks like:

.. XXX: image missing

attachment:icon-sprites.png

These correspond to the sprites defined in
``lib/canonical/launchpad/icing/sprite.css.in``.

Generating sprite image
-----------------------

**Don't forget that you need to build the image**

::

   make sprite_image

General use of sprites in templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, you won't actually need to do anything differently to use
the sprites as the tales link formatters have been updated to do all the
work for you. For example, if you write the following in your template:

::

   <a tal:replace="structure person/fmt:link">Sample Person</a>

Then the generated output will use the sprites automatically. This is
**the preferred way** of using icons in templates.

Similarly, if you need to get just the icon you can just use the icon
formatter. For example, to display the icon separately from the link you
could do the following:

::

   <span tal:replace="structure person/fmt:icon"></span> <a tal:attributes="href person/...">Sample Person</a>

For most normal situations this is all you should need.

Building on the sprites API
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to work with sprites programmatically, here are a few extra
things that you might want to know.

All that the above formatters do is add the appropriate classes to the
html elements. For example, adding the person icon to a link manually
using the sprites is as simple as doing the following (this will show
the person icon on the left side of the link):

::

   <a href="~beuno" class="sprite person">Martin Albisetti</a>

Or if you just want the icon, since it's a CSS class, you need to slap
it into a span:

::

   <span class="sprite person"></span>

If you need to generate the relevant sprite classes programmatically,
you can do so using the sprite_css formatter:

::

   <a href="~beuno" tal:attributes="class person/fmt:sprite_css">Martin Albisetti</a>

If you want a click-able icon without any text then you need to add a
span element with the special class 'invisible-link' inside the anchor
element. This span element should contain the fall-back text which will
be displayed when CSS is disabled. The special 'invisible-link' class
will be used to give the link an actual width:

::

   <a href="+edit" class="sprite edit"><span class="invisible-link">edit</span></a>
