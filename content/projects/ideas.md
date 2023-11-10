---
title: "Ideas"
date: 2014-01-01
modified: 2023-11-10

---

[TOC]

There are so many things that I'd like to work on or play around with
as time permits. My interests and focus are as mercurial as my
personality.

_these are in no meaningful order_


### Current

## sibilant
__lisp dialect that compiles to python__

I got a mostly-working version of [sibilant] going in 2020. It worked
reasonably well. The python importer was modified on load to spot
`.lspy` file extensions and pass them to the sibilant compiler. That
would then load the s-expressions from the module one at a time,
compile them to pseudops, compile the pseudops to version-specific
python bytecode, and then execute the expression in the namespace of
the module. The pseudop translation layer was an excellent
idea... until it wasn't anymore. Once CPython upstream started
releasing updates that removed opcodes it really broke things for me.

So lately I've been working on my own bytecode interpreter loop for
sibilant, called sibilant-ceval. It's been a fun experience, since
I've never worked on something like this before. It's still a
work-in-progress, but it enables proper tailcall optimization without
a trampoline, as well as bounded call/cc forms

[sibilant]: https://github.com/obriencj/python-sibilant
[More on sibilant]({filename}/projects/ideas/sibilant.md)


## rebuild home network

My home network is pretty well cobbled together from inexpensive
nonsense. I'd like to resolve the tangle of wires and mismatched
hardware into some unified wall-mounted rack. I'd also like to try out
dedicated routing hardware instead of cheap SBC linux hosts!

Also, I'd like to get my VPN re-established, so I can connect back
into the home from remote.


## containerized preoccupied.net

I finally shifted off of the ridiculously expensive Rackspace onto a
single image on EC2. In so doing, I collapsed three ancient hosts into
three containers. However, I just sort-of threw those together in a
hurry. I'd like to properly lay out a compose for them, so I can
update or re-deploy without issues.


### Archived

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

Status: I started working in OpenGL, and then read some books that
made me realize my GL was really out of date. Then I started learning
about pipelines and realized they weren't even in use anymore, it was
totally different shaders entirely. I got so frustrated I gave up on
it.


## whoseaura
__world of warcraft addon__

I need to clean up the whoseaura addon. Ever since they introduced the
consolidated buffs I've been annoyed that the tooltips don't show. I'd
like to see who *can* provide a consolidated buff, if one is missing.
And if it's not missing, I'd like to see who is providing it.
Currently the tooltip index doesn't match up with the UnitAura index,
so it's never getting the right caster. Bothersome!

Status: I stopped playing World of Warcraft


## python call/cc
__reified continuations in python__

I've been meaning to look into this for years now, but I never get
around to it. Depending on how the Python stack is constructed and
implemented, it just might be possible to reify and capture the
continuation at a point in execution... and then call it again later!

It seems like such a glorious hack, I really need to devote the time
to it.

Status: After learning how the cpython ceval loop works, I don't think
this can be done anymore.


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

Status: This didn't really provide much of the benefit that I thought
it would, so I stopped using it.


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

Status: IBM bought Red Hat, but it looks like nobody uses Sametime
anymore, so it isn't relevant.


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

Status: I started using [Home Assistant](https://www.home-assistant.io/)


## triple-tree leather guard
__what's better than a tux wrapped in leather__

also it would be neat if I could put together some kind of cover or
wrap for the top of the tripple-tree on the tux. Something that
allowed access to the starter key and let the neutral and fuel
indicators show through, but that kept the other key on that keyring
from scraping things up.

Status: this would still be pretty cool, actually...
