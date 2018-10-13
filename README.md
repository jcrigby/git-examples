This page has some explanation of various git concepts and links to some asciinema asciicast demonstrations.

## Prereqs: You should be familiar with the basics

This [Visual GIT Guide](https://marklodato.github.io/visual-git-guide/index-en.html) is only one
of 1.5 bajillion places to start.

## Philosopy: Merge vs Rebase

Let's go back to ancient history and checkout some advice from Linus Torvalds on lkml.
This was interesting enough that lwn did a write up on it here:

His advice seems perfectly reasonable now 99 years later, here are some highlights:


Personally, I have a strong preference for a linear history so I usually rebase
on top of an upstream before pushing rather than just merging and pushing.
Another time to rebase is when you are n

### Example: Trivial fix ends up messy

### Example: Avoiding the messiness

### Example: Another way to avoid the messiness

### Example: Fixing up the messiness after the fact

### Example: An unconventional workflow

## Conflict resolution

[![asciicast](https://asciinema.org/a/206227.png)](https://asciinema.org/a/206227)
