.. _registering-your-project:

Registering your project
========================

.. include:: /includes/important_not_revised_help.rst

Let's have a quick recap of how you can use Launchpad for your project:

-  **Use Launchpad's applications directly:** bug tracker, code hosting,
   user support tracker, translations, specification tracker,
   distribution package build and hosting, file downloads and so on.
-  **List your project in the directory:** gain publicity for your
   project, make announcements, link to your bug tracker, register your
   code and `make it available <https://code.launchpad.net>`__.

Of course, you can pick and choose almost any combination of what
Launchpad has to offer. The first step is to register your project.

Types of project you can register
---------------------------------

You can register any free software project in Launchpad free of charge.
To find out what we mean by "free software", take a look at our
`licensing
policy <http://www.ubuntu.com/community/ubuntustory/licensing>`__.

Canonical `formerly sold commercial
subscriptions <https://answers.launchpad.net/launchpad/+faq/208>`__
which allowed the use of commercial-only features, including for
projects with non-free-software licences. This scheme is no longer in
operation, although use of commercial-only features may still be granted
on a case-by-case basis.

If you're not sure that your project's licence is suitable, :ref:`talk to
us <get-help>` about it.

.. tip::
    If you want to register a translation team or Ubuntu
    loco team in Launchpad, please :ref:`create a new team <creating-and-running-launchpad-teams>`, not a project.

Registration
------------

To register your project, visit the page at
`Projects <https://launchpad.net/projects>`__ ⟶ `Register a
project <https://launchpad.net/projects/+new>`__.

Registration is straightforward. However, there are a few things to
note:

-  **Name:** the unique name Launchpad gives to your project and uses
   mainly in URLs. For example: `Avant Window
   Navigator <https://launchpad.net/awn>`__'s name is ``awn``.
-  **Display name and title:** used on pages related to your project,
   these should be the project's full name. For example: ``Avant
   Window Navigator``.
-  **Summary and description:** both appear on your project's home page
   but only the summary is returned in search results.
-  **Licenses:** Explain the terms under which that users can modify and
   distribute your project's code

If you choose the "Other/Proprietary" license, your project will be
awarded a 30-day trial commercial subscription that entitles explore the
:ref:`commercial hosting features <consumer-hosting>`.

Note that once you have registered your project you will not be able to
change its name by yourself. If you wish change it you can ask an
administrator to that for you, read the :ref:`Feedback <get-help>` page for
more information.

Project groups
--------------

Some larger free software projects are actually several related projects
working under the same banner. For example: Firefox is part of the
Mozilla project. Launchpad represents these as projects
(`Firefox <https://launchpad.net/firefox>`__) and project groups
(`Mozilla <https://launchpad.net/mozilla>`__).

Project groups are useful because they give you one place from which to
find all the information about the constituent projects.

Read more about the process of registering a project group
:ref:`here <project-groups>`.

.. _sharing-confidential-information-with-trusted-users:

Sharing confidential information with trusted users
---------------------------------------------------

The project maintainer is the default person who can see all the
confidential bugs and branches in a project. Maintainers can share kinds
of information with trusted people -- only those people can see the
confidential information. Project drivers may see who the project shares
with, but cannot make changes.

Users may report bugs that contain private and personal information in
them. Users and developers may work with bugs and branches that deal
with private security issues. Only people that the project shares
confidential information can see these bugs and branches. Some users
might be directly subscribed to the bug or branch to see just that one
thing. Commercial projects have more sharing options and may choose to
set policies that control the kind of information bugs and branches are
by default, and if the information type can be changed.

We recommend that projects share all information types with their
developer teams. Sharing with your organisation team will also ensure
your co-workers are informed and can do their job. Avoid sharing with
users because they leave projects and organisations; if a user needs
access to confidential information either add the user a team that is
already shared with or subscribe the user to just the bugs and branches
then need to work with.

The bug and branch sharing policies determine the default bug or branch
information type, and control what types they may be changed to.
Non-commercial projects cannot configure the policies. Bugs and branches
are Public by default, but can be changed to Private Security or Private
later. Projects with :ref:`commercial subscriptions <consumer-hosting>`
can choose other rules to ensure confidential information is never
disclosed.

Roles within projects
---------------------

People and teams can take different roles within your project. For now,
the two most important roles are:

-  **Maintainer:** has full control of the project and takes all other
   roles in the project until they are filled by other people or teams.
-  **Driver:** exists at both project level and individual series
   (planned releases). Can approve or decline bugs and blueprints
   targeted to future series.
-  **Release Manager:** The drivers of a series are called release
   managers. In addition to the driver privileges, the release manager
   can register and manage the series milestones and releases.

By default, whoever registered the project is its maintainer. However,
you can change this to any other person or team in Launchpad use the
``edit`` link next next to the maintainer on the project overview
page.

Similarly, you can set the driver for the whole of your project with
``Driver: edit`` on the Overview. However, it may be more useful to
set different drivers for each series, as we'll see later.

Other roles that we'll look at in detail later on include:

-  bug supervisor
-  translation group
-  answer contact.

Further information
-------------------

Tell Launchpad how your project :ref:`organises its different lines of development and releases <planning-and-recording-releases>`.
