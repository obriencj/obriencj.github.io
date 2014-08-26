---
layout: post
title: "Well how about Octopress instead?"
date: 2014-01-28 02:24:05 -0500
updated: 2014-02-06 20:29:00 -0500
category: hosting
tags:
  - github.io
  - jekyll
  - octopress

---

I was a bit unhappy with how [JekyllBootstrap] was turning out, so now
I'm playing around with [Octopress].

<!-- more -->

It's taken me a little over a week to get this looking something like
an actual blog. I have no idea why the default layout is so nutty
(huge fonts, etc).

I'm using the [tag-pages] and [tag-cloud] plugins. I'm a little bit
baffled as to why post tagging behavior wasn't included with Octopress
as a baseline feature.

I want to use the [gist plugin], but it's currently rendering code
blocks [terribly wrong][gist bug], so I'm reduced to inserting the
gists directly in any posts I write. This of course has its pros and
cons. I am not reliant on a bit of javascript and the gist site itself
to display my snippets, but I am also no longer receiving live updates
if I make any changes.

I've imported my scant few [Tumblr] posts, and have gone through the
tweaks to make them work in this blog. I believe that I shall now
abandon Tumblr in favor of posting here...

[JekyllBootstrap]: http://jekyllbootstrap.com/ "The Quickest Way to Blog on GitHub Pages"

[Octopress]: http://octopress.org/ "A blogging framework for hackers"

[tag-pages]: https://github.com/robbyedwards/octopress-tag-pages

[tag-cloud]: https://github.com/robbyedwards/octopress-tag-cloud

[gist plugin]: http://octopress.org/docs/plugins/gist-tag/ "Gist Tag"

[gist bug]: https://github.com/imathis/octopress/issues/847 "GitHub gist changes break gist plugin formatting #847"

[Tumblr]: http://obriencj.tumblr.com
