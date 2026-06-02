.. meta::
   :description: Practical how-to guides for using Launchpad features including 
      account management, bug tracking, code hosting, and package building.

.. _user/how-to:

How-to guides
=============

Launchpad supports a wide range of workflows - from managing accounts and
hosting code, to building packages and tracking bugs. This section provides
step-by-step instructions for specific tasks.

Manage your account and access
------------------------------
You need a user account to access most Launchpad features. Once set up, you can
authenticate with SSH and GPG keys and use your Launchpad credentials across
other OpenID-compatible websites.

-  :ref:`Create and manage your Launchpad account <account-management>`
-  :ref:`Import your SSH key <import-your-ssh-keys>`
-  :ref:`Import an OpenPGP key <import-an-openpgp-key>`
-  :ref:`Log into other websites with OpenID <log-into-websites-with-openid>`

Manage your projects and code
-----------------------------
Launchpad hosts your project's code repositories and provides tools for code
review, branching, merge proposals, and linking code to bugs and blueprints.

- :ref:`Manage projects <howto-projects>`
- :ref:`Work with code hosted on Launchpad <work-with-code-hosted-launchpad>`

Build and publish packages
--------------------------
Launchpad builds software packages from your source code without requiring you
to manage build infrastructure. This includes Debian packages in Personal
Package Archives (PPAs), as well as snaps, rocks, charms, and OCI images.

- :ref:`Upload, build, and install software packages <packaging-how-to>`
- :ref:`Create a source package recipe <create-a-source-package-recipe>`

Manage bugs
-----------
The bug tracker lets you file, subscribe to, and manage bugs across your
projects. It also integrates with external trackers - including Bugzilla, Trac,
and Mantis - and can link bug reports directly to code branches.

- :ref:`Work with bugs <work-with-bugs>`

Use the API
-----------
Launchpad exposes most of its data and actions through a REST API.
``launchpadlib``, the official Python client library, lets you script Launchpad
operations as Python objects without dealing with raw HTTP. You can also call
the API directly from other languages or tools.

- :ref:`Use the Launchpad web services API <launchpad-web-services-api>`
- :ref:`Work with launchpadlib <work-with-launchpadlib>`

Contribute to the community 
---------------------------
Launchpad Answers lets you respond to support questions from other users. You
can also take on an ongoing role as an answer contact for a specific project.

- :ref:`Help the community <help-the-community>`


.. toctree::
   :hidden:
   :maxdepth: 1

   Import an OpenPGP key <import-openpgp-key>
   Import your SSH keys <import-ssh-keys>
   Log into websites with OpenID <using-openid>
   Create a source package recipe <source-package-recipe>
   Help the community <community-help>
   Manage your account <account-management/index>
   Projects <projects/index>
   Packaging <packaging/index>
   Launchpad web services API <launchpad-api/index>
   Work with launchpadlib <launchpadlib/index>
   Work with bugs <work-with-bugs/index>
   Work with code hosted on Launchpad <work-with-code-hosted-on-launchpad/index>

