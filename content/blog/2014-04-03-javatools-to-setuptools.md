---
title: Javatools to setuptools
date: 2014-04-03 18:52:24 -0400
category: programming
tags:
  - python
  - javatools
  - setuptools

---

I was supposed to write about [sibilant], but of course I've been
distracted.

My daughter is out of school on spring break, and I've taken leave
from work so that we could hang out together. Of course this means
that we've just been finding new ways to ignore each other as the week
has gone by. We've certainly spent a lot of time at various parks and
playgrounds, and we've played an awful lot of Minecraft together. But
on the evenings we've also set up something approaching residency at
our [favorite coffee shop]. She will sit and munch on chocolate chip
cookies while watching videos and playing games on her ipad--
oblivious to my presence-- and I'll find myself looking for something
unimportant to half-heartedly hack on. It's a pleasant and relaxing
situation, this modern bonding.

And so it came to pass that I was looking over the [python-javatools]
project again.

[sibilant]: http://github.com/obriencj/python-sibilant
[favorite coffee shop]: http://morningtimes-raleigh.com
[python-javatools]: http://github.com/obriencj/python-javatools

<!-- more -->

## Javatools

I typically write my projects and tools in reverse-- that is to say, I
write them as if I had the API that I wanted, and then I create the
library to fulfill that wish. In the end, I have a library and a tool
that consumes it.

[Javatools] still turned out to be a bit of a mess. It arose from a
simple enough question, it was suspected that a change in the binaries
for some classes was limited to line numbering and was otherwise
harmless. I took a quick glance at the format specifications for Java
class files, and indeed that information is trivial to fetch.

Thus, organically, began the life of a tool whose purpose is to
compare class binaries and discover the "meaningful" differences.

[javatools]: http://github.com/obriencj/python-javatools

## Unit tests

This likely sounds mad, but I enjoy writing unit tests. They're easy
to throw together without paying a whole lot of attention, and you
aren't likely to actively break something. Use tools like
[coverage.py] and it becomes a game; trying to reach 100% [unittest]
coverage for some little library that has a total of 20 users in the
entire world.

[coverage.py]: http://nedbatchelder.com/code/coverage/
[unittest]: https://docs.python.org/2/library/unittest.html

I started writing Javatools before I'd developed the habit of writing
tests in parallel. Mind you, I "tested" the project frequently,
running it against all manner of samples from out in the wild. I kept
a script in git whose sole job was to compare two versions of JBoss AS
against one-another-- that was my test case.

Approaching actual test writing for this project seemed daunting at
first-- it meant I'd need to create data to test against, and that
meant writing Java code so that I could disassemble it again later and
check that what my tooling reports is indeed what ought to be there.
But that's exactly what I've been doing this week in the coffee shop--
creating sample classes that I could tear apart. I've found one bug in
javatools so far with this, so I even have something to show for it.

## Setuptools

In order to more easily manage my unittests, I've migrated setup.py
from the in-built [distutils] module to [setuptools]. Setuptools has a
few quirks, and I've had to make adjustments to accommodate those. For
instance, renaming the `src` directory to `javatools`. In theory I
will be able to simplify setup.py by moving the `pylint` command out
into its own file, but I haven't arrived at that point yet.

Unfortunately, I still need to override the `build_py` command class
to pre-compile my [Cheetah] templates into python modules.

[distutils]: https://docs.python.org/2/distutils/
[setuptools]: http://pythonhosted.org/setuptools/
[cheetah]: http://www.cheetahtemplate.org/

Since this introduces a dependency for the project, I've kept these
changes (including the unittests) in a [separate branch] until I can
ascertain that it's not too much churn for the upcoming 1.4 release.

[separate branch]: https://github.com/obriencj/python-javatools/tree/setuptools

Setuptools is widely-enough used that I sincerely doubt there will be
any real issue with the switch. After a few more tests I'll hopefully
merge back to master and finally tag version 1.4 in git.

And then I'll have to go back to thinking about the compiler for
sibilant.
