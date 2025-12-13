Track issues with email
#######################

.. include:: /includes/important_not_revised_help.rst


Launchpad's bug tracker sends you :ref:`email <bug-subscription>` about the bugs you're interested in. If you see something that requires your attention - for example, you want to comment on a bug - rather than leaving your email client to fire up a web browser, all you need to do is reply to the email.

It's not just limited to replying to bug notifications, though. The bug
tracker's email interface allows you to do just about everything you can
in the web interface. Within time, you may find that email is the main
way you interact with the bug tracker.

Before you start
================

Launchpad verifies incoming email by looking for a GNU Privacy Guard (GPG) signature by the sender, or a DKIM signature by a trusted sender domain, such as GMail. Read our :ref:`guide on adding your GPG key <import-an-openpgp-key>` to your Launchpad account.

Messages that just add comments to a bug or merge proposal are not
required to be signed. Messages that contain commands to change the
state of an object do need to be signed.

Anatomy of an email to the bug tracker
======================================

Let's look at the elements of a bug report email:

-  **From address:** the address from which you send the email must be
   `registered in your Launchpad account <https://launchpad.net/people/+me/+editemails>`_.
-  **To address:** new@bugs.launchpad.net for new bugs;
   ``bugnumber@bugs.launchpad.net`` to manipulate an existing bug
   report; ``edit@bugs.launchpad.net`` for bulk edits.
-  **Subject:** Launchpad uses this as the bug report or comment
   summary.
-  **Email body:** the text of your email forms the bug report or
   comment detail. This is also where you can supply commands to
   manipulate the bug.

That last item, the email body, needs a little more explanation. When
you want to use one of the email interface's commands, **you need to
start the line with a space**. Otherwise, Launchpad will treat your
command as a comment only and not as a command.

**Note:** all commands are also posted as a comment to the bug. This is
something we plan to fix.

Getting started with the email interface
========================================

Let's take a look at an imaginary scenario, in which someone reports a
bug requesting a screen cast to help demonstrate the bug tracker's email
interface.

Reporting a bug
---------------

Reporting a new bug by email is simple. Send an email to
new@bugs.launchpad.net and describe the problem you're having. Tell
Launchpad which project, distribution or distribution package the bug
affects by using the ``affects`` command.


Here's an example bug report email:

::

   From: you@example.com
   To: new@bugs.launchpad.net
   Subject: Bug tracker email interface needs a screen cast

   Body:

   I looked on the Launchpad help wiki for information on using the bug tracker's email interface.
   I found the user guide helpful but wanted a screen cast to demonstrate it at my local LUG.

    affects launchpad-documentation

If the bug affects a distribution package, state the distribution name
followed by a slash and the package name. For example: ``affects
ubuntu/firefox``.

Similarly, if the bug affects more than one project or package, use a
new line for each project/package:

::


    affects exaile
    affects ubuntu/exaile

Commenting on and changing the status of a bug
----------------------------------------------

If you've received a notification about a bug and you want to leave a
comment, simply reply to the email. Otherwise, to comment on a bug, send
your email to ``bugnumber@bugs.launchpad.net``. For example:
``123@bugs.launchpad.net``.

Here's an example bug comment email, with a command to change its status
to ``Confirmed``:

::

   From: joey@canonical.com
   To: 123@bugs.launchpad.net
   Subject: Neat idea

   Body:

   What a neat idea! Matt R: can you schedule some time to create a screen cast?

   We should put the screen cast directly in the bug tracker's interface.

    affects launchpad
    status confirmed

Joey has also marked the bug as affecting Launchpad itself, using its
project name ``launchpad``.

Assigning and targeting the bug
-------------------------------

Matthew sees that his boss, Joey, thinks this a good idea, so he assigns
it to himself and targets it to a future milestone:

::

   From: matthew.revell@canonical.com
   To: 123@bugs.launchpad.net
   Subject: I'll tackle this in September

   Body:

   > What a neat idea! Matt R: can you schedule some time to create a screen cast?

   Yeah, this is a great idea. I'll have time for this in September.

    affects launchpad-documentation
    assignee matthew.revell
    milestone 1.2.9

Note that Matthew used the ``affects`` command. Earlier, Joey marked
the bug as also affecting another project. Here, ``affects`` lets
Matthew ensure the assignee and milestone are applied to the bug as it
affects the Launchpad Documentation project. To use *affects* in this
way you must place it before the other commands.

Matthew could just as easily have left out the ``affects`` command
and Launchpad would have selected the most likely project that bug is
reported against. See the :ref:`affects command reference <affects>` for details.

Attaching files to bugs
-----------------------

Once Matthew's started work on the bug, he can attach an image from the
screen cast to the bug report to show how he's getting on.

In most cases, file attachments are useful for screen shots that
demonstrate the bug or for log files.

You can attach a file to a bug report by attaching the file to the email
you send to Launchpad.

The attachment must have its content-disposition set to "attachment" and
not "inline". Images pasted into emails in Mozilla Thunderbird have a
content-disposition of "inline", so attach them rather than paste them
into the email body.

To help prevent unwanted files being attached to bug reports, Launchpad
filters files that are unlikely to be intended for the bug report,
including:

-  signatures
-  VCards
-  MacOS resource forks.

Editing a bug that affects multiple contexts
--------------------------------------------

Every package or project affected by a bug has its own fix status,
assignee, milestone and so on. Use the :ref:`affects command <affects>` to
edit each of these as it affects a particular context.

For example:

::

   From: you@example.com
   To: 29760@bugs.launchpad.net
   Subject: <none>

    affects ubuntu/flash-player
    status fixreleased

When a bug affects only one package or product, the ``affects`` command
is unnecessary.

What to expect when you submit an email
---------------------------------------

Launchpad processes incoming bug mail every three minutes, so a slight
delay between sending a mail and receiving a response is normal.

On success
~~~~~~~~~~

If Launchpad processed your email successfully, it will reply by email
to confirm the changes. This email is identical to the bug notification
that would get if you had made the same changes using the web interface.

For example, if you sent an email like:

::

   From: you@example.com
   To: 28919@bugs.launchpad.net
   Subject: Re: [Bug 28919] error signing code of conduct: "str: No public key"

    status incomplete

You'll receive a response like:

::

   From: you@example.com
   To: you@example.com
   Subject: [Bug 28919] error signing code of conduct: "str: No public key"

   Public bug report changed:
   https://launchpad.net/launchpad/bugs/28919

   Changed in: Launchpad (upstream)
            Status: Unconfirmed => Incomplete

On partial failure
~~~~~~~~~~~~~~~~~~

An email message to new@bugs.launchpad.net can (1) create a bug and (2)
attempt a command on the bug. It is possible for the create to succeed
but the command to fail. The resulting error message will give you the
impression that the whole email failed. You can then create a duplicate
bug.

If you get a failure email message and you wish to avoid duplicate bugs,
you would be prudent to check the web interface for new bugs before
resending your bug with your attempted corrections to your commands.

On failure
~~~~~~~~~~

If an error occurs while processing your email, Launchpad will send you
a failure message.

For example, if you forget to GPG-sign an email reporting a new bug,
you'll receive an error message similar to:

::

   From: noreply@bugs.launchpad.net
   To: you@example.com
   Subject: Submit Request Failure

   An error occurred while processing a mail you sent to Launchpad's email
   interface.


   Error message:

   In order to submit bugs via email you have to sign the message with a
   GPG key that is registered in Launchpad.


   -- 
   For more information about using Launchpad by email, see
   https://wiki.launchpad.canonical.com/Bugs/EmailInterface
   or send an email to help@launchpad.net

If you've waited several minutes and still not received either a change
notification or an error message, please :ref:`let us know <get-help>`.

Filtering bug mail
------------------

If you deal with a large number of bug reports by email, you may find
that you want to filter them to stop them cluttering your in-box.
Launchpad appends custom headers to bug emails to help you filter them.

You can find out :ref:`more about the headers <bug-mail-headers>`
that Launchpad uses in our article on bug subscriptions.

Commands reference
------------------

You must write one email command per line. Remember that you need to
start the line with a space, otherwise it will be treated as part of
your comment.

For example:

::

    status confirmed
    assignee foobar

You can mix commands with non-command text, such as the description when
filing a bug, or comment text when replying to a bug notification.

For example:

::

   This is an example bit of bug description.

    affects ubuntu/firefox

   And this is some more description.

    assignee bradb


.. _affects:

affects
~~~~~~~

``affects [distribution|package|product]``

When filing a bug, ``affects $target`` marks the bug as affecting
``$target``. This must be the first command when reporting a new bug.

You can also, optionally, use ``affects`` when you're editing a bug.
For example, if you want to set the status of a bug as it affects Zope
3, you'd use ``affects zope3``.

If you leave out ``affects``, Launchpad will make your changes to the
bug the following context:

1. the project, distribution or package for which you are a bug
   supervisor
2. the distribution of which you're a member

If Launchpad can't determine the context in which to make your changes,
it will email you with an error message.

The ``affects`` target can take the following forms:

::

    affects $product
    affects $product/$product_series
    affects $distribution
    affects $distribution/$source_package
    affects $distribution/$distro_series
    affects $distribution/$distro_series/$source_package

summary
~~~~~~~

``summary "$summary"``

Change the one-line summary of the bug. Quotes are required.

::

    summary "A better summary"

assignee
~~~~~~~~

``assignee [name|email|nobody]``

Assign a bug to someone.

::

    assignee bradb
    assignee brad.bollenbach@ubuntu.com

Unassign the bug.

::

    assignee nobody

status
~~~~~~

``status [new|incomplete|invalid|wontfix|confirmed|triaged|inprogress|fixcommitted|fixreleased]``

Change the status of a bug.

::

    status fixreleased

importance
~~~~~~~~~~

``importance [wishlist|low|medium|high|critical]``

Change the importance of a bug.

::

    importance high

milestone
~~~~~~~~~

``milestone[I $milestone``

Sets or clears the milestone of the bug. The milestone must already
exist in Launchpad. :ref:`More about milestones <milestones>`.

::

    milestone 1.1.10

You can clear the milestone by sending a hyphen:

::

    milestone -

informationtype
~~~~~~~~~~~~~~~

``informationtype [public|publicsecurity|privatesecurity|private|proprietary]``

Changes the information type of the bug that affects visibility of the
bug. Only the people that the project shares confidential information
with can see "Private", "Private Security", and "Proprietary" bugs.

::

    informationtype privatesecurity

subscribe
~~~~~~~~~

``subscribe [name|email]``

Subscribe yourself or someone else to the bug. If you don't specify a
name or email, Launchpad will subscribe you, the send of the email, to
the bug.

Subscribe yourself to the bug:

::

    subscribe

Subscribe Foo Bar to the bug:

::

    subscribe foo.bar@canonical.com

Subscribe Bjorn to the bug.

::

    subscribe bjornt

unsubscribe
~~~~~~~~~~~

``unsubscribe [name|email]``

The opposite of the subscribe command.

duplicate
~~~~~~~~~

``duplicate $bugid``

Mark the bug as a duplicate of another bug.

::

     duplicate 42

To unmark the bug as a duplicate, specify 'no' as the bug id.

::

     duplicate no

bug
~~~

``bug $bugid``

The ``bug`` command is useful if you want to use one email to make
changes to several bugs.

Send such emails to ``edit@bugs.launchpad.net``.

::

   From: terry.tibbs@tibbsmotors.com
   To: edit@bugs.launchpad.net
   Subject: <whatever>

    bug 42
    status confirmed

    bug 49
    status confirmed

tag
~~~

``tag $tag``

Assign a tag to a bug. You can specify multiple tags with a single
command.

::

    tag foo

Or:

::

    tag foo bar

Remove a tag by prefixing the tag name with ``-``.

::

    tag -foo

done
~~~~

``done`` tells Launchpad to process no further commands.

For example:

::

    tag foo
    status confirmed
    done
    affects everyone using version 1.0.1

The line below ``done`` looks like an ``affects`` command but
Launchpad will ignore it.

