.. meta::
   :description: How Personal Package Archives differ from the official
      Ubuntu archive.

.. _ppa-vs-ubuntu-archive:

PPAs and the Ubuntu archive
===========================


A PPA shares the *infrastructure* of the Ubuntu primary archive — the
same package tools, the same distribution mechanics, the same Debian
pool layout — but it is a separate publication system. Packages
uploaded to a PPA never appear in the Ubuntu archive automatically,
and packages in the Ubuntu archive are not mirrored into PPAs. The two
flows are independent.

The Ubuntu archive is curated: every upload is reviewed by archive
administrators against security, licensing, and quality criteria, and
the archive as a whole is maintained for the lifetime of each Ubuntu
release. A PPA is curated only by its owner.

Why the layouts look familiar
-----------------------------

The deliberate decision to mirror the Ubuntu archive's tools and
conventions reduces the learning curve for developers who are already
familiar with Ubuntu or Debian packaging. The same ``dput``, ``dpkg``,
and source-package workflow that targets the Ubuntu archive also
targets PPAs.

Multi-release publishing
------------------------

PPAs use the standard ``debian pool`` layout. Source and binary files
live in name-based pool locations, and any number of per-series
indexes (``dists``) can reference the same files. As a result, a
single uploaded source revision can be *published* into multiple
Ubuntu series through a copy operation, rather than re-uploaded once
per series. See :ref:`building-a-source-package` for the per-series
version-naming pattern and :ref:`copying-packages` for the copy
operation itself.
