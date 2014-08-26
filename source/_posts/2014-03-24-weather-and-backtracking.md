---
layout: post
title: "Weather and Backtracking"
tagline: "Miserable Drizzle and Muddled Thinking"
date: 2014-03-24 00:05:53 -0400
updated: 2014-03-27 18:45:00 -0400
comments: true
categories:
  - projects
tags:
  - weather
  - sibilant
  - ideas
  - python

---

Spring should be arriving any moment now, and indeed there are hints
of warmth and green coming soon. Those glimpses of a happy future are
punctuated with an almost spiteful enthusiasm by incredibly gross
weather. "Gross" is definitely the right word for it. The temperature
will drop 30 degrees (F) overnight, and a harsh gusting wind will
bring rain and occasionally sleet. The sky becomes dim and grey. You
find yourself bundled up against it, wondering if the previous day's
open heavens and friendly sunshine were just part of a fever dream.

<!-- more -->

I've been spending more time than usual at my [favorite coffee spot]
and while there I've been (of course) hacking around. As some will
know already, I've wanted for a while to write a proper LISP of my
own. I view it as an important exercise, and a bit of a milestone!
There are so many implementations out there already, I am not so
deluded as to think that mine will be of use except as a material
lesson during the course of its creation. It is, to my mind, akin to a
first novel. While composing a book ill suits me -- I'm bereft of
creative stories or unique views into real events -- composing a
compiler around what I consider to be an elegant and inspired computer
language is right up my proverbial alley!

[favorite coffee spot]: http://morningtimes-raleigh.com "The Morning Times, Raleigh"

But this path is not easily traversed. The routes my inadequate brain
travels along are bumpy and often with poor visibility. In my personal
hacks I don't always know where I'm going, psychologically or
programmatically, until I get there. I may indicate -- as with a vague
gesture -- that I'm headed in so-and-so direction. Where the journey
actually ends, who knows.

In this particular venture, I've already found myself at a dead-end. A
LISP compiler must, by the very definition of things, be
incremental. And I have painted myself into a corner, trying to be
clever and converting the structure of the source code into an AST
that includes special forms. Since a LISP macro (they being *the whole
goddamn point*) can conceivably be defined at any expression (at any
depth) I cannot safely create an AST in such a fashion. I need to
delay that step, and compile and execute the expression tree
*in-place*, with the environment traversing along with the
compiler. And so I must back track, a difficult lesson
learned. There's good reason that LISPs don't use structures past
cons-lists, and now I see one of those reasons quite clearly.

But let's focus on the happy discoveries over the frustrating ones,
today, yes? Let's talk about continuations and trampolines!


## Teaching Phantoms

Often, in order to consider things in their entirety in my own mind, I
try to explain them as to an interested novice. I do this in the
shower, or while staring off into space while my coffee grows cold. I
dream up a situation -- as many mad people do -- where another person
exists that wants to learn something, and I must rise to the occasion
to teach them.

This mental habit has served me surprisingly well, though it may have
contributed to my social failings. It's hard to find love while
staring vacantly off into space.

So let me pretend -- in the interest of advancing this narrative --
that there is someone in need of teaching, so that I may be forced to
organize my own thoughts enough to communicate them better to myself.
Or put another way, let me pretend to be someone smarter, and you can
pretend to be me.


## Return of the Continuation

One thing that I've found profoundly exciting is the concept of the
current continuation. Every expression of a program has one, hiding
under the covers, invisible to the eye and editor. It is almost
surprising, given the reclusive nature of the thing, to realize that
most programming languages do in fact offer some view of this wild
creature. It's called often by a familar name, `return`, and you may
well have taken it for granted throughout your years of programming.
Or worse, having memorized a particular implementation of the concept,
you may now be blinded to greater possibilities. A certain amount of
willing flexibility is required to proceed. Remember the wisdom of
Yoda!

The unassuming `return` is almost always disguised as a statement
rather than an expression. `return` does double duty -- it is both a
messenger, and a director. It will duly hand off a value, but it will
also adjust the underlying program state such that execution can
proceed and the program can eventually terminate.

`return` can be viewed thus as a function which executes the rest of
the program, accepting only a single argument as its parameter.

Imagine if you were able to somehow capture that function named
`return`.  Imagine keeping a reference to it somewhere outside of the
current scope!

What in the world would that captive `return` be good for?

If you're polluted with an implementation-based understanding of
`return` you're probably vehemently thinking something like "it pops a
frame off of the call stack! It places the passed value on the stack
so that the caller can get to it! That's what `return` does and what
`return` must do! All other ideas are lies!" That's certainly a
possibility -- in this case, a single instance of `return` works in
all places. It is entirely side-effect driven. But... what if...

What if we made a small adjustment to the common implementation, and
changed our definition of a call stack from a linear piece of memory
to a singly-linked-list. Consider a chain, hanging from a hook,
representing where the program is, and where it will go next. What if
the action of `return` was less about "pop" and more about explicitly
putting a particular link from that chain onto the hook. If that were
the case, then each function would need its own `return`, created with
that *specific* link held within its closure. If you somehow captured
that `return` function and stored it somewhere safe, then calling it
again would result in the call chain being put back to hang on the
hook exactly as it had been the first time that the now-captive
`return` was called. All manner of side-effects may have occurred in
the interim -- values in various scopes may have changed, objects may
have been mutated, output perhaps written to streams -- but execution
picks up once again just where it had. The passage of time is not been
undone, but the path we traverse *has*. Perhaps this go around a
different condition is fulfilled and execution travels down a
different path.

When `return` can behave as such -- when it can be captured -- it is
properly called the "reified continuation." An implementation detail
of the environment of the program, made available as part of that same
program.

It is important to me that the LISP I author supports fully reified
continuations. At any point in the program, I want the opportunity to
ask for the continuation, and to do what I will with it.


## Call Conformity

To this end, I have a powerful tool which can help me to make it
happen. A variety of kung-fu known for convoluting the sanest of
minds. Continuation-passing-style.

Using CPS, we never use the underlying `return` of the implementing
language. Instead, every function we define must take an additional
parameter -- the continuation, sometimes named simply `k`. The idea is
that the function `k` acts as a stand-in for `return`. When `k` is
called, it is given a value, and the job of `k` is to execute the rest
of the program.

Consider the following incredibly simple function.

```python
# return-style
def add_one_hundred(onto_bar):
    return onto_bar + 100
print(add_one_hundred(5))
```

Here we shall convert it to CPS

```python
# continuation-passing-style
def add_one_hundred(k, onto_bar):
    k(onto_bar + 100)
add_one_hundred(print, 5)
```

A wonderful side-effect of implementing a compiler which uses a
continuation-passing call-conformity for all of its compiled
expressions is that at any given point, the continuation is *right
there*, you simply have to snag it.

A less wonderful side-effect is that your more *traditional* call
stack can become quite deep, to the point of over-flowing. The
implementation language doesn't necessarily know that you never intend
to descend back out of the call stack -- that your program is just one
call after another after another. It holds onto data you never wish to
make use of.

Thus, if you're implementing a continuation-passing-style compiler on
top of a language with a traditional stack management system, you're
likely going to exhaust its stack allocation.

Unless, of course, you find a way to dump that call stack from time to
time. You don't need it after-all -- your program only moves
*forward*, never *backwards* now that it's passing `k` along. You need
a harness to assist you in doing this. And that is a trampoline.


## A Trampoline

If you're never going to return, it might become imparative that you
leave the past behind. It'll bog you down, otherwise.

Let's contrive an example. Here we'll use a recursive factorial
definition.

```python
# recursive factorial definition
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# prints 120
print(factorial(5))
```

No problem. Now let's convert that to CPS

```python
# a continuation-passing-style recursive factorial
def factorial(cont, num):
    if num == 0 or num == 1:
        cont(1)
    else:
        k = lambda x: cont(num * x)
        factorial(k, num - 1)

# also prints 120
factorial(print, 5)
```

For large numbers, they're both going to run up against the recursion
limit on Python (or stack space if you disable such limits). However,
the CPS factorial doesn't actually *need* the stack that it is
consuming -- it never returns! The value is accumulated deeper and
deeper down a line of continuations.

What follows is a rewrite of the CPS factorial that makes use of a
trampoline backing the recursive calls. When the call stack becomes
deeper than a certain limit, an exception is raised with the
continutation captured as a parameter. The trampoline catches the
exception, and calls that captive continuation. Python's call stack at
the time of the raised exception is simply discarded. The continuation
was "the rest of the program" and the trampoline made sure that the
program will be run to completion.

```python trampoline https://gist.github.com/obriencj/9555480 Gist
from functools import partial
from inspect import currentframe

import sys


STACK_LIMIT = 64


class ContinueCall(BaseException):
    pass


def countstack():
    # this is the slowest part, by far. There are better ways to
    # implement this metric, but they are signficantly more
    # involved. This is good enough for an example.

    counter = 0
    frame = currentframe()
    while frame:
        frame = frame.f_back
        counter += 1
    return counter


def bounce_call(work, *args):
    # this could also be implemented without a stack check, and as
    # such could bounce every single call.

    if countstack() >= STACK_LIMIT:
        raise ContinueCall(partial(work, *args)).with_traceback(None)
    else:
        work(*args)


def bouncy(func, final_cont, *args):
    work = partial(func, final_cont, *args)
    while True:
        try:
            work()
        except ContinueCall as cc:
            work = cc.args[0]
        else:
            break


def factorial(cont, num):
    if num == 0 or num == 1:
        bounce_call(cont, 1)
    else:
        k = lambda x: bounce_call(cont, num * x)
        bounce_call(factorial, k, num - 1)


def main(value):
    bouncy(factorial, print, value)
```

Just before the end, any remainder Python call stack does indeed get
traversed. But it is an unimportant side-effect at this point -- we
aren't using it to pass a value back, we're just letting Python return
to its normal behavior.


## So What Next?

If we can guarantee a trampoline (and of course we can, we're writing
the compiler and interpreter), then we can with relative safety make
use of CPS in our generated executable. We must be consistent though
-- if we're going to be throwing away the return stack, we need to be
certain that we definitely haven't emitted code that wants to use it!
This is the call-conformity. We must compile every expression into a
series of steps, each of which has the conformity in its evaluation,
that it takes a continuation and will (eventually) pass execution
along to it with the result.

In my next post, I will endeavor to communicate just how I've decided
to do such!

---

_Edited 2014-03-25 : explain the problems I've run into in sibilant
with macros, thus clarifying the post title_
