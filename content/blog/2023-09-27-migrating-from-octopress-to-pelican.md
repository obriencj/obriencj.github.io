---
title: Migrating from Octopress to Pelican
subtitle:

date: 2023-09-27
updated: 2023-10-04

category: hosting
tags:
  - octopress
  - pelican
  - github.io

---

[TOC]

<!-- summary -->

After a number of years using Octopress, it's time to migrate to
something new!

<!-- more -->


## Octopress

At the time of this writing, [Octopress] has been effectively
abandoned [since 2015]. There were a lot of big ideas on the horizon,
but it just didn't seem to manifest.

[Octopress]: https://github.com/octopress/octopress

[since 2015]: http://octopress.org/2015/01/15/octopress-3.0-is-coming/

I want to be clear that I do not blame nor fault the Octopress authors
in this. I understand darn well that sometimes a project becomes a lot
less of a priority as life goes on. They do not owe me or anyone else
anything, and **I thank them very much for their efforts**.

In general a tool being left unsupported isn't something that would
normally worry me. So long as what once worked continues to work, I am
happy. In this case I'm not a Ruby person (like at all), and I found
that my environment for building and deploying the site was broken
pretty frequently. An unsupported tool is one thing, a broken and
unsupported tool is quite another.

Thus I began the arduous task of looking for viable alternatives. I
like a lot of things about the gitops-style content management that
Jekyll and Octopress had both provided. After a bit of searching, I
discovered [Pelican].

[Pelican]: https://github.com/getpelican/pelican

Pelican had a number of good things going for it, from my perspective.
It was sufficiently akin to Octopress in feature and function that
migration of my existing markdown shouldn't be too arduous. It was
written in Python, which I am very comfortable with. It has a good
selection of [plugins] available.
[plugins]: https://github.com/getpelican/pelican-plugins


## Theme Hunt

In researching just what it would take to set up Pelican, I began
browsing the selection of available [themes]. Much to my delight there
was even an [Octopress theme] for Pelican. If I wanted, I could make
the transition practically invisible.

[themes]: https://pelicanthemes.com/

[Octopress theme]: https://github.com/duilio/pelican-octopress-theme

As I browsed I was impressed with how nice some of the more modern
layouts presented themselves. After dwelling on it for a while, I came
to the conclusion that departing from the old theme would be for the
best.


## Elegant Theme

The one theme that really caught my eye was [Elegant]. It seemed to live up
to its lofty name; it was clean, and quite minimal.

[Elegant]: https://github.com/Pelican-Elegant/elegant

However after attempting an initial migration I ran into a few
issues. The way that I'd previously arranged my site had been broken
into two sets of content. Everything was either a page or a post.
Elegant really leaned into the idea that pages were individually quite
special. I could either have every page displayed directly on the top
navigation menu, or nowhere at all. There was no single source
indexing the pages as there was for posts. So I knew I'd need to make
some changes.

I forked Elegant and began working on [InElegant].

[InElegant]: https://github.com/obriencj/pelican-inelegant

InElegant remains quite similar to its origin Elegant, but I added an
index for pages, and altered the layout for pages to include some of
the sidebar data that was pertinent (such as publication and updated
dates).

I also found that I needed to correct some CSS behavior in order to
make my floating embedded images work correctly.

Ultimately I'd like to break InElegant away from the Node dependencies
it inherited from Elegant. These are primarily surrpounding CSS
post-processing and minification. If I can find a suitable alternative
in Python to some of these steps, I should be in the clear.


## Avoiding New Problems

Once I had Pelican and InElegant working locally that was fine.
Hoever, what I really needed was some way to ensure that they'd
continue working *forever*. I was still freshly burned from my
experiences fighting to keep Octopress working. I didn't want to wind
up in that situation again.

In addition to the fear of my deployment environment breaking I
encountered another dillema. Pelican wants its plugins and themes to
be available at some defined path when it is run. I could either opt
to copy my theme and plugins into the git repository (adding to the
existing mess of Octopress literring my repo), or I'd need to ensure
that they were always available in some other location relative to my
site's checkout. I like to keep a copy of the site available on
multiple hosts, so that meant I'd need to ensure each host had the
up-to-date theme and all of the necessary plugins in place before I'd
be able to do a local build. I really didn't like either of those
options.

I could set up a workflow in [GitHub Actions] to reproduce the build
environment and deploy my site from there. However, what about when my
chosen version of Python went out of support and GitHub decided to
stop providing it? What if one of the plugins disappeared or had some
incompatible changes introduced? What if pelican itself introduced
some deprecation of behavior? Avoiding compatability issues could be
solved with a `requirements.txt` and perhaps using git checkouts to a
specific commit, but that still didn't handle the case of something
just disappearing or breaking the version contract entirely.

It occurred to me that these problems were not new, but that they were
are all resolved by a single bit of modern technology -- containers!


## Containerized Solution

I decided that my best course of action would be to bundle everything
up [into a Container][container]. The Python runtime, the pelican
tool, my selection of plugins and theme, all sealed into place
together.  My publication [process] could then rely on that to produce
the final static site.  I'd never have to worry about losing access to
my environment. I could easily pull the container or reproduce it
locally for development.

[container]: https://github.com/obriencj/pelican-inelegant/blob/master/Containerfile

[process]: https://github.com/obriencj/obriencj.github.io/blob/master/.github/workflows/pelican.yml

Because I already had a distinct repository in place for my fork of
the theme, it made the most sense for me to use that to perform double
duty to also store the rest of the environment needed for building the
site. That left me in a good place, with the theme and tools in one
repository, and the content itself in another. I just needed to get
rid of all the years of extra stuff left over from having used Jekyll
and Octopress in the past.


## Purge

Octopress deployment against github.io were typically done
[as follows]:

* the upstream repository is forked
* a source branch is created to hold the site content as authored
* the master branch is repurposed to hold the generated site content
* github pages set to deploy from master

[as follows]: http://octopress.org/docs/deploying/github/

Some of these steps are dated, as they are from a time when pages
needed to be on the master branch to be deployed, which is thankfully
no longer the case. Even if they were out-of-date when I set up my
site, the octopress Rakefile still took those steps for me.

All of this meant that sites based on Octopress would end up with a
lot of inherited history and contributors, and my site was no
different.

In order to get past all of this I created a temporary repository,
forked from my work-in-progress site. From that fork I dropped the
existing master branch, recreated it from the source branch, and then
dropped the old source branch. After that I went about removing all of
the Octopress-specific files. Every single file that wasn't markdown
directly authored by me was removed, even down to the `.gitignore`.
This was all necessary because I wanted to completely purge even the
very history of non-content from the repository. I didn't want the
ghost of Octopress to be dragged along forever. After I was sure that
everything that didn't come from me was removed, I used `git
filter-branch` to
[remove history from all of the untracked files][purge].

[purge]: https://stackoverflow.com/a/33873223/1494961

A quick check in `git history` confirmed that the only commits
remaining were to my own content. I validated that the site built
correctly, and went ahead and force pushed the new master up to my
original repository.


## Final Workflow

In the end I had two repositories. There was [pelican-inelegant]
which would store my modified theme as well as the containerized
tooling for producing the site. Then there was [obriencj.github.io]
which would store all of the source content.

[pelican-inelegant]: https://github.com/obriencj/pelican-inelegant

[obriencj.github.io]: https://github.com/obriencj/obriencj.github.io

Commits to the tooling repository were set to
[automatically rebuild the container][container-action]. Commits to
the content repository were set to
[automatically rebuild the site][site-action] using that tooling
container.

[container-action]: https://github.com/obriencj/pelican-inelegant/blob/master/.github/workflows/container.yml

[site-action]: https://github.com/obriencj/obriencj.github.io/blob/master/.github/workflows/pelican.yml

I'm happy with the theme, the site layout, the minimized content
repository, and the ease of use in publishing. I've got some hope that
I won't need to worry about it just up and breaking if I leave it
alone for too long.


## Updates

* 2023-10-04 - Tried to organize the order of stages to actually match
  the timeline of the migration. I'm so scatter-brained.
