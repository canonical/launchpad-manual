
Authenticate launchpadlib from a text-based browser
===================================================

Sometimes you may want to use launchpadlib-based applications without
benefit of a graphical browser. As of this writing, the Canonical
Launchpad team supports lynx for this purpose. Other users and Launchpad
contributors may support other text-based console browsers.

Selecting a browser
-------------------

Python's webbrowser module, which launchpadlib uses to start a browser,
looks at the BROWSER environmental variable to select a browser.
Therefore, even if you have multiple browsers installed, you can set
that value to control the authentication behavior.

For instance, if you want to run the `ec2 land` command (a tool to
test a Launchpad branch and then submit it to the shared development
branch if the tests pass) with lynx, try `BROWSER=lynx ec2 land`.

lynx
----

lynx is the text-based browser supported by Canonical Launchpad
developers.

You might encounter a "Forbidden" error from Launchpad complaining about
no REFERER header on the last step of the process. By adding the
following to /etc/lynx-cur/local.cfg , you should be able to proceed:

REFERER_WITH_QUERY:PARTIAL

Active bugs: https://bugs.launchpad.net/bugs/535456

elinks
------

Some users have reported success with elinks. Hints welcome!

w3m
---

Some users have reported success with w3m. Hints welcome!

Active bugs: https://bugs.launchpad.net/bugs/556927

links
-----

No users have reported success with links.

links2
------

No users have reported success with links2.

echo
----

If you have access to an open web browser in a separate window, you can
use the Unix 'echo' command to authenticate your OAuth application. This
is especially useful if you are using Gnome Terminal to run an OAuth
application on a headless server via SSH:


#. Run the console application using `/bin/echo` as the browser: \$
   BROWSER=/bin/echo tarmac authenticate
#. The URL to validate the OAuth token will be printed to the console:
   copy it to the clipboard
#. Open a web browser in a different window, paste the token URL into
   the address bar, hit Enter
#. Use the browser to grant the application access
#. Return to the window that contained the original console session, hit
   `Enter` to complete the token authentication
