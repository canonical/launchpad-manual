Privacy, confidentiality and disclosure
=======================================

.. include:: /includes/important_not_revised_help.rst

Launchpad considers personal user data, unfixed software security issues
and proprietary information as confidential knowledge. Launchpad limits
who may know about it. Project maintainers and users can choose who to
disclose confidential information to, and maybe choose to make the
information public.

Email addresses and obfuscation
-------------------------------

Launchpad considers all user email addresses to be confidential
information. Anonymous users may not know any email address that belongs
to a user. Launchpad obfuscates anything that looks like an email
address that appears in text on launchpad pages and all text fields that
can be accessed via the Launchpad API by anonymous users.

Launchpad will reveal user email addresses to other registered Launchpad
users. Users may follow the `Change
details <https://launchpad.net/~/+edit>`__ link on their profile page to
select the "Hide my email addresses from other Launchpad users".

Team email addresses are always public, they cannot be hidden.

Launchpad staff advise team's to **never** use a mailing list with
a public archive as a team's contact address. Public list archives do
not honour Launchpad's confidentiality rules. Users may include
confidential information in emails that cannot be seen in Launchpad, but
are shown in the public archive.

Private (Proprietary) teams
---------------------------

When you maintain a project with a commercial subscription, you will see
the visibility field on the team registration and "Change details"
pages. Setting the field to Private (Proprietary) allows the team to
work in private.

Non-members team cannot see that the team exists in Launchpad.
Non-members cannot see any of the team's pages. Private teams can choose
to be in some public relationships, such as subscribed to a public bug,
but doing so requires the team to agree to reveal its Launchpad Id and
other unique attributes. This rule ensures that no one can spy on
others. Private teams can also have private PPAs, and proprietary branches.

See :ref:`Creating and running a team <creating-and-running-launchpad-teams>` for more
information.

Hiding comments
---------------

Project maintainers and comment authors may choose to hide comments that
they believe contain confidential information. The comment may appear on
a bug, a question, or a branch merge proposal. The "Hide comment" link
you see under your own comments will change the comment to hidden.
Hidden comments are still visible to the comment author as well as the
people the project share Private information with. This allows the user
and project to continue to collaborate without disclosing information to
other Launchpad users.

See Information Types below to learn about how Launchpad treats Private
user information.

Bug, branch, blueprint, and comment information types
-----------------------------------------------------

The cornerstone of Sharing in Launchpad is 'information types'.
Everything that may be considered confidential has an information type
attribute that declares the type of information that it contains. There
are six information types:

Public
~~~~~~

Everyone can see this information.

Public Security
~~~~~~~~~~~~~~~

Everyone can see this security related information.

Private Security
~~~~~~~~~~~~~~~~

Only the security group can see this information. The information pertains to a critical vulnerability or exploit that
can harm computers or users.

Private
~~~~~~~

Only shared with users permitted to see private user information. The information contain data
that is personal to a user and is not public knowledge.

Proprietary
~~~~~~~~~~~

Only shared with users permitted to see proprietary information.
The information belongs to an organisation and it it will not be made public.

Embargoed, can be proprietary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only shared with users permitted to see embargoed information. The information belongs to
an organisation and it will be made Public in the future.


Every bug, branch, blueprint, and comment has an information type. The
information type sets the rule used to determine who the information is
disclosed to. Few things support all information types. Branches support
all of them, but it is easier to delete a branch than to state it
accidentally contains Private user information. Comments only support
Private and Public, so the "Hide/Unhide comment" is all that is needed
to change the type. In general, information that originates from the
user community will support Private and Private Security. Information
that originates from the developer community will support Proprietary,
and Embargoed.

Projects also have information types that also to everything they
contain. The default information type of a project is Public, so
everything that it contains is also public. Some things, such as series
and milestones, inherit the information type of their project;
Proprietary projects only have Proprietary series and milestones. The
things that have their own information type attribute may be set
independent of the project, Public projects can have Private Security
bugs. Dependents cannot be more permissive then what they depend on. You
cannot stack a Public branch on a Proprietary branch. Proprietary
projects cannot have Public bugs.

Sharing
-------

Project maintainers can share information types with people to disclose
all of that kind of information with trusted people. For example,
sharing all Private Security information with a team allows the team's
members to see all Private Security bugs and branches in the project.

The project sharing page lists all people that the project shares with.
Maintainers can review and change who a project shares with by following
the "Sharing" link shown on the project's front page. Project drivers
may see who the project shares with, but cannot make changes. The
Sharing will also lists all the people that share all of a kinds of
information and lists the people where exceptional access to a bug,
branch, or blueprint was shared through a subscription.

When Sharing with people, the maintainer is prompted to choose the
information types to disclose. When unsharing with people, setting the
information type to None, Launchpad will revoke access to that
information immediately, then remove any subscriptions a few minutes
later. Maintainers can also unshare everything with a user to revoke all
access to confidential information and remove all subscriptions.
Launchpad will preserve subscriptions (and access) for users who are
members of one or more teams -- unsharing with a team revokes access to
just the people who are in the team and are not in any other teams that
the project shares with.

All information types are shared with the project maintainer by default.
The maintainer may choose to share with a team or user.

(!) The Launchpad staff recommend sharing with teams because users tend
to leave organisations and communities, so the user must be unshared
with, which is just additional work from removing a user from one or
more teams.

Subscribing people to confidential bugs, branches, and blueprints will
also share them when the people would not otherwise have access to the
information.

(!) The Launchpad staff recommends only sharing individual bugs,
branches, and blueprints with users who are working to solve the issue.

Users do not need access or additional notifications about information
about information that does not directly concern them. Managing many
bug, branch, and blueprint subscriptions for a user requires more labour
than sharing all of a an information type with people.

When users report bugs, they are automatically subscribed to them to
ensure they have access to their bug. The project maintainer can choose
to unshare the bug later. When a branch is created, the owner is
subscribed for the same purpose, and can be unshared with later.

Project sharing policies
------------------------

Project maintainers can set policies that govern which information types
bugs, branches, and blueprints can become. The policy sets the default
type and what types users can change to. Public projects only have the
default "Public" policy. :ref:`Commercial projects <consumer-hosting>` can
choose other policies to control the what, if any, project information
is disclosed.

There is a policy for each kind of thing that can change: bugs,
branches, and blueprints.

-  **Public** 

| ``New items as public unless they contain confidential information. Items``
| ``can be made Private or Private Security later.``

-  **Public, can be proprietary** 

``New items are public, but can be made proprietary later.``

-  **Proprietary, can be public** 

| ``New items are proprietary, but can be made public later.``
| ``Only people who can see the project's proprietary information``
| ``can create new branches or bugs.``

-  **Proprietary** 

| ``New items are always proprietary.``
| ``Only people who can see the project's proprietary information``
| ``can create new branches.``

-  **Embargoed, can be proprietary** 

| ``New branches are embargoed, but can be made proprietary later.``
| ``Only people who can see the project's proprietary information``
| ``can create new branches.``


+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+
|**Sharing Policy**            | **Public** |**Public Security**|**Private**|**Private Security**|**Proprietary**|**Embargoed**| 
+==============================+============+===================+===========+====================+===============+=============+
|Public                        |Default     |Yes                |Yes        |Yes                 | \-            |\-           | 
+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+
|Public, can be proprietary    |Default     |Yes                |Yes        |Yes                 |Yes            |\-           |
+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+
|Proprietary, can be public    |Yes         |Yes                |Yes        |Yes                 |Default        |\-           | 
+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+
|Proprietary                   |\-          |\-                 |\-         |\-                  |Default        |\-           |
+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+
|Embargoed, can be proprietary |\-          |\-                 |\-         |\-                  |Yes            |Default      |
+------------------------------+------------+-------------------+-----------+--------------------+---------------+-------------+

.. note::
   
   Embargoed branches is only settable using Launchpad API.
