---
layout: page
title: "Sibilant"
tagline: "lisp dialect for python modules"
date: 2014-02-22 19:25
footer: false

---

Originally started in 2008 as a followup to the much-maligned [spexy],
sibilant was meant to be a serious take on a LISP dialect that
compiled to a [Python] module. It fell by the wayside when real life
interferred in a big way.

Spexy and Sibilant were both [re-discovered] in January of 2014, and
I've been looking over them to see what-- if anything-- can be
salvaged.

I [imported sibilant] to GitHub in its non-function state, and that's
the starting point for any future hacking.

[spexy]: https://github.com/obriencj/python-spexy
[python]: https://python.org
[re-discovered]: {filename}/blog/2014-01-22-spexy-oh-god-what-did-i-do.md
[imported sibilant]: https://github.com/obriencj/python-sibilant

## Sibilant Goals

* Python 3
* Scheme-like (LISP1, not LISP2)
* REPL
* `import` support for sibilant source files
  * importing sibilant should enable the import features such that it
	will begin searching for `.pyscm` files on further import calls
  * the contents of a `.pyscm` file should be consumable from other
    Python modules
  * should support compiling `.pyscm` into `.pyc`
  * `.pyscm` should be able to import native python modules as well as
	other `.pyscm` modules
* should follow a continuation-passing style call conformity after
  being compiled
* should support tail-call recursion optimization
* should support `call/cc` (even across calls into native Python)
* should support symbols as a type
* should support cons cell style lists as a type
* should support macros
* should provide a way to write DSL in Python (arguably, this is The
  Point)
* should support correctly printing traceback lines
* should support the `with` managed interface from Python objects
* should support generators
* should support multimethods and CLOS-style class definitions
  (dispatching to Pythonic classes? Maybe a metaclass?)

## Related

### Clojure
There is already a serious and strong LISP that runs on Python, and it
is [Clojure]. If anyone were to ask me, "should I use Sibilant?" I
would tell them to look to [Python Clojure] instead. Clojure has a real
community around it, and it is a language that runs on Java as well as
Python platforms.

* [clojure.org][Clojure]
* [clojure-py][Python Clojure] on GitHub

[Clojure]: http://clojure.org/
[Python Clojure]: https://github.com/halgari/clojure-py

### Sibilant Javascript

There is also another project that has come into existence named
"sibilant". What with it being a dictionary word meaning loosely
"speaks with a lisp" this is hardly surprising! The
[other sibilant][sibilant-js] is a lisp that compiles to Javascript.

* [sibilantjs.info](http://sibilantjs.info/)
* [Javascript Sibilant][sibilant-js] on GitHub

[sibilant-js]: https://github.com/jbr/sibilant
