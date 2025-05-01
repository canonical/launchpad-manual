Updating the global configuration for tests
===========================================

Launchpad's configuration is kept in a singleton instance of
``LaunchpadConfig``, and is available via
``from lp.services.config import config`` for production code.

``TestCase`` offers a convenience method to set or update values for testing.

.. code-block:: python

    class TestExample(TestCase):

        def setUp(self):
            self.pushConfig(
                section="artifactory",
                base_url="artifactory.example.com/",
                read_credentials="user:pass",
            )

``TestCase.pushConfig`` expects the section name as a string, and the keys and values
as keyword arguments.
