Email interface command reference
=================================

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

<<Anchor(affects)>>

affects
-------

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

::

    affects $product/$product_series

::

    affects $distribution

::

    affects $distribution/$source_package

::

    affects $distribution/$distro_series

::

    affects $distribution/$distro_series/$source_package

summary
-------

``summary "$summary"``

Change the one-line summary of the bug. Quotes are required.

::

    summary "A better summary"

assignee
--------

``assignee [name|email|nobody]``

Assign a bug to someone.

::

    assignee bradb

::

    assignee brad.bollenbach@ubuntu.com

Unassign the bug.

::

    assignee nobody

status
------

``status
[new|incomplete|invalid|wontfix|confirmed|triaged|inprogress|fixcommitted|fixreleased]``

Change the status of a bug.

::

    status fixreleased

importance
----------

``importance [wishlist|low|medium|high|critical]``

Change the importance of a bug.

::

    importance high

milestone
---------

``milestone $milestone``

Sets or clears the milestone of the bug. The milestone must already
exist in Launchpad. `More about
milestones <Projects/SeriesMilestonesReleases#milestones>`__.

::

    milestone 1.1.10

You can clear the milestone by sending a hyphen:

::

    milestone -

informationtype
---------------

``informationtype
[public|publicsecurity|privatesecurity|private|proprietary]``

Changes the information type of the bug that affects visibility of the
bug. Only the people that the project shares confidential information
with can see "Private", "Private Security", and "Proprietary" bugs.

::

    informationtype privatesecurity

subscribe
---------

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
-----------

``unsubscribe [name|email]``

The opposite of the subscribe command.

duplicate
---------

``duplicate $bugid``

Mark the bug as a duplicate of another bug.

::

     duplicate 42

To unmark the bug as a duplicate, specify 'no' as the bug id.

::

     duplicate no

bug
---

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
---

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
----

``done`` tells Launchpad to process no further commands.

For example:

::

    tag foo
    status confirmed
    done
    affects everyone using version 1.0.1

The line below ``done`` looks like an ``affects`` command but
Launchpad will ignore it.