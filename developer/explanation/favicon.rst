Favicons: Why so many files and what do they do?
------------------------------------------------

These files were generated from a single SVG file containing the logo (``lib/canonical/launchpad/images/src/Launchpad_square.svg``), using https://realfavicongenerator.net/.

* ``favicon.ico`` - Contains the ``16x16``, ``32x32``, and ``48x48`` versions of the favicon. Used by IE.
* ``favicon-16x16.png`` - The classic favicon, displayed in the tabs.
* ``favicon-32x32.png`` - For Safari on macOS.
* ``android-chrome-192x192.png`` - Used as the icon when the web application is added to the Android home screen.
* ``android-chrome-512x512.png`` - Used to show a splash screen when the web application is being loaded. See https://web.dev/add-manifest/#splash-screen.
* ``apple-touch-icon.png`` - Used by iOS when the web application is added to the iOS home screen. See https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html.
* `safari-pinned-tab.svg <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html>`_ - Used as the icon when the tab with the web application opened is pinned.
* `browserconfig.xml <https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/dn320426(v=vs.85)>`_ - Used by Windows to specify the tiles for pinned sites.
* ``mstile-*.png`` - Used by the tiles of various sizes on Windows 8 and newer versions of Windows.
* ``site.webmanifest`` - The web app manifest is a JSON file that tells the browser about your Progressive Web App and how it should behave when installed on the user's desktop or mobile device. A typical manifest file includes the app name, the icons the app should use, and the URL that should be opened when the app is launched. See https://www.w3.org/TR/appmanifest/ and https://developer.mozilla.org/en-US/docs/Web/Manifest.

For more details, see the `FAQ of the code realfavicongenerator site <https://archive.ph/CAqQm>`_.
