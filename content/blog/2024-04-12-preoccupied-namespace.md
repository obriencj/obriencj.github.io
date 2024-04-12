---
title: Preoccupied Namespace
date: 2024-04-12
status: published

category: programming
tags:
    - python
    - pypi

---

<!-- summary -->

Following the advice from [PEP-0423], I've claimed the [preoccupied]
Python package namespace for my experiments.

[PEP-0423]: https://peps.python.org/pep-0423/

[preoccupied]: https://pypi.org/project/preoccupied/

<!-- more -->

[PEP-0423] was deferred, but it makes a lot of sense in some areas.
I've lamented a few times that the python top-level namespace was a
disaster. The [Java packaging namespace specification][javans] of
using a reversed domain may be perhaps verbose, but has always seemed
like a better idea in the FOSS world where everyone is welcome to
contribute their work for others to use. Naming tends to lean heavily
towards using English descriptive words, of which there are only so
many that apply with specificity to a given topic. I've been
regretfully selfish before, taking top-level Python distribution and
package names for myself. It's one thing to stake a claim on the
Java-style `net.preoccupied.promises` and quite another to stake a
claim on `promises`

[javans]: https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html

As a remedy to this I've put down a claim on the [preoccupied]
namespace package in PyPI, and will use that going forward for any of
my one-off weird experiments that I decide to distribute. I've held
the [preoccupied.net] domain for well over two decades, using it for
personal project hosting. I intend to eventually move [mapbind] and
[livelocals] over to it, not that anyone is likely to be using
those. [brine] will have to wait for a Py3 port before it becomes
possible to move it over. My [javatools] project has had enough users
and that bare minimum community involvement that I don't feel too
awful about it being a top level name, so I'll leave that be. I have
no intention of moving [koji-smoky-dingo], unique as the name is.

[preoccupied.net]: https://preoccupied.net/

[mapbind]: https://pypi.org/project/mapbind/

[livelocals]: https://pypi.org/project/livelocals/

[brine]: https://pypi.org/project/brine/

[javatools]: https://pypi.org/project/javatools/

[koji-smoky-dingo]: https://pypi.org/project/kojismokydingo/

I have a [MyPy] plugin that I've been working on lately. That will
probably become the first new thing released in that namespace. More
on that later. It might also be a good idea for me to collect some of
my Github actions configuration into one place, if that's even viable.

[MyPy]: https://mypy-lang.org/
