.. _creating-and-running-launchpad-teams:

Creating and running Launchpad teams
====================================

.. include:: /includes/important_not_revised_help.rst

Building a strong community around your project or a particular effort
within a project is often crucial to its success. Launchpad teams help
you to bring people together by offering:

-  a focal point of collaboration.
-  tools for members to communicate
-  the ability for many people to share a role, such as a project's maintainer or driver.

Teams are easy to use: Launchpad doesn't impose rules or a particular
workflow on how you use your teams. Although most teams are associated
with a particular project, there isn't a formal link.

Anyone can create a team. To get going, visit the `new team <https://launchpad.net/people/+newteam>`__ page. You'll probably notice that creating a team is very similar to :ref:`registering a user account <create-and-personalise-your-launchpad-account>`. This isn't a coincidence: teams and people work in the same way throughout most of Launchpad.

Of course, there are some differences. When you first register a team,
keep an eye out for:

-  **Membership policies**: whether you want the team inclusive to anyone or exclusive to a few people control something in Launchpad.
-  **Subscription period**: (optional) Set a period when membership expires.
-  **Membership renewals**: (optional) Choose how expired members renew their membership.

You can change any of these details later using the ``Change details`` link on your team's overview page.

Private (proprietary) teams
---------------------------

When you maintain a :ref:`project with a commercial subscription <consumer-hosting>`, you will see the visibility field on the team registration and ``Change details`` pages.

Visibility
~~~~~~~~~~
You can choose ``Private`` to hide the team from non-members.

You may be able to change a "Public" team to a "Private" team if it is
not subscribed or own something that can only be public. Once the team
is in a public relationship, it cannot ever be made "Private" Private
team **cannot** ever be made ``Public``. Do not choose to make team
"Private" if you want it to be public in the future.

Non-members team cannot see that the team exists in Launchpad.
Non-members cannot see any of the team's pages. Private teams can choose
to be in some public relationships, such as subscribed to a public bug,
but doing so requires the team to agree to reveal its Launchpad Id and
other unique attributes. This rule ensures that no one can spy on
others. Private teams have additional privileges:

-  **P3A**: the team can have many private personal package archives (sometimes called ``P3As``) to distribute packages.

   Non-member subscribers to an archive may know the team's Launchpad-Id``

-  **Branches**: code branches pushed to the team's personal repository are Proprietary, visible only to the team.

   Branches pushed to a project may also be visible to anyone that the project shares Proprietary information with.

Branding your team
------------------

Branding is one of the ways in which teams are similar to people.
Similar to your own Launchpad account, you can upload images to help
others identify pages associated with your team:

-  **Icon**: this shows up in listings wherever your team's name is mentioned - e.g. on a team member's profile. Must be 14x14 pixels and   no more than 5KB.
-  **Mugshot** appears on the team's profile page. Must be 192x192 pixels and no more than 100KB.

What team membership means
--------------------------

It's up to you what membership of your team means. Some teams exist to
give people the chance to make a public declaration while others grant
access to privileged parts of a project's activity.

In general, members of your team get:

-  Upload rights for all of the team's code branches
-  Permission to upload and build Ubuntu packages in the team's PPA
-  Any access that comes with a role taken by the team (e.g. project maintainer).
-  Disclosure of all confidential information shared with the team

Roles
~~~~~

There are also two special types of membership for people who run your
team:

-  **Administrator**: can add, approve or reject members. They can subscribe the team to bugs, branches, and blueprints.

-  **Owner**: the owner can change the team's description and membership rules, and appoint team admins. The owner is also an administrator by default, but can choose to leave the team.``

These roles can be held by other teams, as well as by people.

.. _membership-policies:

Membership policies
-------------------

There are four kinds of membership policies that control who and how a user
or team can become a member. The choice of policy reflects the need to
build a community (``inclusive``) versus the need to control control
Launchpad projects, branches, and PPAs (``exclusive``).

Open
~~~~

Membership is inclusive; any user or team can join, and noapproval is required.

Delegated
~~~~~~~~~

Membership is inclusive; any user or team can join, but team administrators
approve direct memberships.

Moderated
~~~~~~~~~

Membership is exclusive; users and exclusive teams may ask to join.

Restricted
~~~~~~~~~~

Membership is exclusive; team administrators can invite users and
exclusive teams to join.

Managing membership requests
----------------------------

If you've chosen the moderated or delegated membership policy, Launchpad
will send you an email whenever someone applies to join. The email will
have three components:

-  **From**: the team's display name (e.g. Launchpad Beta Testers)
-  **Reply address**: the prospective member's primary email address
-  **Subject**: ``<their Launchpad system name>`` wants to join.

Let's take a look at the `membership list for the Launchpad Beta Testers team <https://launchpad.net/~launchpad-beta-testers/+members>`_. As a team administrator, you'll see a pencil icon beside each member's name. This allows you to edit existing memberships and new applications.

This is Chris Jones' application.

Here, Launchpad links Chris's name to his profile. A person's profile
page offers you an accurate reflection of the sort of work they do in
Launchpad. Not only does it give you the information they've written
about themselves but it also automatically tells you which teams they're
most active in, what sort of work they do and on which projects. If you
still need more information, Chris's profile shows you different ways of
getting in touch with him.

Whether you choose to accept or reject a membership application,
Launchpad will inform the prospective member and all the team's
administrators by email. You can add a custom message to this email,
which is particularly useful if you want to suggest first steps to new
members or explain why you've declined an application.

Membership expiry
~~~~~~~~~~~~~~~~~

Setting an automatic expiry on team memberships can be useful if your
team is for a time-limited activity or you want to give people a
reminder to review their membership.

You can both:

-  set all subsequent memberships to expire after a specified number of days, on your team's ``Change details`` page
-  and choose a membership expiry date for individual members, when approving or editing that person's membership.

Launchpad emails anyone who has a team membership that is about to
expire. How they renew their membership is up to you:

-  the member must apply to renew: if you want to review someone's contribution to the team
-  allow the member to renew: if you're happy for existing members to remain in the team but you want to ensure they're still interested
-  automatic renewal.

Bulk moderation
~~~~~~~~~~~~~~~

If several people have applied to join your moderated team, you can bulk
approve and decline their memberships with the ``Approve or decline
members`` link below the ``Proposed members`` list.

Teams joining teams
-------------------

`Pyroom <https://launchpad.net/pyroom>`_ is a simple text editor designed to minimise distractions. The Pyroom developers use Launchpad to track bugs, host code and make translations. In addition to a general `Pyroom team <https://launchpad.net/~pyroom-team>`_, they also have a `bug team <https://launchpad.net/~pyroom-bugsquad>`_ that acts as the project's bug contact and a `dev team <https://launchpad.net/~pyroom-dev>`_ that has owns its trunk development branch.

Because teams behave just like people in Launchpad, the Pyroom bug and
dev teams can join the main Pyroom team. Thanks to that, members of
Pyroom's bug and dev teams are indirect members of the main Pyroom team:
they have access to everything that a direct member has.

There are two ways for one team to join another team and which you use
depends on your role:

-  **Your team is joining another**: visit the team you want your team to join, and choose the ``Add one of my teams`` link.
-  **You're adding another team to yours**: Use the ``Add member`` link, then add the team just as you would a person.

If you add another team to your own, you're actually inviting that team
to join. Launchpad will email the other team's admins with your
invitation, allowing them to decide whether or not to add their team to
yours.
