About Launchpad security
========================

This document is an overview of how Launchpad approaches security.
It includes advice on how to build and run Launchpad in a secure way.
And finally it shows how to report security issues.

Launchpad's security strategy is multi-layered and multi-facetted.

Architecture and system design
------------------------------
Launchpad is secure by design, which means that its architecture, its
components and all communication between components were designed to be
fundamentally secure.

We only use Ubuntu LTS releases, which gets professional security support.

We monitor updates of both system and :doc:`Python packages <pip>` closely,
and update or patch our systems and applications accordingly.

We use a restrictive network setup between all our systems, especially
for untrusted builders.
You can read more about the threat model for builds in `LP113`_ (internal
spec).

.. _LP113: https://docs.google.com/document/d/1im8CMxLRNxtt5H0zv461kSYSflN-YlxJ1UZG8_53D9A/edit

All traffic to Launchpad is secured by TLS, with the exception of package
downloads, which are cryptographically verified on the client side.

Component configuration
-----------------------
We take great care to configure our components in a secure way.

Our web servers are configured very strictly, e.g.

- we use HSTS
- we set the ``X-Content-Type-Options`` to ``nosniff``
- we prevent launchpad.net from being used in a frame

You can have a look at the configuration in `canonical-mojo-specs`_ inside
the ``launchpad-manual-servers`` directory, and you can verify the results via
`Mozilla's online analyzer`_.

.. _canonical-mojo-specs: https://launchpad.net/canonical-mojo-specs
.. _Mozilla's online analyzer: https://observatory.mozilla.org/analyze/launchpad.net

We also restrict user-uploaded content in size to prevent issues with
availability.

Our secrets are strictly separated from our source code.

Code
----
We do not use direct SQL statements, but rather use the
`Storm ORM`_. This prevents SQL injection issues.

.. _Storm ORM: https://storm-orm.readthedocs.io/en/latest/index.html

We are using Zope's mighty and fine-grained security framework which provides
a generic mechanism to implement security policies on Python objects.

Compared to other frameworks, the main difference is that we check security
policies on most object attribute accesses, not just at API boundaries.
The exception is when an object isn't wrapped in a security proxy, which is
typically either for the ``self`` parameter to a method, so object methods
don't go through the security proxy when accessing their own internal
attributes, or when ``removeSecurityProxy`` is explicitly used.

Checking at attribute access provides significant defense in depth and is
especially important given the interactions between visibility and mutability
rules of multiple objects found on many Launchpad pages.

You can learn more about how we use it in
:doc:`Handling security policies <../how-to/security>`.

Permissions
-----------
In general we follow the principle of least privilege.

Launchpad engineers do not have direct access to production instances.

Leveraging the mentioned Zope's security framework, we apply fine-grained and
strict access level permissions.

While all Launchpad engineers have permissions to provide basic support for
Launchpad users, only select roles have wider access to administrative
features and security-related areas.

Authorization
--------------
There is :ref:`extensive documentation <sign-web-requests>` for how the OAuth authorization
arrangements work for the webservice API.

Processes
---------
For all but the most trivial code and configuration changes we require a
review by another team member or by IS.

For DB changes we require a second review by an experienced engineer.

Security issues can always be escalated and Canonical's security team supports
us with expert knowledge when necessary.

Security monitoring
-------------------
While we do not have automatic security monitoring in place yet as of July
2023, Launchpad.net was recently pentested by an external security company.

Training
--------
Launchpad engineers are encouraged to stay up to date with modern security
practices.

Canonical offers a training budget which can be used for security training.

Further recommended reading:

- `OWASP top 10`_
- `Mozilla's web security guide`_

.. _OWASP top 10: https://owasp.org/www-project-top-ten/
.. _Mozilla's web security guide: https://infosec.mozilla.org/guidelines/web_security.html

Tooling
-------
Mozilla offers an excellent `web security analyzer`_, which provides a great
overview of the security state of a website.

OWASP's `Zed Attack Proxy`_ is a mighty open-source tool which intercepts
requests to the site under test and allows detailed security checks.

.. _web security analyzer: https://observatory.mozilla.org/
.. _Zed Attack Proxy: https://www.zaproxy.org/

Reporting
---------
Both security issues for Launchpad itself, for all listed projects, and for
e.g. malicious applications hosted on Launchpad, should be reported by
Launchpad's `bug reporting interface`_.
Please set the bug's visibility to either "Public Security" or "Private
Security" as appropriate.

.. _bug reporting interface: https://bugs.launchpad.net/launchpad-project/+filebug

Please be aware that Launchpad.net will send email in plaintext in response to
the bug reports.
