---
layout: post
title: "Brine On the Wire"
date: 2014-03-04 14:35:42 -0500
categories:
  - 'projects'
tags:
  - 'brine'
  - 'draft'

---

I realized while hacking on the test cases for the promises
multiprocess module that it would be really useful if I could easily
pass along anonymous functions. So I threw together some Queue
subclasses that automatically brine/unbrine the passed work function.
