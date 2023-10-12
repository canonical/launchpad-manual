====================
Code import in depth
====================

Launchpad has the ability to constantly sync code from external repositories by
setting up a code import. This is a one-way sync, from the external source to
Launchpad.

Design decisions
================

Code import / code mirroring is not triggered by the remote repository,
but it is rather triggered from the Launchpad side several times a day.
This should be fine for most use cases.

The benefit of doing it this way is there is no need to install a webhook on
the remote repository to trigger an import or update of the repository.

Frequency
=========

While the current implementation has some support for setting it on a
per-import basis, that's actually not exposed right now.

The frequency depends on the type of the revision control system, and is set in
``effective_update_interval``,
see https://git.launchpad.net/launchpad/tree/lib/lp/code/model/codeimport.py.

As the default intervals in the config schema aren't overridden anywhere right
now, you can look them up in the ``codeimport`` section in the configuration
schema:
https://git.launchpad.net/launchpad/tree/lib/lp/services/config/schema-lazr.conf.

Trigger code import
===================

On a high level, each import has a database field, which indicates when the
next import should be performed. We could think of this as task queue.

A scheduler queries the database, and in case there are jobs, a worker will
pick one up.

Let's have a look in detail.

After the import job runs, and if the import is still in the ``REVIEWED``
state, i.e. it hasn't failed too many times, or it hasn't been suspended or
similar, it then schedules a new job, that is, it sets a new date in the 
``date_due`` column.

Depending on the work load, there is no guarantee that a job will be picked up
in time, as the process works like this:

- cronjobs in ``lp-codeimport`` run workers
- when the code import worker is looking for work to do, it calls
  ``getJobForMachine``,
  see https://git.launchpad.net/launchpad/tree/lib/lp/code/xmlrpc/codeimportscheduler.py
- that calls ``getJobForMachine``
  in https://git.launchpad.net/launchpad/tree/lib/lp/code/model/codeimportjob.py
  which makes a DB query to fetch the first job from a table that has
  ``due_date`` not in the future, and that is marked as ``pending``
- it then triggers the import

Conclusion
==========

The short answer is that we currently aim for every 12 hours for code imports
from CVS (very few nowadays), and every 6 hours from all other revision control
systems.
