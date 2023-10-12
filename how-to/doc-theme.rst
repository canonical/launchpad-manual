==================================
Rebuilding the documentation theme
==================================

The Vanilla theme used in the documentation is based on `vanilla-sphinx-test
<https://github.com/evildmp/vanilla-sphinx-test>`_.  All the source files
needed to generate it are in the ``doc/vanilla/`` directory, though for
simplicity the output of building the theme's CSS is currently committed to
git rather than built dynamically.  To rebuild it, run the following on at
least Ubuntu 22.04::

    make -C doc build-css
