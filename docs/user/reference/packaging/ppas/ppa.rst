.. meta::
   :description: Personal Package Archive reference - supported series
      and architectures, quotas, retention, and signing key facts.

.. _personal-package-archive:

Personal Package Archive
========================

A Personal Package Archive (PPA) is a per-user or per-team apt
repository hosted by Launchpad, built from uploaded source packages.

For conceptual background, see :ref:`ppa-overview`. For procedures, see
the :ref:`packaging-how-to` guides.

.. _ppa-series:

Supported series
----------------

Each distribution on Launchpad publishes its supported series at
``https://launchpad.net/<distribution>/+ppas``. For Ubuntu, the most
common case, this is https://launchpad.net/ubuntu/+ppas. The target
series is read from the ``Distribution`` field in the source package's
``debian/changelog`` file. An unknown or unsupported value causes the
upload to be rejected.

.. _ppa-architectures:

Supported architectures
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Architecture
     - Built by default
   * - ``amd64``
     - yes
   * - ``amd64v3``
     - no
   * - ``arm64``
     - no
   * - ``armel``
     - no
   * - ``armhf``
     - no
   * - ``i386``
     - no
   * - ``ppc64el``
     - no
   * - ``riscv64``
     - no
   * - ``s390x``
     - no

Enabling an architecture affects new uploads only. To produce builds
for an already-published source on a newly-enabled architecture, see
:ref:`request-ppa-architectures` and :ref:`copying-packages`.

See https://launchpad.net/builders/ for the live list.

.. _ppa-quotas:

Quotas and limits
-----------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Resource
     - Limit
   * - Disk space
     - 8 GiB; larger quotas considered on request at
       https://answers.launchpad.net/launchpad
   * - Data transfer
     - No fixed cap; unusual volumes may trigger contact from Launchpad
   * - PPAs per owner
     - One or more per user or team; each has its own URL
   * - Visibility
     - Public by default; private PPAs available with Canonical
       approval (see :ref:`consumer-hosting`)
   * - Uploadable artefacts
     - Source packages only; pre-built binary uploads are rejected
   * - Package formats
     - ``.deb`` only

Eligibility and acceptable-use terms are described in
:ref:`project-eligibility`.

.. _ppa-retention:

Package retention
-----------------

A published package remains available until one of the following
occurs:

- the owner removes it, or
- a later upload supersedes it.

Removal is not immediate on disk; see :ref:`package-deletion` for the
cleanup schedule.

.. _ppa-signing-key:

Signing key
-----------

Launchpad generates a unique GPG key for each owner's default PPA and
reuses it for every PPA owned by the same user or team. The key and
the command required to trust it are shown on the PPA's overview page.
Key generation happens after the first upload and may take a few hours
to propagate to the keyservers.
