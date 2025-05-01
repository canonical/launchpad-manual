Branch information types
========================

Launchpad uses "information type" to determine who can know about a
branch. Anyone can see a branch that is Public or Public Security.
Private Security and Proprietary information types restrict who may know
about the branch to only the people that the project shares that
information with.

Branches that fix "Private Security" bugs can themselves be set to
"Private Security" to ensure only trusted people can see the branch.

Proprietary branches are a feature available on request for projects
with commercial subcriptions. For more information, see
`CommercialHosting <CommercialHosting>`__.

Bug sharing policies
--------------------

Visit the project's Sharing page. If the project has a `commercial
subscription <CommercialHosting>`__, set the "branch sharing policy" to
control the default information type of each branch and restrict what
types they can be change to.

When the policy is set to something "Proprietary, can be public", all
new branches are Proprietary. They are only visible to people that the
project shares Proprietary information with and the people that are
subscribed to the branch. The branch can be made public later. Set the
branch sharing policy to "Proprietary" to ensure branches can only be
proprietary, they cannot be changed without first changing the policy.

Non-commercial projects cannot set the branch sharing policy. Branches
are public by default, but can be change to public security if needed.

Share confidential information with trusted teams
-------------------------------------------------

Visit the project's Sharing page. Share the confidential information
types with the development team, and any other team that you trust to
see confidential bugs and branches.

See `Sharing <Projects/Registering#sharing>`__ to learn about managing
who can see confidential information.