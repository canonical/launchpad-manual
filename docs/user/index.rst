.. meta::
   :description: Comprehensive Launchpad user documentation covering code 
      hosting, build services, bug tracking, account management, and more.

.. _launchpad-manual-for-users:

Launchpad user documentation
============================

Launchpad is designed for effective open-source collaboration. It provides the
tools you need to build open-source projects and share them with the 
world.

Launchpad gives you access to everything necessary to build and publish 
software including code hosting, issue tracking, and request tracking for bugs. 
Features unique to this platform include build capacities for different 
languages, and package formats for different architectures such as **AMD64**, 
**AMD64v3**, **ARM**, and **RISC-V**.

Launchpad also offers tracking capabilities across issue trackers to 
seamlessly communicate with upstream projects.

In this documentation
---------------------

Get to know Launchpad
~~~~~~~~~~~~~~~~~~~~~

New to Launchpad? Start here for an overview of the platform and its key
features, and a tour of a standard Launchpad page.

* **Overview**:
  :ref:`Get started with Launchpad <get-started-with-launchpad>` •
  :ref:`What is Launchpad <exp-what-is-launchpad>` •
  :ref:`Page tour <launchpad-page-layout>`
* **Feature highlights**:
  :ref:`Personal Package Archives <personal-package-archives-highlights>` •
  :ref:`Answer tracker <answer-tracker-for-community>` •
  :ref:`The bug tracker <the-launchpad-bug-tracker>` •
  :ref:`Bug watches <monitoring-bugs-in-other-bug-trackers>` •
  :ref:`Bug branch linking <linking-bugs-to-dedicated-branches>`

Projects and code hosting
~~~~~~~~~~~~~~~~~~~~~~~~~

Host your project's Git repositories, review and merge changes, and understand
how code hosting, imports, and continuous integration fit together.

* **Projects basics**:
  :ref:`Register your project <how-to-register-your-project>` •
  :ref:`Transfer project ownership <transfer-ownership-of-a-project>` •
  :ref:`Close a project <closing-your-project>`
* **Code hosting**:
  :ref:`Host your project's code <host-your-project-code-on-launchpad>` •
  :ref:`Work with Git repositories <hosting-git-repositories>` •
  :ref:`Create and maintain a personal branch <create-and-maintain-personal-branch-in-launchpad>` •
  :ref:`Create and manage a merge proposal <create-and-manage-a-merge-proposal>` •
  :ref:`Code imports <code-imports>` •
  :ref:`Branch privacy <branch-information-types>`
* **Create and run software projects**:
  :ref:`Project registration options <registering-your-project>` •
  :ref:`Project groups <project-groups>` •
  :ref:`Planning and recording releases <planning-and-recording-releases>` •
  :ref:`Making project files available for download <making-your-project-files-available-for-download>` •
  :ref:`Publishing project announcements <publishing-project-announcements>` •
  :ref:`Link code changes to bugs <link-code-to-bug-reports-and-blueprints>` •
  :ref:`Continuous integration <continuous-integration>`
* **Project and code hosting options**:
  :ref:`Proprietary hosting options <proprietary-hosting>` •
  :ref:`Roles in code reviews <roles-in-code-review>` •
  :ref:`Comment syntax <launchpad-comment-parsing>` •
  :ref:`Project licenses <project-licenses>` •
  :ref:`General privacy, confidentiality, and disclosure <privacy-confidentiality-disclosure>` •
  :ref:`Project announcements <ref-project-announcements>` •
  :ref:`Display the Launchpad Badge <launchpad-badge-kit>`

Build and publish software packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build and distribute software packages from your source code without managing
build infrastructure or hosting your archives, including Debian packages in
PPAs, as well as snaps, rocks, charms, and OCI images.

* **Personal package archives basics**:
  :ref:`Install software from PPAs <install-software-from-ppas>` •
  :ref:`Install software from private PPAs <install-private-ppa-software>` •
  :ref:`Install software from a PPA snapshot <use-ppa-snapshot-service>` •
  :ref:`Create a PPA <create-ppa>` •
  :ref:`Upload a package to a PPA <upload-a-package-to-a-ppa>`
* **Work with PPAs**:
  :ref:`Copy packages <copying-packages>` •
  :ref:`Delete packages <package-deletion>` •
  :ref:`Create a source package recipe <create-a-source-package-recipe>` •
  :ref:`Understand source package recipes <packaging>` •
  :ref:`Troubleshoot package upload errors <troubleshoot-package-upload-errors>`
* **Build craft artifacts**:
  :ref:`Build snaps <build-snaps-in-launchpad>` •
  :ref:`Build rocks <build-rocks-in-launchpad>` •
  :ref:`Build charms <build-charms-in-launchpad>` •
  :ref:`Build OCI images <build-oci-images-in-launchpad>`
* **Building, packaging, and publishing specifications**:
  :ref:`Personal Package Archive <personal-package-archive>` •
  :ref:`Building a source package <building-a-source-package>` •
  :ref:`Build scores <prioritising-builds>` •
  :ref:`Builder specs <builder-specs>` •
  :ref:`Daily build naming conventions <naming-conventions-for-daily-builds>` •
  :ref:`Source builds knowledge base <source-builds-knowledge-base>` 

Bug tracking
~~~~~~~~~~~~

File, subscribe to, and manage bugs across your projects. Link them to code
changes, and integrate reports from external trackers such as Bugzilla, Trac,
GitLab, and Mantis.

* **Work with bugs**:
  :ref:`File a bug <file-a-bug-in-launchpad>` •
  :ref:`Display bug reporting guidelines <display-bug-reporting-guidelines>` •
  :ref:`Link a bug to a branch <link-a-bug-reports-to-a-branch>` •
  :ref:`Subscribe and unsubscribe to bugs <subscribe-and-unsubscribe-to-bugs>` •
  :ref:`Turning a bug into a question <turn-bug-to-question>` •
  :ref:`Import your project's bug history <import-bug-history>` •
  :ref:`Multi-project bugs <about-multi-project-bugs>`
* **Email interface and external trackers**:
  :ref:`Use the Launchpad email interface <use-the-launchpad-email-interface>` •
  :ref:`Manage bugs through email <manage-bugs-through-email>` •
  :ref:`Use the Bugzilla plugin <use-the-bugzilla-plugin>` •
  :ref:`Use the Trac plugin <use-the-trac-plugin>` •
  :ref:`Use the Malone XMLRPC interface <use-malone-interface>` •
  :ref:`Track bugs with Mantis <track-bugs-with-mantis>` •
  :ref:`Bug tracker plugin API <bug-tracker-api-plugin>`
* **Bug tracking definitions and specifications**:
  :ref:`Bug statuses <bug-status-in-launchpad>` •
  :ref:`Bug attachments <bug-attachment>` •
  :ref:`Bug expiry <bug-expiry>` •
  :ref:`Bug heat <bug-heat>` •
  :ref:`Bug subscription <bug-subscription>` •
  :ref:`External bug statuses <external-bug-statuses>` •
  :ref:`External bug tracker interoperability <interoperability-with-external-bug-trackers>` •
  :ref:`Email interface commands <email-interface-command-reference>` •
  :ref:`The Malone XMLRPC interface <malone-xmlrpc-interface>` •
  :ref:`Bug supervisor role <bug-supervisor>`

API and automation
~~~~~~~~~~~~~~~~~~

Script Launchpad operations through its REST-style API and the ``launchpadlib``
Python client, and automate external integrations with webhooks.

* **Tutorial**:
  :ref:`Get started with launchpadlib <launchpadlib-tutorial>`
* **Use the API**:
  :ref:`Launchpad API <launchpad-api>` •
  :ref:`Sign web requests <sign-web-requests>` •
  :ref:`Using launchpadlib <using-launchpadlib>` •
  :ref:`The Python API <use-the-python-api>` •
  :ref:`Authenticate with a text browser <auth-launchpadlib-text-browser>` •
  :ref:`Integrate a website <authenticated-access-site-integration>` •
  :ref:`View supported fields and methods <view-supported-fields-and-methods>`
* **Understand the API**:
  :ref:`The launchpadlib API <launchpadlib>` •
  :ref:`Integrate third-party applications <application-integration>` •
  :ref:`Launchpad web service <launchpad-web-service>`
* **API and automation specifications**:
  :ref:`API compatibility <launchpadlib-api-compatibility>` •
  :ref:`Applications using the API <table-of-applications-using-the-api>` •
  :ref:`Webhooks <webhooks>`

Accounts and access
~~~~~~~~~~~~~~~~~~~

Set up and secure your Launchpad identity by creating an account and adding
SSH and OpenPGP keys. Signing in to other sites, understand how your
contributions are tracked and how to manage mail from Launchpad.

* **Account basics**:
  :ref:`Create and personalize your account <create-and-personalise-your-launchpad-account>` •
  :ref:`Merge two or more accounts <merging-accounts>` •
  :ref:`Close your account <how-to-close-account>`
* **Keys and sign-in**:
  :ref:`Import your SSH key <import-your-ssh-keys>` •
  :ref:`Verify Launchpad's SSH fingerprints <ssh-fingerprints>` •
  :ref:`Import an OpenPGP key <import-an-openpgp-key>`
* **Understand your account**:
  :ref:`What can you do with a Launchpad account? <your-launchpad-account>` •
  :ref:`Account karma <your-account-karma>` •
  :ref:`Rationale headers in email <rationale-headers-in-email>` •
  :ref:`Troubleshoot your account <ref-troubleshooting>`

Teams and community
~~~~~~~~~~~~~~~~~~~

Group contributors into teams, coordinate around projects, and take part in the
community through Launchpad Answers.

* **Teams**:
  :ref:`Creating and running teams <creating-and-running-launchpad-teams>` •
  :ref:`Team management <exp-team-management>` •
  :ref:`Indirect team members <indirect-team-members>` •
  :ref:`Team repositories <team-repositories>`
* **Launchpad Answers and support**:
  :ref:`Launchpad Answer Tracker <launchpad-answer-tracker>` •
  :ref:`Asking for help <asking-for-help>` •
  :ref:`Question lifecycle <question-life-cycle>` •
  :ref:`Help the community <help-the-community>` •
  :ref:`Support in your native language <support-native-language>`
* **Collaboration**:
  :ref:`Contacting others and managing your contact information <collaborating-with-other-launchpad-users>` •
  :ref:`Getting support (best practices) <getting-support-in-launchpad>`

Translations
~~~~~~~~~~~~

Coordinate localization of your software with Launchpad's Translations feature,
from preparing your project to importing, exporting, and sharing translations.

* **Translate your project**:
  :ref:`Translating with Launchpad <translating-with-launchpad>` •
  :ref:`Using Rosetta <using-rosetta>` •
  :ref:`Translation prerequisites <translating-your-project>` •
  :ref:`Software translation fundamentals <translating-your-software>` •
  :ref:`Managing, tracking, and contributing translations <translating-your-software-ref>` •
  :ref:`Translation groups <translation-groups>` •
  :ref:`Preparing to translate <preparing-to-translate>`
* **Project translation tasks**:
  :ref:`Import project translations <how-to-import-project-translations>` •
  :ref:`Import translation templates <how-to-import-project-translation-templates>` •
  :ref:`Export translations <how-to-export-translations>` •
  :ref:`Exporting partial PO files <exporting-partial-gettext-PO-files>`
* **Translation guidelines and policies**:
  :ref:`Translation guidelines <translation-guidelines>` •
  :ref:`Language-specific guides <language-specific-translation-guides>` •
  :ref:`Permissions policies <choosing-a-permissions-policy>` •
  :ref:`Import policy <translation-import-policy>` •
  :ref:`Launchpad translators group <launchpad-translators-group>` •
  :ref:`Licensing <translations-licensing-faq>` •
  :ref:`Plural forms <plural-forms-information-for-languages>` •
  :ref:`Translation best practices <launchpad-project-translation-best-practices>` •
  :ref:`Reusing translations best practices <reusing-packaged-translations>` •
  :ref:`PO templates <po-templates>` •
  :ref:`Translation sharing and suggestions <translation-sharing-and-suggestions>`


How this documentation is organized
-----------------------------------

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`_.

* :ref:`Tutorial <user/tutorial>`: tutorials to help you interact with Launchpad.
* :ref:`How-to <user/how-to>`: step-by-step instructions for key operations and common tasks.
* :ref:`Reference <user/reference>`: specifications, APIs, architecture.
* :ref:`Explanation <user/explanation>`: discussion and clarification of user topics.

Project and community
---------------------

Launchpad is a member of the Ubuntu family. It’s an open source project that
warmly welcomes community contributions, suggestions, fixes and constructive
feedback.

Get involved
~~~~~~~~~~~~
* `Join our online chat on Matrix <https://matrix.to/#/#launchpad:ubuntu.com>`_
* `Contribute <https://launchpad.net/launchpad/>`_

Releases
~~~~~~~~
* :ref:`Release notes <release-notes>`

.. toctree::
   :hidden:

   Get started <get-started>
   Tutorial <tutorial/index>
   How-to guides <how-to/index>
   Reference <reference/index>
   Explanation <explanation/index>
