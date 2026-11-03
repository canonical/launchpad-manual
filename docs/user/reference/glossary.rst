.. meta::
   :description: Glossary of Launchpad terminology including technical terms, 
      concepts, and definitions for developers and users.

.. _glossary:

Glossary
========

.. include:: /includes/important_not_revised_help.rst

- **Affects:** The affects mechanism allows us to track all the projects, distributions, package and/or PPAs that are affected by a bug. Every instance of the "affect" has it's own status, importance, assignee.

- **Bug heat:** A score that tells you the significance of a bug. It's calculated from the security level of a bug and the amount of attention it's getting from users.

- **Bug supervisor:** A person or team that is responsible for bug management in a project or distribution.

- **Bug watch:** A bug watch is used to monitor the status of a bug that is being managed by an external bug tracker.

- **Bugtask:** A bug tracked in Launchpad can appear in different projects and releases of a project, enabling different teams to work together on solving that bug. We call each appearance of a bug in each different context a bugtask. A bugtask has associated with it an assignee, an importance and a status. It can be targeted to a project or distribution milestone.

- **Component:** Distribution package archives can have arbitrary groupings, which are called components. Ubuntu uses components to bring together packages of a certain licensing type or that have a certain level of support commitment: e.g. main, universe and multiverse.

- **Display name:** Projects, teams and individuals in Launchpad are usually referred to by their display name. This is distinct from the ``Name``, which is mostly used in URLs. Example: Mark Shuttleworth's display name is ``Mark Shuttleworth``, whereas his Launchpad name is ``sabdfl``.

- **Distribution:** A complete operating system made of software packages. Unlike a project, which is one piece of software, a distribution brings together software from many developers, e.g., Ubuntu. Launchpad can build a distribution's packages or track bugs for a distribution built elsewhere.

- **FTBFS:** a source package failed to build.

- **Indirect team member:** If Team A joins Team B, all of Team A’s members are now indirect members of Team B.

- **Karma:** Karma is a score that gives a rough idea of a person's current level of work in Launchpad. See our guide to :ref:`karma <your-account-karma>` for more.

- **Launchpad name (username):** A short unique name serving as a user's unique identifier on launchpad.

- **launchpadlib:** A Python client library that talks to the Launchpad web service. Developers and maintainers use it to write scripts that automate Launchpad tasks, such as looking up bugs, instead of clicking through the website. See :ref:`the launchpadlib explanation <launchpadlib>` for more details.

- **Launchpad web service:** This is Launchpad's API which lets users and applications read and change Launchpad data without visiting the website. See :ref:`the web service explanation <launchpad-web-service>` for more details.

- **Malone:** A unified bug tracker managed by Launchpad designed to ease collaboration between upstream and downstream projects registered with Launchpad. For example, a bug fix found by downstream can easily be viewed and integrated by upstream.

- **Name (project):** This is the unique short name that Launchpad uses to identify a project. It is used in URLs and when registering a bug against a project. **Example:** ``blueprint`` in `<https://launchpad.net/blueprint>`_ for Launchpad's Blueprint Tracker.

- **OOPS:** An error report that Launchpad records when an unexpected error, such as a timeout, stops it from doing what you asked. It has an ID that starts with ``OOPS-``. See :ref:`what-is-an-oops` for more details.

- **OpenID:** OpenID is an open standard and decentralized authentication protocol used to log into websites that accept OpenID authentication using an OpenID identity provider. Launchpad serves as one of many OpenID identity providers.

- **OpenPGP key:** A cryptographic public-private key pair used to sign documents and confirm identities. Launchpad requires you to use your OpenPGP key when signing the Ubuntu Code of Conduct, using the Bug Tracker's email interface and software packaging.

- **Pocket:** A release pocket is a group of packages related to a particular distro series (i.e. a release such as Ubuntu 26.04/Resolute), such as *security*, *updates* or *back-ports*.

- **Project:** A piece of software developed or tracked in Launchpad. It can have features such as code repositories, bug reports, release milestones, and translations. **Example:** ``firefox`` in `<https://launchpad.net/firefox>`_.

- **Project group:** Project groups allow you to gather several Launchpad projects together. Each project within a group inherits the group's preferences regarding bug tracking, translation and security policy. An example project group is Mozilla, with Firefox and Thunderbird as projects within the group.

- **Question / Answer:** Questions and answers in Launchpad are managed by the Launchpad answer tracker, which tracks progress of user questions regarding specific projects, distributions, or packages.

- **Rosetta:** A web-interface translation tool managed by Launchpad.

- **SSH key:** SSH keys are used on Launchpad to authenticate your identity when you push code to repositories or upload packages to Personal Package Archives (PPAs).

- **Staging:** A test copy of Launchpad that starts from a snapshot of real Launchpad data. Changes you make there are not kept, so you can test scripts without affecting real projects or users. Staging runs at ``https://staging.launchpad.net``.

- **Suite:** The combination of a distro *series* and a *pocket* is called a suite: e.g. Hardy backports.

- **Team:** A group consisting of  people involved in a common task.A team can be a maintainer of a project, an assignee of a bug, or an editor of a package for a particular language.

- **Team admin:**A team member with administrative privileges. The team admin can add, approve or reject members. They can subscribe the team to bugs, branches, and blueprints.

- **Team member:** A team member has upload rights to all of the team’s code branches. They can upload and build Ubuntu packages in the team’s PPA, and access confidential information shared with the team. 

- **Team owner:** The owner can change the team’s description and membership rules, and appoint team admins. The owner is also an administrator by default.

- **Triage:** This is the process of sorting bugs based on the progress that has been made to address them. This could be a confirmation that the bug can be replicated, or the status of a proposed fix. 

- **Webhook:** An HTTP request that Launchpad sends to your server when something changes, such as a Git push or a new bug comment. With the Launchpad web service, your program has to ask for data. With a webhook, Launchpad tells your program about changes without being asked. See :ref:`webhooks` for more details.


Request a definition
--------------------

If you're unsure of a term that we use in Launchpad, add it here and we'll provide the definition. Subscribe to this page to receive an email notification when we update the page.

.. note::

    To edit this page, you need to log in using your Launchpad
    username and password.

    - Term (your Launchpad user name, or other contact method).
