---
title: "Ideas"
description: "brainstorms and todos"
category: site
date: 2014-01-01

---

There are so many things that I'd like to work on or play around with
as time permits. My interests and focus are as mercurial as my
personality.

_these are in no meaningful order_


## mudblock
__custom voxel adventure/simulation game__

I started playing around in OpenGL a few years ago, using PyGame. I'd
really like to combine that work with some of the minecraft server
ideas I have and turn it into an actual, real game.

However, I'm also driven to make mudblock a simple and strong
engine. Basically, I saw minecraft and have been bothered by it ever
since. Missing chunks, bandwidth consumption, lag... there are all
these little nigglets that I have which are all concerned with how the
game and server deals with its data. I want to start from a solid base
of how the world data is distributed (replicated?), then move on to
how the event model can be cleaned up. Then we'll see if I can't mix
in a "proper" physics engine (ODE).

It's a pipe-dream... but it's the game I want to play. Maybe minecraft
will evolve more as time goes by and it will fill this space for me,
but I still could end up hacking on it just because I flipping love
reinventing things from my own perspective.


## whoseaura
__world of warcraft addon__

I need to clean up the whoseaura addon. Ever since they introduced the
consolidated buffs I've been annoyed that the tooltips don't show. I'd
like to see who *can* provide a consolidated buff, if one is missing.
And if it's not missing, I'd like to see who is providing it.
Currently the tooltip index doesn't match up with the UnitAura index,
so it's never getting the right caster. Bothersome!


## sibilant
__lisp dialect that compiles to python__

I imported this a few days ago from an old CVS checkout. It's
currently living in GitHub in a non-working state. I'd love to get my
brain wrapped around this and really get it working.

[More on sibilant]({filename}/projects/ideas/sibilant.md)


## python call/cc
__reified continuations in python__

I've been meaning to look into this for years now, but I never get
around to it. Depending on how the Python stack is constructed and
implemented, it just might be possible to reify and capture the
continuation at a point in execution... and then call it again later!

It seems like such a glorious hack, I really need to devote the time
to it.


## jekyll bootstrap theme
__because this site is currently weird__

I'm using the Twitter JB theme right now, and it's been a real
bastard. There are all sorts of weird spots where things aren't
variables (but they ought to be) so I've already had to modify
it. Like the copyright... it was hardcoded to 2012. And the tagline
field was never used, each page just statically displayed the text
"Page Tagline".

Well I want to set up a front page that shows my most recent 3 blog
entries (that aren't tagged with "personal"), merges in my most recent
Twitter posts, and then jumps to a brief "About" page.

I want to create a second rss feed, and filter the default one. The
default should omit any of the "personal" posts just like the front
page does. The second rss feed can include the whole collection.

I want pages to support tags, not just posts. When I look at the tags
view, I want any static pages that I've written up to be listed as
well!

I'm considering discarding the "categories" concept entirely, and just
going with tags all the way. I think if I need to namespace things,
I'll just make them sub-pages and use that as my organization method.


## workspace on GitHub
__a meta git repo__

Since I've got devel directories on a number of different machines, I
wondered if it might not be a good idea to setup some sort of
"workspace" concept, which was itself stored in git. The idea being
that I could sync the workspace repo, and it would do some magic to
automatically create all the other repos I use (perhaps with --bare by
default). This would get me a common layout across the three machines
I commonly use, and would make it easy to get setup on a new machine
as well. Maybe there is already something that does this?


## move off of tumblr
__control freak__

I think once I've got the theme working on this site, as well as the
various rss feeds, etc (and mobile?) I should drop my tumblr and move
it all over here. I really like the idea of how re-hostable Jekyll
is... if github decides to go evil tomorrow evening, I could change
DNS and set up my own repo hosting and stand up a webserver that hosts
the exact same content. I do not like being beholden to Tumblr...


## meanwhile
__lotus sametime library__

I've not worked on the meanwhile project since 2006 or 2007. After I
left IBM, it just became less and less of a priority since I wasn't
faced with having to use a Sametime server on a daily basis.

Before I effectively abandoned the only project I've ever owned that
had actual users, I had been working on a meanwhile2 concept.
GObject-based services, re-thought-out message structures, and a
significantly more development friendly set of headers and
functions. And Python bindings! Glorious Python bindings!

It would be very interesting to sit down with the current state of the
Sametime protocol (I know that the Sametime devs abuse and misuse
Sametime... the flipping thing has feature negotiation built-in and
they don't actually use it, what's that about?) and see if I can't get
up to feature parity. I'm sure the few remaining users would love
that! And I'm certain the Sametime team at IBM would not! Win-win!

Also, and this one is a big one... I've always wanted to write a proxy
from Sametime to XMPP. As in, a tool to allow an established Sametime
user installation to seamlessly migrate off of Lotus and onto a Jabber
server. Users could begin migrating to different clients, but the
stubborn ones could continue using their Sametime client with the
proxy. That would be quite a thing.


## home message bus
__personal internet of things__

I really want to set up an AMQ server at home, and start having all my
different machines and devices start talking to it. There are so many
different notifications that I am interested in (temperature, weather,
chat, mail, doorbell, electricity consumption, mailbox, motion
detectors, landline phone, network status, my coffee pot...)

I want to observe and log EVERYTHING.

And encrypt the everloving shit out of it, because it's my data and
nobody else's!


## migrate preoccupied.net mail to google apps
__because I'm a lazy admin__

I am tired of maintaining the firewall list and software updates for
my mail server. Especially since I'm just `.forward`-ing all my mail
to my gmail account anyway! Let's cut out the middleman. If I ever
need to move back to self-hosting, I can. But right now I don't want
to do it anymore.

I'd also consider collapsing the number of rackspace images I had, if
this were to happen. The cost savings of fewer images and reduced
bandwidth consumption may just offset the monthly cost of two or three
google account users, while at the same time providing the benefit of
not having to spend time on admin duties for the mail server. Sheesh.


## go-pro on my tux
__the tu250x I'm currently dating__

I've been interested in playing around with ride-recording. Just a
go-pro mount and iMovie, basically. Seems like a simple setup to
manage, but I have to invest real dollars in the hardware. Perhaps
come spring this will seem more viable.


## triple-tree leather guard
__what's better than a tux wrapped in leather__

also it would be neat if I could put together some kind of cover or
wrap for the top of the tripple-tree on the tux. Something that
allowed access to the starter key and let the neutral and fuel
indicators show through, but that kept the other key on that keyring
from scraping things up.
