Bug Supervisor
==============

The bug supervisor is a person or team that is responsible for bug
management in a project or in a distribution.

A common pattern is to create a *project*-qa team, containing the
developers and other people who want to help with bug management. For
very large projects the bug supervisor are a group who are neither
project maintainers or drivers who help triage bugs.

Being bug supervisor (or a member of a bug supervisor team) has the
following powers:

-  Can set bugs to Triaged state, indicating that the project team has
   accepted they will work on the bug. (Other users can only set it to
   Confirmed.)

.. raw:: html

   <!-- end list -->

-  Cannot target bugs to a milestone or to a series. (Only project
   drivers/owners/release managers can do this.)

.. raw:: html

   <!-- end list -->

-  Can assign bugs to other people. (Others can only assign bugs to
   themselves.)

When the bug supervisor is set, a `bug
subscription <Bugs/Subscriptions>`__ to the project or distribution is
created for the the user or team. The user or team admin can change the
subscription using "Edit bug mail" link found on the project or
distribution's bug page.

There are two restrictions when you appoint a bug supervisor:

   -  Only the project/distribution owner may appoint the bug
      supervisor.
   - You can only appoint yourself or a team which you administer

.. raw:: html

   <!-- end list -->