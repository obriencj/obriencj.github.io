---
layout: post
title: "My First Lisp Compiler"
tagline: python-sibilant
description:
keywords: sibilant lisp python compiler bytecode
date: 2017-09-17 18:52:59 -0400
updated:
published: true
comments: true
category: projects
tags: sibilant lisp python compiler bytecode

---

There's a lot of liberty to be expressed in programming a project
for which you'll be the only consumer. Really, the same could be said
of any task performed purely for yourself.

I am a one-semester, community-college dropout, a self-taught fool.
Judged on a coarse scale, I don't regret this -- I am content with my
life. However, there are a few features of higher education which I
have felt that I truly am less for missing out on, trials and
endeavors that lend a certain amount of seasoning to the spirit. Some
of it is purely social, and some of it is curriculum.

<!-- more -->

I try to prove myself (to myself) sometimes. The projects I take up
and seek to invent from scratch are (occasionally) my interpretation
of what someone might learn in a more formal setting. Rather than
receiving it as a whole, guided and directed, I have to start from
scratch and just make shit up to accumulate similar experiences.

I reinvent what's already perfected. It's like running, I suppose.
The expenditure of effort doesn't move humanity forward, doesn't solve
some grand problem. It's pleasant, and good exercise, and a healthy
routine. Cars and bicycles exist, and they are more efficient in the
act of transporting a person from one place to another, but the act of
running is the purpose. I am astounded at the number of times I've had
to use this analogy when someone demands "what's it for" about
anything I've done in my own time.

I cannot fix them, and that's okay.

## Sibilant

[Sibilant] isn't for anything. Sibilant is a dialect of lisp which is
implemented in Python. It is compiled to Python bytecode. It has
distinct read, compile, and run times. It can be consumed
transparently from other Python modules, and can in turn transparently
consume more traditional Python modules. It is an effort to make the
Python runtime environment bilingual. I am not the first to start on
such a ridiculous task, and I hopefully will not be the last.

[Sibilant]: https://github.com/obriencj/python-sibilant

Sibilant features tail-call optimization, via a rudimentary trampoline
system. It compiles the vast majority of simple operands and
comparators to the appropriate bytecode, and also allows use of those
ops as run-time functions. It allows user-defined reader and
compile-time macros. It supports closures and global bindings,
exception handling, the managed object interface, generators,
iterative and imperative looping, class definitions, and keyword and
variadic formal arguments and parameters.

I'm pretty happy with it, but it has a long way to go before I'll
really consider it done. The current implementation is really version
zero. When it has enough fetures that I think it's useable, I will
rewrite every aspect of it in itself. I will use version zero to
compile version one of sibilant, and then I will re-compile version
one using itself.

And then sibilant will be done.

Maybe I'll write something in it, or use it for small projects. Maybe
I'll leave it forever.

There's some really great frameworks out there already. Racket is
particularly appealing. I think I'm going to prioritize learning it
next. If I want to write something amazing in a lisp, I'll probably
use that.

Sibilant's purpose is to be an exercise -- author the components of a
compiler without having been taught how to do so. Make mistakes,
realize why some ideas are bad first-hand. Come to new conclusions,
move forward.

Somewhere, there's a course that would have provided me all of this,
bundled up with quizzes, lectures, and some credits at the end. I
didn't get any of that, so I'm making good with what I've got.
