---
title: GitHub Pages Publication Pipeline
date: 2023-10-10
status: draft

---

[TOC]


This is a living document which outlines what I consider to be ideal
GitHub Pages publication pipelines. The document is driven entirely by
opinion and experimentation. Here we identify two distinct major
models making use of GitHub Pages.

The first model is utilized to host the primary site for a user or
organization. This is typically maintained in a repository named in
the pattern `user.github.io`. This site is one such example.

The second model is utilized to host per-project information or
documentation hosting. These are typically maintained as a branch or
deployment directly from the project repo. The [koji-smoky-dingo]
documentation is an example of such.

[koji-smoky-dingo]: https://obriencj.preoccupied.net/koji-smoky-dingo/

As the use cases between these two are quite different, there are
distinct patterns that I've considered for either.


# GitHub Pages for Sites

This method is intended for use with a blog or top-level site as
hosted by github pages.

In these cases I've found the split setup to be advantageous. We'll be
separating the site into two distinct repositories; one for managing
the environment in which the site is built, and another for managing
the content of the site itself.

[Read more ...]({filename}/projects/publishing/pelican.md)


# GitHub Pages for Projects

This method is intended for use in hosting a project's documentation.
Sphinx, javadoc, etc. would be used to produce prose and API
information reflecting versioned releases of the software.

[Read more ...]({filename}/projects/publishing/sphinx.md)
