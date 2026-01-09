The Launchpad JavaScript Build System
=====================================

.. include:: ../../includes/important_not_revised.rst

**Current in process of deprecating, see combo loader docs below.**

Most of the Launchpad JavaScript is bundled, minified, and distributed
in one large stand-alone file: ``launchpad.js``.

Adding new JavaScript modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new JavaScript module simply add a new ``<script>``
line to ``lib/lp/app/templates/base-layout-macros.pt`` in the large
``<devmode>`` JavaScript block.
The file you add to the list will be automatically included in the
``launchpad.js`` roll-up and used by both the test runner and the LP production
site.

Two special scripts, ``utilities/yui_deps.py`` and ``utilities/lp-deps.py``,
look in ``lib/lp/app/templates/base-layout-macros.pt`` for ``<script>`` lines.

The corresponding minified script files, the version of the file ending with
``-min.js``, will be added to ``launchpad.js``.

After making your changes you will probably want to run:

.. code::

  $ make clean_js && make jsbuild

Adding a third-party widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current story for adding a third-party widget is to put it in
``lib/lp/contrib``.

For CSS, follow the rules above to modify the tools. If other assets are
needed, you'll need to create a link in
``lib/canonical/launchpad/icing`` to the proper place in
``lib/lp/contrib`` so the assets can be found. See
``lib/canonical/launchpad/icing/yui3-gallery`` for an example.

New Combo loader Setup
----------------------

Currently an alternative JavaScript build process is under development
using the YUI combo loader system. JavaScript files are copied and
minified into a build directory ``build/js/``.

Files are served out of the ``build/js`` directory based on the YUI
combo loader config that is constructed in the
``lib/lp/app/templates/base-layout-macros.pt``. These are combined and
served out via the convoy WSGI application through Apache.

Developing Javascript
~~~~~~~~~~~~~~~~~~~~~

Because the JS files need to be copied from the Launchpad tree into the
build directory, changes to any JS files must trigger a build. You can
build manually using ``make jsbuild``. There's also a helper script that
can watch the launchpad tree for any JS changes and auto build as the
changes occur. You can start that process with ``make jsbuild\watch``.
This allows for faster JS development iterating.

Adding new Javascript modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add new JS to Launchpad, it needs to go into a proper YUI module. All
modules should be located either in an app, such as
``lib/lp/bugs/javascript/``, or in the base shared space
``lib/lp/app/javascript/``.

Running a ``make jsbuild`` will copy the new module into the build
directory in the proper location.

Once the files is created and part of the build directory, you can just
include that module name in any YUI block.

.. code::

   LPJS.use('modulename', function (Y)...

The combo loader will serve your new module when you reload the page
with that content on it.

Launchpad CSS
-------------

Adding a new CSS file
~~~~~~~~~~~~~~~~~~~~~

Launchpad combines and minifies all of its CSS files into 'combo.css'
before publishing them. The build tool is SCSS, installed via NPM. To
add a new CSS file, add a reference to ``combo.scss``. New YUI/LP
components can be added to ``css/components/_index.scss``.

After making your changes you will probably want to run:

.. code::

       $ make css_combine
