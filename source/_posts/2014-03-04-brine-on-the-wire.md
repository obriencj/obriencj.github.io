---
layout: post
title: "Brine On the Wire"
date: 2014-03-05 13:00:00 -0500
categories:
  - 'projects'
tags:
  - 'brine'

---

I realized while hacking on the test cases for the [promises]
multiprocess module that it would be really useful if I could easily
pass along anonymous functions. So I threw together a new
[queues module] for [brine] that provides some [Queue] subclasses
which automatically brine/unbrine any passed work.

This got me to thinking about the potential for sending code between
processes, or even between machines. Certainly powerful, but also
hazardous.

[promises]: http://github.com/obriencj/python-promises

[brine]: http://github.com/obriencj/python-brine

[queues module]: http://obriencj.preoccupied.net/python-brine/queues/

[Queue]: http://docs.python.org/2/library/multiprocessing.html#multiprocessing.Queue

<!-- more -->

One possible application of such ridiculousness is in passing
higher-order functions around over queues such that multiprocessing
can execute them and pass the new function back to the controller. I
can envision a trampoline-like model that could cross processors or
even machines. Of course that is remote code execution. And holy-shit
is that ever a can of worms.

As had been suggested by a [good friend], I could implement a signing
step. When unpickling callable code it could be checked for a proper
signature and an exception raised if something were amiss. It could
use out-of-band key exchange or a certificate-based system... but I am
torn as to whether I should be providing such a facility or if it
properly ought to live in whatever transport layer a user comes up
with. Should I rely on everyone else to secure their communications
and to verify the messages being sent?  Or should I do the work to
craft a verification step that is in-built?

This is likely moot as I doubt anyone will ever use this -- even I
don't actually have a use for it! The project only exists because I
was once told _"you can't pickle functions,"_ and I thought, _"the
hell I can't!"_ However, I feel that if I've made such a tool freely
available (and I have) I should also take some care that it can be
used responsibly.

[good friend]: https://plus.google.com/+PhillipJones/ "Phillip Jones on G+"

There is a light-on-details [TrustedPickle] project, but I cannot help
noticing it commits one of the major sins in cryptogrophy --
unnecessarily re-implementing things themselves. And there are no
tests cases. And it was last updated in 2003.

[TrustedPickle]: http://sourceforge.net/projects/trustedpickle/

Setting up a pickle-like module (or wrapper) that automatically
creates and attaches a cryptographic signature seems to be useful
enough to warrant some attention. Connecting that to a Queue
implementation that performs the sign/verify steps transparently would
be simple enough. This may become another entry for my
[ideas](/projects/ideas) page...

---

_Note: I [posted] about this topic on G+ as well. I should probably
have written it up here first... oh well, next time_

[posted]: https://plus.google.com/114793537781613459114/posts/gY8zXQjefEJ
