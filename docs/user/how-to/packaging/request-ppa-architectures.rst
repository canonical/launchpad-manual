.. meta::
   :description: Enable additional build architectures for a Launchpad
      Personal Package Archive.

.. _request-ppa-architectures:

Enable additional build architectures for a PPA
===============================================

Steps
-----

1. From the PPA's page, open "Change details".
2. Tick the desired architectures. The full list of available
   architectures is at :ref:`ppa-architectures`.
3. Save.

New uploads are then built for the enabled architectures.

Building existing sources for new architectures
-----------------------------------------------

Enabling an architecture affects only new uploads; sources already
published in the PPA are not built for it. To build an
already-published source for a newly-enabled architecture, copy the
source within the PPA. Use the :ref:`copying-packages` workflow with
"This PPA" as the destination, "The same series", and "Copy existing
binaries". Launchpad then creates the missing builds, with no re-upload
needed.
