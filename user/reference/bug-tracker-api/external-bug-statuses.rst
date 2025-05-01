
External bug statuses
=====================

Bugs in free software projects are often tracked in more than one place. For example: a bug in OpenOffice.org may be tracked in Launchpad by Ubuntu's OpenOffice.org team and in OpenOffice.org's own Bugzilla instance.  

Translating the status of external bug watches
----------------------------------------------

Launchpad can track the status of the bug in OpenOffice.org's external tracker and display its current status on the Ubuntu team's bug report.  

Bugzilla and Launchpad use different statuses to describe the stages of a bug's lifecycle. It could quickly become confusing to use two different sets of bug statuses on the same page. Instead, Launchpad translates the status of the external bug report.

Status mapping tables
---------------------
  Last generated: 2008-12-01 14:13 UTC.

Bugzilla
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Bugzilla status
     - Bugzilla resolution
     - Launchpad status
   * - ASSIGNED **or** ON_DEV **or** FAILS_QA **or** STARTED
     - (*ignored*)
     - In Progress
   * - NEEDINFO **or** NEEDINFO_REPORTER **or** WAITING **or** SUSPENDED
     - (*ignored*)
     - Incomplete
   * - PENDINGUPLOAD **or** MODIFIED **or** RELEASE_PENDING **or** ON_QA
     - (*ignored*)
     - Fix Committed
   * - REJECTED
     - (*ignored*)
     - Invalid
   * - RESOLVED **or** VERIFIED **or** CLOSED
     - CODE_FIX **or** CURRENTRELEASE **or** ERRATA **or** NEXTRELEASE **or** PATCH_ALREADY_AVAILABLE **or** FIXED **or** RAWHIDE
     - Fix Released
   * - 
     - WONTFIX
     - Won't Fix
   * - 
     - * (*any*)
     - Invalid
   * - REOPENED **or** NEW **or** UPSTREAM **or** DEFERRED
     - (*ignored*)
     - Confirmed
   * - UNCONFIRMED
     - (*ignored*)
     - New

Mantis
~~~~~~

.. list-table::
   :header-rows: 1

   * - Mantis status
     - Mantis resolution
     - Launchpad status
   * - assigned
     - (*ignored* )
     - In Progress
   * - feedback
     - (*ignored*)
     - Incomplete
   * - new
     - (*ignored*)
     - New
   * - confirmed **or** ackowledged
     - (*ignored*)
     - Confirmed
   * - resolved **or** closed
     - reopened
     - New
   * - 
     - fixed **or** open **or** no change required
     - Fix Released
   * - 
     - unable to reproduce **or** not fixable **or** suspended **or** duplicate
     - Invalid
   * - 
     - won't fix
     - Won't Fix

* ### **Request Tracker (RT)**

.. list-table::
   :header-rows: 1

   * - RT status
     - Launchpad status
   * - new
     - New
   * - open
     - Confirmed
   * - stalled
     - Confirmed
   * - rejected
     - Invalid
   * - resolved
     - Fix Released

* ### **Roundup**

.. list-table::
   :header-rows: 1

   * - Remote host
     - Roundup status
     - Roundup resolution
     - Launchpad status
   * - bugs.python.org
     - 1
     - None
     - New
   * - 
     - 
     - 1
     - Confirmed
   * - 
     - 
     - 2
     - Confirmed
   * - 
     - 
     - 3
     - Fix Committed
   * - 
     - 
     - 4
     - Invalid
   * - 
     - 
     - 5
     - Confirmed
   * - 
     - 
     - 6
     - Invalid
   * - 
     - 
     - 7
     - Confirmed
   * - 
     - 
     - 8
     - Won't Fix
   * - 
     - 
     - 9
     - Confirmed
   * - 
     - 
     - 10
     - Won't Fix
   * - 
     - 
     - 11
     - Invalid
   * - 
     - 2
     - None
     - Won't Fix
   * - 
     - 
     - 1
     - Fix Committed
   * - 
     - 
     - 3
     - Fix Released
   * - 
     - 
     - 7
     - Won't Fix
   * - 
     - 
     - 2
     - Confirmed
   * - 
     - 
     - 4
     - Invalid
   * - 
     - 
     - 5
     - Confirmed
   * - 
     - 
     - 6
     - Invalid
   * - 
     - 
     - 8
     - Won't Fix
   * - 
     - 
     - 9
     - Confirmed
   * - 
     - 
     - 10
     - Won't Fix
   * - 
     - 
     - 11
     - Invalid
   * - 
     - 3
     - None
     - Incomplete
   * - 
     - 
     - 7
     - Won't Fix
   * - 
     - 
     - 1
     - Confirmed
   * - 
     - 
     - 2
     - Confirmed
   * - 
     - 
     - 3
     - Fix Committed
   * - 
     - 
     - 4
     - Invalid
   * - 
     - 
     - 5
     - Confirmed
   * - 
     - 
     - 6
     - Invalid
   * - 
     - 
     - 8
     - Won't Fix
   * - 
     - 
     - 9
     - Confirmed
   * - 
     - 
     - 10
     - Won't Fix
   * - 
     - 
     - 11
     - Invalid
   * - * (*any*)
     - 1
     - (*ignored*)
     - New
   * - 
     - 2
     - (*ignored*)
     - Confirmed
   * - 
     - 3
     - (*ignored*)
     - Incomplete
   * - 
     - 4
     - (*ignored*)
     - Incomplete
   * - 
     - 5
     - (*ignored*)
     - In Progress
   * - 
     - 6
     - (*ignored*)
     - In Progress
   * - 
     - 7
     - (*ignored*)
     - Fix Committed
   * - 
     - 8
     -  (*ignored*)
     - Fix Released

SourceForge or SourceForge derivative
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - `SourceForge <https://help.launchpad.net/SourceForge>`_ status
     - `SourceForge <https://help.launchpad.net/SourceForge>`_ resolution
     - Launchpad status
   * - Open
     - None
     - New
   * - 
     - Accepted
     - Confirmed
   * - 
     - Duplicate
     - Confirmed
   * - 
     - Fixed
     - Fix Committed
   * - 
     - Invalid
     - Invalid
   * - 
     - Later
     - Confirmed
   * - 
     - Out of Date
     - Invalid
   * - 
     - Postponed
     - Confirmed
   * - 
     - Rejected
     - Won't Fix
   * - 
     - Remind
     - Confirmed
   * - 
     - Won't Fix
     - Won't Fix
   * - 
     - Wont Fix
     - Won't Fix
   * - 
     - Works For Me
     - Invalid
   * - Closed
     - None
     - Fix Released
   * - 
     - Accepted
     - Fix Committed
   * - 
     - Fixed
     - Fix Released
   * - 
     - Postponed
     - Won't Fix
   * - 
     - Duplicate
     - Confirmed
   * - 
     - Invalid
     - Invalid
   * - 
     - Later
     - Confirmed
   * - 
     - Out of Date
     - Invalid
   * - 
     - Rejected
     - Won't Fix
   * - 
     - Remind
     - Confirmed
   * - 
     - Won't Fix
     - Won't Fix
   * - 
     - Wont Fix
     - Won't Fix
   * - 
     - Works For Me
     - Invalid
   * - Pending
     - None
     - Incomplete
   * - 
     - Postponed
     - Won't Fix
   * - 
     - Accepted
     - Confirmed
   * - 
     - Duplicate
     - Confirmed
   * - 
     - Fixed
     - Fix Committed
   * - 
     - Invalid
     - Invalid
   * - 
     - Later
     - Confirmed
   * - 
     - Out of Date
     - Invalid
   * - 
     - Rejected
     - Won't Fix
   * - 
     - Remind
     - Confirmed
   * - 
     - Won't Fix
     - Won't Fix
   * - 
     - Wont Fix
     - Won't Fix
   * - 
     - Works For Me
     - Invalid

Trac
~~~~

.. list-table::
   :header-rows: 1

   * - Trac status
     - Launchpad status
   * - New **or** open **or** reopened
     - New
   * - Trac status
     - Launchpad status
   * - accepted **or** assigned **or** duplicate
     - Confirmed
   * - fixed **or** closed
     - Fix Released
   * - invalid **or** worksforme
     - Invalid
   * - wontfix
     - Won't Fix