Debug Tests with Visual Studio Code
===================================================

Debugging Launchpad tests in Visual Studio Code (VS Code) can streamline your
development process by allowing you to inspect code, set breakpoints, and
interactively solve problems within your tests. This guide will help you set up
VS Code for debugging Launchpad tests.

SSH Access to LXD Containers within VS Code
--------------------------------------------------

To run and debug Launchpad tests inside a local LXD container using Visual
Studio Code, you need to set up SSH access. This guide assumes that SSH has been
configured as described in the :doc:`Running <running>` section.

1. **Install the SSH Extension**: Install the 'Remote - SSH' extension from the
   VS Code marketplace to enable SSH capabilities within your development
   environment.

2. **Open Command Palette**: Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   and type 'Remote-SSH: Connect to Host', then select it.

3. **Select Your LXD Container**: Choose your previously configured LXD
   container from the list of available SSH hosts or add a new one.

4. **Start Working**: Once connected, VS Code will treat the container as a
   local environment. You can now navigate to your project directory and run or
   debug tests without any additional configuration changes.

Create the ``launch.json`` File
-------------------------------

First, you need to set up your debugging environment by creating a
``launch.json`` file in the ``.vscode`` directory at the root of your project.
This file will tell VS Code how to launch the debugger for your project's tests.
Here’s how the ``launch.json`` file should look:

.. code-block:: json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Debug Launchpad Tests",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/bin/test",
                "console": "integratedTerminal",
                "args": [
                    "-vvc", "-t", "${command:pickArgs}"
                ]
            }
        ]
    }

You can find this configuration file inside the
`dev-configs <https://code.launchpad.net/~launchpad/+git/dev-configs>`_
repository, under ``vscode/ruinedyourlife/launch.json``.

This configuration uses the Python debugger extension (``debugpy``) and
specifies that the debugger should start the ``test`` script located in your
project's ``bin`` directory, with verbose output. The additional test selection
arguments allow you to specify which test to debug; when you launch the
debugger, a pop-up window will appear, prompting you to input the test name you
want to debug using the ``${command:pickArgs}`` command.

Launch the Debugger
-------------------

After setting up the ``launch.json``, you can start the debugger using one of
the following methods:

1. **Command Palette:** - Open the Command Palette (``Ctrl+Shift+P`` or
   ``Cmd+Shift+P`` on macOS) and type 'python debugger'. Select ``Python
   Debugger: Debug using launch.json``.

2. **Debug Menu in Activity Bar:** - Click on the Debug icon on the left/right
   Activity Bar (or press ``Ctrl+Shift+D``), select the configuration you wish
   to launch (which are picked from your ``launch.json`` file), then click the
   green start icon at the top.

3. **Debug Icon in Tab Bar:** - At the top right, you'll see a debug icon with a
   dropdown for your debug configurations—select the ``Python Debugger: Debug
   using launch.json`` option. Select the configuration you wish to launch.

Additional Resources
--------------------

For more detailed information on debugging with Visual Studio Code, especially
for Python applications, refer to the `VS Code Python debugging documentation
<https://code.visualstudio.com/docs/python/debugging>`_.

To customize your debugging experience further, such as using conditional
breakpoints, logpoints, and more, consult the `VS Code general debugging
documentation <https://code.visualstudio.com/docs/editor/debugging>`_.
