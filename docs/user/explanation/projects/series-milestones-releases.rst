.. _planning-and-recording-releases:

Planning and recording releases
===============================

.. include:: /includes/important_not_revised_help.rst

Let's look at how you can use Launchpad to plan your project's development and to record releases:


* **Series:** parallel lines of development within your project, working towards a major release.
* **Series goals:** bugs or blueprints that will be fixed in a particular series.
* **Milestones:** points in the development of a series, such as future minor releases or release candidates.
* **Releases:** once a milestone results in a release of your software, you can turn it into a release in Launchpad.

Launchpad doesn't impose a particular workflow on your project, so you can pick and choose how you use Launchpad's development and release planning.

How bugs and blueprints are targeted is largely determined what you need to plan, and how the work is supported when the goal is complete. You can answer the question for yourself by exploring three axes that represent the destination, the journey, and continuity. Most projects favour one side of each axis, but will always use the other side when needed.

.. _series:

Series
------

When we think of the way a project organises itself, there are major lines of development from which releases are "cut". Typically these lines of development represent:


* **Development trunk:** this is the current "tip" of development across the core project community, representing the very cutting edge of work on that project. In general, the only releases made from the development trunk are snapshot, milestone or test releases to generate more widespread testing and feedback.

* **Stable and supported branches:** these represent the latest work on the stable versions of the project, which are still supported. If updated stable releases are to be made they will come from these branches.

* **Obsolete branches:** for major release versions that are now out of date and no longer updated. It's likely that work no longer happens on these branches.

We call each of these "major" lines of development a "series" because they represent a series of releases of the same major version.

In Launchpad, each series behaves almost like a sub-project, having its own:

* branches of code
* milestones - specific points in the roadmap leading to a release
* bugs marked as affecting that series
* bugs and blueprints proposed as goals for the series
* translation effort
* releases
* release manager.

For an example, take a look at the `OpenShot Video Editor <https://launchpad.net/openshot>`_ 
project. There you'll see a number of series each with their related milestones 
and releases.

Project maintainers and drivers can register series. When a driver registers a series, the user is also set as
the series release manager. Project maintainers and series release managers can create and manage milestones and releases.

Destination axis: Leading or trailing series?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A *trailing series* is created **after** the work is completed.


* The focus of development is always the same series: trunk, head, master, main, etc.
* The *trailing series* marks a interesting point in development.
* The *trailing series* is often a supported release that will get backports and bug fixes while main development happen in trunk.
* This approach is common for small projects or project tied to a non-distributed repository.
* Bugs and features are never targeted to a series.

A *leading series* is created **before** the work is complete.


* The *leading series* has a set of features and fixes it intends to complete.
* The *leading series* is the focus of development.
* Previous series are supported or obsolete...
* Except for experimental series, which are concurrent with the series that is the focus of development.
* This approach is more common in large projects or projects that use a distributed repository.
* Bugs and features may be targeted to a series.

Creating series
~~~~~~~~~~~~~~~

To create a series, provided you're either the project's owner or driver, click Register a series
in the Series and milestones section of your project overview page.

Different projects have different ideas of what a series represents and what naming convention to use.
For example, in the GNOME project, the "development trunk" is a series with an odd version number, such
as 2.17. When it is ready for release, it is branched with an "even" version number, such as 2.18. Once
GNOME make the stable release, they branch it to create 2.19, the new "trunk".

Sometimes, projects also call the trunk "MAIN", a term from the days of CVS.

You can name and use your series however you choose in Launchpad. However, for convention,
we suggest you follow the *trailing series* model. We encourage you to call your project's development focus
"trunk" and to use that same branch for development over time. When creating a new stable series, such as the
line of development for your next major release, we suggest you:


* branch from trunk
* create the new series
* register your new branch in Launchpad and link it to the new series
* leave trunk in place for ongoing development.

This ensures that people who create a branch of "trunk" always get the tip of your development,
rather than discovering later on that it has turned into a stable release.

This last point is not entirely true, Launchpad allows projects to use ``leading series`` without
the need to rebranch the focus of development. You can choose the series that is the focus of development.
This changes were ``lp:your-project&gt;`` points to. Anyone who branches or pulls using the short-hand
URL will always get the branch associated with the focus of development series.

You can tell people the purpose of each series with a short description. 

.. _milestones:

Milestones
----------

Milestones are specific points during the life of a series, such as:

* beta tests
* release candidates
* minor and major point releases.

They're an ideal lightweight way to group a number of bugs and blueprints, optionally targeted to a particular date.

Just like series themselves, you can target individual bugs and blueprints to a particular milestone.
However, they differ in a couple of important ways:

* only a project owner, driver, series release manager or bug supervisor can target a bug or blueprint to a milestone: other people cannot nominate a chunk work for a milestone

* milestones exist within a series -- your project must have at least one series.

  Milestones naturally lead to releases. Once the software associated with the milestone is released, you can turn that milestone into a release in Launchpad.

* milestone names are unique to a project. Two series cannot have the milestones with the same name. There can be only one project 1.1.beta milestone to ensure there is no ambiguity about project release names.

Journey axis: Time-directed or feature-directed milestones?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A time-directed milestone restricts development by time.


* The milestone is complete when the date is reached.
* Time-directed milestones are by their nature, the series; work happens in one milestone at a time.
* Work is focused on the current milestone.
* Incomplete work is moved to another milestone or untargeted when the milestone's date is reached.
* If a bug is fixed from a another milestone, it is targeted to the current milestone.
* Time-directed milestones emphasises cadence; delivering value to stakeholders at regular intervals.
* Time-directed milestones requires more commitment from the developers to deliver work on schedule.

A feature-directed milestone restricts development to a feature.


* The milestone is complete when the feature is complete; there is no expected completion date.
* A series may have several feature milestones working in parallel.
* Feature-directed milestones allow multiple developers/teams to work independent or each other (models real behaviour).
* Feature-directed milestones are harder to manage since the manager (and hopefully not the team or developer) must change focus often.

Working with milestones
~~~~~~~~~~~~~~~~~~~~~~~

You can use both kinds of milestones to plan your series.

* Use feature-directed milestones to represent the goals of the series.

  They are commonly named ``future`` or ``horizon`` , but naming it after the series is most clear to users: 'Series3.1' or 'series future'

* Use time-directed milestones to represent cadence and to target work that really has a date to complete.

  * Create a milestone that represent dates that features and fixes must be committed to the code base by.
  * Create a milestone for each development release you plan.

* Move fixes and features from the series milestone to other milestones.

  * Move low priority items to the current milestone only when you are certain the work will be completed.
  * Move high priority items to other milestones when developers will commit to meeting the dates.

* Use feature-directed milestones to when you need to work in parallel. You are free to move them to other series if you wish.
* If your goals are continuous, when a development series is complete rename the series milestone to the new series name. If you are using leading series, move the milestone to the new series.

Series goals
------------

As series tend to represent planned releases, it's useful to target bugs and blueprints to particular series. These are called series goals and must be approved by either the project or that series' release manager.

`AppArmor <https://launchpad.net/apparmor/>`_ is a project for a security module that protects linux systems by limiting the capabilities of individual applications. AppArmor drivers have accepted `bug 2105986 <https://bugs.launchpad.net/apparmor/+bug/2105986>`_ as affecting six of their series.

Only the bug supervisor for a project can nominate a bug or blueprint as affecting a particular series with the Nominate for release link.

As both these series represent separate code bases, implementing a bug fix in them may fall to different people. It's also likely that the bug will have a different implementation status and importance in each series. As you can see in the BeeSeek example, Launchpad tracks separate importance, status and assignee information for the same bug in each series. BeeSeek have chosen not to fix the bug in their Hive series but Andrea Corbellini has already committed a fix in the Honeybee series.

Launchpad excels at tracking how an individual bug affects different communities and contexts; we'll see more of that later in this guide.

Continuity axis: Continuous or discrete goals?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continuous goals are project goals to exist beyond the life of a series.

* Incomplete features and fixes for a series become the goals of the next series.
* The priority of fixes and features do not necessarily change from one series to the next.
* ``Trailing series`` development encourages continuous goals.

Discrete goals belong to the series and they are not important after the series.

* Incomplete features and fixes are untargeted.
* The incomplete features and fixes must re-evaluated for the next development series.
* The priority of each bug or feature will change because the goals of the new series changes.
* ``Leading series`` development encourages discrete goals.

Problems when targeting work to a series
----------------------------------------

* You cannot untarget a bug from a series. Targeting created a bugtask and that cannot be deleted! You can mark The series bugtask as invalid, but still clutters the interface.

   **This is incompatible with continuous goals.** `bug 211855 <https://bugs.launchpad.net/malone/+bug/211855>`_

* You cannot move a bug between a series and milestone. As you revise your plans, you need to move bugs to be find anytime in a series to a specific time, but you cannot.

* Targeting to series and milestones happen in separate places, and milestones are much easier that series.

* You can target a bug to be fixed in trunk or to a obsolete series, which makes no sense. Targeting rarely makes sense when working with *trailing series* with one exception, when you want to backport a fix in trunk to a supported series. `bug 424118 <https://bugs.launchpad.net/malone/+bug/424118>`_, `bug 369419 <https://bugs.launchpad.net/malone/+bug/369419>`_

* Series reporting appears to be broken. Viewing the bugs for a series does not show you the bugs targeted to the series' milestones. The milestone is just a subset of the series. If you move a milestone to another series, you know you are also moving the targeted bugs to that series. `bug 423692 <https://bugs.launchpad.net/malone/+bug/423692>`_, `bug 314432 <https://bugs.launchpad.net/malone/+bug/314432>`_

.. _releases:

Releases
--------

Launchpad helps you to record and publicise the actual details of your release, such as its release date and changelog. Each release shows up in the timeline on your project's Launchpad home page, providing a historical record of what happened and when.

Further information
-------------------

Making those files available for :ref:`download <making-your-project-files-available-for-download>` is what we'll look at next.
