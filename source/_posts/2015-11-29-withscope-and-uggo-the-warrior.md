---
layout: post
title: "Withscope and Uggo the Warrior"
tagline: a tale of two projects
description:
keywords: vt500ft, python, withscope, uggo, honda
date: 2015-11-29 23:13:03 -0500
updated:
published: false
comments: true
category: projects
tags: vt500ft, python, withscope, uggo, honda

---

My Thanksgiving vacation draws to a close. It is 11PM on a Sunday
night, and tomorrow morning I will haul my carcass back down to my
desk and log in to work and get back to the grind. The days are once
again depressingly short, and I must combat the darkness by soaking up
as much sunlight as possible. It becomes difficult to see the sun at
all -- wake up, walk downstairs into the home office, and stay there
until the workday is done.

<!-- more -->

## Uggo Yesterday

As previously noted, I have been working like mad to get Uggo running
and in good condition again. This effort is redoubled because Tux has
had her exaust pipe off for ceramic coating for the past two weeks,
rendering her unrideable.

Yesterday was Saturday, and I took her out for a ride down to
Lillington. The beast hadn't seen much real road time since I'd bought
her and started tearing her apart. I really opened her up on those
empty roads, and was pleasantly surprised. The new coils and plugs,
the cleaned carbs, the new clutch plates all let her just jump forward
with a twist of the wrist. She seemed genuinely eager to haul ass. If
you can get her to 6k RPM, it doesn't seem to matter what gear she's
in, a quick rev and she'll jump to 9k like it's nothing at all. The
resulting acceleration is exhilerating to say the least. Sometimes a
little terrifying. Not once did the new plates slip.

The new front brake was fantastic as well. A firm pressure on the
lever had a very satisfying stopping time.

There's a lot of buzzing and rattling at various RPMs -- some of this
I think is due to the bent-up heat shields that act as barriers
between my right leg and her two exhaust pipes as they emerge from the
cylinder head. Since those suckers regularly get to 500F, I can
appreciate the presence of the shields, even if they make an
incredibly annoying noise when the engine frequency makes them
wiggle. Perhaps I should get these pipes coated as well, and then wrap
them? I could probably leave off the guards at that point.

I put 115 miles on the bike before parking for a refresher at
Boxcar. Much to my dismay when I went to leave, she started but idled
weakly and then stalled out. I could not get her to start again. I was
concerned I'd fouled her plugs, or she'd swamped, or any number of
things. But then the cavalry arrived (my sister) and with her a simpler
suggestion.

Out of gas. Apparently, Uggo gets around 46 miles per gallon. Coupled with
a 2.6 gallon tank... I must have arrived at Boxcar on fumes.

A quick run to a nearby station for a container of fuel, and I was on
my way home! Thank goodness for cool sisters!

## Uggo Today

I started today by attacking Uggo's wiring harness, one of the few
really bad bits remaining. Her turn signals had long given me issue,
and the wiring in general has been a disaster since day one, almost a
year ago. Sometimes she wouldn't start, sometimes the headlight
wouldn't work, sometimes indicator lights would sporadically stop
functioning.

I disconnected the entirety of the mess that was tangled beneath her
headlight and took a serious look at it. The majority of the bulk was
the result of a number of butt-end connectors that combined the
various control lines together to be sent off elsewhere on the
loom. The plug-in segment that these connectors had been sharing space
with was a totally separate piece, and with some arranging I was able
to move all the joinery up into the headlight bucket where it belongs.
Suddenly what was once a fat nest was just a few parallel bundles, and
there was plenty of room for control cables and the final outer
plastic covering.

I pulled out the manual while I was at this, and pored over the wiring
diagram to discern what was the issue with the turn signals. There
were a few color mis-matches (possible replacement pieces, who knows)
to act as stumbling blocks, but my multi-meter and I prevailed, and
with a bit of electrical cleaner spray and pliers-work, all four
signals were blinking as intended!

Just in time to get her inspected, since her registration is
approaching its expiration point!

## Withscope

With my morning cup of coffee, before I attacked Uggo's wiring, I got
a few final touches on another project of mine. [python-withscope] is
yet another one of those odd-ball things that nobody will ever use,
but which I've written for fun. It adds nestable lexical scopes,
similar to the special form `let` from scheme. I'm still somewhat
amazed that I could make such a feature work.
