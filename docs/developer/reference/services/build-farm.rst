Build farm
==========

Short description
-----------------
Builds and tests software for Ubuntu and related systems.

Detailed description
--------------------
The build farm builds packages, such as debs, snaps, charms, and other
formats for Ubuntu in a secure and isolated way.

The build farm consists of a manager, a proxy for outbound communication,
and various builder regions.
Build jobs are created by other parts of Launchpad, such as a change to a
git repository resulting in snap recipe builds.
They are then scheduled onto builders as virtual machines by
``buildd-manager``.

``buildd-manager`` continuously monitors all builders in the farm, and when
a builder is idle it chooses the next highest priority job for dispatch to
the idle builder.
It does this by using XML-RPC, passing relevant data to the builder, which
in turn fetches all ingredients for executing the build.
When a build has completed, ``buildd-manager`` gathers the resulting files
and injects them into Launchpad via an upload queue processor, and then the
builder is reset to a baseline state.

The manner in which a build is executed is determined by the build type.
This typically involves invoking some external tools; ``sbuild`` for Ubuntu
package builds, ``snapcraft`` for snap builds, etc.

Builders do not have direct access to the Internet, but rather need to
acquire an authentication token to be able to access a restricted set of
URLs on the Internet via a proxy. This can either be a squid proxy or the
:doc:`fetch service <fetch-service>`, determined by a ``use_fetch_service``
flag. Currently, the fetch service can only be used for building snaps, charms,
rocks and sourcecraft packages.

Builder regions are physically co-located and consist of machines of the
same architecture family.
Builder regions comprise per-architecture image builders, and each physical
location contains a ``launchpad-vbuilder-manage`` instance which handles
resets for all architectures within that location.

Each builder region maintains clean VM images for its builders; these are
built using ``glance-simplestreams-sync``, which automatically and
periodically copies standard pre-built images from
``cloud-images.ubuntu.com``, and ``launchpad-buildd-image-modifier``, which
hooks into ``glance-simplestreams-sync`` to produce modified images with
``launchpad-buildd`` installed.

Documentation
-------------
* `Documentation for launchpad-buildd <https://launchpad-buildd.readthedocs.io/en/latest/index.html>`_
* `Documentation for the Launchpad CI runner <https://lpci.readthedocs.io/en/latest/>`_
* :ref:`Documentation for Launchpad CI <continuous-integration>`

Git repositories
----------------
* `buildd-manager <https://git.launchpad.net/launchpad/tree/lib/lp/buildmaster/>`_
* `launchpad-buildd <https://git.launchpad.net/launchpad-buildd>`_
* `Launchpad CI runner <https://git.launchpad.net/lpci>`_
* `glance-simplestreams-sync charm <https://git.launchpad.net/~launchpad/charm-glance-simplestreams-sync/tree/?h=scalingstack>`_
* `launchpad-buildd-image-modifier charm <https://git.launchpad.net/charm-launchpad-buildd-image-modifier>`_
* `launchpad-vbuilder-manage <https://git.launchpad.net/launchpad-vbuilder-manage>`_

Bug trackers
------------
* https://bugs.launchpad.net/launchpad-project/+bugs?field.tag=soyuz-build
* https://bugs.launchpad.net/launchpad-buildd
* https://bugs.launchpad.net/lpci
* https://bugs.launchpad.net/charm-glance-simplestreams-sync
* https://bugs.launchpad.net/charm-launchpad-buildd-image-modifier
* https://bugs.launchpad.net/launchpad-vbuilder-manage

Deployment
----------
* `Deployment of launchpad-buildd <https://launchpad-buildd.readthedocs.io/en/latest/how-to/deployment.html>`_
* `Production deployment notes for launchpad-buildd <https://launchpad-buildd.readthedocs.io/en/latest/explanation/deployment.html>`_
* `vbuilder Mojo spec <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/tree/vbuilder?h=vbuilder>`_
* `lp-builder-proxy Mojo spec <https://git.launchpad.net/launchpad-mojo-specs/tree/lp-builder-proxy/>`_
* `lp-fetch-service Mojo spec <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/tree/lp-fetch-service>`_

Related specifications (only accessible for Canonical employees)
----------------------------------------------------------------
`LP113: Threat model for builds <https://docs.google.com/document/d/1im8CMxLRNxtt5H0zv461kSYSflN-YlxJ1UZG8_53D9A>`_

Log files
---------
See `Reading Launchpad logs via rsync <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/reference/reading-launchpad-logs-via-rsync/>`_.

Production
~~~~~~~~~~

buildd-manager
^^^^^^^^^^^^^^

* ``rless buildd-manager.lp.internal::lp-logs/buildd-manager.log``
* ``rless buildd-manager.lp.internal::lp-logs/process-build-uploads.log``
* ``rless buildd-manager.lp.internal::lp-logs/buildd-retry-depwait.log``

vbuilder-manage
^^^^^^^^^^^^^^^

Builder reset logs.
Each celery worker has a different log file, named ``celery.ppareset-*.log``.

* ``rsync -v vbuilder-manage-lcy02.lp.internal::vbuilder-manage-logs/``
* ``rsync -v vbuilder-manage-bos01.lp.internal::vbuilder-manage-logs/``
* ``rsync -v vbuilder-manage-bos02.lp.internal::vbuilder-manage-logs/``
* ``rsync -v vbuilder-manage-bos03.lp.internal::vbuilder-manage-logs/``

builder-proxy (auth)
^^^^^^^^^^^^^^^^^^^^

* ``rless builder-proxy-auth.lp.internal::rutabaga-logs/rutabaga-access.log``
* ``rless builder-proxy-auth.lp.internal::rutabaga-logs/rutabaga-error.log``
* ``rless builder-proxy-auth.lp.internal::rutabaga-logs/rutabaga-purge.log``

builder-proxy (squid) 
^^^^^^^^^^^^^^^^^^^^^

* ``rless 10.131.48.38::squid-logs/access.log``
* ``rless 10.131.48.38::squid-logs/cache.log``
* ``rless 10.131.48.24::squid-logs/access.log``
* ``rless 10.131.48.24::squid-logs/cache.log``

fetch-service
^^^^^^^^^^^^^

See :doc:`Fetch Service <fetch-service>` logs section.


Staging
~~~~~~~

buildd-manager
^^^^^^^^^^^^^^

* ``rless 10.132.54.143::lp-logs/buildd-manager.log``
* ``rless 10.132.54.143::lp-logs/process-build-uploads.log``
* ``rless 10.132.54.143::lp-logs/buildd-retry-depwait.log``

builder-proxy (auth)
^^^^^^^^^^^^^^^^^^^^

* ``rless builder-proxy-auth.staging.lp.internal::rutabaga-logs/rutabaga-access.log``
* ``rless builder-proxy-auth.staging.lp.internal::rutabaga-logs/rutabaga-error.log``
* ``rless builder-proxy-auth.staging.lp.internal::rutabaga-logs/rutabaga-purge.log``

builder-proxy (squid) 
^^^^^^^^^^^^^^^^^^^^^

* ``rless 10.132.224.179::squid-logs/access.log``
* ``rless 10.132.224.179::squid-logs/cache.log``
* ``rless 10.132.224.16::squid-logs/access.log``
* ``rless 10.132.224.16::squid-logs/cache.log``

fetch-service
^^^^^^^^^^^^^

See :doc:`Fetch Service <fetch-service>` logs section.

Monitoring
----------
The "Build farm" section of the `Launchpad dash <https://grafana.admin.canonical.com/d/oIhMaXhMk/launchpad-dash>`_.

Search for "build" in https://git.launchpad.net/canonical-is-prometheus/tree/ols/launchpad.rules.

Common support cases
--------------------
See `Launchpad's playbook for support rotation <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/builder/>`_

More information
----------------

* `Live overview of Launchpad's build farm <https://launchpad.net/builders>`_
* `Launchpad services diagram <https://app.diagrams.net/?src=about#Uhttps%3A%2F%2Fgit.launchpad.net%2Flaunchpad%2Fplain%2Fdoc%2Fdiagrams%2Farchitecture.html#%7B%22pageId%22%3A%2214glVH8XSJX-2FxTRWny%22%7D>`_
