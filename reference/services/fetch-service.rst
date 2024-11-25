Fetch service
=============

Short description
-----------------
A proxy that can be used by Launchpad builders as an alternative to the squid
proxy. When used, it keeps track of requests and dependencies for the build.

Detailed description
--------------------
The fetch service is a proxy service used by Launchpad builders (see
:doc:`Build Farm <build-farm>`) that keeps track of dependencies downloaded
during a build. This ensures developers have a trustworthy record of all the
parts that make up the software being built.

The service contains a set of APIs endpoints that can be distinguished into
two groups:

* Control endpoints (default port ``9999``): used by Launchpad to manage the
  fetch service sessions

* Proxy endpoints (default port ``9988``): used within the builder to access
  external resources

The life-cycle of a fetch-service session within Launchpad goes as follows:

1. Launchpad (specifically,
   `launchpad-buildd-manager <https://git.launchpad.net/~launchpad/launchpad/tree/charm/launchpad-buildd-manager>`_)
   makes a request to the fetch service control endpoint for the creation of
   a fetch service session, which returns a ``session ID`` and a ``token``.
   Launchpad sends those details to 
   `launchpad buildd <https://git.launchpad.net/~launchpad/launchpad-buildd>`_
   to be used during the build.

2. During a build, any external requests go through the fetch service proxy
   endpoint, using the specific ``session ID`` and ``token``. The fetch
   service keeps track of all requests made during the build to that given
   ``session ID``.

3. After the pull-phase or at the end of the build (depending on the
   configuration of the snap itself within Launchpad), `launchpad-buildd`
   makes a request to the fetch service control endpoint to revoke the
   ``token``, meaning no new external requests can be made during that build.

4. After the end of the build, when Launchpad gathers the resulting artifacts,
   Launchpad makes a request to the fetch service control endpoint to gather
   the metadata from the session (i.e., a file that contains all the requests
   and dependencies fetched during the build) for the specified ``session ID``.

5. Launchpad makes a final request to the fetch service control endpoint to
   end session ``session ID``, which deletes all data for that session that
   was stored in the fetch service database.

Using the fetch service
~~~~~~~~~~~~~~~~~~~~~~~
Currently, the fetch service can only be used for building snaps, rocks and
source packages.

To do so, a Launchpad admin is required to set the
``use_fetch_service`` flag for the recipe to ``true``, either in the API or in
the UI by accessing the admin area. The UI option may not be available for all
build types the fetch service supports.

The fetch service can be run in two modes, "strict" and "permissive", where it
defaults to the former on production. The "strict" mode only allows certain
resources and formats, and errors out in any case the restrictions are
violated. The "permissive" mode works similar, but only logs a warning when
encountering any violations.

The mode can be configured using the ``fetch_service_policy`` option via API,
with the currently two possible values ``permissive`` and ``strict``.

Requests to use the fetch service shall be made to the Launchpad team through
the usual channels (by
`opening a question <https://answers.launchpad.net/launchpad>`_, or emailing
the team at feedback@launchpad.net).

Fetch service maintainers
~~~~~~~~~~~~~~~~~~~~~~~~~
The fetch service code itself is not maintained by Launchpad - it is
maintained by Canonical's Starcraft team. Nonetheless, the service was created
to be used by Launchpad builders, and that's currently its purpose.

Launchpad maintains its mojo specs and deployment to its environments.

Documentation
-------------
* `Snap docs <https://github.com/canonical/fetch-service/tree/main/docs>`_

Git repositories
----------------
* `Fetch service snap <https://github.com/canonical/fetch-service>`_
* `Fetch service charm <https://github.com/canonical/fetch-operator>`_
* `lp-fetch-service Mojo spec <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/tree/lp-fetch-service>`_

The following repositories also contain code relevant to how Launchpad uses
the fetch service:

* `buildd <https://git.launchpad.net/~launchpad/launchpad-buildd>`_
* `launchpad-buildd-manager <https://git.launchpad.net/~launchpad/launchpad/tree/charm/launchpad-buildd-manager>`_

Bug trackers
------------
* `Fetch service snap GitHub issues <https://github.com/canonical/fetch-service/issues>`_
* `Fetch service charm GitHub issues <https://github.com/canonical/fetch-operator/issues>`_
* `Launchpad buildd bug tracker <https://bugs.launchpad.net/launchpad-buildd>`_

Deployment
----------
We deploy the fetch service using the specs defined in
`fetch service mojo specs <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/+ref/master>`_.

In order to be able to evaluate new fetch service versions, we use different
Snap channels for qastaging and production, so we are able to
test new releases. This information is both defined in above mentioned mojo
specs, and in `ST118 fetch service release process <https://docs.google.com/document/d/1HZvFo78LqFGgdpM7v3teG9gV-pMyvXpXTD1vcLLv_d0/>`_.

Qastaging
~~~~~~~~~
For qastaging deployment, SSH into
``stg-lp-fetch-service-qastaging@launchpad-bastion-ps5``, and run
``upgrade-qastaging``.

Production
~~~~~~~~~~
For production deployment, SSH into
``stg-lp-fetch-service@launchpad-bastion-ps5``, and run
``upgrade-production``.


Related specifications (only accessible for Canonical employees)
----------------------------------------------------------------
* `LP136 - Integrating the fetch service for snap builds <https://docs.google.com/document/d/1Z2kVh8eGzDV1-zEyTRYbCNQ0fsXJWt9-vutAjZ9Cxck>`_
* `ST108 - Fetch service control API <https://docs.google.com/document/d/1Ta0THOsHLwbOA6H7ewHa-6s2GtZRWxvvtiMKFk5jiq8>`_

Log files
---------
See `FreshLogs documentation <https://wiki.canonical.com/Launchpad/FreshLogs>`_.

Production
~~~~~~~~~~

* ``rless fetch-service.lp.internal::fetch-service-logs/fetch-service.log``

Qastaging
~~~~~~~~~

* ``rless fetch-service.qastaging.lp.internal::fetch-service-logs/fetch-service.log``

Alternatively, to access the fetch-service internal logs, one needs to:

1. SSH into Launchpad's bastion and switch to the following user: 
   ``stg-lp-fetch-service-qastaging@launchpad-bastion-ps5``.

2. SSH into the fetch-service juju unit by running
   ``juju ssh fetch-service/leader``.

3. Run ``sudo snap logs fetch-service -n 100 -f`` (where ``-n`` sets the number
   of log lines, and ``-f`` keeps up the latest logs up-to-date).

You can also check the logs in the following directory:
``/var/snap/fetch-service/current``.

Monitoring
----------
Not set up.

Common support cases
--------------------
The fetch service is not currently widely used. As such, there haven't been a
lot of support requests made.

More information
----------------
None.
