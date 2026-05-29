.. meta::
   :description: Conceptual overview of Personal Package Archives in
      Launchpad — what they are, how they fit into the Ubuntu
      toolchain, and the guarantees they offer.

.. _ppa-overview:

PPA overview
============


A Personal Package Archive (PPA) is a per-user or per-team apt
repository hosted by Launchpad. A developer uploads source packages,
Launchpad builds binary packages from them, and publishes both. End
users can add a PPA to their computer using ``add-apt-repository``.
Just as with the official Ubuntu archive, they can then install
packages from the PPA and receive updates.

Why PPAs exist
--------------

PPAs let independent developers and teams distribute software through
the same channels that Ubuntu uses for its own software, without
needing the package to be accepted into the Ubuntu archive. The model
trades off some of the assurances of the official archive (curation,
security review, archive-admin oversight) for a much lower barrier to
publication.

Trust and signing
-----------------

Each owner has a single signing key, generated on first upload and
reused across the owner's PPAs. Consumers can verify that a downloaded
package was built and signed by Launchpad on behalf of that owner.

This is the only trust signal a PPA provides; it is not a security or
quality review. PPA packages are standard Debian packages: they run
unsandboxed, execute maintainer scripts as root during installation,
and can install or replace any package on the system. Adding a PPA
therefore grants its owner the same level of trust as installing
software directly from that owner — consumers should add only PPAs
whose owners they trust.

Limits of the model
-------------------

- Source-only: pre-built binaries are not accepted; Launchpad performs
  every build itself.
- Free software only: see :ref:`project-eligibility`.
- Separate from Ubuntu: see :ref:`ppa-vs-ubuntu-archive`.

See :ref:`personal-package-archive` for supported series, architectures,
and quotas.
