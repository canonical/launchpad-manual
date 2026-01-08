.. _bug-triage-process-background:

Bug triage process background
=============================

Triage is the act of sorting bugs into different priority groups.

There are many conflicting sorts; everyone has their pet bug that should be 
'first'. The sort order we choose is from the project's perspective: we try to 
balance the needs of our users.

So, bug triage is: sorting bugs by importance-to-the-project, and these are the 
influences we try to strike a balance between in assessing that importance:

- Things affecting Launchpad project health.
- Things affecting stakeholders
- Things affecting other users

When a bug has been triaged, its status is set to "Triaged" in the Launchpad UI, 
and its importance is set to a value other than "Unknown".

Why triage
----------

This may be obvious, but having just a big bucket of open bugs isn't very 
efficient: there are more genuinely important issues to fix than engineers and,
as such, engineers will forget what things are urgent and what aren't.

Secondly, each of the groups of users whose needs we're trying to compromise 
between are interested in when things will get done. By sorting the bugs we 
provide a proxy metric for when tasks will be worked on.


How much triage is needed?
--------------------------
The world is dynamic and constantly changing; as such any sort we come up with 
for our bugs will be outdated pretty quickly. We could make the sort complete 
(so all bugs are ranked) and constantly refresh it. However this is inefficient. 
The only times the sort actually matters are:

-   when a new bug is being selected to work on (by project importance).
-   when a user is taking a decision based on how long until the bug is likely 
    to be worked on. For instance, they might decide to work up a patch, or 
    whether to use Launchpad at all.

So how much sorting is enough? Two interesting metrics are freshness and 
completeness.

If the sort is too old, bugs will be indicated as 'should be next to work on' 
that are not valid as that any more. Our priorities may change month to month 
but they rarely change faster than that : so we can tolerate things being 
months (or more) stale.

The sort is complete enough if the answers to 'what is an important bug to work
on now' and questions that users may ask (like 'how long till this will be 
worked on') get answers accurate enough... and how accurate do we need?

We answer that question in the :ref:`bug triage policy <triaging-launchpad-project-bugs>` 
itself.

Bug Importance
--------------

Bug importance in Launchpad is where we record the result of the triage process; 
we have 5 buckets we can use in Launchpad: critical/high/medium/low/wishlist.

We don't actually ever block a release based on having a particular importance 
bug - we block releases based on having regressions, which any commit can have 
- and we mark that on the bug mapping to the commit.

The buckets combine to give a partial sort: bugs in the critical bucket are 
sorted before bugs in the high bucket.

We can choose to use some or all of these 5 buckets.

How many do we need? A good way to answer that is to consider our hypothetical 
complete, fresh sort, and consider how many slices we'd need to make in it to 
answer questions well; we also need to consider what would change to those 
slices when things change (such as new things coming that sort to the front).

Also buckets have a cost : we need a ruleset for triage that will let us assign
bugs to buckets: every bucket makes the heuristics more complex.

Given that we have a freshness tolerance for most bugs of some months, that we 
don't want to update many bugs when a single bug shuffles in front, and that 
because we have more bugs coming in than we fix - we need three or perhaps four
buckets:

-   A topmost bucket that is generally empty and crisis bugs go into.
-   A default bucket that bugs we haven't picked out as being important enough 
    to sort above any other specific bug go into.
-   [optional] a bucket for bugs that are reasonably important but not extremely
    so
-  And a bucket containing bugs which are within the first 6 months of work

We map these buckets into:

-  critical : generally empty, bugs that need to jump the queue go here.
-  high: bugs that are likely to get attention within 6 months
-  low: All other bugs.
-  We don't use wishlist.

In this case, time-till-we-start-work offers some guidance on which bucket to 
put a bug in.