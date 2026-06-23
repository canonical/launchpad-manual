.. meta::
   :description: Reference guide to proprietary git hosting for projects on Launchpad.

.. _proprietary-hosting:

Proprietary git repository hosting
==================================

Launchpad is meant for open-source projects, but it can also be used for
proprietary projects.

Projects with prior approval from Canonical can use additional privacy features.
Proprietary projects may only use Launchpad with such approval. Details are
found on the project's "Sharing" page.

You can configure approved projects to use one of the following bug and branch
sharing policies:

- *Public:* Branches or bugs are public unless they contain sensitive
    security information (marked as "private security").

- *Public, can be proprietary:* New branches or bugs are public by default, but
    can be made proprietary later.

- *Proprietary, can be public:* New branches or bugs are proprietary by
    default, but can be made public later. Only people who can see the
    project's proprietary information can create new branches or bugs.

- *Proprietary:* Branches or bugs are always proprietary. Only people who can
    see the project's proprietary information can create new branches or bugs.

If the project is proprietary, the sharing options are as follows:

- *Embargoed, can be proprietary:* Branches or bugs are always proprietary.
    Only people who can see the project's proprietary information can create
    new branches or bugs.

- *Proprietary:* New branches or bugs are proprietary.

We recommend that projects share all information types with their developer
teams. Sharing with your organization's team will also ensure your co-workers
are informed and can do their job. Avoid sharing with users because they leave
projects and organizations; if a user needs access to confidential information
either add the user a team that is already shared with or subscribe the user to
just the bugs and branches they need to work with.

As the maintainer of a project with commercial support, you can create:

- *Private teams:* Visible to team members only.

- *Private package archives (PPAs):* Visible to team members and to users you
    offer a package subscription to.

Use of commercial-only features is granted on a case-by-case basis for a defined
time period. If you require a commercial subscription to use these features,
please contact commercial@launchpad.net.
