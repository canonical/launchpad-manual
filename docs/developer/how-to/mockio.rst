.. _mockio-library:

MockIo library
==============

MockIo is a simple library to help you test code that does Y.io calls
by intercepting those calls and providing a server response of your own.

Files and namespaces
--------------------

MockIo is found in ``lib/lp/app/testing/mockio.js`` and its namespace is 
``Y.lp.testing.mockio``. The instrumentation helpers are in ``Y.lp.client``
because they need to be usable by production code.

Instrumentation
---------------

Before you can test your code you need to instrument it to intercept
Y.io calls. This is done by passing an extra argument to the function or
adding an attribute to an objects config. By convention this parameter
is called io_provider because it provides a replacement io method. 
During test you pass in an instance of MockIo via this parameter, in 
production you just leave it undefined (or pass in Y).

Here is an example for a class.

::

   var MyClass = function(config) {
       this.io_provider = Y.lp.client.get_configured_io_provider(config);
   };

   MyClass.prototype.do_something() {

       // Some code that prepares an url and an io_config for an xhr request.

       // This is where Y.io used to be called.
       this.io_provider.io(url, io_config);
   };

Here is an example for a simple function.

::

   var myfunc = function(param1, param2, io_provider) {

       // Some code that prepares an url and an io_config for an xhr request.

       // This is where Y.io used to be called.
       Y.lp.client.get_io_provider(io_provider).io(url, io_config);
   };

Mocking io calls in tests
-------------------------

Mocking happens in three steps.

::

   // 1. Create the MockIo instance.
   var mock_io = new Y.lp.testing.mockio.MockIo();

   // 2. Pass it to your instrumented code.
   Y.mynamespace.myfunc(param1, param2, mock_io);

   // 3. Prepare and send a response.
   mock_io.success({
       responseText: "['Some JSON data']",
       responseHeaders: {'Content-type': 'application/json'}
   });

   // Now you can check what the succcess handler in your code did.

The ``success`` method is a convenience method that calls the ``respond``
method and sets ``status`` to 200 and ``statusText`` to OK. You can also call
``respond`` directly and pass in your own ``status`` and ``statusText``. There is 
also a ``failure`` method which sends a status of ``500 Internal server error``.
Obviously, the latter will result in the failure handler being called.

The above example responds to the last request that your code sent out.
If your code sends out multiple requests, you have access to those
through the ``requests`` attribute of MockIo which is a list of all received requests. 
You can respond to a request via its ``respond`` method.

::

   var mock_io = Y.lp.testing.mockio.MockIo();

   // This time myfunc will issue two requests.
   Y.mynamespace.myfunc(param1, param2, mock_io);

   // Check that the requests were received.
   Y.Assert.areSame(2, mock_io.requests.length);

   // Respond to each request in whatever way is appropriate.
   mock_io.requests[0].respond({
       status: 200,
       responseText: "Some data"
   });

   mock_io.requests[1].respond({
       status: 404,
       statusText: "Not found"
   });

You can explicitly access the last request via the ``last_request`` attribute.

Already instrumented code
-------------------------

The Launchpad client has already been instrumented. When you instantiate
it, pass in a config with an ``io_provider`` attribute. As this usually happens 
in your code you will have to instrument it to receive the io_provider from 
your test harness.

An example is FormOverlay which now has an extra attribute ``io_provider``
which defaults to ``Y``. In your test simply configure FormOverlay with an
``io_provider`` attribute and set that attribute to an instance of MockIo.