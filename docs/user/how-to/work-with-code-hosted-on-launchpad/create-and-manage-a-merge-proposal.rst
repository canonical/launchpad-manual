.. _create-and-manage-a-merge-proposal:

Create and manage a merge proposal
==================================

.. include:: /includes/important_not_revised_help.rst

Thanks to git's distributed model, you can get full access to the code of any 
repository hosted on Launchpad, with version control and history, right on your 
own machine.

That flexibility means you can start work on a project without having to
get special permissions to commit code. Of course, if you make changes
that you want to see integrated into the project's main line you need a
way of telling the main line's owner that you want to merge.

Launchpad and git make that easy. Git was made to merge: even
complex merges can be relatively easy. Launchpad helps look after the
community process of discussing whether a proposed merge is a good idea.

See also this description :ref:`code-review relationships <roles-in-code-review>`.

Propose a merge
---------------

When you've come to a stage in your development where you're ready to
merge your code into another branch registered against the project -
such as its main line - you can make a public merge proposal.

To do so, visit your branch's overview page, click ``Propose for merging
into another branch``, then follow the on-screen instructions.

Now, Launchpad will notify the proposed target branch's owner of your
proposal. Anyone viewing the overview page for your branch, or the
target branch, will also see a link to view the details of your
proposal.

The flow of this process
~~~~~~~~~~~~~~~~~~~~~~~~

Understanding how the Code Review process works may be a little tricky
to get the hang of, but once you have got the hang of it, then it's
really easy. If you're new to this process, this is how it works:

-  You submit your request to merge your branch into the main one (or
   whichever target branch interests you)
-  Wait for one of the target branch's reviewers to review your code,
   they'll either:

   -  Accept your code, and it will be merged.
   -  Modify your code slightly, then merge it.
   -  Tell you what to do with a :ref:`comment <launchpad-comment-parsing>`, marking your
      review as "Needs Fixing".

      -  If you're happy to, you do make the changes requested and push
         them into your branch. Then :ref:`comment <launchpad-comment-parsing>` back on your
         proposal that you have done that. You should now await further
         action.

   -  Reject the changes. At this point, you can either try again
      discuss with the branch owner how to make your changes acceptable
      or continue work in your own branch.

Manage the merge proposal
-------------------------

A merge proposal can be in one of several statuses, each representing
the proposal's current state in the review lifecycle, as described
above.

Several rules apply to the transitions in-between these statuses.
Transitioning to ``Approved`` or ``Rejected`` from ``Work in progress``
or ``Needs review`` needs the user to be a valid reviewer (branch owner
and designated reviewers).

Code review
-----------

Once you've proposed a merge, anyone who has a Launchpad account can
:ref:`comment <launchpad-comment-parsing>` and vote on the proposal. Taking part in a code
review is virtually hassle-free:

-  **No barriers:** anyone can take part, so long as they have a
   Launchpad account
-  **Convenient:** you can get updates and contribute using email, as
   well as the web interface.

Each review consists of votes - approve, abstain or disapprove - and a
threaded conversation much as you might find on a web forum or a mailing
list. If you're already familiar with :ref:`Launchpad Bugs <bugs>`, you'll
be right at home with code reviews.

As a subscriber to the branch or a participant in the code review,
you'll receive email updates each time someone adds a vote or message to
the review. Just as with the bug tracker, you can take part in the
review both by visiting Launchpad's web interface and by replying to any
of the emails you receive. In effect, each code review becomes an ad-hoc
mailing list that exists for the lifetime of the review.

If you want to make your vote specific to one aspect of the proposed
merge, you can add a tag. For example: if you wanted to vote disapprove,
based on the user interface, you could add a tag of *ui*.

For an example of a review, take a look at a `code review in the Storm project <https://code.launchpad.net/~therve/storm/binary-and/+merge/387>`_.

Use the email interface
~~~~~~~~~~~~~~~~~~~~~~~

Using the code review email interface is straightforward. Reply to an
email from the code review and your :ref:`comment <launchpad-comment-parsing>` is added to
the discussion in Launchpad.

If you want to include commands to modify the approval or status of the
review you must either sign your email with your GPG key that is
associated with your Launchpad account, or send through a trusted DKIM
sender such as GMail.

Here is the list of available commands:

.. note::
    You **must** start the command line with a space or your command will not be recognized.

-  ``review`` - inform the developer what you think of their changes

   -  ``review approve`` - approve the change (`alias <http://www.python.org/dev/peps/pep-0010/>`_: ``+1``)

   -  ``review disapprove`` - disapprove of the change (`alias <http://www.python.org/dev/peps/pep-0010/>`_: ``-1``)

   -  ``review abstain`` - abstain from deciding (`alias <http://www.python.org/dev/peps/pep-0010/>`_: ``-0`` and ``+0``)

   -  ``review resubmit`` - tell the developer to rework the change

   -  ``review needs-fixing`` - tell the developer that a few things need improvement (alias: ``needsfixing`` and ``needs_fixing``)

   -  ``review needs-info`` - tell the developer that you need more information (alias: ``needsinfo`` and ``needs-information`` and ``needsinformation``)

-  ``merge`` - either approve or reject the proposed change

   - ``merge approved`` - approve of the merge proposal (alias: ``approve``)
   -  ``merge rejected`` - reject the merge proposal (alias: ``reject``)

-  ``reviewer`` - add a new reviewer to the merge proposal

   - ``reviewer <name>`` where ``<name>`` is the Launchpad user name or email address of the new reviewer.

-  ``vote`` (deprecated: use ``review``)
-  ``status`` (deprecated: use ``merge``)

You can combine commands, so if you wanted to vote ``disapprove``, add a
tag of ``UI``, leave a :ref:`comment <launchpad-comment-parsing>`, and reject the merge
proposal, you'd write::

   This is a sensible change but I find the user interface confusing.

    review disapprove UI
    merge rejected

If you simply want to approve the proposal, using \`merge approved\`
will also implicitly add an equivalent \`review approve\` unless you
specify a ``review`` command separately.

Make the merge
--------------

Once you're ready to merge another branch into yours, follow the
instructions on the page.

Next steps
----------

You can pick choose which parts of Launchpad you want to use. However, when you use different parts of Launchpad together you can make them work together. Let's look at how you can :ref:`link bug report and blueprints to branches of code <link-a-bug-reports-to-a-branch>`.
