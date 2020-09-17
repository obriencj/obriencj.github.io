---
layout: post
title: "Meanwhile Again"
tagline: "IBM buys Red Hat, Potential Meanwhile Comeback"
description: An Open Source implementation of Sametime stirs in the darkness
keywords: meanwhile ibm redhat sametime
date: 2018-10-31 15:54:07 -0400
updated: 2020-08-30 20:23:00 -0400
published: true
comments: true
category: projects
tags: meanwhile ibm redhat sametime

---

In 1999 I was working for IBM. Instant messaging was "in" and there
were new clients appearing regularly. AOL's was dominant, but there
was also a strong ICQ user base, Yahoo was putting forth an effort,
and Jabber had a lot of promise. At IBM, there was an internal
effort to use this otherwise unknown service named "VP Buddy."

<!-- more -->

VP Buddy looked like any typical IM client would. It had a buddy list
with presence and status messages, one-on-one chat, and group chats in
their own windows. But VP buddy was only one part of a larger online
experience called Virtual Places. With the help of a Virtual Places
server and a Java applet, web sites would stop being collections of
documents and suddenly become communal locations. Imagine going to a
news site and being able to chat in realtime with avatars of everyone
else viewing that particular news story. That was the dream of Virtual
Places, but in the end all that ended up getting used regularly was
simple chat and presence services. It was purchased by Lotus as part
of an aquisition, and hence its use inside of IBM.  Interestingly
Oscar, the original protocol that AOL's instant messenger used, was
also written by Ubique prior to its acquisition.

In 2004 I was one of the growing number of Linux desktop users within
IBM. VP Buddy had evolved and rebranded into Lotus Sametime. I had
been working hard to implement an Open Source version, based on
network dumps and a subtly incorrect [IETF draft] published by Lotus
and Ubique which documents portions of the Virtual Places protocol. I
named the project Meanwhile. It began accumulating users as I
developed a plugin for the popular cross-platform and cross-protocol
messaging client named Gaim (currently known as [Pidgin]). Bugs were
discovered and fixed, features grew. All in all, I considered the
project a success. It was stable, integrated well, behaved as
expected, and Linux users had something better than an awful and dated
Java app to use with their Sametime servers.

[IETF draft]: https://tools.ietf.org/html/draft-houri-sametime-community-client-00

[Pidgin]: https://www.pidgin.im/

Then in 2007 I left IBM to come to Red Hat. Red Hat didn't use
Sametime, and so I no longer had a need for Meanwhile. Meanwhile
worked just fine, so I was able to slowly stop paying much attention
to it.

Eleven years went by.

October 29th, 2018. The announcements were all over the financial
sites, buzz and rumors everywhere. IBM was acquiring Red Hat. After 11
years working with Red Hat they had grown immensely, and now we were
looking at becoming a part of IBM.

So I looked over at the old, outdated, ad-ridden sourceforge page for
Meanwhile. I thought to myself, "hey. This might be important again."

I've now migrated the project from sourceforge over to a new git
repository under my github account. I'm going to dig up some of the
patches that were applied by fedora and suse in the years since I
stopped actively working on the project, merge them in. I'm going to
see if I can't get this project rolling and modernized a bit.

There's some oddities that definitely need fixing, like the embedded
MPI code which should be replaced by a dependency on GMP. I'll wager
there's a bunch of ugly nonsense I'll cringe at. I could complete the
version 2.0.0 which was based on GObject, perhaps. I could flesh out
the python bindings and write some simple command-line pieces. There's
a lot of opportunity!

I've started hanging out in #meanwhile on freenode again. If you find
yourself having to use Sametime and would like to try out an Open
Source client, maybe Pidgin with Meanwhile is for you?
