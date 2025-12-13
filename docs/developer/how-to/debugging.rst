Debug Stories/Pagetests
=======================

Debugging stories (a.k.a. pagetests) can be kind of a pain because they
build up state as they go. If a test fails down deep in the doctest,
and you want to see what the page really looks like at that point, you'd
normally have to manually click through each step in the doctest until
you get to the place that's broken.

But there's an easier way!

Just add this at the point where your pagetest is failing:

::

       >>> stop()

This is just a convenience wrapper around ``pdb.set_trace()`` except
that it also redirects ``stdout`` back to your console. When your pagetest
hits this line, you'll be dropped into the debugger. Now, go to a
different shell and type:

::

       % make LPCONFIG=testrunner run

(*Note from deryck: To get the above make run command working, I had to
use the value in os.environ['LPCONFIG'] obtained at the pdb prompt,
rather than just "testrunner"*)

This starts up the appserver, except that it will use the
``testrunner`` configuration. What's cool about that is that this
configuration attaches to the same database as the pagetest you're now
stopped inside of. Meaning, all that state your doctest has built up, is
available to your browser. So just hit the URL of the page that your
doctest is failing on, and see it in all it's wondrous, albeit borked,
glory.

Additionally, it is also possible to connect directly to the database
the page test is using.

::

       % psql -d launchpad_ftest

However, uncommitted transactions will not be visible in the database.
So if there is something particular you are trying to query, like a bug
subscription, you may need to add the following to the page test:

::

       >>> transaction.commit()

Debugging memory leaks
----------------------

The app servers and the Librarian install a signal handler to dump their
memory using `meliae <https://launchpad.net/meliae>`__. To make use of
that you just have to send the 44 signal to the appropriate process.
This will create a file named /tmp/launchpad-memory.dump (or
/tmp/librarian-memory.dump, for the Librarian), which you can debug
later.

In general, though, the leaks will happen in production, so the LOSAs
will give us a memory dump. Assuming you've got a ``memory.dump`` file, this
is how you load it:

::

       $ ./bin/py
       >>> from meliae import loader
       >>> om = loader.load('memory.dump')
       >>> s = om.summarize(); s

This will give you a nice summary of the kinds of objects that consume
the most memory. Something like:

::

   Total 704144 objects, 768 types, Total size = 129.5MiB (135823229 bytes)
    Index   Count   %      Size   % Cum     Max Kind
        0  108751  15  68190568  50  50 3146008 dict
        1  192992  27  16136424  11  62    6904 tuple
        2  162136  23  14850362  10  73   11103 str
        ...

You can then use that information to navigate the object tree as
described in `John Meinel's excellent
post <http://jam-bazaar.blogspot.com/2010/01/meliae-020.html>`__, and
hopefully find what's leaking.

Debugging With GDB
------------------

Some kinds of bugs (segfaults, hung processes, out-of-control daemons)
are hard to debug from within Python. See
`Debugging with GDB <https://wiki.python.org/moin/DebuggingWithGdb>`__ for how to debug them.

Debugging Core Dumps 
--------------------

A quick sketch of how to read core files produced from production machines by IS:

1. Have core dump files moved to ``osageorang``
2. Ensure you have access to ``osageorange``. You'll need to ping a member of IS on #launchpad-ops to get access; you cannot ssh from ``devpad`` to ``osageorange``.
3. Get ``pygdb`` (``lp:pygdb``) in your ``$HOME`` on ``osageorang``
4. Ssh to ``osageorange``, and do:

::

   schroot -c lucid-cat-amd64

This puts you in a chroot with the same packages installed as on production.

5. Then cd into pygdb dir and do something like:

::

   python backtrace.py -c $PATH_TO_FILE/core.XXX > ~/core.XXX-out.txt

6. Read output and profit! 


Debugging Buildd with the Visual Studio Code IDE
------------------------------------------------

Although we `set up Buildd in a
VM <https://dev.launchpad.net/Soyuz/HowToDevelopWithBuildd>`__, Unit
tests can be debugged in a visual & interactive way with Visual Studio
Code with below setup for remote ssh&debug.

::

   sudo snap install --classic code

Launch VSCode and install the "Python" and "Remote - SSH" extensions.
For the Python extension perform the install on the remote host (your
Buildd VM) as well.

F1 to open the command palette and type:

::

   Remote-SSH: Open SSH Configuration file

From the drop-down choose your home ssh config file (``~/.ssh/config`` -
if you don't have one create it and add your configuration). Add the
following entry to it (for Host I have the name of my Buildd VM and for
the IP of my Buildd VM):

::

   HostName


::

   Host buildd
       HostName xxx.xx.x.xxx
       User ubuntu
       IdentityFile ~/.ssh/buildd_rsa.pub

F1 to open the command palette and type "Remote-SSH: Connect to Host..."
and choose "buildd" from the drop-down. You might be prompted for the
password for the "ubuntu" user.

Once the ssh connection is established, go to the Explorer and "Open
Folder" -> ``launchpad-buildd`` (the git clone of the buildd repo on your
VM).

Configure the test framework (visual examples
`\here <https://code.visualstudio.com/docs/python/testing#_configure-tests>`__). 
For buildd choose unittests for the lpbuildd folder and the test*.py file pattern.

Tips:

1. Command palette opens with F1.

2. When the workspace is large and contains many files VS Code file
watcher is running out of handles (ENOSPC Error visible is you start
VSCode in terminal with): 

::

   code --verbose

Solution to this is: to see your current limit:

::

   cat /proc/sys/fs/inotify/max_user_watches

Add this line:

::

   fs.inotify.max_user_watches=524288

to /etc/sysctl.conf and then:

::

    sudo sysctl -p 

.

Special URLs
------------

Launchpad provides special URLs that can be used to help with debugging.

.. list-table:: URL Debug Options
   :header-rows: 1
   :widths: 10 100 10 10

   * - **URL element**
     - **Description**
     - **Availability**
     - **Example**
   * - ``++debug++tal``
     - Show the TAL declarations *in the HTML source code*
     - developer box
     - https://launchpad.test/++debug++tal
   * - ``++debug++source``
     - Show path to templates for a given view *in the HTML source code*
     - developer box
     - https://launchpad.test/++debug++source
   * - ``++profile++``
     - Get help on how to use the ++profile++ option.
     - developer box, [qa]staging
     - https://launchpad.test/++profile++ or https://qastaging.launchpad.net/++profile++
   * - ``++profile++sql``
     - See SQL queries used by the page.
     - developer box, [qa]staging
     - https://launchpad.test/++profile++sql or https://qastaging.launchpad.net/++profile++sql
   * - ``++profile++sqltrace``
     - See SQL queries and Python stack traces that led to them.
     - developer box, [qa]staging
     - https://launchpad.test/++profile++sqltrace or https://qastaging.launchpad.net/++profile++sqltrace
   * - ``++profile++show``
     - Show Python profile data and OOPS data, including SQL queries and timing.
     - developer box, [qa]staging
     - https://launchpad.test/++profile++show or https://qastaging.launchpad.net/++profile++show
   * - ``++profile++pstats``
     - Generate a pstats (Python standard library) profile file on the file system. Browser page gives you full path to generated file. **Note that, on [qa]staging, you will need to ask LOSAs to get you the file.**
     - developer box, [qa]staging
     - https://launchpad.test/++profile++pstats or https://qastaging.launchpad.net/++profile++pstats
   * - ``++profile++callgrind``
     - Generate a KCacheGrind profile file on the file system. Browser page gives you full path to generated file. **Note that, on [qa]staging, you will need to ask LOSAs to get you the file.**
     - developer box, [qa]staging
     - https://launchpad.test/++profile++callgrind or https://qastaging.launchpad.net/++profile++callgrind
   * - ``++oops++``
     - Record an OOPS report while still rendering the page correctly. The OOPS id is provided in the HTML source code.
     - ALL
     - https://launchpad.test/++oops++ or https://qastaging.launchpad.net/++oops++
   * - ``++form++``
     - Not a debug tool. Used for JS. Gives inner form HTML.
     - ALL
     - https://launchpad.test/~/+edit/++form++



Some of those can be combined, like: ``++debug++tal,source`` or
``++profile++show,pstats``.

``++debug++errors`` is not working currently, probably because of
Launchpad customizations. It is supposed to show tracebacks of errors
handled in the template.

Tracing SQL statements through STORM
------------------------------------

These can be useful when optimising pages to run fewer queries, as you
can see exactly when and what is executed rather than pulled from cache.

Tracing a full request
~~~~~~~~~~~~~~~~~~~~~~

Set ``LP_DEBUG_SQL=1`` environment variable before running ``make
harness`` or ``make run`` to get the SQL statements as they are run,
along with the start and stop times and the name of the database on
which the statement was run. Note that in a request the times are
relative to the start of the request. For scripts and ``make harness``,
the start time is always 0 and the stop time is the duration of the SQL
call.

Set ``LP_DEBUG_SQL_EXTRA=1`` to get all of the above, plus tracebacks
for every query execution, including template and traversal information.

When using ``make run``, these affect all requests while the server is
running, and output the value in the console.

Alternatively, to only look at a *single* request's values in the
browser, use ``++profile++sql`` instead, which includes the
information equivalent to ``LP_DEBUG_SQL=1``; or use
``++profile++sqltrace``, which gives you all of the information
equivalent to ``LP_DEBUG_SQL_EXTRA=1``. These are described above in
the "Special URLs" section.

Tracing a part of a request
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``from storm.tracer import debug; debug(True)`` will cause all
statements run by Storm to be written to stderr. ``debug(False)``
disables this behaviour.

Alternatively, if you find ``LP_DEBUG_SQL=1`` and/or
``LP_DEBUG_SQL_EXTRA=1`` handy but want more control turning it on and
off within a request, in the debugger you can make sure the
``LaunchpadStatementTracer`` is the first in the results of
``get_tracers`` and modify as needed. For instance, you can do the
following.

This gives output equivalent to ``LP_DEBUG_SQL=1`` but for only as
long as ``_debug_sql = True``:

::

   from storm.tracer import get_tracers
   get_tracers()[0]._debug_sql = True

This gives output equivalent to ``LP_DEBUG_SQL_EXTRA=1`` but for only
as long as ``_debug_sql_extra = True``:

::

   from storm.tracer import get_tracers
   get_tracers()[0]._debug_sql_extra = True

Tracing a code snippet
~~~~~~~~~~~~~~~~~~~~~~

Similar to the previous section, sometimes you want to look at the SQL
of just a certain slice of code, such as within ``make harness``. The
``StormStatementRecorder`` can be a useful tool for this.

Basic usage will get you the SQL run while the recorder is used:

::

   from lp.testing import StormStatementRecorder

   with StormStatementRecorder() as recorder:
       ...code that touches the DB goes here...

   print recorder

Printing the recorder gives you a full output of what happened. You can
also look at ``.statements``, ``.count``, and so on (use dir!).

You can get all tracebacks by passing ``True`` when you instantiate the
recorder:

::

   StormStatementRecorder(True)

Again, print the recorder to see the results.

You can conditionally get tracebacks by passing a callable that receives
a SQL query string and returns a boolean True if a traceback should be
collected, and False if it should not. The SQL will be normalized to
capitalization and space normalized. For example:

::

   StormStatementRecorder(lambda sql: 'STRUCTURALSUBSCRIPTION' in sql)

would get you tracebacks when the SQL has something to do with
structural subscriptions.

Getting more information in your tracebacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tracebacks from ``LP_DEBUG_SQL_EXTRA=1`` and
``++profile++sqltrace`` include extra information from page templates
and traversals to tell you the expressions and values being processed.
If you have functions or loops for which you'd also like to add your own
extra debugging information to the tracebacks, here is how.

If you don't plan on checking the change in, or if the string you want
already exists and does not need to be generated, just assign the string
with the extra information you want to the variable name.

::

   __traceback_info__

That string will then be included in the information for that frame in
tracebacks generated by this machinery, as well as in renderings of
tracebacks from the appserver.

If you plan on checking the change in, you should be more careful: we
only want to do the work if a traceback is rendered, not every time the
code path is traveled. Then you have two options. The first is to create
an object that will do the work only when it is cast to a string (in
``__str__``) and assign it to a variable named ``__traceback_info__``,
as above.

The second, more involved option is to assign a two-tuple to
``__traceback_supplement__`` . The first element of the tuple should be
a factory, and the second argument should be an iterable that is passed
to the factory as ``*args``. The factory should produce an object with
any or all of the following attributes:

- ``source_url``: Some string that represents a source. For page templates, this is the path to the template file.
- ``line``: A value castable to ``str`` that is presented as a line number.
- ``column``: A value castable to ``str`` that is presented as a column number.
- ``expression``: A value castable to ``str`` that is presented as an expression currently being processed (like a TALES expression).
- ``warnings``: An iterable of strings that represent some warning to communicate.
- ``getInfo``: A callable that returns some extra string.


Tracing SQL statements with PostgreSQL
--------------------------------------

Statement logging can be configured in ``postgresql.conf``, by setting
``log_statement`` to one of ``none``, ``ddl``, ``mod`` or ``all``
(`docs <http://www.postgresql.org/docs/8.3/static/runtime-config-logging.html#GUC-LOG-STATEMENT>`__).
The server needs to be reloaded (by ``SIGHUP`` or ``pg_ctl reload``) for
changes to take effect.

It can also be set for a session, user, or database:

.. code-block:: sql

   SET log_statement TO 'all';  -- 
   `docs <http://www.postgresql.org/docs/8.3/static/sql-set.html>`__

   ALTER ROLE launchpad SET log_statement TO 'all';  -- 
   `docs <http://www.postgresql.org/docs/8.3/static/sql-alterrole.html>`__

   ALTER DATABASE launchpad_dev SET log_statement TO 'all';  -- 
   `docs <http://www.postgresql.org/docs/8.3/static/sql-alterdatabase.html>`__

Once enabled, statements will be logged to
``/var/log/postgresql/postgresql-*-main.log``.

.. _tal-template-tracebacks:



Getting past "LocationError: 'json'" in TAL template tracebacks
---------------------------------------------------------------

If you're testing with a new TAL template (.pt file) and you get
nasty-looking tracebacks that says something about

::

     LocationError: (<lazr.restful.tales.WebLayerAPI object at 0xd932ccc>, 'json')

then try visiting the corresponding URL in the web services API. For
example, if https://bugs.launchpad.net/launchpad gets an unwieldy
traceback, then try
https://launchpad.net/api/beta/launchpad instead; you'll often get a
*much* more comprehensible error
trace that way.

Using iharness for digging error tracebacks
-------------------------------------------

If you are reading this, most probably you have noticed that when things
get wrong, ZOPE and TAL will rather give you a pointless
``**LocationError**`` without to much information about what is causing it.

To find out what exactly went wrong you can use ``make iharness`` and
investigate that specific ``LocationError``

Let's say that you got this error for ``language_translation_statistics``:

::

   LocationError: (<zope.browserpage.metaconfigure.SimpleViewClass
   from PATH_TO_TEMPLATE/template.pt object at 0xcf60fec>,
   'language_translation_statistics')

To start the testing/debugging environment (the harness) run:

::

   make iharness

Next you will have to import your classed and get your object. In our
example we were trying to get the *PerLanguageStatisticsView* for
*ubuntu['hoary']* series.

::

   from canonical.launchpad.webapp.servers import LaunchpadTestRequest
   from lp.our.module import  PerLanguageStatisticsView

   #create and initialize the view
   ubuntu = getUtility(ILaunchpadCelebrities).ubuntu
   view = PerLanguageStatisticsView (ubuntu['hoary'], LaunchpadTestRequest())
   view.initialize()

   #request the view key
   key = view.language_translation_statistics

Now you should see a more meaningful message.

Profiling page requests
-----------------------

You can generate
`KCacheGrind <https://apps.kde.org/kcachegrind/>`__ and
pstats (Python standard library) profiles of requests on your local
system.

On your developer machine, try going to
https://launchpad.test/++profile++ or
https://launchpad.test/++profile++/~mark/+archive/ppa . Inserting
++profile++ in the URL like this will give you instructions on how to
use the feature.

The ++profile++ mechanism has a number of features now, as described in
the "Special URLs" section above. For Python profiling, it can generate
immediate profiles in the browser (++profile++show), profiles on the
filesystem ready for kcachegrind (++profile++callgrind), profiles on the
filesystem ready for pstats (++profile++pstats),or combinations (such as
++profile++show,pstats).

If you want to use this on ``staging`` or ``qastaging``, this is
already set up for you. You may need to ask a LOSA to
temporarily increase the timeout for the page that you want to analyze
using the feature flags mechanism (e.g., if you want to profile
BugTask:+index pages, you'll need to ask LOSAs to add something like:

::

   hard_timeout   pageid:BugTask:+index   2   30000

to https://qastaging.launchpad.net/+feature-rules. That sets a timeout
of 30 seconds (30000 milliseconds).

You can also turn on a configuration variable to profile *every*
request. Edit ``configs/development/launchpad-lazr.conf`` and add the
following section:

::

   [profiling]
   profile_requests: True

Then start the development server and make **ONE** request to the URL
you wish to profile (in order to make a single request on pages that
make subsequent JS calls immediately on load, you may need to use wget
or similar):

::

   $ make run
   ... server starts...
   $ curl -k https://launchpad.test/ -o /dev/null
   # or
   $ wget --no-check-certificate https://launchpad.test

You can now load the resulting ``*.prof`` file into KCacheGrind

::

   $ kcachegrind 2010-07-20_10\:01\:46.680-RootObject\:index.html-OOPS-1662X1-Dummy-2.prof

The doc for these features is lib/canonical/launchpad/doc/profiling.txt
, but you may find that the ++profile++ overlay gives you sufficient
instructions, if you use that approach.

Profiling one part of your page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are working on a developer instance of Launchpad, you can also
insert calls directly in your code to profile certain code paths when
viewing pages. This will aggregate profiling calls within the request,
so you can do this around code that is called multiple times in the
request. Try something like this:

::

   from lp.services.profile import profiling
   with profiling():
       # Do the work that you want profiled here!

This will then generate a pstats file for you on the filesystem at the
end of the request, and give you the data in the browser as well.

Debugging production OpenID problems
------------------------------------

You can use the production OpenID provider to debug problems that can't
be reproduced with the test provider by changing
configs/development/launchpad-lazr.conf thusly:

::

    [vhost.testopenid]
   -hostname: testopenid.dev
   +hostname: login.launchpad.net

Debugging security proxy problems
---------------------------------

Ever wondered which attributes are protected on an instance and by which
permission? You can use debug_proxy to get the information you need.

Example make harness session:

::

   francis@Casteneda:~/canonical/launchpad/bug-365098$ make harness
   bin/harness
   execute_zcml_for_scripts()...
   Reading $PYTHONSTARTUP...
   Initializing storm...
   Creating the factory...

   >>> from lp.registry.interfaces.distribution import IDistributionSet
   >>> ubuntu = getUtility(IDistributionSet).getByName('ubuntu')
   >>> evolution = ubuntu.currentseries.getSourcePackage('evolution')
   >>> from lazr.restful.debug import debug_proxy
   >>> debug_proxy(evolution)
   'zope.security._proxy._Proxy (using zope.security.checker.Checker)\n    
   public: __eq__, __getitem__, __hash__, __ne__, _getOfficialTagClause, 
   all_bugtasks, bug_reported_acknowledgement, bug_reporting_guidelines, 
   bugtargetdisplayname, bugtargetname, bugtasks, closed_bugtasks, createBug, 
   critical_bugtasks, currentrelease, deletePackaging, development_version, 
   direct_packaging, displayname, distinctreleases, distribution, 
   distribution_sourcepackage, distroseries, enable_bugfiling_duplicate_search, 
   format, getBranch, getBranches, getBugCounts, getBugTaskWeightFunction, 
   getBuildRecords, getCurrentTemplatesCollection, getCurrentTranslationFiles, 
   getCurrentTranslationTemplates, getFirstEntryToImport, 
   getLatestTranslationsUploads, getMergeProposals, getPocketPath, 
   getSharingDetailPermissions, getSharingPartner, getSuiteSourcePackage, 
   getTemplatesAndLanguageCounts, getTemplatesCollection, 
   getTranslationImportQueueEntries, getTranslationTemplateByName, 
   getTranslationTemplateFormats, getTranslationTemplates, getUsedBugTags, 
   getUsedBugTagsWithOpenCounts, get_default_archive, has_bugtasks, 
   has_current_translation_templates, has_obsolete_translation_templates, 
   has_sharing_translation_templates, has_translation_files, 
   has_translation_templates, high_bugtasks, id, inprogress_bugtasks, 
   latest_published_component, latest_published_component_name, linkedBranches, 
   linked_branches, max_bug_heat, name, newCodeImport, new_bugtasks, 
   official_bug_tags, open_bugtasks, packaging, path, product, productseries, 
   published_by_pocket, recalculateBugHeatCache, releases, searchTasks, 
   setBranch, setMaxBugHeat, setPackaging, 
   setPackagingReturnSharingDetailPermissions, shouldimport, sourcepackagename, 
   summary, title, unassigned_bugtasks\n'

--------------

CategoryTipsAndTricks CategoryTesting