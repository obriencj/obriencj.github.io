---
layout: post
title: "Delivering on Promises"
date: 2014-03-02 14:16:30 -0500
categories:
  - 'projects'
tags:
  - 'python'
  - 'promises'

---

It's beautiful, this fine sunny Sunday. Zoe is outside playing with
the neighbors and I'm relaxing in the breeze. I'm working on a bit of
clean-up coding from yesterday's hacking session on [python-promises].
I had finally gotten around to [writing][xmlrpc-gist] a unit test
harness for the XML-RPC multicall promise bits. I was so excited to
have that working that I charged through writing tests and fixing bugs
for the multiprocess and multithread modules as well. Before I knew
it, my promises module was looking darn-near worthy of a 1.0

[xmlrpc-gist]: https://gist.github.com/obriencj/9298654
[python-promises]: http://github.com/obriencj/python-promises

<!-- more -->

As I had done before with [brine] I went ahead and set up [travis.ci]
and [coveralls.io] hooks. I am still astounded (and grateful) that
there's such infrastructure available gratis to the open source
community.

[brine]: http://github.com/obriencj/python-brine
[travis.ci]: https://travis-ci.org/obriencj/python-promises
[coveralls.io]: https://coveralls.io/r/obriencj/python-promises?branch=master

I've also started the more tedious task of going through the
docstrings and getting them into the format that [numpydocs] and
[sphinx] are expecting. I need to write up significantly more examples
for [the documentation]. That can be what I work on in the evenings in
bed, this week.

[numpydocs]: https://github.com/numpy/numpydoc
[sphinx]: http://sphinx-doc.org/
[the documentation]: http://obriencj.preoccupied.net/python-promises/

I'll let the project sit for a bit, and see if anything else crops up
that needs changing. But if all goes well, I think I'll be tagging
version 1.0.0 soon, and posting the module up on PyPI.
