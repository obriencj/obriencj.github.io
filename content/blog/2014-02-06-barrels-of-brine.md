---
title: Barrels of brine
date: 2014-02-06
modified: 2014-02-07
category: programming
tags:
  - python
  - brine
  - github
  - unittest
  - coverage

---

I've been very happy spending my evenings working with a small project
entitled [python-brine]. The code is relatively straight-forward, the
functionality and goals are well-defined. Put simply, brine allows you
to pickle actual python code. For a significantly more in-depth
explanation, click the above link and peruse the README.

[python-brine]: https://github.com/obriencj/python-brine "Advanced function pickling for Python"

[readme]: https://github.com/obriencj/python-brine#overview-of-python-brine "Overview of python-brine"

<!-- more -->

Brine was originally written back in 2008. It had been written as an
"I-wonder" rather than an "I-need" and as such it never saw use except
in its own hackish example scripts. Thus from October of 2008 until
January of 2014 is sat forgotten.

And then I found it again, and decided it merited resucitation.


## Get it moved

The very first thing I did was import it to github. It had been living
on code.google.com for all those years... with only one commit.

Before code.google, it had been in a CVS (remember that?) repository
on a machine which has long since disappeared. So all history for
brine prior to that snapshot in October of 2008 is gone. A lesson in
the value of a distributed system like git.


## Get it tested

Next I took all of five minutes to "port" it from [distutils] to
[setuptools]. I had to shuffle a few files around, but in the end it
built and the "test" scripts (more like examples) let me confirm that
it still worked.

In the last few years one of the things that I've discovered that I
enjoy doing is writing unit tests and getting to 100% code coverage.
As sad as it may sounds, yes I actually have been doing that for
fun. It's very much like a game. The tasks are clearly defined,
there's a simple attainable goal of a perfect score. Right up my
alley!

So I took the example scripts and converted them to real [unittest]
cases.

Those tests came in handy when I started actively hacking again on the
code itself. I'd resolved to add the remaining missing features, clean
things up, document it -- to really polish this little project up
before setting it on a shelf again. And of course as I tinkered I
broke it in weird and unexpected ways. But my unit tests were there to
catch me in my errors before I strayed too far.

And so more tests got written, and old code got untangled.

Thank goodness for [coverage.py] -- incredibly easy to use, with
detailed reporting. I was able to definitively throw out legacy
methods in some cases, while in others I expanded upon my unit tests
until in no time at all I'd reached the much vaunted 100% coverage.

[distutils]: http://docs.python.org/2/distutils/

[setuptools]: http://pythonhosted.org/setuptools/

[unittest]: http://docs.python.org/2/library/unittest.html "unittest &mdash; Unit testing framework"

[coverage.py]: http://nedbatchelder.com/code/coverage/


## Fill in the blanks

The TODO is rapidly shrinking. Tonight I added support -- including
unit tests -- for wrapping `functools.partial` instances.

I also want to add support for unbound instance methods and class
methods. Should be trivial.

The only large change I want to make involves a tweak to the timing on
when a barrel brines its contents. Currently the values are brined
immediately, which is too early. It needs to wait until just before
pickling, to ensure that mutable values haven't changed.

I should look at generating proper HTML documentation. There is almost
certainly something that is the de-facto standard for such a task, I
only need to discover it.

But after that... I think I can call it a wrap. I'll let it sit for a
week to make sure that I didn't forget anything. Maybe read over it
once or twice. And then I'll call it 1.0.0, tag it, and post it to
PyPI.

And maybe in another five years I'll find a reason to pick it up
again!
