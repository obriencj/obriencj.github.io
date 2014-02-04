---
title: "gist -- output of spexy_try"
date: 2014-01-25
comments: true
layout: post
categories:
  - python
  - spexy
  - hack

---

Because it's Friday night and I have nothing else going on, I've been
hacking away at [Spexy] again. It remains an utterly insane body of
work, which no clear-minded individual should approach with a straight
face.

<!-- more -->

But... I'm surprised how the me from 2007 thought some of the features
through -- especially taking into consideration the state of my brain
at the time. The module itself runs the input code through distinct
parsing and evaluation steps, which includes a macro expansion pass
before moving on to specials. I get the idea that I may have intended
to write parts of Spexy **in** Spexy once I got `defmacro` support
written. Maybe that can be next.

On this fine (albeit very cold) evening, I suffered a fit of
inspiration (and giggling). When the dust settled, Spexy had gained
support for `try/except` expressions.

It's pretty ugly. It's ugly pretty. Most importantly, it's satisfying
the rules of Spexy. "What rules," you ask? As I've been toiling over
this I've remembered more about just why the thing exists. It's not a
project -- it's a puzzle! The inspiration was never "I need a tool
that will do..." it was "I wonder if I can..." and from there sprung
up some [rules].

[spexy]: https://github.com/obriencj/python-spexy
[rules]: https://github.com/obriencj/python-spexy/blob/master/README.md#concept
