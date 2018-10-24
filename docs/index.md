This page has some explanation of various git concepts and links to some asciinema asciicast demonstrations.

## Prerequisites: You should be familiar with the basics

The git documentation has a basic [tutorial](https://git-scm.com/docs/gittutorial).
It contains the same info as what you get from man gittutorial if you have
the git man pages installed.

The git documentation also has the complete [ProGit book](https://git-scm.com/book/en/v2).
It does a better job of explaining everything here, so why are you here anyway?.

Don't forget the manpages, either on your local machine or [online](https://git-scm.com/docs).

This [Visual GIT Guide](https://marklodato.github.io/visual-git-guide/index-en.html)
may be useful if you are a visual thinker.

This [git cheat sheet](http://ndpsoftware.com/git-cheatsheet.html) is a great guide
to how different commands affect your working directory, index, local repository,
remote repository and stash.

The above cheat sheet has a link to a
[flow chart](http://justinhileman.info/article/git-pretty/git-pretty.png)
that guides you out of any git mess you find yourself in.

## Basics: Git log can show more than a straight history


## Philosophy: Merge vs Rebase

Let's go back to ancient history (2009) and checkout some advice from Linus
Torvalds that is still relevant today.
This was deemed important enough that LWN did a write up on it
[here](https://lwn.net/Articles/328436/) and the original email from Linus
is also on LWN [here](https://lwn.net/Articles/328438/).

The context is the Linux kernel mailing list and he is specifically addressing
what he expects from subsystem maintainers, however, the spirit of the message
is true more widely:

* Never rewrite aka rebase published history.
* Don't publish work-in-progress crap.

Pushing to a private remote repo does not constitute publishing.
Publishing is pushing to a repo that others will be consuming.

One excerpt from Linus explains why I always rebase locally:

> Keep your own history readable,
>
> Some people do this by just working things out in their head first, and 
> not making mistakes. But, that's very rare, and for the rest of us, we 
> use "git rebase" etc while we work on our problems. 

> So "git rebase" is not wrong. But it's right only if it's YOUR VERY OWN 
> PRIVATE git tree.

## Examples: How rebase can help you clean up your history

### Pathological Merge

In this contrived example a developer tries to push a trivial change but the
upstream keeps changing out from under him.
On each failure he pulls again with `git pull` which results in a merge commit.
Eventually he succeeds; however, the log is a mess.

<script src="https://asciinema.org/a/208164.js" id="asciicast-208164" async></script>

### Avoiding the messiness

In this example everything is the same as above except we add the `--rebase`
option to the `git pull` command.
The same number of attempts at pushing are required; however, the resulting
history is much cleaner.

<script src="https://asciinema.org/a/208158.js" id="asciicast-208158" async></script>

### Another way to avoid the messiness

### Fixing up the messiness after the fact

### An unconventional workflow

## Conflict resolution

[![asciicast](https://asciinema.org/a/206227.png)](https://asciinema.org/a/206227)


