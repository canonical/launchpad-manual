=================
Charm development
=================

The direction of our official deployments is to use `Juju charms
<https://juju.is/docs/sdk>`_.  (We still have a number of manually-deployed
systems, so we aren't there yet.)

To get an overview of how this works, you'll need to look in the ``charm/``
directory of Launchpad itself, as well as `ols-layers
<https://git.launchpad.net/ols-charm-deps>`_, `launchpad-layers
<https://git.launchpad.net/launchpad-layers>`_, and `launchpad-mojo-specs <https://git.launchpad.net/launchpad-mojo-specs>`_.  
Each of the subdirectories of ``charm/`` represents a single logical function 
which can be deployed as a Juju `application <https://documentation.ubuntu.com/juju/3.6/reference/application/>`_
with one or more `units <https://documentation.ubuntu.com/juju/3.6/reference/unit/>`_.  
The layers provide common code used by multiple charms.  The specs are used 
with `Mojo <https://mojo.canonical.com/>`_ to coordinate whole deployments of 
multiple applications; they contain configuration of individual applications 
and `integrations <https://documentation.ubuntu.com/juju/3.6/reference/relation/>`_ between applications.

Principles
==========

Wherever possible, charm code should live in the same repository as the code
it deploys (the payload).  This makes it easier to evolve both in parallel.

Launchpad is open source.  Its charms and its configuration (aside from a
small number of necessary secrets) should also be open source.  As well as
being the right thing to do, this also allows using machinery such as
Launchpad's charm recipes that upload to `Charmhub <https://charmhub.io/>`_.
When used in combination with Charmhub, Juju can easily be instructed to
upgrade charms and update configuration using a single `bundle
<https://documentation.ubuntu.com/juju/3.6/reference/bundle/>`_, allowing the 
top-level spec to be relatively simple.

Each charm should correspond to a deployment of a single top-level payload.
On the other hand, it's fine for a single payload to have multiple charms
corresponding to different ways in which it can be deployed: for example,
Launchpad itself will have charms for the appservers, buildd-manager,
publishers, and so on.

If a legacy deployment bundled multiple logical functions onto a single
machine purely for economic convenience, don't be afraid to split those up
in a way that makes sense.  However, there's no need to go to extremes: if
multiple cron jobs all have broadly the same system requirements, then we're
unlikely to want each cron job to be deployed using its own Juju
application.

It will not always make sense to expose every single configuration option of
the payload directly in the charm.  Some configuration options may only
exist for internal testing purposes or for backward-compatibility, and some
may make sense for the charm to use internally but not expose in ``juju
config``.  A good rule of thumb is to consider whether a given configuration
option needs to differ between deployments; if it doesn't, there's probably
no need to expose it.

`DRY <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_ applies to
configuration as well as code, and can help to avoid gratuitous differences
between deployments.  `Jinja <https://jinja.palletsprojects.com/>`_
templates are widely used in both charms and Mojo specs as part of this.

Keep multi-data centre operation in mind where possible.  We don't have
enough experience with this yet to know what we'll need to do, but it's
likely to involve deploying parts of an application in different data centres
from other parts, so loose coupling will help: for example, it may be useful
to allow configuring connections using explicit configuration as well as or
instead of Juju integrations.

Creating a Launchpad charm
--------------------------

If you don't already have a suitable testbed, then see the `Juju tutorial
<https://juju.is/docs/juju/tutorial>`_ for how to set one up;
you should use the non-Kubernetes approach here.

Assuming you have a suitable testbed to deploy charms with Juju, you can follow
these guidelines to build your charm for Launchpad:

.. note::

  These are just **optional guidelines** for developing charms specifically for
  Launchpad.
  
1. **Consider your application:** Think about what parts it entails and
   consider: what do you need to get your application running? Do you need a
   database, a celery worker, etc.? Does it makes sense to divide your
   application into multiple charms related to each other?

2. **Create your charm base:** Either create a charm from scratch or base it
   off existing ones. Without adding any code (i.e., the reactive code, within
   the ``/reactive`` folder) update ``layer.yaml``, ``charmcraft.yaml`` and 
   ``metadata.yaml``, to create your base. You can find more information about
   what each file is important for in the `reactive charms documentation
   <https://charmsreactive.readthedocs.io/en/latest/structure.html#charm-layer>`_.
   Note that the `charmcraft.yaml` file is not part of reactive charms, but
   it's an important file to be able to use ``charmcraft`` tools (e.g. 
   ``charmcraft pack`` for packing a charm). See 
   `here <https://juju.is/docs/sdk/charmcraft-yaml>`_ for information about the
   `charmcraft.yaml` file specifically. If you take a look at the ``parts``
   section of the existing Launchpad charms, you will see a few common ones
   used as a base to build your charm:

   * ``charm-wheels``: contains Python dependencies for ols-layers.

   * ``ols-layers``: contains common charm code used by both the Snap Store and
     Launchpad teams; it provides layers that deal with the way that we
     normally deploy simple web services, some common interfaces, and a few
     generic layers such as ``basic`` and ``apt``.

   * ``launchpad-layers``: contains common charm code specific to charms
     maintained by the Launchpad team. It deals with things like unpacking the
     Launchpad payload, configuring common relations, and setting up Launchpad
     configuration files.

3. **Write minimal code:** You can start by writing minimal reactive code
   that gets the source tree deployed (nothing too specialized).
   This should give you something you can build and deploy to a Juju model to
   test out. (Tip: have a look at ``charm/launchpad/`` charm. It can be used as
   a minimal skeleton that does nothing except deploy a Launchpad payload with
   some basic configuration).
   If your application doesn't publish artifacts that can be used by your charm
   to deploy the source code, have a look at
   :ref:`Create Jobs to Publish Artifacts <create_job_to_publish_artifacts>`.

4. **Add configurations:** Have a look at configurations related to your app
   in `lp-production-configs 
   <https://bazaar.launchpad.net/lp-production-config>`_ - what is common
   between environments and what changes. You should be able to create a config
   Jinja template in your charm ``/templates`` folder with all the base
   configurations, where the configuration that changes between environments
   should be variables.
   These variables should be set in the ``config.yaml`` file with reasonable
   default values (ideally, values that would allow a local deployment) - note
   that some config variables might already be set by other layers of your
   charm, if your charm is based on other layers. The actual values that will
   be running in each environment (production, staging, qastaging),
   should later be set in the ``lp/bundle.yaml`` file within the
   `launchpad-mojo-specs <https://git.launchpad.net/launchpad-mojo-specs>`_
   repo (you should only worry about these specs after your charm is ready).

5. **Write your reactive code:** Start adding code that it might need
   to configure and start your application. Setup any crontabs, logrotate...

6. **Test:** Test your new charm(s) deploys correctly with all its
   integrations, and your application is running. This can be challenging for
   some applications. See `Workflow` section below for some tips.

Workflow
========

You can run test deployments using `Juju <https://documentation.ubuntu.com/juju/3.6/howto/manage-your-deployment/>`_ 
and `LXD <https://documentation.ubuntu.com/lxd/en/latest/>`_.

Each Mojo spec has a ``README.md`` file explaining how to deploy it, and
that's usually the easiest way to get started.  You should normally use the
corresponding ``devel`` stage, as that's intended for local deployments: for
example, it will normally deploy fewer units, and doesn't assume that parts
of Canonical's internal infrastructure will be available.

Once you've successfully deployed an environment, you will probably want to
iterate on it in various ways.  You can build a new charm using ``charmcraft
pack`` in the appropriate subdirectory, and then use ``juju deploy`` to deploy
a new charm, or ``juju refresh`` to upgrade your local deployment to that.
You can change configuration items using ``juju config``.  Alternatively, you
can make a local clone of the Mojo spec and point ``mojo run`` at that rather
than at a repository on ``git.launchpad.net``, and then you can iterate by
changing the spec.

Use ``juju debug-log`` and ``juju status`` liberally to observe what's
happening as you make changes. You can also use ``juju ssh`` to ssh into your
deployed unit. to See `How to debug a charm
<https://juju.is/docs/sdk/debug-a-charm>`_ for more specific advice on that
topic.

Secrets
=======

Cryptographic secrets should not be stored in Mojo specs, and nor should
some other pieces of information (such as configuration relevant to
preventing spam).  These are instead stored in a secrets file on the
relevant deployment host (``launchpad-bastion-ps5.internal`` or
``is-bastion-ps5.internal`` for official deployments), and are updated
manually.  The ``bundle`` command in the Mojo manifest will have a
``local=`` parameter pointing to this file, relative to
``$MOJO_ROOT/LOCAL/$MOJO_PROJECT/$MOJO_STAGE``.

Managing secrets like this is more cumbersome than updating Mojo specs, so
try to keep it to a minimum.  In some cases there may be automation
available to help, such as the `autocert charm
<https://charmhub.io/autocert>`_.

Database roles
==============

PostgreSQL considers "users" and "roles" to be very nearly synonymous.  In
this section, "user" means specifically a role that has login credentials.

Launchpad uses lots of different database roles.  We used to deal with this
by having each user on each machine that runs Launchpad code have a
``.pgpass`` file with credentials for the particular set of users that it
needs, and then it would log in as those users directly.  However, this
approach doesn't work very well with Juju: the ``postgresql`` charm allows
related charms to request access to a single user (per interface), and they
can optionally request that that user be made a member of some other roles;
SQL sessions can then use ``SET ROLE`` to switch to a different role.

In our production, staging, and qastaging environments, we use a proxy charm
to provide charms with database credentials rather than relating them to
``postgresql`` directly (partly for historical reasons, and partly to avoid
complications when the database is deployed in a different region from some
of our applications).  As a result, we need to do some manual user
management in these environments.  On staging and qastaging, developers can
do this themselves when adding new charms to those existing deployment
environments.

Taking the librarian as an example: ``charm/launchpad-librarian/layer.yaml``
lists the ``binaryfile-expire``, ``librarian``, ``librarianfeedswift``, and
``librariangc`` roles as being required (this corresponds to the database
users used by the services and jobs installed by that particular charm).  To
create the corresponding user, we first generate a password (e.g. using
``pwgen 30 1``), then log into the management environment (``ssh -t
launchpad-bastion-ps5.internal sudo -iu stg-launchpad``), set up environment
variables for qastaging (``. .mojorc.qastaging``), run ``juju ssh
launchpad-admin/leader``, and run ``db-admin``.  In the resulting PostgreSQL
session, replacing ``<secret>`` with the generated password:

.. code-block:: psql

    CREATE ROLE "juju_launchpad-librarian"
    	WITH LOGIN PASSWORD '<secret>'
        IN ROLE "binaryfile-expire", "librarian", "librarianfeedswift", "librariangc";

The user name here should be ``juju_`` plus the name of the charm, since
that matches what the ``postgresql`` charm would create.

Having done that, we need to install the new credentials.  On
``stg-launchpad@launchpad-bastion-ps5.internal``, find the
``db_connections`` option under the ``external-services`` application, and
add an entry to
``~/.local/share/mojo/LOCAL/mojo-lp/lp/qastaging/deploy-secrets`` that looks
like this, again replacing ``<secret>`` with the generated password:

.. code-block:: yaml

    launchpad_qastaging_librarian:
      master: "postgresql://juju_launchpad-librarian:<secret>@database-ps5-1.qastaging.lp.internal:6432/launchpad_qastaging?connect_timeout=10"
      standbys: []

In the connection string URL, the database host, port, and name (in this
case, ``database-ps5-1.qastaging.lp.internal``, ``6432``, and
``launchpad_qastaging`` respectively) should match those of other entries in
``db_connections``.

The configuration for the ``pgbouncer`` connection pooler must also be
updated to match.  For now, take the relevant username/password pair from
the ``deploy-secrets`` file above; then, on each of the ``postgresql`` units
in ``stg-launchpad-db@launchpad-bastion-ps5.internal``, add this pair to
``/etc/pgbouncer/userlist.txt`` and run ``sudo systemctl reload
pgbouncer.service``.  In the near future this will be turned into a Mojo
spec.

Staging works similarly with the obvious substitutions of ``staging`` for
``qastaging``, and using
``stg-launchpad-db-qastaging@launchpad-bastion-ps5.internal``.

Production works similarly, except that IS needs to generate the user on the
production database, add it to the production ``pgbouncer`` by editing
``userlist.txt`` in ``prod-launchpad-db@is-bastion-ps5.internal`` and
pushing it out using Mojo, and update the secrets file found in
``~/.local/share/mojo/LOCAL/mojo-lp/lp/production/deploy-secrets`` on
``prod-launchpad@is-bastion-ps5.internal``.  Developers should request this
via RT, using this document to construct instructions for IS on what to do.

Finally, the corresponding application in `launchpad-mojo-specs
<https://git.launchpad.net/launchpad-mojo-specs>`_ needs to be configured
with the appropriate database name (``launchpad_qastaging_librarian`` in the
example above).  This normally looks something like this, where
``librarian_database_name`` is an option whose value is set depending on the
stage name:

.. code-block:: yaml

  launchpad-librarian:
    ...
    options: {{ base_options() }}
      databases: |
        db:
          name: "{{ librarian_database_name }}"
