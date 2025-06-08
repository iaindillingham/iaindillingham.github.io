Title: Weeknotes
Date: 2024-09-13
Category: Weeknotes
Slug: weeknotes-2024-09-13

Weeknotes for the week finishing Friday, 13th September 2024.

This was my first full week as Katie's buddy.
We covered:

* setting up a GPG key
* the differences between a GPG key and an SSH key
* signing commits
* the pros and cons of HTTP and SSH for communicating with a remote repository
* a couple of useful key bindings; <kbd>Ctrl-l</kbd> (clear screen) and <kbd>Ctrl-r</kbd> (reverse search history)
* piping to `xclip` (not bad for week one!)

I was pleased we talked about empirical method ("hypothesis-driven development").
Katie seemed to embrace it!
We used it to test that Katie could sign her commits,
although this took longer than it should have taken because I misunderstood GitHub's UI.

I decided to learn more about [Tig](https://jonas.github.io/tig/) this week.
I got confused, because Tig wasn't doing what I wanted it to do.
But then I realised that I was thinking of it as a tool you open once per session,
when I should have been thinking of it as tool you open many times per session,
once for each task.
I set up a couple of useful key bindings, nonetheless.

Getting confused prompted me to learn more about [revision selection](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection)
and to find a well-hidden page in the Git docs called "[gitrevisions](https://git-scm.com/docs/gitrevisions)".
`^` and `~` started to make more sense, which meant `git log` started to make more sense too.

Finally, I learnt more about Git internals (Chapter 10 of [Pro Git](https://git-scm.com/book/en/v2)).
Understanding
[Git references](https://git-scm.com/book/en/v2/Git-Internals-Git-References)
better helped me work out why `git branch` didn't report the branch name, but `git status` did, for a newly-initialised repository.
Katie spotted the discrepancy when we were testing that she could sign her commits.
Thanks, Katie!
