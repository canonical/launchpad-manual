Question Life-cycle
===================

The question ``Status`` attribute describes the current state of the
question. This attribute is displayed on the question's main page (well
hidden in the question portlet) as well as in most questions listing.

Status definitions
------------------

The statuses defined for a questions are:

``Open``: The question needs an answer. This may be because the quesiton is new or because a previous answer didn't solve completely the problem.

:literal:`Needs information`: More information is required from the reporter before an answer can be provided.

``Answered``: An answer was provided to the question. We don't know if this answer solved the user's problem or not.

``Solved``: The question received an answer and the owner confirmed that the problem is solved.

``Expired``: A question in the ``Open`` or :literal:`Needs information` states that doesn't see any activity for more than two weeks
is automatically set to this status.

``Invalid``: The quesiton's content isn't really a valid support or help question related to the project.

A question starts its life in the ``open`` state and will change its state automatically based on users' actions.

Actions that affect the question status
---------------------------------------

The following actions are possible on a quesiton and will change its
status in the described way.

1. A person (other than the reporter) comes in requests more information. When the status of the question is ``Open``, this will change it to
   :literal:`Needs information`.

2. The reporter provides more information on the problem. When the status of the question is :literal:`Needs information`,
   this will change it back to ``Open``.

3. A user gives an answer to the question. When the status of the question is ``Open`` or :literal:`Needs information`,
   this will change it   to ``Answered``.

4. The question owner indicates that he has found the solution to the problem himself. This will change the status of
   the question to ``Solved``.

5. The question owner confirms an answer given by another user. This will change the status of the question to ``Solved``.

6. After receiving an answer, the question owner replies that the problem still occurs. This will change the status of the
   question back to ``Open``.

7. After two weeks gone by with no new information added to a question in the statuses ``Open`` or :literal:`Needs information`,
   the question's status is changed to ``Expired``.

8. An answer contact or administrator rejects a question which contains spam or is a duplicate. This changes the status to ``Invalid``.

9. An administrator can change the status to an arbitrary value using the :literal:`Change status` link.