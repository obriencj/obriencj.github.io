---
title: GitHub Pages Publication Pipelines
date: 2023-10-21
status: published

---

This is a living document which outlines what I consider to be an
ideal for GitHub Pages publication pipelines. The document is driven
entirely by my own opinions, experiences, and experimentation. Here we
identify two distinct major models making use of GitHub Pages.


# GitHub Pages for Sites

This publication model is utilized to host the primary site for a user
or organization. This is typically maintained in a repository named
using the pattern `user.github.io`. This very site is one such
example.

In these cases I've found the split setup to be advantageous. We'll be
separating the site into two distinct repositories; one for managing
the environment in which the site is built, and another for managing
the content of the site itself.

[Read more ...]({filename}/projects/publishing/pelican.md)


# GitHub Pages for Projects

This model is utilized to host per-project information or
documentation hosting. These are typically maintained as a branch or
deployment directly from the project repo. The [koji-smoky-dingo]
documentation is an example of such.

[koji-smoky-dingo]: https://obriencj.preoccupied.net/koji-smoky-dingo/

This method is intended for use in hosting a project's documentation.
Sphinx, javadoc, etc. would be used to produce prose and API
information reflecting versioned releases of the software.

[Read more ...]({filename}/projects/publishing/sphinx.md)
