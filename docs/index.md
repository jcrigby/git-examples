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

## Basics: Viewing history

### There is more to git log than you may think

Like nearly all git commands, git log has many options.
You probably already know about some of the standards,
with no option you get a basic log.
With `-p` your get diff output.
The `--stat` option gives you diffstat info.
An option that you may not have ever heard of is the `-g` for graphical
or at least as graphical as terminal output can be.

Adding lines like these to your .gitconfig give you three flavours or graphical
git log.

```
[alias]
    lg = !"git lg1"
    lg1 = !"git lg1-specific --all"
    lg2 = !"git lg2-specific --all"
    lg3 = !"git lg3-specific --all"

    lg1-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
    lg2-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
    lg3-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed: %cD)%C(reset) %C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset)%n''          %C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'
```

The `git lg3` version is demonstrated here:

<script src="https://asciinema.org/a/208167.js" id="asciicast-208167" async></script>

### Gitk is the one gui tool even command line folks should be using

As useful as graphical git log can be, you will probably still prefer gitk.
It is written in ancient tcl/tk but is a pretty good tool for seeing git logs
and branching.

If takes a branch name as an argument, if you are lazy try --a -a, one of these means all branches
and I have no idea what the other means.
If you are inspecting a repo that has been around for a long time and you don't want gitk to spend
forever sucking in old history then use the `--since` option.

```
gitk -a --all --since='1 month'
gitk -a --all --since=1.month
```

The second version means the same thing and is much easier to type.

There is an appendix to the online git doc that says a bit about
[gitk](https://git-scm.com/book/en/v2/Appendix-A:-Git-in-Other-Environments-Graphical-Interfaces).
Another command git-gui is mentioned, I have accidently stumbled into git-gui a few times
and was as confused as a non-vi user is when she accidently types `vi`.

### Bitbucket sucks

Our bitbucket instance teases at having branch visualization but then does a
bait and switch and tells you that you need to pay for the supposedly Awesome
Graphs plugin.

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

#### tl;dr

Adding `--rebase` to your `git pull` can make your resulting history less ugly.
However, all the problems or rebase apply so only do this if you know what you are doing.
If you only have your own changes locally and you are simply syncing with upstream
then you are probably ok.
If you have pulled other changes into your repo then you definitely do not want to rebase.

