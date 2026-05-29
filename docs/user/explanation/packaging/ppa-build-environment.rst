.. meta::
   :description: The build environment used by Launchpad for Personal
      Package Archives, and what that implies for isolation and
      architecture coverage.

.. _ppa-build-environment:

The PPA build environment
=========================

Isolation
---------

Launchpad runs each PPA build inside an isolated cloud instance,
provisioned for that build alone. Each build starts in a clean chroot
and is torn down on completion. This guarantees two properties:

- Each build depends only on the source package and its declared
  build dependencies, with no carry-over from prior builds
- One developer's build cannot affect another's, accidentally or
  otherwise.

Implications for architecture coverage
--------------------------------------

The list of architectures a PPA can build for (see
:ref:`ppa-architectures`) is constrained by what the underlying build
cloud supports. Architecture availability can therefore change as the
build infrastructure evolves; the authoritative current list is at
https://launchpad.net/builders/.
