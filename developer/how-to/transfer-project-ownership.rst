Transferring ownership of a Launchpad project
=============================================

Transferring the ownership of a project in Launchpad takes more than simply
changing the maintainer of a project when there is private content
associated with it.

This is particularly evident for private projects, when after updating the
project's maintainer, the maintainer themselves might not be able to see the
private project they maintain.

This is because the permissions to see and update a project are defined via
its sharing policies, which need updating in such cases.

How to transfer the ownership of a private project
--------------------------------------------------

To transfer the ownership of a project from team A to team B:

1. Update the project's maintainer to team B. To do so, either:
    
   * access your project's page and click on the "edit" button near the
     "maintainer" field.
    
   * go directly to https://launchpad.net/<project_name>/+edit-people.

2. Check the project's "Sharing policies". To do so, either:

   * go to your project page, and click on the "Sharing" button on the right
     panel.

   * go directly to https://launchpad.net/<project name>/+sharing.

3. If any sharing policies are in place, update them so that the policies
associated with team A are now associated with team B instead.


You can find more details about "Sharing policies" in your project's "Sharing
policies" page.
