Title: Reflections on my first six months as a tech lead
Date: 2025-05-25

I became a tech lead in December 2024.
My team is small: just Alice, a junior developer, and me.
We were asked to work alongside researchers and health informaticians on the OpenPathology project
with the aim of designing, implementing, and evaluating dashboards.
Here, I'd like to reflect on my first six months as a tech lead,
rather than on the OpenPathology project.

What does the Bennett Institute expect of its tech leads?
We describe [the role][1] as about 80% leadership and about 20% hands-on engineering,
I haven't gone through my calendar,
but I feel that on average I've spent about 40% of my time on leadership
and about 60% of my time on hands-on engineering, ±10%.
However, both my team and the project are small,
and my team isn't responsible for all aspects of the project;
just the tech aspect.

We describe leadership as a mix of three activities:
line management,
providing support (coaching, mentoring, training),
and owning the architectural direction of the [OpenSAFELY][] platform.
It's structured around three weekly meetings:

* a one-to-one with Alice (about 30 minutes)
* a tactical meeting with the other tech leads (about 40 minutes)
* a strategic meeting with the other tech leads (about 40 minutes)

I was apprehensive about line management;
thoughts of filling in Word forms and approving annual leave depressed me.
For the most part, though, line management has been straightforward.
There *are* Word forms to fill in and there *is* annual leave to approve,
but I've found I can manage the former by blocking out time in my calendar
(and forgetting about the Word forms until the blocked out time arrives).
Similarly, managing the latter means clicking "Approve" every so often.
Hardly onerous!

The leadership activity I've found most rewarding is providing support.
I was Katie's buddy [from last September](<{filename}/Weeknotes/2024-09-13.md>) to this January
and I enjoyed helping her become an effective junior developer.
Being a buddy and being a tech lead are different;
I have more direct influence over Alice's career progression than I had over Katie's, for example.
However, providing support is common to both roles and I'm enjoying helping Alice just as much as I enjoyed helping Katie.
Answering questions about our systems and processes, and
having to think about how I know what I know, or whether I actually know it,
has helped me reason more effectively.
We've also taken some useful and interesting deep-dives that I wouldn't have taken otherwise:
nginx configuration and Django's `AppConfig` with Katie;
[just shebang recipes][2] and [Python design patterns][3] with Alice.

I don't think I've fully taken ownership of the architectural direction of the OpenSAFELY platform,
although I am writing a proposal for a feature that will touch several of our systems and processes.
Writing a proposal is hard,
and there always seem to be more [important and urgent][4] things to do.
Maybe the things *are* important but *aren't* urgent,
so I should schedule them rather then do them?
If I did, then my leadership/hands-on engineering split would move from 40/60 to 80/20.

Project management doesn't fit into any of the leadership activities.
I've found it rewarding, nonetheless.
Writing good issues, like all writing, is a skill.
There are more opportunities to practice this skill as a tech lead than as a senior developer
(*someone* has to write the issues, after all!).
There's also something about setting up a Kanban-style board
and watching the issues move across it from left-to-right that I find rewarding.

To summarise:
providing support and project management are rewarding;
line management isn't nearly as onerous as expected;
and taking ownership of the architectural direction of the OpenSAFELY platform needs more work.

Time's up!

[1]: https://gist.github.com/inglesp/ccfbe2f1c8480cd1717e37d07f560ed4#tech-lead
[2]: https://just.systems/man/en/shebang-recipes.html
[3]: https://python-patterns.guide/
[4]: https://untools.co/eisenhower-matrix/
[OpenSAFELY]: https://www.opensafely.org/
