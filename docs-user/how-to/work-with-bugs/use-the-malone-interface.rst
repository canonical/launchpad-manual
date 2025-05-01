Use the Malone (Launchpad) XMLRPC Interface
===========================================

Malone currently provides an XML-RPC interface for filing bugs.

Report a product bug
~~~~~~~~~~~~~~~~~~~~

We'll define a simple function to extract the bug ID from the URL
return value.

::

       >>> def get_bug_id_from_url(url):
       ...     return int(url.split("/")[-1])

       >>> login("test@canonical.com")

       >>> params = dict(
       ...     product='firefox', summary='the summary', comment='the comment')
       >>> bug_url = filebug_api.filebug(params)
       SQLObjectCreatedEvent: <Bug ...>
       >>> print bug_url
       http://launchpad.dev/bugs/...

       >>> from zope.component import getUtility
       >>> from canonical.launchpad.interfaces import IBugSet

       >>> bugset = getUtility(IBugSet)
       >>> bug = bugset.get(get_bug_id_from_url(bug_url))

       >>> print bug.title
       the summary
       >>> print bug.description
       the comment
       >>> print bug.owner.name
       name12

       >>> firefox_bug = bug.bugtasks[0]

       >>> print firefox_bug.product.name
       firefox

Report a distro bug
~~~~~~~~~~~~~~~~~~~

::

       >>> params = dict(
       ...     distro='ubuntu', summary='another bug', comment='another comment')
       >>> bug_url = filebug_api.filebug(params)
       SQLObjectCreatedEvent: <Bug ...>
       >>> print bug_url
       http://launchpad.dev/bugs/...

       >>> bug = bugset.get(get_bug_id_from_url(bug_url))

       >>> print bug.title
       another bug
       >>> print bug.description
       another comment
       >>> print bug.owner.name
       name12

       >>> ubuntu_bug = bug.bugtasks[0]

       >>> print ubuntu_bug.distribution.name
       ubuntu
       >>> ubuntu_bug.sourcepackagename is None
       True

Report a package bug
~~~~~~~~~~~~~~~~~~~~

::

       >>> params = dict(
       ...     distro='ubuntu', package='evolution', summary='email is cool',
       ...     comment='email is nice', security_related=True,
       ...     subscribers=["no-priv@canonical.com"])
       >>> bug_url = filebug_api.filebug(params)
       SQLObjectCreatedEvent: <Bug ...>
       >>> print bug_url
       http://launchpad.dev/bugs/...

       >>> bug = bugset.get(get_bug_id_from_url(bug_url))

       >>> print bug.title
       email is cool
       >>> print bug.description
       email is nice
       >>> bug.security_related
       True
       >>> bug.private
       True
       >>> sorted(p.name for p in bug.getDirectSubscribers())
       [u'name12', u'no-priv', u'ubuntu-team']
       >>> bug.getIndirectSubscribers()
       []

       >>> evolution_bug = bug.bugtasks[0]

       >>> print evolution_bug.distribution.name
       ubuntu
       >>> print evolution_bug.sourcepackagename.name
       evolution