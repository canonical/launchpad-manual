.. meta::
   :description: Grant a specific Launchpad user permission to upload
      to a PPA without adding them to the owning team.

.. _manage-ppa-upload-permissions:

Grant upload permission to a non-team-member
============================================

Prerequisites
-------------

- A local checkout of ``ubuntu-archive-tools`` from
  https://code.launchpad.net/ubuntu-archive-tools.
- Owner privileges on the target PPA.

Steps
-----

From the root of the ``ubuntu-archive-tools`` checkout, run::

    ./edit-acl -A ppa:OWNER/DISTRO/ARCHIVE -p PERSON -c main -t upload add

Replace ``OWNER`` with the PPA owner, ``DISTRO`` with the distribution
the PPA belongs to (``ubuntu`` for Ubuntu PPAs), ``ARCHIVE`` with the
PPA name, and ``PERSON`` with the Launchpad ID of the user being
granted access. The named user can then upload to ``main`` in the
specified PPA.
