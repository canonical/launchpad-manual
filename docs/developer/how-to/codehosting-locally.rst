How To Use Codehosting Locally
==============================

.. include:: /includes/bazaar-discontinued.rst

**Note:** This guide is for bazaar hosting. For git hosting, see `the
turnip README <https://git.launchpad.net/turnip/tree/README.rst>`__.

Just as it's possible to run the launchpad web application locally, it
is also possible to run the complete codehosting stack on your
development machine. The main awkwardness is that you have to manually
kick off some of the things that are usually done by cronjobs.

Make sure Apache is set up
--------------------------

Various parts of the codehosting system require that Apache is
configured appropriately. If launchpad.test works at all for you, you've
probably already done this, but if it doesn't work, running

::

   sudo make install

from the root of your launchpad tree should configure things
appropriately.

Get things running
------------------

Getting all the servers that need to be running started is as simple as
running

::

   make run_all

or

::

   make run_codehosting

in the root of your Launchpad tree.

Set up a user
-------------

First ensure you have an mta installed e.g. postfix. If you run

::

   ./utilities/make-lp-user <your real launchpad id>

, you can use

::

   lp://test/

shortcuts.

You can also use the 'mark' launchpad user, the only user in the sample
data with an ssh key set up, but it's probably best not to these days.

Push up a branch
----------------

If you ran

::

   make-lp-user

, this is just a few more keystrokes than pushing a branch to launchpad:

::

   bzr push -d <some branch> lp://test/~<you>/+junk/branchname

You might have to add the following to ~/.ssh/config:

::

   Host bazaar.launchpad.test
       Port 5022
       Hostname launchpad.test

Pull and scan the branch
------------------------

At this point the branch is just in the 'hosted area', and needs to be
*scanned* (data about the branch copied into the Launchpad database).

On production, this happens via the magic of cron. Locally you can make
it happen by running

::

   cronscripts/process-job-source.py IBranchScanJobSource

.

Now you have a fully working and up-to-date branch -- you should be able
to look at the branch page in Launchpad, view the source in codebrowse,
and so on.

Troubleshooting
---------------

-  If you have troubles pushing to a local code hosting instance with an
   error like below, the stale /var/tmp/launchpad_forking_service.sock
   might be the problem. Remove it and restart code hosting.

.. raw:: html

   <!-- end list -->

::

       $ bzr push lp://test/~danilo/translated/trunk
       exec request failed on channel 0
       bzr: ERROR: Connection closed: Unexpected end of message. Please check connectivity and permissions, and report a bug if problems persist.

-  If you are receiving connection refused to port 5022, in
   \`configs/development/launchpad-lazr.conf`, under the
   \`[codehosting]\` heading, amend the line:

.. raw:: html

   <!-- end list -->

::

       port: tcp:5022:interface=127.0.0.88

to

::

       port: tcp:5022:interface=0.0.0.0

Alternatively, push from within the container.
