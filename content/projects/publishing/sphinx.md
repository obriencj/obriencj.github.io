---
title: GitHub Pages Publication for Projects
date: 2023-10-10
status: published

---

[TOC]


This is very much a work in progress, but I can't just leave it as an
unpublished draft forever, so here we go


## tl;dr

* store written documentation in a `docs` dir for the project
* pull API documentation from project sources via autodoc
* add an initializer to `docs/conf.py` to pull metadata from your
  `setup.cfg` to avoid duplication of values
* use pandoc to produce `docs/overview.rst` from your `README.md`
  for the documentation
* use tox to manage the environment that sphinx will run in
* build docs as dirhtml, and host via `http.server` for local preview
* use a Makefile to handle all the above steps easily
* github action triggered on published release: checkout, build, and
  deploy docs to github pages


## Sphinx

[Sphinx] is my go-to, but that is primarily because most of my projects
are based on Python.

[sphinx]: https://www.sphinx-doc.org


## Tox

While [tox] may seem like primarily a harness to hang test environments
off of, it's fantastic at ensuring that a virtualenv is set up in
place for just about anything. Using a tox definition to define the
environment that you want to build docs in is a winning proposition.

[tox]: https://github.com/tox-dev/tox


## Automation

GitHub actions can be set to trigger docs builds via tox just like
they can be set to trigger unit tests via tox. It's a simple matter of
selecting the right triggering event (like a release moving to the
published state), then invoking tox, collecting up the output, and
publishing it to your GitHub pages for the project.
