---
title: GitHub Pages Publication for Projects
date: 2023-10-10
status: draft

---

[TOC]


## tl;dr

* store written documentation in a `docs` dir for the project
* pull API documentation from project sources via autodoc
* add an initializer to `docs/conf.py` to pull metadata from your
  `setup.cfg` to avoid duplication of values
* use pandoc to produce `docs/overview.rst` from your `README.md`
  for the documentation
* use tox to manage the environment that sphinx will run in
* builds docs as dirhtml, and host via `http.server` for local preview
* use a Makefile to handle all the above steps easily
* github action triggered on published to checkout, build, and deploy
  docs to github pages


## Sphinx


## Tox


## Automation
