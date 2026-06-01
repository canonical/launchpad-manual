.. meta::
   :description: Understand Launchpad concepts including accounts, karma, 
      collaboration, answers, projects, teams, translations, and code hosting.

.. _user/explanation:

Explanation
===========

Launchpad brings together tools for hosting code, tracking bugs, publishing
packages, coordinating translations, and more. These pages explain how the key
features and systems work. For an overview, see
:ref:`feature highlights <launchpad-feature-highlights>` or
:ref:`What is Launchpad? <exp-what-is-launchpad>`.

Your Launchpad account
----------------------
There is a lot of freedom when it comes to what you can work on in Launchpad. 
Launchpad tracks your contributions through a Karma points system and sends
email notifications to keep you informed about projects, bugs, and teams you
are following.

- :ref:`What can you do with a Launchpad account? <your-launchpad-account>`
- :ref:`Account Karma <your-account-karma>`
- :ref:`Understanding rationale headers in Launchpad mail <rationale-headers-in-email>`

Community and collaboration
---------------------------
You can contact other contributors on Launchpad, but also manage who can see
your contact information. There are also defined policies around privacy,
confidentiality, and the disclosure of personal and project information.

- :ref:`Contacting others and managing your contact information <collaborating-with-other-launchpad-users>`
- :ref:`Privacy, confidentiality, and disclosure of information <privacy-confidentiality-disclosure>` 

Launchpad Answers
-----------------
`Launchpad Answers <https://answers.launchpad.net>`_ is a community Q&A tracker
where users can post questions about projects and receive answers from other
community members or designated answer contacts. Projects can embed the tracker
in their support workflow and build up a library of stock answers.

- :ref:`Understanding Launchpad Answers <exp-answers>`

Projects, packages, and translations
-------------------------------------
Launchpad organizes software around projects, which can have series,
milestones, and releases. You can distribute packages through Personal Package
Archives (PPAs) and coordinate localization using the Translations feature.

- :ref:`Managing projects on Launchpad <exp-projects-in-launchpad>`
- :ref:`Packaging your software for release <exp-packaging>`
- :ref:`Translating with Launchpad <exp-translating>`

Code hosting
------------
Launchpad hosts Git repositories, supports importing code from external
platforms, and provides a CI pipeline for running automated checks against
your code.

- :ref:`Understand how to work with code on Launchpad <working-with-code>`

Teams
-----
Teams allows you to group contributor and assign them roles, permissions, and
responsibilities across projects. Teams can own projects, have their own code
branches, and act collectively as answer contacts or reviewers.

- :ref:`Understanding Launchpad Teams <exp-launchpad-teams>`

Launchpad API and launchpadlib
------------------------------
Launchpad exposes most of its objects and actions through a REST API.
``launchpadlib`` is the official Python client that wraps this API, letting
you work with Launchpad resources as Python objects in scripts and
applications.

- :ref:`Launchpad API and launchpadlib <launchpad-api>`

Testing and troubleshooting
---------------------------
Launchpad provides a staging environment where you can test integrations and
workflows without affecting production data. When errors occur, Launchpad
generates an OOPS ID that you can include when filing a support request to help
the team investigate.

- :ref:`The staging environment <staging-environment>`
- :ref:`Understanding OOPSes <what-is-an-oops>`
- :ref:`Filing and managing support requests <filing-new-support-request>`

.. toctree::
    :hidden:
    :maxdepth: 1

    What is Launchpad? <what-is-launchpad>
    Your Launchpad account <your-launchpad-account>
    Understanding karma <your-account-karma>
    Collaborating using Launchpad <collaborating-using-launchpad>
    Answers <answers/index>
    Feature highlights <feature-highlights/index>
    Launchpad API <launchpad-api/index>
    Rationale headers in Launchpad email <message-rationale-headers>
    OOPS <oops>
    Packaging <packaging/index>
    Privacy, confidentiality and disclosure <privacy-confidentiality-and-disclosure>
    Projects <projects/index>
    Staging environment <staging-environment>
    Support requests <support-requests>
    Teams <teams/index>
    Translating <translating-with-launchpad/index>
    Working with code <working-with-code/index>
    