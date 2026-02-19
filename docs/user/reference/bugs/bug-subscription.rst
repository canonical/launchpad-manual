.. _bug-subscription:

Bug subscription
================

.. include:: /includes/important_not_revised_help.rst

This document is a reference for Launchpad's bug subscription feature. This 
feature helps you to keep track of bugs via email and Atom feeds.

X-Launchpad-Bug
---------------

The ``X-Launchpad-Bug`` header collates most of the other
information about a bug's status, importance, etc. It gives you slightly
different information, depending on whether you're dealing with a
distribution package or a project:

Project
........

-  ``product``
-  ``status``
-  ``importance``
-  ``assignee``
-  **For example:** ``X-Launchpad-Bug: product=terminator;
   status=Confirmed; importance=Low; assignee=None;``

Package
.......

-  ``distribution``
-  ``sourcepackage```
-  ``component``
-  ``status``
-  ``importance``
-  ``assignee``
-  **For example:** ``X-Launchpad-Bug: distribution=ubuntu; sourcepackage=exaile; component=universe; status=Confirmed; importance=Medium; assignee=None;``

.. _bug-mail-rationale:

Bug mail rationale
------------------

The ``X-Launchpad-Message-Rationale`` header tells you why you've
received the notification.

You can be either:

-  ``Assignee``
-  ``Subscriber``
-  ``Registrant``

For example: ``X-Launchpad-Message-Rationale: Assignee``

An ``@`` symbol shows that you're related to the bug through
membership of a team:

::

       X-Launchpad-Message-Rationale: Assignee @ubuntu-kernel-bugs
       X-Launchpad-Message-Rationale: Subscriber @ubuntu-core-dev

If you're the project/package owner, the product/package name is show in
parentheses:

::

       X-Launchpad-Message-Rationale: Registrant (kiwi)

If the notification is about a duplicate bug, the rationale shows you
which bug this report duplicates:

::

       X-Launchpad-Message-Rationale: Assignee via Bug 1332

This makes it easy to filter out bug mail about duplicate bugs. For
example: let's say this bug notification is for bug 2129. This header
means you are the assignee of bug 1332, of which 2129 is a duplicate.
