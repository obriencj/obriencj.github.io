---
title: Summer Madness
date: 2015-10-05
updated: 2015-10-06
category: personal
tags:
  - rambling
  - summer
  - vt500ft
  - tu250x
  - tomos
  - boxcar
  - python
  - withscope
  - running

---

Spring and Summer happened. I'm still in shock that they've already
gone by and Autumn has arrived.

I haven't been keeping record of my doings and thinkings, which now
seems short-sighted. Let's use this post as a TODO, marking up the
activites of warm weather that I need to write about!

<!-- more -->

## Running

Last winter was awful, but when spring finally showed up it was
glorious. I took PTO from work over the week of my birthday (which is
in April) and started running. My goal at the time was to simply get
to the point where I could run an entire mile without stopping -- a
feat I'd never before been capable of. I managed it, and I've kept
slowly increasing the distance every week since. At the time of this
writing I can regularly make 2.5 miles, and have made it to 3 miles in
a single run.

My new goal is to surpass a 5k (3.1 miles), and to register and
complete a real run before the end of Autumn.


## Uggo

Uggo was properly re-assembled and has been running great! I
re-re-disassembled her carbs and properly chemdipped them. That did so
much good I feel like a fool for not doing it this way the first
time. Uggo has, since I purchased her, new clutch plates, new brake
pads, new brake cylinders and seals, new master cylinder and braided
line, new oil filter and oil, new coils, new spark plugs, a new
battery, a new fuse box, new center stand, a repaired airbox, a new
air filter, new bars, new grips, new mirrors.

She has a new front disk as well, which I need to mount. She's been
taken for a few test rides, and that old disk seems to have a
deformity or very uneven wear -- braking is a very shuddering and
exciting event. But holy smokes does she run!

I intend to make her into a gift for my sister, as soon as I get the
last few tweaks made. There's a bit of a wiring issue with the left
turn signal, and the headlight is being obstinate. Also, the radiator
fan is unplugged and needs an inline fuse. But then that's it, I
think. Maybe a clear-coat for her metal tank, and black for the
plastics. She'll be lovely!

TODO: more pics, maybe a new video


## Tux

Tux has been such a trooper, as always. I removed her intake snorkel
and wired her up with a PowerCommander-V. I played with fuel maps for
a while to get her happy with the new exhaust. There aren't any shops
around here that are willing to let me tune her on a dyno,
unfortunately. The Harley place (Ray Price Harley Davidson) flat-out
refuses to work on anything they don't sell, and they're the only
remaining shop that is certified for PC-V dyno tuning.

Other than that, Tux has been a perfect trooper. Great gas mileage,
zoomy and fun. At the time of this post she's up to 15600 miles. Not
bad for a 2013-model motorcycle!

TODO: maybe a new video, and post my fuel map and some new pics


## Python Hacking

I've been poking around Python internals this past month, working on a
module I've named [`withscope`][withscope]. It lets you push lexical
scopes onto an existing block. It's a total hack, and apart from the
weird factor it's absolutely useless -- awfully slow and confusing to
use if you aren't already expecing your namespace to be modified.

[withscope]: https://github.com/obriencj/python-withscope/

I'm still making modifications to it, trying to make it into the best
representation of this crooked idea. I'll probably have a last commit
ready in a few weeks, depending on spare time.

It's worth noting that Python 3 has a `nonlocal` statement, for
declaring write-access to freevars, something that Python 2 cannot
do without some hackery.

TODO: write up a doc about variable scoping in Python 2, and how
co\_names, co\_vars, co\_cellvars, co\_freevars, and the frame
fast_locals work.


## Tomos Targa

My daughter turned 11 years old at the start of this month
(October). She'd been wishing for two major presents since Christmas
-- an iPhone and a powered bike of her own.

Of course she got both. She now has a better phone than I do, and an
awesome little 49cc, 1.5HP moped -- a 1994 Tomos Targa! It starts, it
goes, it stops, it's the cutest thing. Zoe loves it already, and has
been zooming around the cul-de-sac.

When she went off to visit her mother, I decided to take a look at the
guts of the thing. It has some serious gear whine, and had a bit of a
hard time starting. I wanted to see if there was something obvious
that I could fix.

Well, first off it was filled with regular motor oil rather than
transmission fluid. Not a huge deal, but something to change. Then
I took a look at the clutch and saw that the first gear clutch pads
were entirely worn away.

What is it with craigslist bikes and worn clutches? Uggo was the same
way, all the friction material just gone.

Second gear clutch was a bit chewed up, but still present. I ordered a
new set of OEM first gear pads, as well as the clutch-cover gasket.

I found bits of the starting engagement spring while I was in
there. Ordered a replacement for that as well. The bike runs without
one just fine, but not having it there can cause the kickstarting
ratchet to rub every now and then. Nothing serious, but if I'm already
in there fixing things I may as well replace it.

The front light didn't come on when I bought it. I took that housing
apart and discovered it wasn't properly plugged in. Easy enough. The
front left turn signal cover was smashed up. The bulb and electric
worked just fine, it just didn't have an orange lense over it. Ordered
that from ebay.

I found that the carburetor had been covered in some sort of liquid
gasket material as well, where it joins to the cylinder. Possible air
leak there? I'll check that gasket fitment when I reassemble. I've got
the carb off in prep of dipping (since it sat for a while before I
bought it).

The exhaust was collecting some serious grime and rust. I cleaned and
sanded that down, and painted it with some high-temperature rustoleum.

The chain was sticking a bit, so I've got a new chain coming from
Amazon. I managed to destroy the pin on the master link when I
attempted to take the old one apart. I never was good with those.

I'll run some cleaner through the brake and throttle wire lines, hang
'em up to drip, and then put some teflon into them. That should smooth
the actions of those up nicely.

My daughter wants to paint the whole thing blue, like Rainbow Dash
from My Little Pony. It's currently an awful white and red/brown. I've
ordered some rattle-cans of light metallic blue paint. I figure I can
give it a quick sanding job and just spray it over. It's a moped, it
hardly needs to be show-room quality, and to be honest I've always
favored a little bit of the rough and beaten look on a bike!

As of July 1, 2015, [North Carolina law][moped-law] requires that
[mopeds be registered][moped-faq] with the DMV. This was a surprise to
me! Once it's running again I'll have to go and get that taken care
of, and mount a license plate. Not a huge problem, but it makes me
wish I could lock the ignition on it. There's a steering lock in place
on the neck, but it didn't come with any key -- I'll have to keep an
eye out on ebay for one of those. I wonder if I could wire something
up so that the start switch circuit was only closed when the neck was
unlocked?

[moped-law]: http://www.ncleg.net/Sessions/2013/Bills/House/PDF/H1145v8.pdf
[moped-faq]: http://www.ncdot.gov/dmv/vehicle/title/vehicles/mopedfaq.html

I need to find a print copy of the service manual and parts list.

TODO: put together a Tomos Targa project page!


## Heartsick

I discovered a new place to hang out, a little Bar & Arcade
downtown. A brilliant venue, really excellent atmoshpere. They had a
Galaga in great condition, and I worked my way up to where I could
reliably get to 1 million points. I also got a lot better at 1942,
with my personal high score now sitting at just a bit over 1.25
million points. I spent so much time there this summer. I'd hop on tux
and ride into town, and play games and sip beer all night long.

But the real reason I was going wasn't the games, or the beer. There
is a bartender.  A brilliant woman, a clever woman, a beautiful
woman. She was my age, and her smile set my heart thudding. I'd go
just to sit at the bar and chat with her. She had such an interesting
view into the process of thinking, of dealing with emotions and the
directions of life. I became ridiculously smitten with this treasure
of a human being.

Of course, it was never meant to be. She's unavailable, and even if
she were I'm hardly a "catch." The situation makes a mess of my head,
as if it weren't enough of one already. "Limerance" the affliction is
called, bothersome malady. So I've been dealing with that; trying to
distance myself from the place and the woman and the disappointment.

TODO: Get over her and find someplace else to hang out.
