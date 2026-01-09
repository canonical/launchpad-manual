.. _code-concepts:

Code Concepts
=============

In order to fully understand the **\`lp.code\`** modules, it helps to
have an understanding of a number of core concepts.

Registry objects are those Launchpad-wide objects that are shared
between the different Launchpad applications. The registry objects that
**\`lp.code\`** modules are associated with are:

-  Person
-  Product
-  Project
-  SourcePackage
-  Distribution
-  DistroSeries
-  DistributionSourcePackage

``  ''Please be aware of the confusion between ``\ *:literal:`\`Products\``*\ `` and ``\ *:literal:`\`Projects\``*\ `` in the codebase.  To the outside world a ``\ *:literal:`\`Product\``*\ `` is a project, and a ``\ *:literal:`\`Project\``*\ `` is a project group (or super-project).''``

There are a few major concepts in **\`lp.code\`** to do with branches:

-  `Branch <#branch>`__
-  `Merge proposal <#merge-proposal>`__
-  `Namespace <#namespace>`__
-  `Target <#target>`__
-  `Collection <#collection>`__

<<Anchor(branch)>>

Branch
------

The branch object in Launchpad refers to a real Bazaar branch.

A branch has an owner. The owner can be either an individual or a team.
The owner defines who can write to the branch.

A branch also has a target. There are three current targets:

-  PersonBranchTarget - these are \`+junk\` branches
-  ProductBranchTarget - these are branches associated with a product,
   sometimes called an upstream
-  PackageBranchTarget - these branches are associated with source
   packages. A source package is effectively tuple of a particular
   package name in a distribution series.

You almost never need to know about these objects though, since they are
IBranchTarget adapters: \`IBranchTarget(person)`,
\`IBranchTarget(product)`, \`IBranchTarget(source_package)`.

A branch also has a name.

Together the owner, target and name make the \`unique_name\` of the
branch.

<<Anchor(merge-proposal)>>

Merge proposal
--------------

A merge proposal (`BranchMergeProposal`) is used to record information
around the process of merging one branch into another.

In situations where feature branches are used, it is normal for each
feature branch to have a merge proposal for the main trunk branch. In
these cases the feature branch is the \`source_branch`, and the trunk is
the \`target_branch`.

The code review process happens around a merge proposal. People can
review and comment on the proposal, and proposals can be approved (or
rejected) to land on the target branch.

<<Anchor(namespace)>>

Namespace
---------

A namespace is (usually?) an owner and a target.

A namespace has exactly one branch collection associated with it. In
some sense, it **is** a branch collection. (is-a could mean inheritance
or adaptation).

A namespace is, conceptually, everything up to the last part of a
branch's unique name.

There's no hierarchy of branches beneath a namespace.

A branch belongs to exactly one namespace.

::

   IBranchNamespace
     target :: IBranchTarget
     getBranches() :: [IBranch]
     createBranch(*args) :: IBranch

<<Anchor(target)>>

Target
------

**Target** is the most nebulous of these concepts. A target is a thing a
branch is a branch \*of*, or perhaps a thing a branch lives on. A
product is a target, a source package is a target, a person's +junk area
is a target. A project (i.e. a collection of products) is not a target.

Each branch has exactly one target.

A target is not a namespace (in general). A +junk target is, at some
level, a namespace, but other targets are not (only because +junk is
associated with a person).

A target has a collection naturally associated with it: the collection
of all branches with that target. Does this mean a target is, in some
sense, a collection? Probably not.

::

   IBranchTarget
     context :: (registry object)
     collection :: IBranchCollection
     default_stacked_on_branch :: IBranch
     default_merge_target :: IBranch
     getNamespace(person) :: IBranchNamespace
     -- implemented by BranchTarget only.

<<Anchor(collection)>>

Collection
----------

A collection has no semantic value beyond being a collection. It need
not be tied to a specific registry object, namespace or target. "All
branches" is a special, well-known branch collection. A collection is
simply a clear API for "a bunch of branches". A collection is the
preferred way of talking about a bunch of branches in our code-base.

::

   IBranchCollection
     getBranches
     getMergeProposals
      - implemented using getBranches,
      - merge proposals where the source branch is in getBranches()
     # separately,
     # a bunch of filter methods.