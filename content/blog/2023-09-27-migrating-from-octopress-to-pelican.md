---
title: Migrating from Octopress to Pelican
subtitle:

date: 2023-09-27
updated:

category: hosting
tags:
  - rambling
  - octopress
  - pelican
  - github.io

---

[TOC]

<!-- summary -->

After a number of years using Octopress, it's time to migrate to
something new.

<!-- more -->


## Octopress

At the time of this writing, [Octopress] has been effectively
abandoned [since 2015]. There were a lot of big ideas on the horizon,
but it just didn't seem to manifest.

[Octopress]: https://github.com/octopress/octopress

[since 2015]: http://octopress.org/2015/01/15/octopress-3.0-is-coming/

I want to be clear that I do not blame nor fault the octopress authors
in this. I understand darn well that sometimes a project becomes a lot
less of a priority as life goes on. They do not owe me or anyone else
anything, and I thank them very much for their efforts.

In general a tool being left unsupported isn't something that would
normally worry me too much. In this case though I'm not a Ruby person
(like at all), and I found that my environment for building and
deploying the site was broken pretty frequently. An unsupported tool
is one thing, a broken and unsupported tool is quite another.

Thus I began the arduous task of looking for viable alternatives. I
liked a lot of things about the gitops-style content management. I
didn't want to go back to raw Jekyll, that much was for certain. After
a bit of searching, I discovered [Pelican].

[Pelican]: https://github.com/getpelican/pelican

Pelican had a number of good things going for it, from my perspective.
It was sufficiently akin to Octopress in feature and function that
migration of my existing markdown shouldn't be too arduous. It was
written in Python, which I am very comfortable with. It has a good
selection of [plugins] available. There was even an [Octopress theme]
for Pelican, though I didn't end up using that.

[plugins]: https://github.com/getpelican/pelican-plugins

[Octopress theme]: https://github.com/duilio/pelican-octopress-theme


## Purge

Octopress deployment against github.io were typically done [as follows]:

* the upstream repository is forked
* a source branch is created to hold the site content as authored
* the master branch is repurposed to hold the generated site content
* github pages set to deploy from master

[as follows]: http://octopress.org/docs/deploying/github/

Some of these steps are dated, as they are from a time when pages
needed to be on the master branch to be deployed, which is thankfully
no longer the case. Even if they were out-of-date when I set up my
site, the octopress Rakefile still took those steps for me.

All of this meant that sites based on octopress would end up with a
lot of inherited history and contributors, and my site was no
different.

In order to get past all of this I created my own temporary
repository, forked from my original site.

I completely dropped the existing master branch, and then renamed the
source branch to master. After that I went about removing all of the
octopress-specific files from the master branch. Every single file
that wasn't markdown directly authored by me was removed, including
the `.gitignore` file. This was all necessary because I wanted to
completely purge the history of non-content from the repository. I
didn't want the ghost of octopress to be dragged along forever. After
everything was removed, I used `git filter-branch` to
[remove history from all of the untracked files][purge].

[purge]: https://stackoverflow.com/a/33873223/1494961

After a quick check in `git history` confirmed that the only commits
remaining were to my own content, I was ready to continue with
migrating to Pelican.


## InElegant Theme

At first I'd been committed to using the Octopress theme, but after
some consideration I realized that refreshing the look-and-feel would
actually be a good idea for the site. I started shopping around for
[themes] in earnest. The one that really caught my eye was [Elegant].
It seemed to live up to its lofty name; it was clean, and quite
minimal.

[themes]: https://pelicanthemes.com/

[Elegant]: https://github.com/Pelican-Elegant/elegant

However after attempting an initial migration I ran into a few
issues. The way that I'd previously arranged my site had been broken
into two sets of content. Everything was either a page or a post.
Elegant really leaned into the idea that pages were individually quite
special. I could either have every page displayed directly on the top
navigation menu, or nowhere at all. There was no single source
indexing the pages as there was for posts. So I knew I'd need to make
some changes.

I forked Elegant and began work on [InElegant].

[InElegant]: https://github.com/obriencj/pelican-theme-inelegant


## New Problems

Freshly burned by my inexperience with Ruby I was still feeling the
pain of a broken Octopress environment. Once I had Pelican and
InElegant working locally that was fine. Hoever, what I really needed
was some way to ensure that they'd continue working *forever*.

In addition to the fear of my deployment environment breaking I
encountered a new dillema. Pelican wants its plugins and themes to be
available at some defined path when it is run. This presented a choice
for me; I could either copy my theme and plugins into the git
repository (recreating the mess I'd just purged), or I'd need to
ensure that they were always available in some other location relative
to my site's checkout. I like to keep a copy of the site available on
multiple hosts, so that meant I'd need to ensure each host had the
up-to-date theme and all of the necessary plugins in place before I'd
be able to do a local build. I really didn't like either of those
options.

I could set up a workflow in [GitHub Actions] to reproduce the build
environment and deploy my site from there. Howver, what about when my
chosen version of Python went out of support and GitHub decided to
stop providing it? What if one of the plugins disappeared or had some
incompatible changes introduced? What if pelican itself introduced
some deprecation of behavior? Avoiding compatability issues could be
solved with a `requirements.txt` and perhaps using git checkouts to a
specific commit, but that still didn't handle the case of something
just disappearing or breaking the version contract entirely.

It occurred to me that these problems were not new, but that they were
are all resolved by a single bit of modern technology.


## Containerized Solution

I decided that my best course of action would be to bundle everything
up [into a Container][container]. Python version, pelican version,
plugins and theme, all sealed into place together. My publication
[process] could then rely on that to produce the final static site.
I'd never have to worry about losing access to my environment. I could
easily pull the container or reproduce it locally for development.

[container]: https://github.com/obriencj/pelican-theme-inelegant/blob/master/Containerfile

[process]: https://github.com/obriencj/obriencj.github.io/blob/master/.github/workflows/pelican.yml


## Final Workflow

In the end I had two repositories. There was [pelican-theme-inelegant]
which would store my modified theme as well as the containerized
tooling for producing the site. Then there was [obriencj.github.io]
which would store all of the source content.

[pelican-theme-inelegant]: https://github.com/obriencj/pelican-theme-inelegant

[obriencj.github.io]: https://github.com/obriencj/obriencj.github.io


Commits to the tooling could be set to automatically rebuild the
container. Commits to the content could be set to automatically
rebuild the site, using the aforementioned container.

So that's what I've finally settled upon here. In theory I can now
direct my focus solely to writing content when I feel like it, and
publishing is just a commit and push away, without needing to worry
about how my local environment.
