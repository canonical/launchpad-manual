The Malone xmlrpc interface
===========================

Malone currently provides an XML-RPC interface for filing bugs.

Synopsis
--------

::

   #!/usr/bin/python

   from xmlrpclib import ServerProxy

   s = ServerProxy("https://test@canonical.com:test@xmlrpc.launchpad.net/bugs/")
   s.filebug(dict(
       distro="ubuntu", package="mozilla-firefox",
       summary="the summary", comment="the description",
       subscribers=["foo.bar@canonical.com"]))

For the truly interested
------------------------

``   >>> from canonical.launchpad.xmlrpc import FileBugAPI``

``   >>> filebug_api = FileBugAPI(None, None)``

The filebug API
~~~~~~~~~~~~~~~

The filebug API is:

::

       filebug_api.filebug(params)

params is a dict, with the following keys:

| `` REQUIRED ARGS:``
| ``   *  summary: A string``
| ``   *  comment: A string``

| `` OPTIONAL ARGS:``
| ``   *  product: The product name, as a string. Default None.``
| ``   * distro: The distro name, as a string. Default None.``
| ``   * package: A string, allowed only if distro is specified. Default None.``
| ``   * security_related: Is this a security vulnerability?  Default False.``
| ``   * subscribers: A list of email addresses. Default None.``

Either product or distro must be provided. The bug owner is the
currently authenticated user, taken from the request. The return value
is the bug URL, in short form, e.g.:

``   ``\ http://launchpad.net/bugs/42

Examples
--------

First, let's define a simple event listener to show that the
ISQLObjectCreatedEvent is being published when a bug is reported through
the XML-RPC interface.

::

       >>> from canonical.launchpad.event.interfaces import ISQLObjectCreatedEvent
       >>> from canonical.launchpad.ftests.event import TestEventListener
       >>> from canonical.launchpad.interfaces import IBug

       >>> def on_created_event(obj, event):
       ...     print "SQLObjectCreatedEvent: %r" % obj

       >>> on_created_listener = TestEventListener(
       ...     IBug, ISQLObjectCreatedEvent, on_created_event)

Error Handling
--------------

Malone's xmlrpc interface provides extensive error handling. The various
error conditions it recognizes are:

Failing to specify a product or distribution.

::

       >>> params = dict()
       >>> filebug_api.filebug(params)
       <Fault 60: 'Required arguments missing. You must specify either a product or distrubtion in which the bug exists.'>

Specifying \*both\* a product and distribution.

::

       >>> params = dict(product='firefox', distro='ubuntu')
       >>> filebug_api.filebug(params)
       <Fault 70: 'Too many arguments. You may specify either a product or a distribution, but not both.'>

Specifying a non-existent product.

::

       >>> params = dict(product='nosuchproduct')
       >>> filebug_api.filebug(params)
       <Fault 10: 'No such product: nosuchproduct'>

Specifying a non-existent distribution.

::

       >>> params = dict(distro='nosuchdistro')
       >>> filebug_api.filebug(params)
       <Fault 80: 'No such distribution: nosuchdistro'>

Specifying a non-existent package.

::

       >>> params = dict(distro='ubuntu', package='nosuchpackage')
       >>> filebug_api.filebug(params)
       <Fault 90: 'No such package: nosuchpackage'>

Missing summary.

::

       >>> params = dict(product='firefox')
       >>> filebug_api.filebug(params)
       <Fault 100: 'Required parameter missing: summary'>

Missing comment.

::

       >>> params = dict(product='firefox', summary='the summary')
       >>> filebug_api.filebug(params)
       <Fault 100: 'Required parameter missing: comment'>

Invalid subscriber.

::

       >>> params = dict(
       ...     product='firefox', summary='summary', comment='comment',
       ...     subscribers=["foo.bar@canonical.com", "nosuch@subscriber.com"])
       >>> filebug_api.filebug(params)
       <Fault 20: 'Invalid subscriber: No user with the email address
       "nosuch@subscriber.com" was found'>

       >>> on_created_listener.unregister()