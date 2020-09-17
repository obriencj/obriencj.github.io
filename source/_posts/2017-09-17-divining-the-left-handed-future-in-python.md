---
layout: post
title: "Divining the Left-Handed Future in Python"
tagline: Tea Leavings and Stack Frames
description:
keywords: python, mapbind, objbind, funbind, takebind
date: 2017-09-17 09:00:16 -0400
updated:
published: true
comments: true
category: projects
tags: python mapbind

---

Composing words is hard. Too much to tell, too many ideas; they all
run together. Okay, let's start from here and now, and I can work my
way backwards in later posts. This is my own fault for not writing
up all my projects as I was actually working on them. Ah well!

Let's start with looking at Python bytecode to detect how the results
from a function call will be consumed, and what we can do with that
knowledge.

<!-- more -->

## Mapbind

A good friend of mine mentioned an idea he'd had for an extension of
the Python syntax for structured binding. Put simply, he was tired of
copying the contents of large dictionaries into the local namespace in
order to operate on them. He proposed an expression similar to the kwd
variadic parameters of function calls.

```python
# proposed syntax
** = big_ol_dictionary
```

My familiarity with how Python implemented local variables told me
that this wouldn't work -- Python needs to know the variables far in
advance, during compilation, so that it can allocate fast local
storage for them, and compile subsequent accessors into `LOAD_FAST`
and `STORE_FAST` ops. Fetching those variables from a dictionary at
run time would be much too late. But if the local variables all
existed, surely we could implement something that would assign to
them?

But that means you still need to have assigned to those values in
advance, to tell the compiler that they exist.

```python
# declare them first
a = None
b = None

# then this could then in theory bind mappings matching "a" and "b",
# since they already exist.
** = big_ol_dictionary
```

The problem then becomes that the declaration is somewhat verbose, and
we aren't being perfectly clear just which local variables we want to
assign to.

In another project, I'd been spending a lot of time becoming familiar
with the [Python bytecode] ops. I'd recently implemented structured
unpacking for [that project], and I knew the layout of those
operations after the right-hand side of the assignment had been
evaluated.

[Python bytecode]: https://docs.python.org/3.5/library/dis.html
[that project]: https://github.com/obriencj/python-sibilant

So I reasoned, a simple heuristic could be implemented which would
look at a frame, take its code and index values, and check for the
unpacking and assignment operations that followed. From there, a
list of binding names could be harvested, and the function could
return a value crafted specifically for such an assignment.

In other words, I could write a function `bindings` which when used
in an assignment such as

```python
a, b, c = bindings()
```

Would be able to determine at run time that its results were destined
for three variables, and that their names in order were "a", "b", and
"c".

The next logical step would be to give `bindings` a unary function to
use to provide those values, and that became `funbind`:

```python
def do_something(dest_name):
	return "I'm bound to " + name
a, b, c = funbind(do_something)
```

From this generalized concept I could create `mapbind` which
would discover the bindings, and then look up the appropriate return
value from a dictionary:

```python
a, b, c = mapbind({"a": 1, "b": 2, "c": 3, "ignored": 900})
```

Similar implementation could be created for `objbind` which
instead of finding map items, would look up object attributes:

```python
a, b, c = objbind(some_object)
```

Finally, I also realized that this had uses in cases where perhaps the
names didn't matter, like unpacking an iterable. I could ensure that
I'd fetch exactly the right amount of values from the iterable, and
thus `takebind` was created.

```python
a, b, c = takebind(range(0, 1000))
```

I wrapped all this up into a package named `mapbind` and wrote a pile
of unit tests.

[python-mapbind on GitHub](https://github.com/obriencj/python-mapbind)
