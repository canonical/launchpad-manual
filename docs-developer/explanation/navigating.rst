===================
Navigating the tree
===================

See :doc:`../how-to/running` to learn how to get Launchpad's code and set up
a local development environment.

The Launchpad tree is big, messy and changing.  Sorry about that.  Don't panic
though!  Keep a firm grip on ``grep`` and pay attention to
these important top-level folders:

``bin/``, ``utilities/``
    Where you will find scripts intended for developers and admins.  There's
    no rhyme or reason to what goes in bin/ and what goes in utilities/, so
    take a look in both.

``configs/``
    Configuration files for various kinds of Launchpad instances.
    ``development`` and ``testrunner`` are of particular interest to developers.

``cronscripts/``
    Scripts that are run on actual production instances of Launchpad as
    cron jobs.

``daemons/``
    Entry points for various daemons that form part of Launchpad.

``database/``
    Our database schema, our sample data, and other things related to those.

``doc/``
    General system-wide documentation. You can also find documentation on
    the `developer wiki <https://dev.launchpad.net/>`_, in docstrings, and
    in doctests.

``lib/``
    Where the vast majority of the code lives, along with our templates,
    tests, and the bits of our documentation that are written as doctests.
    ``lp`` is the most interesting package, with ``canonical`` containing
    some things like images and style sheets.  To learn more about how the
    ``lp`` package is laid out, take a look at its docstring.

``Makefile``
    The ``Makefile`` has all sorts of goodies.  If you spend any length of
    time hacking on Launchpad, you'll use it often.  The most important
    targets are ``make clean``, ``make compile``, ``make schema``, ``make
    run`` and ``make run_all``.

``scripts/``
    Scripts that are run on actual production instances of Launchpad,
    generally triggered by some automatic process.


You can spend years hacking on Launchpad full-time and not know what all of
the files in the top-level directory are for.  However, here's a guide to some
of the ones that come up from time to time.

``brzplugins/``
    Breezy plugins used in running Launchpad.

``zcml/``
    Various configuration files for the Zope services.

Can I look at the code without downloading it all?
==================================================

Yes, you can browse the `source code
<https://git.launchpad.net/launchpad/tree>`_ on Launchpad.  You can also use
``git clone https://git.launchpad.net/launchpad`` to download the code
without setting up a development environment.
