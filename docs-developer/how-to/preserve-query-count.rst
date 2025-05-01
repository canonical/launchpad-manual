======================
Preserving query count
======================

Given you want to read or create many items instead of one,
you need to make sure that the number of queries stays constant.

In Launchpad this can be done by using `lp.testing.record_two_runs`,
as outlined in the following example:

.. code-block:: python

    def test_view_query_count(self):
        # Test that the view bulk loads artifacts.
        person = self.factory.makePerson()
        pillarperson = PillarPerson(self.pillar, person)
        recorder1, recorder2 = record_two_runs(
            tested_method=lambda: create_initialized_view(pillarperson, "+index"),
            item_creator=lambda: self.makeArtifactGrantee(
                person, True, True, True, False
            ),
            first_round_number=5,
            login_method=lambda: login_person(self.owner),
        )
        self.assertThat(recorder2, HasQueryCount.byEquality(recorder1))

For further information, please have a look at `record_two_runs`' docstring.
