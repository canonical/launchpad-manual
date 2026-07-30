.. meta::
   :description: Learn how to file a bug report to help developers understand
      and fix issues.

.. _file-a-bug-in-launchpad:

File a bug in Launchpad
=======================

Getting started
---------------

After you :ref:`register a project <how-to-register-your-project>` in
Launchpad, you have the option to configure where its bugs are tracked. If
you chose any option other than Launchpad, you will need to activate the
Launchpad bug tracker for your project to continue with the steps on this page.

To do so, in your project's "Bugs" tab, click on "Configure Bugs", choose
Launchpad as the bug tracker, and save your changes.

Importing your existing bug history
-----------------------------------

In some cases, the Launchpad team can import your existing bug history from
another bug tracker. This may mean that you can switch to Launchpad's bug
tracker without having to maintain your previous bug tracker for historical
purposes.

:ref:`Get in touch <get-help>` to see if we can help.

Setting roles
---------------

Bug supervisor
~~~~~~~~~~~~~~~

A bug supervisor has bug-editing privileges. This allows them to handle the
day-to-day management of bugs — triaging new bugs, planning bug work, ensuring
that existing bugs are properly managed, etc.

Many projects :ref:`create specific teams <creating-and-running-launchpad-teams>`
to act as the bug supervisor, allowing several people to manage bugs without
giving them access to other administrative functions.

By default, the project owner is the bug supervisor. This can be changed by
visiting the "Bugs" tab of your project and clicking the edit icon next to the
bug supervisor role.

File a bug with extra data in Launchpad
----------------------------------------

Prior to filing a bug, extra data can be stored in Launchpad via
`<https://launchpad.net/+storeblob>`_. This blob needs to follow a specific
format which can be understood by Launchpad. Please see the
`apport report format`_ for more details about the format. Upon successful submission of the blob, a
ticket ID will be provided which can be used to reference the blob when filing
a bug. This ID can also be found in the ``X-Launchpad-Blob-Token`` HTTP header.

A bug can be filed by visiting ``https://bugs.launchpad.net/<distribution>/+source/<package>/+filebug/<token>``
or ``https://bugs.launchpad.net/<project>/+filebug/<token>`` replacing
``<token>`` with the ticket ID received previously, and ``<distribution>``,
``<package>``, and ``<project>`` as appropriate.

The process after this point is the same as filing a bug normally, except
that certain fields may be pre-populated.

Next step
---------
Now that you have set up the basics, you're ready to start managing your
project's bug reports in Launchpad. However, let's first look at how Launchpad
:ref:`tracks the hottest bugs <bug-heat>`.


.. _apport report format: https://ubuntu.com/project/docs/contributors/debugging/apport/#report-format