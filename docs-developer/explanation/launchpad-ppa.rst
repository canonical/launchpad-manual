The Launchpad PPA
=================

.. include:: ../includes/important_not_revised.rst

The Launchpad PPA (https://launchpad.net/~launchpad/+archive/ppa)
contains dependencies for running Launchpad.

Launchpad-specific packages
---------------------------

bzr-lpreview-body
~~~~~~~~~~~~~~~~~

This package contains the `lpreview_body
plugin <https://launchpad.net/lpreview-body>`__ for Bazaar. The
packaging can be found in lp:~launchpad/lpreview-body/packaging.

geoip-data-city-lite
~~~~~~~~~~~~~~~~~~~~

This package is a single data file, which upstream publishes updates to
monthly. Why haven't we updated it since 2008?

-  Because we are using it only for tests and updating too frequently
   may actually break some tests (we've seen it happen). It's no big
   deal if developers don't get the fully up-to-date geoIP DB.
   Production uses the proprietary geoIP DB instead. — Danilo
   (2010-01-21)

launchpad-dependencies
~~~~~~~~~~~~~~~~~~~~~~

The launchpad-dependencies source is managed in Bazaar branches at
https://code.launchpad.net/meta-lp-deps.

Policy/procedure for updates:

1. You will need bzr-builddeb and debhelper packages installed.
2. Edit debian/control to add or change the dependencies.
3. Set the DEBEMAIL and DEBFULLNAME environment variables. Your name and
   email address must match an identity in your GPG key exactly. You may
   want to put this in your shell rc file so you don't have to set it
   manually every time.
4. Run 'debchange -i' in the root to increment the version number and
   add a changelog entry in the correct format. Remember that
   launchpad-dependencies should not have an ubuntu1 suffix on its
   version number, so if debchange -i adds that for you, take it out
   again and increment the unsuffixed version number instead.
5. debcommit or bzr commit
6. Exercise personal judgement on whether your change merits a merge
   proposal, or is sufficiently trivial to just be committed directly.
7. If preparing a merge proposal, please ensure your branch for review
   contains a complete debian/changelog entry ready for release.
8. Go to the trunk (or older distro) branch and merge / commit or pull
   changes ready to build.

9. Test-build your package:

   ::

       bzr builddeb

10. Since the package has a `Launchpad build recipe <https://code.launchpad.net/~launchpad/+recipe/meta-lp-deps-on-demand>`__,
    you only need to push the branch to Launchpad:

    ::

        bzr push lp:meta-lp-deps

launchpad-buildd
~~~~~~~~~~~~~~~~

This is from https://launchpad.net/launchpad-buildd.

python-lpbuildd is used by the test suite, so is part of
launchpad-developer-dependencies. launchpad-buildd itself runs an actual
buildd and is only needed on slaves.

`The package is built daily or on request by a
recipe <https://code.launchpad.net/~launchpad/+recipe/launchpad-buildd-daily>`__

lpsetup
~~~~~~~

?? (probably only used by parallel buildbot slaves, which are probably
using the puppet fork anyway)

mmm-archive-manager
~~~~~~~~~~~~~~~~~~~

??

Backported or patched Ubuntu packages
-------------------------------------

postgresql-10, postgresql-common, postgresql-debversion, slony1-2 (Trusty, Xenial)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Straight backports of PostgreSQL 10 and paraphernalia from Bionic to
Trusty. Bionic's version is fine.

pgbouncer (Trusty)
~~~~~~~~~~~~~~~~~~

Trusty's pgbouncer with wgrant's ENABLE/DISABLE patch as required by
full-update.py. For the benefit of launchpad-dependencies, the patched
package additionally Provides pgbouncer-with-disconnect.

The ENABLE/DISABLE patch is included upstream in pgbouncer 1.6, so
Xenial's version is fine.

libgit2, git (Bionic)
~~~~~~~~~~~~~~~~~~~~~

Various updates backported from Focal for use on git.launchpad.net.

convoy
~~~~~~

`Daily builds of lp:convoy with custom
packaging <https://code.launchpad.net/~launchpad/+recipe/launchpad-convoy>`__.
The packaging is based on
`Landscape's <https://code.launchpad.net/~landscape/+recipe/convoy-daily-trunk-lds>`__,
but modified to install Launchpad's convoy.wsgi. Ubuntu's modern
packaging uses dh-python and supports Python 3.

debian-archive-keyring (Xenial, Bionic, Focal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Straight backport for new Debian archive keys for gina's mirror.
hirsute's version is fine.

git-build-recipe
~~~~~~~~~~~~~~~~

`Daily builds of
lp:git-build-recipe <https://code.launchpad.net/~launchpad/+recipe/git-build-recipe-daily>`__
for builds.

Distro series support
---------------------

Stable
~~~~~~

-  Trusty (obsolete production LTS, still used by databases)
-  Xenial (current production LTS)
-  Bionic (next production LTS)

In progress
~~~~~~~~~~~

-  Focal (next, next production LTS?)

When the supported series change, remember to also update
:doc:`../how-to/getting` and :doc:`../how-to/running`.
