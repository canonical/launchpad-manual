.. _use-the-launchapd-email-interface:

Use the Launchapd email interface
=================================

.. include:: /includes/important_not_revised_help.rst

Launchpad's bug tracker sends you :ref:`email <bug-subscription>` about
the bugs you're interested in. If you see something that requires your
attention - for example, you want to comment on a bug - rather than
leaving your email client to fire up a web browser, all you need to do
is reply to the email.

It's not just limited to replying to bug notifications, though. The bug
tracker's email interface allows you to do just about everything you can
in the web interface. Within time, you may find that email is the main
way you interact with the bug tracker.

Before you start
----------------

Launchpad verifies incoming email by looking for a GNU Privacy Guard
(GPG) signature by the sender, or a DKIM signature by a trusted sender
domain, such as GMail. Read our :ref:`guide on adding your GPG
key <import-an-openpgp-key>` to your Launchpad account.

Messages that just add comments to a bug or merge proposal are not
required to be signed. Messages that contain commands to change the
state of an object do need to be signed.

Get started with the email interface
------------------------------------

Let's take a look at an imaginary scenario, in which someone reports a
bug requesting a screen cast to help demonstrate the bug tracker's email
interface.

.. _report-a-bug:

Report a bug
------------

Reporting a new bug by email is simple. Send an email to
new@bugs.launchpad.net and describe the problem you're having. Tell
Launchpad which project, distribution or distribution package the bug
affects by using the ```affects`` command.

.. important::

    *Affects* must be the first command you give in the email
    when reporting a new bug.

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
followed by a slash and the package name. For example: ``affects ubuntu/firefox``.

Similarly, if the bug affects more than one project or package, use a
new line for each project/package:

::

    affects exaile
    affects ubuntu/exaile

Comment on and change the status of a bug
-----------------------------------------

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

Assign and target the bug
-------------------------

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

Attach a files to a bug
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

Edit a bug that affects multiple contexts
-----------------------------------------

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

Filter bug mail
---------------

If you deal with a large number of bug reports by email, you may find
that you want to filter them to stop them cluttering your in-box.
Launchpad appends custom headers to bug emails to help you filter them.

You can find out :ref:`more about the headers <bug-mail-headers>`
that Launchpad uses in our article on bug subscriptions.
