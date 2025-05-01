Pre merge reviews
=================

.. include:: ../includes/important_not_revised.rst

Introduction
------------

All changes to Launchpad need to have a merge proposal discussing the
change. Read this document carefully for a description of the review
process and what it entails. We use Launchpad Code Merge Proposals to
manage this process.

What are Pre-Merge Reviews?
---------------------------

Pre-merge reviews are peer reviews of source code modifications. They
are one tool for finding defects in code changes to Launchpad. Some
knowledge sharing and tips n tricks can be shared via code review as
well, though that is a secondary (and low frequency) effect. We do code
reviews because it is easy when making non trivial (or even trivial)
changes to miss something that a second set of eyeballs will catch. This
is particularly the case in some areas of Launchpad which have deep and
unobvious coupling.

Pre-Implementation Call
-----------------------

We recommend that new contributors chat to an experienced developer
before committing a lot of time to a change: often a small amount of
discussion can make the coding time much shorter and less likely to run
into friction within the Launchpad code base or product needs.

If desired, a voice call can be held

-  the extra bandwidth of such calls can help avoid misunderstandings
   and get to the bottom of things much more quickly.

Experienced developers are also able to have such pre implementation
calls - and its particularly good to do them when working on an area of
the code base they are not already familiar with.

Working with PreMergeReviews
----------------------------

For pre-merge reviews to be effective, however, small modifications to
the development workflow are required. The main modification is, of
course, requesting peer review of your code changes before merging your
code into :doc:`Trunk <branches>`. The sections below go into the details
of how this is best performed. There is a crib sheet for getting a
branch merged on the WorkingWithReviews page.

Branch size limits
~~~~~~~~~~~~~~~~~~

Complex changes are harder to review and more likely to let harmful
changes into the code base. We use a limit of 800 lines for the diff of
a branch as a proxy metric for complexity: if the diff of your branch on
the merge proposal page has more than 800 lines a reviewer may well ask
you to break it into smaller pieces for targeted review. Note that 800
lines is simple a proxy metric: any reviewer can suggest that an overly
complex change be split into multiple simpler steps - even if the line
count in the diff is much smaller than 800. Conversely much longer
branches are ok if they are actually simple : the reviewer and proposer
need to talk about such cases.

What are reviewers looking for?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reviewers are checking both the design of your branch and the quality of
the code in it. The best way to understand what a review is looking for
is to read TipsForReviewers. (You can also use the CodeReviewChecklist
cheat-sheet to do a self-review.)

Use a branch
~~~~~~~~~~~~

All changes going into Launchpad require a branch with the change(s) on
it, and a merge proposal proposing those changes and explaining what the
change wants to accomplish, why its desired and how it goes about it.

You are responsible for your branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The central rule that is used in the Launchpad review process is:

**The coder is responsible for getting his branch through the review process.**

This means that you, as a coder, are responsible for

1. writing the code
2. requesting review (use Launchpad Merge Proposals)
3. finding a reviewer (ask an on-call reviewer on #launchpad-dev, or
    arrange with another reviewer)
4. dealing with review comments / requests
5. landing your change (You may land when the proposal is Approved)

The reviewer, conversely, is responsible only for two important things:

-  Reviewing requests in a timely manner, respond to requests on 
   ``#launchpad-dev``, review proposals on
   `+activereviews <https://code.launchpad.net/launchpad/+activereviews>`_.

-  Participating in follow-up discussion once a review is sent.
-  Be clear about things you are:
    * suggesting
    * requiring
    * asking for discussion or consideration
-  Set the status of your review
-  Set the status of the merge proposal, unless other requested
   reviews are outstanding

Requesting review
~~~~~~~~~~~~~~~~~

Before you request a review, you should make sure that

::

   make check

reports no errors after having first merged trunk, as fixing any broken
tests after a review might involve an unnecessary additional review
which could have been avoided.

Choosing to self review
~~~~~~~~~~~~~~~~~~~~~~~

If you are a **reviewer** then you can choose to review your own code
under some conditions.

Not all changes benefit from code review / are high enough risk to need
formal peer review. For instance (not exhaustive):

-  mechanical things (like moving code)
-  updating source deps
-  rollbacks
-  typo fixes
-  improvements to documentation

For many of these things a review may add value - but less value than
doing the review uses up. We want reviews to be a net win for the effort
being put into developing Launchpad, and so we should, once we're
comfortable people know how things should be, allow them to decide if a
particular change is an improvement on its own, or an improvement that
also /needs/ other input before landing.

Becoming a fully fledged reviewer is the trigger that marks our comfort
that a developer can make this assessment effectively.

There are some parts of the system that we do not currently permit self
review: UI changes.

To do a self review, do exactly the same thing as normal, but claim the
review yourself and vote approve.

To do a self review of database changes, you need to be a database
reviewer.

Dealing with reviews
~~~~~~~~~~~~~~~~~~~~

A thorough guide to dealing with reviews and finally merging your
changes is available at WorkingWithReviews.
