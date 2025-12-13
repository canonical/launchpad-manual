Launchpad Registry
==================

.. include:: ../../includes/important_not_revised.rst

The registry is a core domain that most all Launchpad applications
require. The code is primarily located in lp.registry and
lp.services.mailman.

Pillars
-------

Pillars are distributions, projects and project groups. They share a
common set of features.

| ``   * Name Blacklist: The rules that prevent names for being used either``
| ``   because of application restrictions or organisational ownership.``
| ``   * Announcements: They appear on pages and in RSS.``
| ``   * Application Configuration: The pages that allow owners to set where``
| ``   services are hosted and configure Launchpad usage.``

Projects
~~~~~~~~

Projects commonly produce software, art, or some work that can be used.
Projects have maintainers, and drivers, but are shared by communities
who make contributions according to their own interests.

| ``   * Licenses: The terms that govern the use, distribution and modification``
| ``   of the work produced by the project. <``
| ``>``
| ``   * Commercial subscriptions: The rules that permits proprietary projects``
| ``   to use Launchpad.``
| ``   * Project groups: A grouping of projects that provides aggregated views``
| ``   of bugs, blueprints, and answers. The group drivers are drivers of the``
| ``   projects.``

Distributions
~~~~~~~~~~~~~

Ubuntu's releases are mirrored by other sites.

| ``   * Mirrors: CD and archive mirrors of distribution releases.``
| ``   * Distribution mirror prober: The process that checks the freshness of``
| ``   mirrors.``

Series, Milestones, and releases
--------------------------------

Projects and distributions have series of milestones that mark progress
toward a goal (releases). Project releases are often associated with
tarballs or installers.

| ``   * Series: A sequence or grouping of goals that constitute an planned``
| ``   effort to produce a finished work.``
| ``   * Milestones: time-bases or feature-based goals.``
| ``   * Releases: A completed goal that culminated in a release of files that``
| ``   may by finished or be in an alpha or beta state.``
| ``   * Product release finder: A process to locates release files on remote``
| ``   sites and uploads them to Launchpad, possibly creating milestone and``
| ``   releases on series.``
| ``   * timelines: A representation of series, releases, and timelines.``

Source Packages
---------------

Distribution and distro series source packages summarise current and
historical uploads of packages.

| ``   * Source package names``
| ``   * Distribution source package``
| ``   * (Distro series) source package``
| ``   * Packaging links``

Persons
-------

Persons are users or teams registered either by a human or an import
process. Person may own, manage, or interact with Launchpad artefacts.

Users
~~~~~

Users represent a person. Most are registered by processes. Some users
are active, meaning that a human may authenticate to assume the identity
of a person.

| ``   * GPG``
| ``   * SSH``
| ``   * IRC``
| ``   * Jabber``
| ``   * Wiki name``
| ``   * Code of Conduct``
| ``   * Location``
| ``   * Karma``

Teams
~~~~~

Teams represents a group of users that discuss common issues or may
control Launchpad artefacts. Teams are mostly registered by users,
though some may be registered by an import process.

| ``   * Team membership``
| ``   * Team participation``
| ``   * Polls``
| ``   * Privacy``

