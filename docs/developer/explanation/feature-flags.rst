Feature Flags
=============

.. include:: ../../includes/important_not_revised.rst

**Feature Flags allow Launchpad's configuration to be changed while it's
running, and for particular features or behaviours to be exposed to only
a subset of users or requests.**

Please note, that any changes to feature flags need to be 
`recorded <https://docs.google.com/document/d/1lxQJJWL2VD3mgCLp-KqDRxPYrhHv-020hn9qd2wL07Q/edit?tab=t.0>`__.

Key points
----------

-  Guard new potentially-dangerous or controversial features by a flag.
-  Make sure the documentation is clear enough to make sense to a LOSA
   in a high-pressure situation; **don't assume** they will be familiar
   with the detailed implementation of the feature.

Scenarios
---------

-  Dark launches (aka embargoes: land code first, turn it on later)
-  Closed betas
-  Scram switches (e.g. "omg daily builds are killing us, make it stop")
-  Soft/slow launch (let just a few users use it and see what happens)
-  Site-wide notification
-  Show an 'alpha', 'beta' or 'new!' badge next to a UI control, then
   later turn it off without a new rollout
-  Show developer-oriented UI only to developers (e.g. the query count)
-  Control page timeouts (or other resource limits) either per page id,
   or per user group
-  Set resource limits (e.g. address space cap) for jobs.

Concepts
--------

A **feature flag** has a string name, and has a dynamically-determined
value within a particular context such as a web or api request. The
value in that context depends on determining which **scopes** are
relevant to the context, and what **rules** exist for that flag and
scopes. The rules are totally ordered and the highest-priority rule
determines the relevant value.

Flags values are strings; or if no value is specified, \`None`. (If an
empty value is specified, the flag's value is the empty string).

For a list of available flags and scopes see
https://launchpad.net/+feature-info

Priority
--------

Priority is exposed as an integer that gives a total order across all
rules for a particular flag. The numerically highest priority wins. `For
example <https://bugs.launchpad.net/launchpad/+bug/669942>`__ with these
rules

::

   hard_timeout team:admins 1 18000
   hard_timeout default 0 15000

the first rule has a higher priority (1 > 0). So that rule is evaluated
first, and it will match for anyone in ~admins. If that doesn't match,
the second is evaluated and it is always true. So admins get a 18s
timeout, and everyone else 15s.

Operations
----------

A change to a flag in production counts as a production change: it is
made by the Launchpad team on request. Make the change `on the appropriate
documentation page <https://docs.google.com/document/d/1lxQJJWL2VD3mgCLp-KqDRxPYrhHv-020hn9qd2wL07Q/edit?tab=t.0>`__
(sorry, company internal), including `an approval per the usual
policy <https://wiki.canonical.com/Launchpad/PolicyandProcess/ProductionChangeApprovalPolicy>`__,
and then ask in
`~launchpad-private <https://chat.canonical.com/canonical/channels/launchpad-private>`__.

Feature rules are loosely coupled to code changes: you can activate
rules before the code they control is live.

Web interface
-------------

-  https://launchpad.net/+feature-rules shows the currently active
   rules. This is visible to ~launchpad (developers etc) and writable by
   losas
-  https://launchpad.net/+feature-info describes the available features
   and scopes.

Debugging
---------

A html comment at the bottom of rendered pages describes which features
were looked up, and which scopes were consulted to make that decision.
This doesn't include features that could be active but aren't relevant
to the page, or scopes that may be active but aren't relevant to
deciding the value of the features.

Performance
-----------

Feature flags are designed and intended to be fast enough that they can
be used as much as is useful within reason. The result of a flag and of
a scope is checked at most once per request.

If the page does not check any flags, no extra work will be done. The
first time a page checks a flag, all the rules will be read from the
database and held in memory for the duration of the request.

Scopes may be expensive in some cases, such as checking group
membership. Whether a scope is active or not is looked up the first time
it's needed within a particular request.

Naming conventions
------------------

Flag naming
~~~~~~~~~~~

Flags should be named as

**``area.feature.effect``**

where each of the parts is a legal Python name (so use underscores to
join words, not dashes.)

The **area** is the general area of Launchpad this relates to: e.g.
'code', 'librarian', ...

The **feature** is the particular thing that's being controlled, such as
'recipes' or 'render_time'.

The **effect** is typically 'enabled', 'visible', or 'timeout'. These
should always be in the positive sense, not 'disabled'. If timeouts are
given, they should be in seconds (decimals can be given in the value.)

Scope naming
~~~~~~~~~~~~

Scopes are matched using a simple regexp and for those that take
parameters they are separated by a colon, e.g. ``team:admins``.

There is no way at present to give a rule that checks multiple scopes or
any other boolean conditions. You need to either choose one to match
first, or add a new scope that matches just what you need, or extend the
feature flag infrastructure to evaluate boolean expressions.

Reading a feature flag
----------------------

-  Python code: lp.services.features.getFeatureFlag(name) => value

-  TAL code: hello world!"

.. note:: 

    ``features/name`` may not work! If you get a ``KeyError`` for
    ``features``, try ``request/features/name`` instead.

You can conditionally show some text like this

::


     <tal:survey condition="features/user_survey.enabled">
       &nbsp;&bull;&nbsp;
       <a href="http://survey.example.com/">Take our survey!</a>
     </tal:survey>

You can use the built-in TAL feature of prepending ``not:`` to the condition,
and for flags that have a value you could use them in ``tal:replace`` or
``tal:attributes``.

If you just want to simply insert some text taken from a feature, say
something like 

.. code::
        
    Message of the day: ${motd.text}

Templates can also check whether the request is in a particular scope,
but before using this consider whether the code will always be bound to
that scope or whether it would be more correct to define a new feature:

::

     <p tal:condition="feature_scopes/server.staging">
       Staging server: all data will be discarded daily!</p>

Boolean values
--------------

Frequently it is desired to have a boolean feature flag that can be used
to toggle something on or off.

Decide what the default should be with the flag unset and this should be
the \`False\` value of the boolean, so name the flag accordingly.

Then when checking the value do a bool() of the return value and use
that as the value of the flag.

This means that unset and the empty string are \`False\` and anything
else is \`True\` (note that this means that "false", "False", "off", 0,
etc. all mean \`True`)

For example

::

       if getFeatureFlag('soyuz.frobble_the_wotsits.enabled'):
           wotsit.frobble()

Adding and documenting a new feature flag
-----------------------------------------

If you introduce a new feature flag, as well as reading it from
wherever is useful, you should also:

-  Add a section in lib/lp/services/features/flags.py flag_info
   describing the flag, including documentation that will make sense to
   people not intimately involved with development of the feature. For
   example:

::

   # This table of flag name, value domain, and prose documentation is used to
   # generate the web-visible feature flag documentation.
   flag_info = sorted([
       ('code.recipes_enabled',
        'boolean',
        'enable recipes',
        ''),

The last item in that list is descriptive, not prescriptive: it
*documents the code's default behaviour* if no value is specified. The
flag's value will still read as None if no value is specified, and
setting it to an empty value still returns the empty string.

Adding a new scope controller
-----------------------------

Add a new class in

::

   lib/lp/services/features/scopes.py

and make sure it's in

::

   HANDLERS

in that file. (You'll normally do this by adding it to

::

   WEBAPP_SCOPE_HANDLERS

and/or

::

   SCRIPT_SCOPE_HANDLERS

depending on whether it applies to web app requests, scripts, or both).

Testing
-------

``FeatureFixture`` uses the testtools fixtures API to hook into your code. When
it is installed on a TestCase object, the fixture will be automatically torn
down and reset between tests, restoring all of the originally set flags.


.. note::

    There is one gotcha: all existing flags are wiped out by the
    fixture for the duration of the test. If you want them to carry over,
    you need to do so yourself.*

You can use the fixture three different ways:

- With the ``TestCase.useFixture()`` method
- As a context manager, using the ``with`` statement
- By directly calling a fixture instance's ``setUp()`` and ``cleanUp()`` methods

Here is some sample code demonstrating each:

.. code:: python

     from lp.services.features.testing import FeatureFixture
     from lp.services.features import getFeatureFlag


     class FeatureTestCase(TestCase):

       layer = DatabaseFunctionalLayer  # Features need the database for now

       def test_useFixture(self):
         # You can use the fixture with the useFixture() TestCase method:
         self.useFixture(FeatureFixture({'reds': 'on'}))
         self.assertEqual('on', getFeatureFlag('reds'))

       def test_with_context_manager(self):
         # Or as a context manager:
         with FeatureFixture({'blues': None}):
           self.assertEqual(None, getFeatureFlag('blues'))

       def test_setUp_and_cleanUp(self):
         # You can call a fixture's setUp() and cleanUp() directly.
         # This is good for use in doctests.
         flags = FeatureFixture({'greens': 'mu'})
         flags.setUp()
         self.addCleanup(flags.cleanUp) # or use a try/finally

For more details on using the fixture and other feature flag utilities,
check the module docs in ``lib/lp/services/features/__init__.py``.

For sample code, check:

-  ``lib/lp/services/features/testing.py``
-  ``lib/lp/services/features/tests/test_helpers.py``
-  ``$ grep -r FeatureFixture lib/lp/``

See also
--------
-  `bugs tagged feature-flags <https://bugs.launchpad.net/launchpad/+bugs?field.tag=feature-flags>`__
