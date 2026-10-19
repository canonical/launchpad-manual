.. meta::
   :description: Glossary of Launchpad terminology including technical terms, 
      concepts, and definitions for developers and users.

.. _glossary:

Glossary
========

.. include:: /includes/important_not_revised_help.rst

- **Bugtask:** A bug tracked in Launchpad can appear in different projects and releases of a project, enabling different teams to work together on solving that bug. We call each appearance of a bug in each different context a bugtask. A bugtask has associated with it an assignee, an importance and a status. It can be targeted to a project or distribution milestone.

- **Component:** Distribution package archives can have arbitrary groupings, which are called components. Ubuntu uses components to bring together packages of a certain licensing type or that have a certain level of support commitment: e.g. main, universe and multiverse.

- **Display name:** Projects, teams and individuals in Launchpad are usually referred to by their display name. This is distinct from the ``Name``, which is mostly used in URLs. Example: Mark Shuttleworth's display name is ``Mark Shuttleworth``, whereas his Launchpad name is ``sabdfl``.

- **Distribution:** A complete operating system made of software packages. Unlike a project, which is one piece of software, a distribution brings together software from many developers. Launchpad can build a distribution's packages or track bugs for a distribution built elsewhere. **Example:** ``ubuntu``. See :ref:`the Packaging explanation <packaging>` for more details.

- **FTBFS:** a source package failed to build.

- **Karma:** Karma is a score that gives a rough idea of a person's current level of work in Launchpad. See our guide to :ref:`karma <your-account-karma>` for more.

- **launchpadlib:** A Python client library that talks to the Launchpad web service. Developers and maintainers use it to write scripts that automate Launchpad tasks, such as looking up bugs, instead of clicking through the website. See :ref:`the launchpadlib explanation <launchpadlib>` for more details.

- **Launchpad web service:** An application programming interface (API) that lets programs read and change Launchpad data. It is also called the Launchpad API. People use the website, while programs use the web service. See :ref:`the web service explanation <launchpad-web-service>` for more details.

- **Name (project):** This is the unique short name that Launchpad uses to identify a project. It is used in URLs and when registering a bug against a project. **Example:** ``blueprint`` in `<https://launchpad.net/blueprint>`_ for Launchpad's Blueprint Tracker.

- **OOPS:** An error report that Launchpad records when an unexpected error, such as a timeout, stops it from doing what you asked. Launchpad shows you an ID that starts with ``OOPS-``. When you ask the Launchpad team for help, give them this ID. See :ref:`what-is-an-oops` for more details.

- **Pocket:** A release pocket is group of packages related to a particular distro series (i.e. a release such as Ubuntu 9.04/Jaunty), such as *security*, *updates* or *back-ports*.

- **Project:** A piece of software developed or tracked in Launchpad. It can have features such as code repositories, bug reports, release milestones, and translations. **Example:** ``firefox``. See :ref:`the Projects explanation <exp-projects-in-launchpad>` for more details.

- **Project group:** Project groups allow you to gather several Launchpad projects together. Each project within a group inherits the group's preferences regarding bug tracking, translation and security policy. An example project group is Mozilla, with Firefox and Thunderbird as projects within the group.

- **Series:** Series are major lines of development that usually result in one or more releases. For example: Firefox 3 and Firefox 2. In Launchpad, they can have independent translations, bug reports, code and more. In a distribution, such as Ubuntu, it would be releases such as Jaunty, Intrepid, Hardy and so on.

- **Staging:** A test copy of Launchpad that starts from a snapshot of real Launchpad data. Changes you make there are not kept, so you can test scripts without affecting real projects or users. Staging runs at `<https://staging.launchpad.net>`_.

- **Suite:** The combination of a distro *series* and a *pocket* is called a suite: e.g. Hardy backports.

- **Webhook:** An HTTP request that Launchpad sends to your server when something changes, such as a Git push or a new bug comment. With the Launchpad web service, your program has to ask for data. With a webhook, Launchpad tells your program about changes without being asked. See :ref:`webhooks` for more details.

Request a definition
--------------------

If you're unsure of a term that we use in Launchpad, add it here and we'll provide the definition. Subscribe to this page to receive an email notification when we update the page.

.. note::

    To edit this page, you need to log in using your Launchpad
    username and password.

    - Term (your Launchpad user name, or other contact method).
