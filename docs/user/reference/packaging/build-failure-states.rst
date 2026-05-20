.. meta::
   :description: States in which a Launchpad build may halt or fail,
      their meaning, and how to resolve them.

.. _build-failure-states:

Build failure states
====================

A Launchpad build may halt or fail with one of the following states.

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - State
     - Meaning
     - Resolution
   * - ``failed-to-build``
     - The source or its metadata is broken
     - Read the build log; upload a fix
   * - ``dep-wait``
     - A build-time dependency is unavailable
     - Auto-retried when dependencies become available; otherwise
       correct the dependency list and re-upload
   * - ``chroot-wait``
     - Build chroot unavailable (infrastructure failure)
     - Report to the :ref:`Launchpad team <get-help>`
   * - ``builder-failure``
     - Build host failure (infrastructure failure)
     - Report to the :ref:`Launchpad team <get-help>`
   * - ``failed-to-upload``
     - Built artefacts cannot be published (for example, duplicates)
     - Re-upload a corrected source
