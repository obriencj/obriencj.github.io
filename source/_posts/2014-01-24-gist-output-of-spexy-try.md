---
title: "gist - output of spexy_try"
date: 2014-01-25
comments: true
layout: post
category: projects
tags:
  - python
  - spexy
  - hack
  - lisp
  - gist

---

Because it's Friday night and I have nothing else going on, I've been
hacking away at [Spexy] again. It remains an utterly insane body of
work, which no clear-minded individual should approach with a straight
face.

<!-- more -->

But... I'm surprised how the me from 2007 thought some of the features
through -- especially taking into consideration the
[state of my brain] at the time. The module itself runs the input code
through distinct parsing and evaluation steps, which includes a macro
expansion pass before moving on to specials. I get the idea that I may
have intended to write parts of Spexy **in** Spexy once I got
`defmacro` support written. Maybe that can be next.

On this fine (albeit very cold) evening, I suffered a fit of
inspiration (and giggling). When the dust settled, Spexy had gained
support for `try/except` expressions.

```text output of spexy_try https://gist.github.com/obriencj/8610594 Gist
maybe:python-spexy siege$ PYTHONPATH=./ python tmp/spexy_try.py
The original spexy source is
-----
(defun division (x y)
  (let ((result None))
    (try
      (setf result (/ x y))

      ((ZeroDivisionError)
        (println "division by zero!" x "/" y)
        False)
      (:else
        (println "result is" result)
        result)
      (:finally
        (println "executing finally clause")))))
-----

parses into tree
-----
['defun', 'division', ['x', 'y'], ['let', [['result', 'None']], ['try', ['setf', 'result', ['/', 'x', 'y']], [['ZeroDivisionError'], ['println', '"division by zero!"', 'x', '"/"', 'y'], 'False'], [':else', ['println', '"result is"', 'result'], 'result'], [':finally', ['println', '"executing finally clause"']]]]]
-----

processed into Python
-----
globals().__setitem__('division', (lambda x, y: ((lambda result: (lambda _lcls:(eval(compile('def try_block(try_clause,except_0,else_clause,finally_clause):\n\tfrom sys import exc_info\n\ttry:\n\t\ttry_clause()\n\texcept (ZeroDivisionError,):\n\t\treturn except_0(*exc_info())\n\telse:\n\t\treturn else_clause()\n\tfinally:\n\t\tfinally_clause()\n','<spexy>','single'),globals(),_lcls), _lcls)[-1])({})['try_block']((lambda : result.__setitem__(0, (x / y))),(lambda exc_type, exc_val, exc_tb: (__import__('sys').stdout.writelines(map(str, ("division by zero!", " ", x, " ", "/", " ", y, '\n'))), False,)[-1]), (lambda : (__import__('sys').stdout.writelines(map(str, ("result is", " ", result[0], '\n'))), result[0],)[-1]), (lambda : __import__('sys').stdout.writelines(map(str, ("executing finally clause", '\n'))))))([None]))))
-----

division(1, 2)
result is 0
executing finally clause
result: 0

division(4, 2)
result is 2
executing finally clause
result: 2

division(2, 0)
division by zero! 2 / 0
executing finally clause
result: False

it works!
```

It's pretty ugly. It's ugly pretty. Most importantly, it's satisfying
the rules of Spexy. "What rules," you ask? As I've been toiling over
this I've remembered more about just why the thing exists. It's not a
project -- it's a puzzle! The inspiration was never "I need a tool
that will do..." it was "I wonder if I can..." and from there sprung
up some [rules].

[spexy]: https://github.com/obriencj/python-spexy

[rules]: https://github.com/obriencj/python-spexy/blob/master/README.md#concept

[state of my brain]: http://www.toothpastefordinner.com/052210/ambien-walrus-adventure.gif "Come with me on an adventure you'll never remember"
