Using Launchpad with Bazaar
===========================

.. toctree::
    :hidden:
    :maxdepth: 2

    Host your project on Launchpad with Bazaar <host-project-on-launchpad-with-bazaar>
    Create and publish branches <create-and-publish-branches>

Using Launchpad, you can publish `Bazaar <https://www.breezy-vcs.org>`__
branches or `Git <Code/Git>`__ repositories of your code and,
optionally, associate them with projects. You can also mirror Bazaar
branches that are hosted elsewhere on the internet and even import git,
Subversion and CVS repositories into Bazaar branches.

Thousands of people have done that already, meaning that Launchpad has a
huge directory of branches of code. You could think of it as a `code
supermarket <http://news.launchpad.net/general/the-great-source-code-supermarket>`__
because it's so easy to browse and get hold of the code you want.

Over the next few pages, we'll look at:

-  downloading and working with code that's hosted on Launchpad
-  hosting your code on Launchpad
-  working with a team on the same branch of code
-  proposing code merges and conducting code reviews
-  importing code from git, CVS and Subversion repositories

New to Bazaar or distributed version control?
---------------------------------------------

If you're already familiar with Subversion or CVS, it's worth noting
that Bazaar is a `distributed version control
system <http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/>`__.

So, with Bazaar, your workflow no longer looks like this:

1. jump through hoops to get read/write permission for a central code
   repository
2. check code out of that central repository
3. hack, hack, hack
4. commit code back to the central repository

Instead, Bazaar lets anyone create their own branch—with full version
control—of any other Bazaar branch. That gives everyone much more
freedom and tears down the barriers to new and drive-by contributors.
When you—as the owner of the main-line branch—want to use something that
appears in another branch of your project, Bazaar makes it supremely
easy to merge their work into the main-line.

Also see:

-  `Bazaar in five
   minutes <https://www.breezy-vcs.org/doc/en/mini-tutorial/index.html>`__
   to learn the basics of Bazaar and set it up on your local machine
-  and Ian Clatworthy's excellent \*[Distributed version control systems

   -  why and
      how](http://ianclatworthy.files.wordpress.com/2007/10/dvcs-why-and-how3.pdf
      "wikilink")\* (PDF).

You may also find it useful to read the Bazaar project's `guide to using
Breezy together with
Launchpad <https://www.breezy-vcs.org/doc/en/tutorials/using_breezy_with_launchpad.html>`__.

Where Launchpad comes in
------------------------

If you're new to distributed version control, this way of working may
seem a little chaotic. Launchpad helps tie everything together by:

-  providing one place to find and download all code associated with a
   project, whether that code's in official lines of development or
   branches owned by anyone else
-  making it easy to distinguish official project lines of development
   from unofficial branches
-  giving you free hosting for your code
-  linking branches of code to the `bug reports <Bugs>`__ and
   `blueprints <Blueprint>`__ that they address
-  offering public code review for proposed branch merges.

Next step
---------

Let's start by `finding and downloading <Code/FindingAndDownloading>`__
code using Launchpad and Bazaar.
