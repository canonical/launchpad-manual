.. _use-ppa-snapshot-service:

Use the PPA snapshot service
==============================

Similar to the `Ubuntu snapshot service <https://snapshot.ubuntu.com/>`_, you 
can use the PPA snapshot service to retrieve and install a package from a 
Personal Package Archive (PPA) as it was at a specific point in time. This is 
useful in scenarios such as:

* When you want to reproduce a deployed package as it was at some point in the past   
* When determining when something changed in an archive 

This feature has been available since 1st March 2023. No PPA has snapshots from
before this date.

Snapshot IDs
------------

Unlike regular PPAs, you need a snapshot ID to install a package from a PPA 
snapshot. A snapshot ID specifies the date and UTC time of the snapshot you 
would like to use. The ID is written in the format *YYYYMMDDTHHMMSSZ*. 

For example, the PPA snapshot ID for 1st January 2025 at midnight UTC will be 
20250101T000000Z. 

How to use PPA snapshots
------------------------

There are two methods of installing packages from PPA snapshots. You can change
a PPA's config file in ``sources.list.d`` to use a specific snapshot when any 
package is installed from that PPA, or you can use a ``--snapshot`` flag when 
installing a package to specify the snapshot it will be sourced from. 

In the examples below, we install a package from a snapshot of the checkbox PPA
(specifically the stable releases of the PPA).

Option 1: Define the snapshot in the PPA's configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetch the PPA repository::

    sudo add-apt-repository ppa:checkbox-dev/stable

Navigate to ``/etc/apt/sources.list.d`` and open the configuration file for the 
PPA, i.e., ``checkbox-dev-ubuntu-stable-noble.sources``.  Add a ``Snapshot`` 
field and enter the ID of the snapshot to be used when installing any package 
from this PPA:: 

    Types: deb
    URIs: https://ppa.launchpadcontent.net/checkbox-dev/stable/ubuntu/
    Suites: noble
    Components: main
    Signed-By:
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    ...
    ...
    -----END PGP PUBLIC KEY BLOCK-----
    Snapshot: 20250101T000000Z

Save your changes and update the package indexes::

    sudo apt update

One of the outputs should contain a URL with a ``snapshot`` sub-subdomain, e.g.,::

    Hit:6 https://snapshot.ppa.launchpadcontent.net/checkbox-dev/stable/ubuntu/20250101T000000Z noble InRelease

The next time you install a package from this PPA, it will be downloaded from 
the snapshot instead of the live archive.

Option 2: Use the ``--snapshot`` flag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also download a package from a snapshot directly without changing the 
configuration file. This gives you the flexibility of defining a snapshot at 
the time of installation. 

Fetch the PPA repository::

    sudo add-apt-repository ppa:checkbox-dev/stable

Install a package, e.g., checkbox-provider-base, directly from the snapshot 
using the ``--snapshot`` flag and the snapshot ID::

    sudo apt install checkbox-provider-base --update --snapshot 20250101T000000Z

.. note::
    Private PPAs require additional configuration when using the PPA snapshot service

Snapshot retention policy
-------------------------

Snapshots are enabled by default on all PPAs and a snapshot is created each 
time a publisher run finishes. 

By default, public PPA snapshots are retained for approximately two weeks. 
Reach out to the Launchpad team if you require a longer retention period. 
Private PPA snapshots have an indefinite retention period by default. 