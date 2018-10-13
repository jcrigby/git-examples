This page has some explanation of various git concepts and links to some asciinema asciicast demonstrations.

## Prereqs: You should be familiar with the basics

This [Visual GIT Guide](https://marklodato.github.io/visual-git-guide/index-en.html)
is only one of 1.5 bajillion places to start.

## Philosopy: Merge vs Rebase

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
> not making mistakes. but that's very rare, and for the rest of us, we 
> use "git rebase" etc while we work on our problems. 

> So "git rebase" is not wrong. But it's right only if it's YOUR VERY OWN 
> PRIVATE git tree.

### Example: Trivial fix ends up messy

<script src="https://asciinema.org/a/206227.js" id="asciicast-206227" async></script>

### Example: Avoiding the messiness

### Example: Another way to avoid the messiness

### Example: Fixing up the messiness after the fact

### Example: An unconventional workflow

## Conflict resolution

[![asciicast](https://asciinema.org/a/206227.png)](https://asciinema.org/a/206227)


