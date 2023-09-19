---
title: Some Kind of Call Conformity
date: 2014-04-10 18:45:35 -0400
status: draft
category: programming
tags:
  - sibilant
  - lisp
  - python

---

I have a bunch of ideas that might manifest into sibilant some day

<!-- more -->


## The transformer

I figured out the transformer for collecting a list of expressions in k style


## Writing Unit Tests

Wrote tests for sib parser


## Figuring Out The Procedure

Wrote parser -> AST

Started writing AST -> Expressions


## The Macro Road Block

blam, road block. macros.


## Where I Need To Go From Here

need incremental evaluation at a finer level than what I'd written

change to parser -> AST -> Module(expressions)

Apply(*li) compiles when first called to a python AST and from there
to a code object which is then evaluated to produce a callable function with
the appropriate k conformity and parameters.
