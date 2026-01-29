.. _your-account-karma:

Your account karma
==================

Karma is one way of showing how large a contribution someone has made in
Launchpad.

Almost everything you do in Launchpad helps you build karma. For example:

- Registering bugs
- Translating strings
- Answering support requests, etc.

Your karma is a reflection of the type of work you've done and when you did
it.

Karma is only attributed for work done in Launchpad and does not apply to 
items imported from other sources.

How Launchpad calculates your karma
-----------------------------------

Different sorts of work are often valued differently by the projects you work
with. When you work in Launchpad, it makes a note of actions that might be
valuable to the relevant community.

Then, once a day, Launchpad looks at all of the work you've done and gives
each action a score. The score it gives depends on:

- What sort of work you did - e.g. posting an answer to a support request that
  gets accepted may result in more karma than just posting a comment
- When you did the work

For example, if you answer a support request today, Launchpad will give you
the full score. Six months from now, that action counts for half the score.
After one year it drops to zero because karma decays over time, as
explained in the next section.

Your karma is the total of the score Launchpad awards you in each category of
work. Karma is recalculated daily to include any new actions and to reduce the
value of older ones, so your total reflects both fresh contributions and the
decay of past work.

Karma decays over time
----------------------

Over time, particularly if you are not as active as you used to be, you may
notice that your karma drops.

Launchpad reduces the karma it gives to older actions for two reasons:

- To reflect each individual's current work
- To give newer users the opportunity to catch up with longer-term users

How Launchpad calculates the score for each type of work
--------------------------------------------------------

Launchpad ensures that the total score in each application is in the same
range. For example, if the total karma for work in the Bug Tracker were 500,
but the total for the Answer Tracker were 1,000, Launchpad would tune each
category's score so the two are closer together.

To do this normalisation, Launchpad sums the karma awarded in each category,
calculates a scaling factor for each one, and multiplies everyone's karma in
that category by that factor. As these factors are recalculated daily,
you may see a little day-to-day wobble, but it evens out over time.

Viewing your karma
------------------

You can see your own karma in the summary section of your Launchpad profile
page.

You can also view a `breakdown of where you earned your karma
<https://launchpad.net/~/+karma>`_, along with a log of recent activities that
will count towards your score. (At present Launchpad only shows the last 25
karma-earning activities, and only the type of activity, not the specific
action: see `bug 275938 <https://bugs.launchpad.net/launchpad/+bug/275938>`_).
