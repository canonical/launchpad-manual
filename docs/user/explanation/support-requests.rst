.. _filing-new-support-request:

Filing a new support request
============================

.. include:: /includes/important_not_revised_help.rst

So, you are going to file a new support request. Before you proceed, you
should look at existing tickets in order to find similar requests who
fit your needs. You can do so by looking at `support requests
page <https://launchpad.net/support>`__. This task is very important and
helps a lot in order to avoid to duplicate efforts. Remember, it is
always a win choice to spend some time here before attempting to insert
a new ticket.

Where to Practice
-----------------

If this is your first time with support requests and you do not feel too
confident with Launchpad support tracker, you can use the Launchpad
`staging
server <https://staging.launchpad.net/distros/ubuntu/+tickets>`__ where
you can insert and modify tickets as you like. It provides the same
environment you will find in the real world production Launchpad, but it
is wiped and updated with the production server data periodically, so
every operation you are going to make will be gone for good next time a
sync will be executed. Feel free to try it out!

Filing the support request
--------------------------

You can add a new ticket by clicking the ``Request Support`` link on the
top left edge of the page. A form will be displayed which asks you a
summary, which will be used as an initial subject of your ticket.

Try to follow these rules:

-  Be concise
-  Focus your question in a few words
-  Avoid espressions such as "help me" or "I have got a problem" without
   any clue about the real matter

Once you have provided a summary and clicked the ``Continue`` button, you
will be showed a list of tickets which resemble your summary. If you did
not search similar tickets before, this is the right time to do it. If
no ticket matches your request, provide a detailed description of your
problem and click the ``Continue`` button.

Your ticket has been inserted and everyone can post a comment or an
answer. That ticket will be marked as ``Open`` in the support tracker
page.

Managing support requests
-------------------------

Once a support request has been inserted, it is possible to make a lot
of things on it. Here is the main ones:

Posting comments
~~~~~~~~~~~~~~~~

When selecting a support request, a text box is shown at the bottom of
the page where you can insert your feedbacks about the given ticket.

You can also insert URLs by providing full address (such as
http://launchpad.net) or bug reports (with the syntax ``bug #number``),
even if the best way to do so is by linking it through the apposite
function as stated below.

There are three types of feedback a user can submit:

Additional information
^^^^^^^^^^^^^^^^^^^^^^

If you are ticket's reporter, you can provide additional informations by
inserting a detailed description in the text box and pressing the ``I'm
Providing More Information`` button.


Information and answers proposals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you think so, you can ask the reporter to provide more informations
on a given ticket by inserting your motivation in the text box and
pressing ``Add Information Request``. That ticket will be marked as ``Needs
info`` in the support tracker page.

If you are able to give an answer proposal to a given ticket, you can do
so by inserting a detailed description in the text box and pressing the ``Add
Answer`` button. That ticket will be marked as ``Answered`` in the support
tracker page.

Closing tickets
~~~~~~~~~~~~~~~

If you are ticket's reporter and you have received sufficient feedbacks
to satisfy your request, you are encouraged to close that ticket. You
can do that by providing a detailed description of the procedure
followed to solve a specific issue and clicking the ``I Solved my Problem``
button.

If one or more users posted an answer, you can choose which one solved
your problem by clicking the ``This Solved my Problem`` button located in
the given answer box.

This way user who posted that answer proposal will be marked as the one
who solved that ticket.

Once a ticket has been closed, it no longer remains in pending requests
pool but it is marked as ``Solved``. This helps new users a lot because
they can find a solution quicker than inserting a new ticket.

Linking existing bug
~~~~~~~~~~~~~~~~~~~~

The best way to report the existence of a bug report related to a ticket
is by clicking on ``Link Existing Bug`` on the top left edge of the page.

You will be asked to insert the number of the bug you wish to link. By
clicking the ``Link`` button, a new box will appear on the right of the page
which lists the bugs currently linked.

Once a bug is linked, you can remove it by clicking on ``Remove Bug
Link``. You have to select which bug(s) you want to remove and click the
``Remove`` button.

Editing requests
~~~~~~~~~~~~~~~~

If you ever need to modify the summary or the description of a support
request, you can easily do so by clicking on ``Edit Request``.

Here you can specify a new summary which best describes a given ticket
or edit its description. This way you can fix typos too: some tickets
are redundant because reporters chose to open a new request in order to
fix such errors.

If you think a ticket should be assigned to a specific package, you can
modify it by inserting the chosen one directly in the text box on the
bottom of the page or by clicking the ``(Choose...)`` link on the right,
where you will be able to search among the package list in order to find
the right one.

Reopen requests
~~~~~~~~~~~~~~~

If you previously closed a ticket and you feel the need to reopen it,
you can do so by inserting a valid reason to do so and clicking the ``I'm
Still Having This Problem`` button. That ticket will be marked as ``Open``
in the support tracker page.

Support contacts
----------------

Support contacts users receive a copy of new tickets, comments, answers
and every event generated by the support tracker. Anyone can join
support contacts by clicking on ``Support Contact`` link on the top left
edge of the page. Users who are support contacts have some additional
abilities in support tracker management.

Rejecting tickets
~~~~~~~~~~~~~~~~~

Support contacts have the option to reject tickets by clicking on
``Reject Request`` on the top left edge of the page. They will be asked to
provide a short description meant to explain why that ticket should be
rejected. That ticket will be marked as ``Invalid`` in the support tracker
page.

There are situations where you are encouraged to reject support requests
such as:

-  Duplicate tickets (by reporting a valid one)
-  Test tickets
-  Offensive content

Sometimes it is not advisable to reject a request, e.g. a user placed an
heavy critic about a feature she do not like (see `ticket
#1601 <https://launchpad.net/distros/ubuntu/+ticket/1601>`__).