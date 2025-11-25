.. _bug-tracker-api-plugin:

Bug tracker API plugin
======================

.. include:: /includes/important_not_revised_help.rst

We want Launchpad to share bug reports, comments, statuses and other
information with as many bug trackers as possible. We've already
produced plugins that enable :ref:`Bugzilla <use-the-bugzilla-plugin>` and
:ref:`Trac <use-the-trac-plugin>` to communicate directly with Launchpad.

Here you can find the details of Launchpad bug tracker plugin API. This
gives you all the information you need to write a Launchpad plugin for
your preferred bug tracker.

Authentication
--------------

When pushing information to a remote bug tracker, Launchpad needs to
authenticate with that bug tracker.

An account should automatically be created for Launchpad to use. The
user name need not be the same on all bug trackers the API gets
installed in, however we recommend that the default be "launchpad" with
email address ``noreply-$bugtracker@launchpad.net``.

Launchpad can authenticate with a remote tracker using any number of
mechanisms, depending on the underlying protocols chosen for the API.
The goal is simply to ensure that the remote bug tracker knows that it
really is Launchpad that is making these calls. An example
authentication protocol is given below.

The authentication shouldn't be made using a password. Instead Launchpad
should authenticate like this:

1. Launchpad gives the remote tracker a random token, $token. For
   example, it might call an unauthenticated API passing it that value
   as a parameter. Before it replies:
2. The remote tracker checks if ``https://launchpad.net/tokens/$token``
   exists (200 HTTP reply status)
3. If the URL above exists, the remote tracker knows that it's Launchpad
   talking to it.
4. The remote tracker returns a cookie, or similar, for Launchpad to use
   as authentication in the next few numbers of requests.

$token is a list of characters in the set of {a-z,A-z,0-9}. The client
should URL encode the token when checking whether the token exists on
Launchpad. This is to prevent someone passing in a token like
"../+index" and be able to log in with that.

Each token will only be used once. After the initial authentication,
Launchpad should be able to do a number of requests without
authenticating using the method above again. Instead the returned cookie
should be sufficient to authenticate.

In some cases, Launchpad will be passing information to the remote
tracker which was contributed by a Launchpad user, either through the
web interface at launchpad.net or through email or an API. Launchpad
will add information about who initiated the action to the content
itself, for example in the comment or bug text. So, if user Joe comments
on a bug, and Launchpad wants to forward that comment to the remote
tracker, it will add text identifying Joe as the commenter to the
comment before passing it to the remote tracker.

API protocol
------------

It's not that important whether the APIs can be accessed via XML-RPC, a
REST interface or some other interface as long as it's structured,
stable, and easy to parse. Using a protocol built on top of HTTP is
preferred. Possible alternatives include:

| ``* XML-RPC``
| ``* REST (XML, JSON)``

XML-RPC is the preferred method if no API exists already.

General assumptions
-------------------

We make some general assumptions when we're interacting with remote bug
trackers:

1. **Time and time zone accuracy**. We assume that the bug tracker knows
   what time it is. Specifically, we assume that the bug tracker knows
   what time its database thinks it is when it starts trying to answer
   the question we have asked it. Each reply from the bug tracker should
   also include that time, so that we can keep track of the "window"
   that has been covered since we spoke to it last. We want to know the
   time that the queries started, not the time that they finished,
   because things might be changing in other transactions during the
   course of this one, and next time we come along we want to pick up
   those changes. If we were told the time the queries finished, we
   should risk missing changes that happened during our query the next
   time we come along. We also assume that the bug tracker knows what
   time zone it is in, and each API should document whether times are
   given in local time or UTC.

2. **Bugs have unique IDs**. We assume that every bug has a unique ID,
   and that the ID is immutable. A given ID refers to a given bug all
   the time. Note - we DO NOT assume that the title and description of a
   bug are immutable. Thus, a bug with ID "qwerty" may have a title
   "foo" today, and a title "bar" tomorrow.

3. **Bugs are ordinal**. We assume that Bug ID's have some ordinality
   that is immutable. This means that we assume bugs can be ordered in a
   given sequence which does not change. We allow for bugs to be
   *inserted into that sequence* because of issues with database
   transactions. We use bug ID's to specify ranges of bugs, and we ask
   the bugtracker to specify ranges using bug id's. In other words,
   imagine we have been told about two bugs, with ID's "xyz" and "abc",
   and we have been told that bug "xyz" precedes "abc". We can ask
   questions like "tell us about the statuses of all bugs between xyz
   and abc". Today, there might be three bugs between "xyz" and "abc",
   and tomorrow there might be four bugs in that range, but we assume
   that "xyz" will *always* precede "abc", and any bug which lies in
   the range from "xyz" to "abc" today will always lie in that range.

    Note, we do not assume that bugs have integer ID's. The bug ID can be something like "issue56" or "ticket2576", or literally "abc" or "qwe". Note that we don't assume we can always see a particular ID - bugs in the bugtracker can be deleted or marked confidential after Launchpad has previously seen them. Also, we don't assume that we can see a bug which looks like it logically should exist - if we have been told about a bug "90" and another bug "100", and we ask for information about bugs between them, it's fine for us to be told that there are bugs "90", "93" and "100" only. Tomorrow, we might see but "96" because it is no longer confidential.

    This "belated insertion" happens in real life. Say I start a transaction to file a bug which will have ID X. For whatever reason, the transaction to do so takes a minute. A second after my transaction starts, someone files a bug with ID X+1. A second later, Launchpad asks for the top bug and is told X+1 (which has been filed).  But at this stage, bug X is still in its transaction. If Launchpad asks for Bug X, it does not yet actually exist in the database, it's still in its transaction. So, while the bugs are ordered, bug X can show up after bug X+1, which is why I say we assume ordinality but allow for insertions.

4. **Bugs can be specified in ranges**. We assume that we can refer to
   sets of bugs by the range between two bug ID's. We might have to
   limit this to the idea that bugs have a "date filed". We want this so
   that we can talk to big bugtrackers in sets of queries rather than in
   huge ones. We would prefer to be able to assume unique integer ID's
   on bugs with the ability to express ranges of them, i.e. "from bug
   '100000' to bug '200000'".

5. **Launchpad can push and pull information**. By enabling this API in
   the remote tracker, the admin of the instance trusts Launchpad to
   pull and push information, and to relay information to users in
   Launchpad.

General API Methods
-------------------

bugtracker_version(): Retrieve the version of the bug tracker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will need to verify that the bug tracker version is one that we can
talk to, and also to know if there are any version-specific quirks we
should be aware of. There should be an API to establish:

-  the bug tracker version
-  the version of the API that implements this Launchpad capability

For example, we might want to know that we are talking to a Bugzilla
installation that is version 3.1 running version 1.2 of the Launchpad
API.

time_snapshot(): Get current database time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to avoid issues where there's a skew between the time in
Launchpad, and the time in the remote tracker, there should be a call to
get the current time in the database. For example, if a new bug is
filed, what timestamp will be used for its creation time.

-  **Input**: nothing
-  **Output**: the time zone name, the current database time in local
   time, and the current database timestamp in UTC

It may seem unusual to ask for all three pieces of information, but
doing so allows us to make sure that we have EXACTLY the same
understanding about relevant time zones and current time as the remote
bug tracker. Therefor, we want to be able to verify that the bug tracker
is doing "sane" things w.r.t. time, and the only way to be sure is to
ask for all three pieces of information.

Pulling information
~~~~~~~~~~~~~~~~~~~

We need to keep the bugs we're watching in sync regularly. This can be a
great number of bugs, sometimes all bugs in the bug tracker. The API for
pulling new information about these bugs need to be efficient enough, in
order not to put too much load on the remote server. The less requests
that are needed to get the information, the better. However, that
doesn't mean that there has to be one request to get all information.
The API that gives us information about a bug should be able to return
multiple bugs at once; issuing one request per bug isn't scalable.

These sections describes only what APIs we need. Several of the sections
could be combined into one API method.

The information we need to know for each bug is:

| ``id``
| ``when was the bug filed``
| ``status``
| ``resolution (Status and resolution can be combined into one field if that's how the remote tracker handles statuses)``
| ``severity``
| ``priority (Like status and resolution, this can be combined with severity if there aren't separate fields for the two)``
| ``assignee``
| ``comments``
| ``bug which this bug is a duplicate of (if any)``
| ``product/component? (If multiple projects are tracked by this bug tracker then we should be able to get back the details of the project that this bug was filed against.)``

The current database time when the call started (see above) should be
included in the output for all the API calls to avoid time skew issues.

get_bugs(): Get information about a set of bugs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a set of bug ids, return information about the bug. It should be
possible to specify how much information should be returned. Possible
levels should be 'bug ids only', 'metadata about the bug only',
'metadata + comment ids', and 'metadata plus full comment information'.

-  **Input**: information level, bug ids
-  **Output**: all the specified bugs that exist. If a bug that doesn't
   existed is requested, the method should simply not return any data
   about that bug, rather than throwing an error. This allows Launchpad
   to handle non-existent bugs internally rather than having to deal
   with errors over-the-wire.

**Note**: It may be possible to overload ``get_bugs()`` to include the
functionality of ``get_all_bugs()``, ``get_bugs_changed_since()`` and
``get_new_bugs_since()``, below.

get_all_bugs(): Get all bugs in the bug tracker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will be used in order to do an initial import of a bug tracker. It
will only be used for bug trackers with a small amount of bugs, or
partial imports.

An error may be raised if the limit is too high, i.e. if the bug tracker
doesn't want to return too many bugs at once due to performance reasons.

-  **Input**: information level, optional range of bugs (e.g. start=0,
   limit=50), optional product/component
-  **Output**: all bugs in the bug tracker for the given
   product/component ()

get_bugs_changed_since(): Get all bugs that have changed since a given timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will be used when we update bugs that we're watching. If possible
(and easy), only the things that have changed since the given timestamp
should be returned, but returning the current state of the bug is
acceptable.

product/component:

-  **Input**: a UTC timestamp, information level, optional range of
   bugs, optional product/component
-  **Output**: all bugs that have changed since the given timestamp

get_new_bugs_since(): Get new bugs that were filed since a given timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This could be combined with the API call above.

-  **Input**: a UTC timestamp, optional product/component
-  **Output**: all bugs that have been filed since the given timestamp

get_bug_count(): How many bugs are currently in the bug tracker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simple count of the number of bugs the bug tracker contains.

-  **Input**: optional product/component
-  **Output**: the number of bugs (open+closed)

last_modified_date(): Last modified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When was any bug last modified? This is a query about the last time the
database was touched rather than referring to any specific bug.

-  **Input**: optional product/component
-  **Output**: the UTC timestamp of when any bug as last modified.

latest_bug_id(): ID of latest bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What's the ID of the latest bug filed in the bug tracker?

-  **Input**: optional product/component
-  **Output**: bug ID of the latest filed bug

status_list(): Get the set of statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What are the possible status values a bug can have?

-  **Input**: nothing
-  **Output**: list of status values

Synchronising comments
----------------------

For a comment we need to know:

* who added the comment
    * A unique identifier is necessary. Preferably an e-mail address.
* when was the comment added
* title/body
* unique, immutable comment id
* in-reply-to, if available

The comment id is important, so that we can identify the comment. It
should be unique across the bug tracker.

Assumptions
~~~~~~~~~~~

When synchronising comments with remote bug trackers, Launchpad makes
the following assumptions:

1. **Unique comment ID's**. Every comment has a unique ID, so that we
   can talk to the bug tracker about sets of comments using only the
   unique ID. The ID can be a compound ID (i.e. bugnumber+commentnum or
   bug+timestamp+commenter) but it must be unique... we should be able
   to have APIs which pass a comment ID and the bug tracker should know
   exactly which comment we are referring to. Similarly, the bug tracker
   needs to be able to provide a list of comment ID's, and we should be
   able to know if we have the comment or not. The documentation for the
   API should define the format of a comment ID. For example, the
   documentation could say that "Comment ID's take the form of a
   positive integer, and reflect the database primary key on the
   BugComment table."

2. **Immutable comments**. We assume that comments are immutable. I.e.,
   the comment text and title never change. So, as long as we know we
   have the comment corresponding to a particular ID on their side, we
   don't need to ask for that comment again.

3. **Comment on one and only one bug**. We assume that a particular
   comment applies to a particular bug, and that each comment applies to
   only one bug, and that comments do not move from one bug to another.
   In other words, if we have been told that comment with ID "xyz" is
   for bug "qwerty", we never expect to see a comment with id "xyz" on
   any other bug.

4. **There is a "Launchpad" user in the remote bug tracker**. We assume
   that there will be a "user" in the remote bug tracker which denotes
   "Launchpad". That user may have an email address assigned to it. We
   do not assume any particular value for the email address, but we
   recommend that it either be `noreply-$bugtracker@launchpad.net`
   (which may or may not get human attention), or
   `noreply-launchpad@domain.com` in the case where the email address
   is required to be at a specific domain. The admins of that domain may
   in turn choose to forward email sent to that address to
   `noreply-$bugtracker@launchpad.net`, or `feedback@launchpad.net`.

    The user of Launchpad in that bugtracker is generally used as the "user" who makes comments on bugs, or files new bugs.

Required API Methods
~~~~~~~~~~~~~~~~~~~~

These are the methods that we expect the remote API to provide for
comment syncing. In order to be able to do syncing reliably we'll also
need the `time_snapshot()` and `get_bugs()` methods described above
to be implemented.

add_comment(): Add a comment to an existing bug
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's important to have some kind of unique non-changing id for comments,
so we can identify them and avoid importing the same comment twice.

-  **Input**: Remote bug id, comment text, title (optional)
-  **Output**: comment id, unique with the bug and non-changing.

get_comment(): Get comments by comment id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When getting information about bugs using the API above, we will mostly
only include the comment ids to save bandwidth. After deciding which new
comments we need to import, we want to fetch them separately, in a
single method call.

-  **Input**: a list of comment ids
-  **Output**: the comments with the given ids

Pushing information
-------------------

We want to make it easy for users to forward bugs to remote bug trackers
from within Launchpad. A Launchpad user will initiate the action and
Launchpad will execute it for the user. The user initiating the action
might not have an account on the remote tracker.

The special Launchpad user is the one that actually files the bug or
adds a comment in the remote tracker, not the person requesting the
action from within Launchpad. Launchpad won't give the remote tracker
the person's e-mail address due to privacy reasons. This is fine,
though, the remote tracker users can ask the real reporter questions.
Launchpad will relay all communication about the bug to/from the person
in Launchpad. This imples that the remote tracker trusts Launchpad to
relay comments back and forth.

Each API below has a recommended name (like "report_bug") but the name
can be varied if needed.

report_bug(): File a new bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Input**: Summary, description, product/component, launchpad bug id
-  **Output**: reference to the bug

set_launchpad_bug(): Set the corresponding Launchpad bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to improve collaboration between the two bug trackers, we'd
like the remote tracker bug to "know" what the corresponding bug is in
Launchpad. The remote tracker will need to be able to store the
Launchpad bug ID as an integer, for each bug in its database, and this
API would be used to set the value stored for any particular bug.

The can be only one link to a bug in Launchpad per bug in the remote
tracker.

-  **Input**: Remote bug id, Launchpad bug id
-  **Output**: the previous value, or null if it was not set

The Launchpad bug id passed could be null, which means that this
information is getting "unset".

The corresponding Launchpad bug should be displayed on the remote bug
page, as a number linked to the relevant bug at Launchpad.net, for
example: :literal:`LP #12345`

It may also be appropriate to display the corresponding Launchpad bug
number in other reports and pages. It should be possible for users of
the remote tracker to update the corresponding Launchpad bug number for
any given bug in the remote tracker directly.

get_launchpad_bug(): Retrieve the current Launchpad bug id for a given bugtracker bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the read operation that matches set_launchpad_bug.

-  **Input**: Remote bug id
-  **Output**: the current value, null if it is not set

Further information
-------------------

Feel free to reach out to the :ref:`Launchpad team <get-help>`. We'd love 
to hear your experiences.
