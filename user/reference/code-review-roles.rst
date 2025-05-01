Roles in code review
====================

This is a description of the various people who may be involved in code
review, their capabilities and the kinds of email they receive. There
may be considerable overlap. For example, a branch's review team will
commonly also be subscribed to code review on that branch, or the merge
proposal registrant will commonly also be the source branch owner.

Per-branch relationships
------------------------

Owner
~~~~~

Each branch has an owner, who is the only person or team, aside from
admins, who can write to the branch.

Review Team
~~~~~~~~~~~

Each branch may have a "review team". This is the group of people (or
person) whose reviews are trusted input for deciding whether to accept a
merge into this branch. By default, this team is requested to review any
new proposal to merge into this branch, but the merge proposal
registrant can specify an alternate reviewer. If the review team is not
set, the branch owner is used as the review team. This setting does not
cause any additional mail to be sent to members of the review team.

Subscribers
~~~~~~~~~~~

Each branch has zero or more subscribers. They may be subscribed to
metadata changes, revision updates, and / or code review. Subscriptions
allow the subscriber to control the kinds of email sent to them, and
also the size of branch update diffs. They allow an individual to
override the subscription settings their team may have. Subscribers to
code review are notified when this branch is the source or target of a
merge proposal. When a branch is created, we automatically subscribe its
owner to code review. In the future, we may also subscribe the review
team.

Per merge-proposal relationships
--------------------------------

In the descriptions below, "edit rights" includes:

-  setting the commit message
-  deleting the merge proposal
-  requesting a review
-  resubmitting the merge proposal

It does not include setting the status of the merge proposal, which is
restricted to the review team and branch owner.

Registrant
~~~~~~~~~~

The person who proposed the merge. This person has edit rights on the
merge proposal.

Source branch owner
~~~~~~~~~~~~~~~~~~~

The source branch owner has edit rights on the merge proposal.

Target branch owner and review team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

They have edit rights on the merge proposal. Their reviews are not shown
as "(community)". They can set the overall status of the merge proposal
(i.e. mark it "approved"/"rejected"/"work in progress").

Team Reviewers
~~~~~~~~~~~~~~

Teams who have been requested to review. Members of these teams may
claim their team's review. If a member of this team performs a review,
and the requested review type doesn't conflict with the specified review
type, the team review request is automatically reassigned to the
reviewer.

Review types are considered not to conflict if:

-  One of them is blank, or
-  both are the same

Individual Reviewers
~~~~~~~~~~~~~~~~~~~~

People who have been requested to review or who have performed reviews.
They receive all email about this merge proposal. If they have not yet
reviewed, they can only opt out by reassigning their review request.
Otherwise, they cannot opt out.

Commenters
~~~~~~~~~~

People who have made comments about the merge proposal. Being a
commenter does not cause them to receive email, and there is no way for
them to opt-in to email about this particular proposal.

They could subscribe to code review on the source branch, and this would
have the same effect as being subscribed to the merge proposal, as long
as no further merge proposals were made for the source branch.