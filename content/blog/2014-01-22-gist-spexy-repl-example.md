---
title: gist - spexy repl example
date: 2014-01-22
modified: 2014-01-24
category: programming
tags:
  - python
  - spexy
  - lisp
  - gist

---

For those with strong stomachs I present an example of [Spexy], and the
perfectly valid Python it emits

[Spexy]: https://github.com/obriencj/python-spexy

<!-- more -->

```text spexy repl example https://gist.github.com/obriencj/8567348 Gist
[siege@maybe src]$ python spexy.py
>>>> (defun make_pair ()
        (letrec ((value None)
                (getter (lambda () value))
                (setter (lambda (v) (setf value v))))
            (make-list getter setter)))
--> globals().__setitem__('make_pair', (lambda : ((lambda value, getter, setter: ((value.__setitem__(0, None), getter.__setitem__(0, (lambda : value[0])), setter.__setitem__(0, (lambda v: value.__setitem__(0, v))),)[-1], [getter[0], setter[0],],)[-1])([None], [None], [None]))))
>>>> (letrec ((gs (make_pair)))
        (define getter (getf gs 0))
        (define setter (getf gs 1)))
--> ((lambda gs: (gs.__setitem__(0, make_pair()), globals().__setitem__('getter', gs[0].__getitem__(0)), globals().__setitem__('setter', gs[0].__getitem__(1)),)[-1])([None]))
>>>> (getter)
--> getter()
>>>> getter
--> getter
<function <lambda> at 0xb76c0df4>
>>>> setter
--> setter
<function <lambda> at 0xb76c0e2c>
>>>> (setter)
--> setter()
## <lambda>() takes exactly 1 argument (0 given)
>>>> (setter "hello world")
--> setter("hello world")
>>>> (getter)
--> getter()
'hello world'
>>>> (getter)
--> getter()
'hello world'
>>>> (setter "919")
--> setter("919")
>>>> (getter)
--> getter()
'919'
```

```text more spexy repl https://gist.github.com/obriencj/8609890 Gist
maybe:python-spexy siege$maybe:python-spexy siege$ PYTHONPATH=./ python
Python 2.7.6 (default, Nov 18 2013, 15:12:51)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from spexy import repl
>>> from datetime import datetime
>>> repl(globals())
>>>> (let ((who "siege") (date 1999))
       (letrec ((fmt "Hello %s, party like it is %i!")
                (msg (% fmt (make-tuple who date))))
         (println msg)))
 --> ((lambda who, date: ((lambda fmt, msg: (fmt.__setitem__(0, "Hello %s, party like it is %i!"), msg.__setitem__(0, (fmt[0] % (who[0], date[0],))), __import__('sys').stdout.writelines(map(str, (msg[0], '\n'))),)[-1])([None], [None])))(["siege"], [1999]))
Hello siege, party like it is 1999!
>>>> (println "But..." "it isn't" 1999 "anymore, it's" (. (datetime.now) year))
 --> __import__('sys').stdout.writelines(map(str, ("But...", " ", "it isn't", " ", 1999, " ", "anymore, it's", " ", datetime.now().year, '\n')))
But... it isn't 1999 anymore, it's 2014
>>>> (quit)

>>> quit()
maybe:python-spexy siege$
```
