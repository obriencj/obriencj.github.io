---
title: Exceptions and the Signaling Trampoline
date: 2014-08-28
category: programming
tags:
  - python
  - sibilant

---

I was thinking lately about the continuation-passing trampoline, and
how to allow it to work with exception handling code.

<!-- more -->

A problem with the initial example is that it uses a try/except block
in a loop to discard the call stack and continue execution. This means
that any exception handling code using the in-built python facilities
will consider the continued execution to be no longer in its scope, so
it won't catch the exceptions that it was set up to catch!

Fortunately, an idea has sprung to mind, and with it a wealth of
opportunities for additional ridiculous features.

The core idea is that we can use a variety of exceptions as
signals. We were already doing this with the ContinuationCall
exception. We can expand upon it though, with a few additional
signals. For example, an ExitCall -- an exception which when caught by
the trampoline will cause it to end execution and return a value.

We could use this system to implement cooperative multi-threading. We
would need a type to keep a reference to the most recent continuation
for each thread (which was simply the work callable in the original
example). We'd then need a new exception type for: creating a new
thread; yielding execution to the next queued thread; completing
execution of the current thread; destroying a different thread.

We can also use this system to register and pop our own exception
handlers. A nifty feature of Python's try/except syntax is that you
can specify the types as a tuple. That tuple can be a runtime
variable. Which means if we have an exception to signal we want to
push an exception handler function, all we have to do is put the type
onto the front of a tuple, and keep an index of handlers to go along
with it, and catch that tuple as the last except clause of our
trampoline. We'll also need a signal to pop the first N clauses off,
to signal that the handlers have fallen out of our continuation scope.
