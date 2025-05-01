Launchpad mailing lists
=======================

*Having a problem with mailing lists? See
the* `troubleshooting <#troubleshooting>`__ *section below.*

Your team can have its own mailing list, hosted and managed by
Launchpad.

Team mailing lists are useful because they:

-  use team memberships to control mailing list permissions: many
   projects use Launchpad teams to group their users and developers into
   convenient teams
-  accept posts from any email address registered in a subscriber's
   Launchpad profile
-  allow team members to manage all their Launchpad list subscriptions
   in one place
-  greatly simplify administration: manage multiple lists through one
   interface
-  automatically archive posts: copies are archived on Launchpad itself
   and at `mail-archive.com <http://mail-archive.com>`__, a popular
   long-term list archive site.

For the technically minded, Launchpad mailing lists are managed by `GNU
Mailman <http://www.list.org>`__, although we have simplified the web
interface, allowing you to easily administer multiple lists through
Launchpad.

Taking part in mailing lists
----------------------------

Launchpad mailing lists are team-oriented: every team may have one
mailing list and every mailing list is associated with exactly one team.

As a team member, you can subscribe to that team's mailing list but it
is optional: joining a team does not automatically subscribe you to its
mailing list.

Subscribing
~~~~~~~~~~~

**Step 1:** Visit the `Edit
emails <https://launchpad.net/people/+me/+editemails>`__ page in your
profile.

**Step 2:** Scroll to the bottom of the page, where you'll see all the
mailing lists you can join.

\||<tablestyle="font-size: 0.8em; width:30%; background:#F1F1ED; margin:
1em 1em 1em 0;" style="padding:0.5em;">|\| \||<style="text-align:
center;">\ **Mailing list subscriptions**\ \|\|

**Step 3:** Use the drop-down, beside your chosen to list, to select the
email address where you want to receive the emails.

**Step 4:** Click ``Update Subscriptions``.

You don't need to confirm your subscription as you've already confirmed
your email addresses and you're logged into Launchpad.

As soon as your subscription is live, Launchpad will send you a welcome
email, which may include a custom message from the team's owners.

Using the list
~~~~~~~~~~~~~~

Let's say you've joined the launchpad-doc team's mailing list. To send
email to the list, you'd use the address
``launchpad-doc@lists.launchpad.net``. You can send it from any
address that's registered in your Launchpad profile. However, Launchpad
will only send email to the address you specified when subscribing to
the list.

After a few minutes, depending on network latencies, you should receive
your message in your inbox. It'll also appear in the list's archive.

It's just the same for all other lists: take the name of the team and
append it to ``@lists.launchpad.net``.

.. note::
    -  Postings by people who are not Launchpad members are immediately discarded.
    - Postings by Launchpad members who are not team members are held for approval by the team owner.
    - All Launchpad mailing list messages are publicly archived and **the archives are open to everyone**, not just Launchpad or team members.
    If you have any issues with information available in the archives, you should contact `the Launchpad administrators <https://help.launchpad.net/Feedback>`__.
    However, our general policy is **never to remove archive messages or information contained therein**.

If you use Gmail
^^^^^^^^^^^^^^^^

If you use Gmail and don't see your own posts arrive in your inbox, it
is probably because of `this
issue <http://wiki.list.org/display/DOC/I+use+Gmail-Googlemail%2C+but+I+can%27t+tell+if+any+of+my+messages+have+been+posted+to+the+list>`__.
Unfortunately, this not something that we can fix. Instead, check the
list's archive to confirm your message has been accepted.

Unsubscribing and changing your subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To unsubscribe from a list, or change the email address where you
receive a particular list's mails, visit your `Edit
emails <https://launchpad.net/people/+me/+editemails>`__ page. There,
you can select:

-  another address that's already registered in your profile
-  the ``Don't subscribe`` option to unsubscribe
-  the ``Preferred address`` option for Launchpad to automatically
   track your preferred email address

Establishing a list for your team
---------------------------------

The Launchpad team reviews all new requests for mailing lists. This is
to help reduce misuse of the Launchpad's list hosting.

You can request a mailing list for your team by clicking ``Configure
mailing list`` on the team's overview page.

We handle new mailing list application requests several times a day and
will enable your mailing list as soon as possible. Once we've approved
your mailing list, you'll see a ``Configure mailing list`` on your
team's overview page.

Privacy
~~~~~~~

Mailing list archive privacy is inherited from team privacy, which must
be established before the mailing list is requested. Once a mailing list
is requested, the team's privacy cannot be changed.

Customizing your team's welcome message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can specify a custom message to be included in the welcome message
that Launchpad sends to new list subscribers.

Click ``Configure mailing list`` on your team's overview page to
enter your custom message.

.. note::
    
    This feature is not currently implemented.

Size limit
~~~~~~~~~~

Messages posted to your mailing list have a maximum size limit of 40KB.
Messages larger than this cannot be posted to your mailing list.
`contact us <https://answers.launchpad.net/launchpad>`__ if that is a
problem for you.

Renaming your team
~~~~~~~~~~~~~~~~~~

When a team has a mailing list, it cannot be renamed. However, you can
take the following steps to rename your team:

-  Deactivate your team's mailing list. You can do this on the
   ``Configure mailing list`` page. It will take a few minutes for
   this deactivation request to complete.
-  `Open a question <https://answers.launchpad.net/launchpad>`__ to have
   a Launchpad administrator ``purge`` your mailing list. This
   erases all traces of your old mailing list and allows you to rename
   your team.
-  Once that question is answered, you can rename your team.
-  Request a new mailing list for your newly renamed team.
-  When your mailing list is approved and activated, all your old
   subscriptions will be restored.

If you want to migrate the old mailing list archives to the new team,
re-open the original question you submitted above, providing the old and
new team names so that the Launchpad administrators can import your old
archives.

Viewing list archives
---------------------

Full archives for each mailing list are available by clicking
``Mailing list archive`` on the team's overview page.

The archives are available to view by date or thread.

Further information
-------------------

Teams are a great way for communities to organise themselves. If,
however, your project isn't yet in Launchpad's directory, you need to
`register it <Projects/Registering>`__ to use track its bugs and code,
translate it into different languages and more.

Troubleshooting
---------------

If you're having problems with mailing lists, there are a few things you
can try to do before you submit a `bug
report <http://bugs.launchpad.net/launchpad>`__ or
`question <http://answers.launchpad.net/launchpad>`__. Here are some
common problems and easy solutions.

Unable to post to a mailing list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common symptom is that you post a message to a mailing list, but you
never see the list copy of the message in your inbox.

There are several possible reasons for this; here are the things to
check:

1. **Is the message in the list's archive?** If so, and you are using
   Google Mail, you should read `this Mailman FAQ
   item <http://wiki.list.org/x/2IA9>`__.
2. **Are you registered with Launchpad?** The email address you use in
   the \`From:\` field of your message **must** be registered and
   validated with Launchpad. If not, your message will get discarded and
   you will not get a bounce.
3. **Are you a member of the team?** All team members may post to their
   team's mailing list. Non-member postings will get held for the
   approval of the team owner. If you are not a member of the team,
   contact the team owner to see if your message is being held.

If all else fails, you can `post a
question <http://answers.launchpad.net/launchpad>`__ to the Launchpad
answer tracker and we will respond as soon as possible.