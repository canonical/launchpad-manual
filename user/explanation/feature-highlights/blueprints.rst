Blueprints: lightweight specifications
======================================

Planning isn't quite the least-favorite thing for most free software
developers - but it's more or less in the same region as dealing with
spam.

The free software process is highly agile, with release management
policies that span the full range from "time based" (set the date and
forget the features) to "when it's done" (set the features and forget
the date). Launchpad doesn't aim to change the psychology of projects by
imposing any planning, but it does help projects to communicate
internally, and with other projects.

Launchpad tracks placeholders for each chunk of work, idea for
implementation or section of documentation that needs to be written. We
call those placeholders Blueprints. A Blueprint can be as little as a
single sentence, or a fully-fledged specification with data model and
user interface mock-ups. The level of detail required is entirely a
matter for the project to decide.

Each Blueprint belongs to a particular project. That means you can see
lists of all the ideas, proposals or suggestions that are "out there"
for a given project. For example, Ubuntu has more than 1,000 such
blueprints, in various states of completion or discussion:

`` ``\ https://blueprints.launchpad.net/ubuntu

At the time of writing, the most "important" of these blueprints were:

Blueprint status and priority
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each Blueprint has a priority, a "definition" status, and a "delivery"
status.

The priority is set by project leaders. Anybody can contribute
Blueprints for any project - there is no way to prevent someone from
posting their ideas. However, the project leaders can set the priority -
which means the extent to which they endorse the idea, or think it is
important to implement soon.

The "definition" status tells you whether or not the project has reached
consensus on how the idea should be implemented. In some projects there
will be a person, or team of people, who will approve the plan. In
others, plans are considered unnecessary or harmful, so this value is
less important. In Ubuntu, we try to have a senior contributor review
and approve any significant piece of work that is planned for any given
release. Of course, lots happens without these plans, but it does give
us some certainty that the various plans gel well, and that people have
thought about the most important issues before they commit to getting
something done in a particular release.

Finally, the "delivery" status is all about implementation and
execution. It tells you whether the work has been done, or whether it is
on track to be done.

Storing the detail of a Blueprint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad itself only contains a summary of the Blueprint - usually just
the introductory paragraph - and then a URL to the location of the real
document. In some cases, the single paragraph (or sentence) is enough,
but it's more typical to keep the full document in a wiki, where members
of the community can easily collaborate.

Just having a list of proposals and ideas in one place is useful, even
if, as in the case of Ubuntu, there are clearly many more ideas than
developers! It's convenient to be able to point new members of the
community at a single place where those ideas are cataloged and to allow
people to gravitate towards the pieces they are most interested in.
People can subscribe to Blueprints and get notifications when their
status changes and even when the wiki document they are in is updated.

Newcomers can easily see which ideas are important to the project
leaders, and which are not, so they can choose to focus their
contributions on those pieces most likely to be accepted into the
project.

Linking Blueprints
------------------

Launchpad allows you to link a blueprint and a bug, or a blueprint and a
branch of code. This allows people to see how pieces of work relate to
one another.

It's very useful, for example, to be able to see the code that
implements a blueprint evolving over time. It's also possible to link
blueprints to one another, indicating rough dependencies. This lets you
map out the order in which pieces should be implemented.

Release management
------------------

The most useful aspect of Launchpad's blueprint tracker, however, is the
ability to group the blueprints that describe chunks of work that the
project thinks are important to track for the next major series.

Here is the list for the Gutsy (7.10) release of Ubuntu:

`` ``\ https://blueprints.launchpad.net/ubuntu/gutsy

As you can see, this is a much shorter list of around 100 blueprints,
instead of 1100. These are blueprints that have been reviewed by the
team. At he beginning of the Feisty development cycle, the team planned
to implement those features.

In general, about 80% of the planned feature goals have landed in each
Ubuntu release. We choose to ship on time, rather than necessarily
waiting till every feature lands. However, different projects can adopt
different release management goals.

The important thing, of course, is that everyone can see where we stand
on any particular item.

Helping improve communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The blueprint capability in Launchpad is not designed for hard-core
project management. It doesn't offer Gantt charts or waterfall diagrams
or block out developers hour by hour. But it certainly can improve the
communication within a project, and between projects, about the status
of work that has been discussed. Organising blueprints by release helps
to communicate a clear picture of where any give release stands - what's
in, what might get in, and what's not going to make it.

The release management that we've described here is at the level of
major releases - what we call a series.

Sometimes you may want to group just the blueprints that are relevant
for an interim release. For that, we'll use milestones. And learning
about those is the `final stop on our
tour <FeatureHighlights/MilestoneUsage>`__.