---
title: GitHub Pages Publishing for Sites
date: 2023-10-10
status: published

---

[TOC]


Here I attempt to organize my thoughts around the site publishing
patterns that would work best for me. This solution may or may not
apply to your own needs. I hope at the least that it can serve as
inspiration, or even a good laugh over how complicated I've made
things.


## tl;dr

* separate the tools from the content
* create a container holding pelican, plugins, and theme
* use container to build site from content source
* ensure a local rebuild of the container can be used with local copy
  of content
* use github actions to rebuild the container when tool changes happen
* use github actions to rebuild and deploy site when content changes
  happen


## Builder Repository

This repository will be used to hold a working copy of your pelican
theme, as well as a `requirements.txt` that defines your pelican
version and relevant plugins, and a `Containerfile` to produce the
complete runtime in an reusable and easily-consumed manner.

Using this site as an example, the builder repository is
pelican-inelegant: <https://github.com/obriencj/pelican-inelegant>


### Produce the Theme

Depending on the theme chosen, there may be a need to rebuild some
static content used by the theme itself.

This site is using a fork of the [Elegant] theme, and as such there
are some processing steps applied to its sources.  Primarily these
actions are focused on producing a minified site-wide CSS and JS. To
accommodate this, the container process will be multi-stage. The first
stage will be used to pull in the original source CSS and JS files,
then transform and crunch them down into the singular files that will
be copied into the final container.

```Docker
FROM node:20 AS BUILD

WORKDIR /build

COPY package.json yarn.lock .
RUN yarnpkg

COPY gulpfile.babel.js .
COPY source/ /build/source/
RUN npx gulp
```

Depending on the theme chosen it may not be necessary to perform these
steps. If the theme is available already complete, then you can move
directly onto bundling it up.

[Elegant]: https://github.com/Pelican-Elegant/elegant


### Containerize Pelican

Once we have our theme ready to go -- either available statically,
built in a previous stage, or parts of both -- it's time to produce
the tooling container.

Here we will be using a `requirements.txt` to ensure that we're
operating on a known working version of the tools.  This way rebuilds
with theme changes can be guaranteed to operate with the same tools as
before. If we do need to perform a component upgrade, it can be done
using pip-tools, and the modified requirements can be committed.

```Docker
FROM python:3.9

ARG GIT_REPO="https://github.com/obriencj/pelican-inelegant.git"
ARG GIT_COMMIT=""

LABEL \
  git-repository="${GIT_REPO}" \
  git-commit="${GIT_COMMIT}"


# We needeed exiftool for the pelican-image-process plugin, or else
# our photos will lose their EXIF orientation data
RUN apt-get update ; apt-get install -y exiftool

WORKDIR /pelican


# Install pelican and available plugins
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt


# Fetch a shallow clone of the pelican-plugins git repository
ENV PLUGIN_PATHS=/pelican/plugins
RUN git clone --depth=1 --single-branch --branch master --no-tags \
  https://github.com/getpelican/pelican-plugins.git /pelican/plugins

# We installed these two previously via pip, and don't want the old
# copies from the plugins repo to conflict
RUN rm -rf /pelican/plugins/image_process \
           /pelican/plugins/liquid_tags


# Copy and install theme from previous stages and working directory
COPY --from=BUILD /build/static/ /pelican/inelegant/static/
COPY static/ /pelican/inelegant/static/
COPY templates/ /pelican/inelegant/templates/
RUN pelican-themes -i /pelican/inelegant


# since Pelican configurations are loaded as python modules, let's
# avoid writing out a __pycache__ every time they're used
ENV PYTHONDONTWRITEBYTECODE=1


# launch this container with the site checkout mounted as /work
WORKDIR /work
ENTRYPOINT ["pelican"]
CMD []
```

Then simply build and tag it locally. In my case, I prefer to use a
Makefile with a phony `container` target to wrap this call, but for
simplicity's sake we'd just need to call `podman build` directly.

```bash
podman build . --tag pelican-inelegant:latest
```

Once built and tagged, this container will now behave similarly to a
copy of Pelican which has our theme and plugins made available by
default. So long as we can pull the container, we know that we can
rebuild our site. We don't need to worry about incompatible versions
of python on various systems, or API breaking with upgrades to the
tools or plugins.

Thus from the content repository, we can run the container to invoke
pelican. Again, I prefer to use a Makefile to take care of this, but
in effect we'd be just using `podman run`.

```bash
# effectively the same as launching pelican directly in the current
# directory

podman run --rm -it -v.:/work pelican-inelegant:latest
```

References:

* my builder repository's [Containerfile](https://github.com/obriencj/pelican-inelegant/blob/master/Containerfile)
* my builder repository's [Makefile](https://github.com/obriencj/pelican-inelegant/blob/master/Makefile)


### Automate

Obviously building locally is one thing, but we want to be using this
container to actually deploy our site. This means we need the
resulting image published somewhere, and regenerated whenever a
pertinent change is committed to the repository. Thus:

* watch for commits to the master branch which modify our
  `Containerfile`, the theme sources or static elements, the
  `requirements.txt`, and in my case the `yarn.lock` as well.
* trigger a container build from the commit
* publish that container build into ghcr.io so it can be utilized


## Content Repository

Shifting


### Automate

We'll want our site to build and deploy itself into GitHub Pages
whenever we commit new content. This will mean a github actions
workflow:

* watch for commits to the master branch which modify our content or
  configuration
* build the site by running our tooling container against the relevant
  content checkout
* deploy the built site to github pages
