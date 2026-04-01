.. meta::
   :description: Practical how-to guides for using Launchpad features including 
      account management, bug tracking, code hosting, and package building.

.. _user/how-to:

How-to guides
=============

If you are already familiar with Launchpad, these how-to guides can provide 
guidance on how to achieve specific goals when using the platform. You can
adapt these to meet other needs, but you may need to refer to some explanation 
and reference docs as well.

Account and access management
-----------------------------
You need a user account to access many Launchpad features. There are additional 
options to customize your account, and you may also need to set up 
authentication using SSH and GPG keys.

-  :ref:`Create and manage your Launchpad account <account-management>`
-  :ref:`Import your SSH key <import-your-ssh-keys>`
-  :ref:`Import an OpenPGP key <import-an-openpgp-key>`

Since Launchpad uses OpenID, once you set up your account, you can use the same 
credentials to :ref:`log into other websites <log-into-websites-with-openid>`.

Manage your projects and code
-----------------------------
Hosting your project code on Launchpad allows you to collaborate with others,
build software packages from the code for distribution, translate the project 
into other languages, and more.

- :ref:`Manage projects <howto-projects>`
- :ref:`Work with code hosted on Launchpad <work-with-code-hosted-launchpad>`

Software Packages
-----------------
Launchpad allows you to build software packages from source code without having
to manage any build infrastructure. You can upload source packages to a 
Personal Package Archive (PPA), where Launchpad builds them into installable 
binary packages.

- :ref:`Upload, build, and install software packages <packaging-how-to>`
- :ref:`Create a source package recipe <create-a-source-package-recipe>`

Manage bugs
-----------
There are many ways to work with bugs on Launchpad from simply filing bug 
reports and subscribing to bugs, to using plugins to track bugs in external 
trackers and linking bugs to branches.

- :ref:`Work with bugs <work-with-bugs>`

API access
----------
The Launchpad API allows you to interact with Launchpad using scripts, 
applications, and other websites. You can also use ``launchpadlib`` which allows
you to treat the resources published by the API as Python objects. This makes 
integration with other applications more straightforward.

- :ref:`Use the Launchpad web services API <launchpad-web-services-api>`
- :ref:`Work with launchpadlib <work-with-launchpadlib>`

Contribute to the community 
---------------------------
When you sign up to Launchpad you get to benefit from the contributions 
of other community members. There are different ways that you can also give 
back to the community, e.g., by becoming an answer contact for a project or 
responding to questions others post on Launchpad Answers.

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

