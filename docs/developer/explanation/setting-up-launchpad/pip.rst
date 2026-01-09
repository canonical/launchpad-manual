Launchpad pip integration
*************************

Launchpad uses the pip_ build system for managing Python packages.

We have at least two other ways of managing dependencies.  Apt
manages our Python language installation, as well as many of our
non-Python system-level dependencies, such as PostgreSQL.  The
sourcecode directory is our other way of managing dependencies.  It is
supposed to only contain dependencies that are not standard Python
packages.  bzr plugins and JavaScript libraries are existing examples.

All developers will at least want to read the very brief sections about the
`Set Up`_ and the `Everyday Usage`_.

Developers who manage source dependencies probably should read the general
information about `Managing Dependencies and Scripts`_, but will also find
detailed instructions to `Add a Package`_, to `Upgrade a Package`_, to `Add a
Script`_, and to `Work with Unreleased or Forked Packages`_.

.. _pip: https://pip.pypa.io/

======
Set Up
======

If you use the ``rocketfuel-get`` script, run that, and you will be done.

If you don't, you have just a bit more initial set up.  I'll assume you
maintain a pattern similar to what the ``rocketfuel-*`` scripts use: you have a
local, pristine branch of trunk from which you make your other branches.  You
manually update the trunk and rsync sourcecode when necessary.  When you make
a branch, you use ``utilities/link-external-sourcecode``.

Developers that take this approach should do the following, where ``trunk`` is
the trunk branch from which you make local branches.

::

    git clone --depth=1 lp:lp-source-dependencies download-cache

Then run ``make`` in the trunk.

See the `Everyday Usage: Manual`_ section for further instructions on how to
work without the ``rocketfuel-*`` scripts.

.. _`Everyday Usage: Manual`: Manual_

==============
Everyday Usage
==============

``rocketfuel`` Scripts
======================

If you typically use ``rocketfuel-get``, and you don't change source
dependencies, then you don't need to know any more.  Switching between
ordinary git branches will do the right thing; if you're using worktrees,
then you can use ``link-external-dependencies``.

Manual
======

If you don't use the rocketfuel scripts, you will still use
``link-external-dependencies`` as before.  When ``pip`` complains that it
cannot find a version of a dependency, do the following, from within the
branch::

    git -C download-cache pull

After this, retry your ``make``.

That's it for everyday usage.

=================================
Managing Dependencies and Scripts
=================================

What if you need to change or add dependencies or scripts?  As you might
expect, you need to know a bit more about what's going on, although we can
still keep this at a fairly high level.

First let's talk a little about the anatomy of what we have set up.  To be
clear, much of this is based on our own decisions of what to do.  If you see
something problematic, bring it up with other Launchpad developers.  Maybe
together we can come up with another approach that meets our needs better.

These are the items in or near the top-level Launchpad directory associated
with pip:

``setup.py``, ``setup.cfg``
    These are the files that use ``distutils``, extended by ``setuptools``,
    to specify direct dependencies, scripts, and other elements of the local
    source tree.

    pip uses them, but the reverse is not true: ``setup.py`` and
    ``setup.cfg`` do not know about pip.

    Describing these files in full is well beyond the scope of this
    document.  We will give recipes for modifying them for certain tasks
    below. For more information beyond these recipes, see the setuptools and
    distutils documentation.

``requirements/ztk-versions.cfg``
    This is a copy of the dependency versions file published by the `Zope
    Toolkit`_.  It is preprocessed into a pip-compatible form by
    ``utilities/make-requirements.py``.

``requirements/setup.txt``
    This is a `requirements file`_ used to upgrade pip itself to a
    reasonably recent version and install a few other packages that must be
    installed before installing anything else.  We use this so that we
    aren't confined to features of pip supported by the version supplied by
    the operating system.

``requirements/launchpad.txt``
    This is a `constraints file`_ that specifies the precise versions of the
    dependencies we use, in addition to those specified in
    ``requirements/ztk-versions.cfg`` and ``requirements/setup.txt``.  This
    means that we can have several versions of a dependency available
    locally, but we only build the precise one we specify.  We give an
    example of its use below.

``env``
    The ``env`` directory holds a virtualenv built from the downloaded
    distributions.  You have one of these per branch (virtualenvs do not
    relocate especially well).  This directory is local to your system--we
    do not manage it in a branch.

``download-cache``
    The ``download-cache`` directory is a set of downloaded distributions--that
    is, exact copies of the items that would typically be obtained from the
    Python Package Index ("PyPI"), or another download source. We manage the
    download cache as a shared resource across all of our developers with a git
    branch in a Launchpad project called ``lp-source-dependencies``.

    We run pip with the ``--no-index`` and ``--find-links`` options, which
    cause it to *not* use network access to find packages, but *only* look
    in the download cache.  This has many advantages.

    - First, it helps us keep our deployment boxes from needing network access
      out to PyPI and other download sites.

    - Second, it makes the build much faster, because it does not have to
      look out on the net for every dependency.

    - Third, it makes the build more repeatable, because we are more
      insulated from outages at download sites such as PyPI, and poor
      release management.

    - Fourth, it makes our deployments more auditable, because we can tell
      exactly what we are deploying.

    - Fifth, it gives us a single obvious place to put custom package
      distributions, as we'll discuss below.

    The downside is that adding and upgrading packages takes a small additional
    step, as we'll see below.

In addition to these directory entries, after you have run the Makefile, you
will see an additional entry:

``bin``
    The ``bin`` directory has already been discussed many times.  After
    running the build, it also holds many executables, including scripts to
    test Launchpad; to run it; to run Python or IPython with Launchpad's
    sourcetree and dependencies available; to run harness or iharness (with
    IPython) with the sourcetree, dependencies, and database connections; or
    to perform several other tasks.  For now, the Makefile provides aliases
    for many of these.

Now that you have an introduction to the pertinent files and directories,
we'll move on to trying to perform maintenance tasks.  We'll discuss adding
a dependency, upgrading a dependency, adding a script, adding an arbitrary
file, and working with unreleased packages.

.. _`Zope Toolkit`: https://github.com/zopefoundation/zopetoolkit
.. _`requirements file`: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _`constraints file`: https://pip.pypa.io/en/stable/reference/requirement-specifiers/

Add a Package
=============

Let's suppose that we want to add the "lazr.foo" package as a dependency.

1.  Add the new package to the ``setup.cfg`` file in the
    ``install_requires`` list under ``[options]``.

    Generally, our policy is to only set minimum version numbers in this
    file, or none at all.  It doesn't really matter for an application like
    Launchpad, but it's a good rule for library packages, so we follow it
    for consistency.  Therefore, we might simply add ``'lazr.foo'`` to
    install_requires, or ``'lazr.foo>=1.1'`` if we know that we are
    depending on features introduced in version 1.1 of lazr.foo.

2.  [OPTIONAL] Add the desired package to the ``download-cache/dist``
    directory.

    You should only need to do this if the package is one that doesn't exist
    on PyPI at all (which should be unusual).  Otherwise, it's less
    error-prone to fetch the desired package from PyPI along with any new
    dependencies it may have.

3.  Run the following command (or your variation):

    .. code-block:: shell

        bin/pip install --no-binary :all: lazr.foo

    This will either produce some errors which you'll need to fix, or it
    will succeed and finish with a line such as this:

    .. code-block:: shell

        Successfully installed lazr-foo-1.1.2 z3c.shazam-2.0.1 zope.bar-3.6.1

    You can use `requirements specifiers`_ on this command line, so, for
    instance, if you already know you want lazr.foo 1.1.2, you might run
    this command instead::

        bin/pip install --no-binary :all: lazr.foo==1.1.2

4.  Add the successfully-installed packages to the shared download cache for
    future use.

    .. code-block:: shell

        bin/pip download -d download-cache/dist/ --no-deps \
          --no-binary :all: ...

    You'll need to copy the list of packages from the "Successfully
    installed" line above, replacing the ``-`` immediately before each
    version number with ``==`` to turn each package/version pair into a
    requirements specifier.  So, in the case above, you would run:

    .. code-block:: shell

        bin/pip download -d download-cache/dist/ --no-deps \
          --no-binary :all: \
          lazr-foo==1.1.2 z3c.shazam==2.0.1 zope.bar==3.6.1

    This will normally be able to fetch package files that were saved to
    your ``pip`` cache directory (``~/.cache/pip/`` by default) by ``pip
    install``, so it shouldn't need to download them from PyPI again.

    We use ``--no-deps`` here because ``pip install`` has already done the
    hard work of resolving dependencies and told us the result, and because
    ``pip download`` doesn't consider what's currently installed and so is
    liable to download too much otherwise.

5.  Add the new versions to ``requirements/launchpad.txt``, still using the
    requirements specifier syntax:

    .. code-block:: shell

        lazr.foo==1.1.2
        z3c.shazam==2.0.1
        zope.bar==3.6.1

6.  Run ``make``.  If it breaks, go back to step 3.

7.  Test.

8.  Check old versions in the download-cache.  If you are sure that
    they are not in use any more, *anywhere*, then remove them to save
    checkout space.  More explicitly, check with the LOSAs to see if
    they are in use in production and :ref:`contact the Launchpad team<get-help>` 
    before deleting anything if you are unsure.  A rule of thumb is that it's 
    worth starting this investigation if the replacement has already been in 
    use by the Launchpad tree for more than a month. You can approximate this
    information by using ``git log`` on the newer (replacement)
    download-cache/dist file for the particular package.

9.  Now you need to share your package changes with the rest of the
    team.  You must do this before submitting your Launchpad branch to
    PQM or else your branch will not build properly anywhere else,
    including buildbot.  Commit the changes (``cd download-cache``,
    git add the needed files, ``git pull``, ``git commit -m 'Add
    lazr.foo 1.1.2 and dependencies'``) to the shared download cache
    when you are sure it is what you want.

*Never* modify a package in the download-cache.  A change in code must mean a
change in version number, or else very bad inconsistencies and
confusion across build environments will happen.

.. _`requirements specifiers`: https://pip.pypa.io/en/stable/reference/requirement-specifiers/

.. _upgrade-package:

Upgrade a Package
=================

Sometimes you need to upgrade a dependency.  This may require additional
dependency additions or upgrades.  In general, this works just like adding a
new package, so follow the `Add a Package`_ instructions above.

If you know what version you want, specify it explicitly on the ``pip
install`` line.

If you don't know what version you want, but just want to see what happens
when you upgrade to the most recent version, then omit the version and
specify the ``--upgrade`` option to ``pip install``.  Note that, when not
given an explicit version number, pip prefers final releases over alpha and
beta releases.  If you want to temporarily override this behaviour, use the
``--pre`` option to ``pip``.

Add a Script
============

We often need scripts that are run in a certain environment defined by Python
dependencies, and sometimes even different Python executables.  Several of the
scripts we have are specified using setuptools.

For the common case, in ``setup.cfg``, add a string in the
``console_scripts`` list under ``[options.entry_points]``. Here's an example
string::

    'run = lp.scripts.runlaunchpad:start_launchpad'

This will create a script named ``run`` in the ``bin`` directory that calls the
``start_launchpad`` function in the
``lp.scripts.runlaunchpad`` module.

Work with Unreleased or Forked Packages
=======================================

Sometimes you need to work with unreleased or forked packages.  Hopefully,
these situations will be rare, but they do occur.

At the moment, our solution is to use the download-cache.  Basically, make a
custom source distribution with a unique suffix in the name, and use it (and
its version name) for the normal process of adding or updating a package, as
described above.  Because the custom package is in the download-cache, it
will be found and used.

In general, the suffix should comply with `PEP 440`_; in the case of a
forked package, you should use ``lp`` as a local version identifier.  For
example, you might start by appending ``+lp1``, followed by ``+lp2`` and so
on for further revisions.

.. _`PEP 440`: https://www.python.org/dev/peps/pep-0440/

Developing a Dependent Library In Parallel
==========================================

Sometimes you need to iterate on change to a library used by Launchpad that
is managed by pip.  You could just edit what is in the ``env`` directory,
but it is harder to produce a patch while doing this.  You could instead
grab a branch of the library and produce an sdist every time you make a
change and make pip use the new sdist, but this is slow.

Instead, we can use "editable mode" so that changes are picked up instantly
without us having to create a distribution.  For example:

        bin/pip install -e /path/to/branch

Now any changes you make in that path will be picked up, and you are free
to make the changes you need and test them in the Launchpad environment.

Once you are finished you can produce a distribution as above for inclusion
in to Launchpad, as well as sending your patch upstream.  At that point you
are free to revert the configuration to only develop Launchpad.  Make sure
to test with the final distribution before submitting your branch.

=====================
Possible Future Goals
=====================

- Use wheels.
- No longer use make.
- Get rid of the sourcecode directory.
