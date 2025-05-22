Firewall
========

Overview
--------

There are 2 configuration locations for firewall rules:

- `launchpad-mojo-specs`_: Managed by the Launchpad team, this repository
  contains charm firewall rules.
- `canonical-is-firewalls`_: Managed by the IS team, this repository contains
  firewall rules that govern interactions between services.

.. _launchpad-mojo-specs: https://launchpad.net/launchpad-mojo-specs
.. _canonical-is-firewalls: https://launchpad.net/canonical-is-firewalls

Launchpad-mojo-specs
--------------------

This repository focuses on managing firewall rules between charms.

Structure
~~~~~~~~~

- ``lp/``, ``lp-*/``, ``ubuntu-mirrors/``:
  These directories hold environment-specific charm firewall rules in
  ``custom-secgroups-<environment>.yaml``

.. code::

   ├── lp
   │   ├── bundle.yaml
   │   ├── configs
   │   │   ├── custom-secgroups-production.yaml
   │   │   ├── custom-secgroups-qastaging.yaml
   │   │   └── custom-secgroups-staging.yaml
   │   ├── manifests
   │   │   ├── deploy
   │   │   ├── secgroups
   │   │   └── verify
   │   ├── utils -> ../utils
   │   ...

Rules
~~~~~

A ``custom-secgroups-<environment>.yaml`` file that holds rules looks like:

.. code:: yaml

   applications:
       codehosting-lb:
           type: neutron
           rules:
               - http
               - https
               ...
   rules:
       http:
           - {"protocol": "tcp", "family": "IPv4", "port": 80, "cidr": "0.0.0.0/0"}
           - {"protocol": "tcp", "family": "IPv6", "port": 80, "cidr": "::/0"}
       https:
           - {"protocol": "tcp", "family": "IPv4", "port": 443, "cidr": "0.0.0.0/0"}
           - {"protocol": "tcp", "family": "IPv6", "port": 443, "cidr": "::/0"}

Applying security groups: ``utils/custom-secgroups.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Read configuration files**: parses the YAML configuration files mentioned
   above.
#. **OpenStack Neutron environments**: the script communicates with the Neutron
   API to create and manage security groups.
#. **Non OpenStack Neutron environments**:

   a. **Generate iptables scripts**: using the Jinja2 template
      ``utils/templates/firewall.sh.j2``, it converts the configuration
      data into bash scripts that control iptables.

   #. **Configure Firewall service**: uses
      ``utils/templates/files/lp-firewall.service`` to set up the firewall
      service.

.. terminal::

   :input: ./utils/custom-secgroups.py --help

   Manage custom security groups on a Juju model.

   options:
     -h, --help
     --config-path CONFIG_PATH
             config file to load in addition to Mojo stage and default configs
     --dry-run
     --skip-stages SKIP_STAGES
     --local-networks LOCAL_NETWORKS
             space-separated CIDR addresses of networks to consider as local

Canonical-is-firewalls
----------------------
This repository focuses on managing firewall rules between services within the
Canonical ecosystem. You can find more info about how it works in
`IS-Firewalls User Documentation`_.

It contains four subdirectories - ``defs``, ``external``, ``rules`` and
``services``. Both ``services`` and ``rules`` are organised by team and
service.

.. _IS-Firewalls User Documentation: https://docs.admin.canonical.com/is-firewalls/mojo-is-firewalls/user/

Defs
~~~~

It contains host, port, route and subnet definitions for all of Canonical.

Services
~~~~~~~~

It defines the hosts and subnets associated with services. Hosts specified in a
service can be a reference to a host defined in ``defs/hosts.yaml`` or
specified as an IP address.

- ``services/lp/``: Defines frontend, backend, and content-cache machines for
  each Launchpad service and environment.

A service file inside ``services/lp/`` dir looks like:

.. code:: yaml

   launchpad:
     owner: lp
     hosts:
       frontends:
       - 185.125.189.222
       - juju/prodstack-is-ps5/admin/prod-launchpad/frontend-api/public
       - juju/prodstack-is-ps5/admin/prod-launchpad/frontend-main/public
       ...

Rules
~~~~~

It contains the rules which bring together all the other pieces to specify
the firewall policies.

- ``rules/lp/``: Specifies firewall rules for each Launchpad service and
  environment.

A rule file inside ``rules/lp/`` dir looks like:

.. code:: yaml

   launchpad:
     rules:
       - comment: "Allow access to Launchpad"
         from: [any]
         to: [services/lp/launchpad/frontends]
         ports: [http, https, ping]

There is a file for each service:

.. code::

   ├── rules
   │   ├── lp
   │   │   ├── archive.yaml
   │   │   ├── bazaar.yaml
   │   │   ├── buildbot.yaml
   │   │   ├── buildd.yaml
   │   │   ├── builder-proxy.yaml
   │   │   ├── codeimport.yaml
   │   │   ├── fetch-service.yaml
   │   │   ├── forgejo.yaml
   │   │   ├── git.yaml
   │   │   ├── kubernetes.yaml
   │   │   ├── launchpad.yaml
   │   │   ├── librarian.yaml
   │   │   ├── lp-database.yaml
   │   │   ├── mailman.yaml
   │   │   ├── mirrors-index.yaml
   │   │   ├── misc.yaml
   │   │   ├── signing.yaml
   │   │   ├── soyuz.yaml
   │   │   ├── stg-testingfarm.yaml
   │   │   └── webhooks-proxy.yaml

