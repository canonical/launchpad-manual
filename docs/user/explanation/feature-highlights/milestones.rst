.. _milestones-exp:

Milestones
==========

.. include:: /includes/important_not_revised_help.rst

We've discussed projects and series, which are the major ways in which
we keep track of the progress of a free software project in Launchpad.

In general, most of Launchpad's tools allow you to group information at
the level of the series. For example, different series in the same
project can have different translations, and you can plan to fix bugs in
a given series or implement blueprints in a series.

Launchpad allows you to have strict control over the bugs and blueprints
that are planned for fixing or implementing in a given series. If you
want to, you can require that a project driver approve each bug or
blueprint that is linked to a particular series. In this way you can
ensure that you are only making commitments that the project can keep.
This is quite a heavyweight management approach, but it's useful for
large projects like Ubuntu. Smaller projects often just turn that
control off.

By contrast, milestones are a very lightweight way to organise a group
of bugs or blueprints

A milestone is a point in time, or a test release, for which you need to
keep track of a few bugs or blueprints. In Launchpad, you can easily
create a milestone, and then link bugs or blueprints to that milestone
as a way of saying "we think these items are worth keeping track of as
we get closer to that date".

Here's an example, the 1.0 milestone of Inkscape:

    https://launchpad.net/inkscape/+milestone/1.0

At the time of writing, it looked something like this:

Milestones are useful as a quick way to focus attention on a subset of
bugs or blueprints which are important over the next week or month,
before a specific point in time, or before a test release is made. They
are not as rigorous in terms of control: anybody can throw a bug onto
the list, or a blueprint. However, they are very useful for smaller
projects, or projects that don't have the resources to plan major
releases.