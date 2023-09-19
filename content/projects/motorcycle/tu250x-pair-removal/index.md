---
title: "TU250x PAIR Removal"
summary: "Removing the PAIR valve on a Suzuki TU250x"
keywords:
date: 2014-08-26
updated: 2014-08-30
comments: false
tags:
  - tu250x
  - motorcycle
  - mechanical

---

[TOC]

## About the Suzuki TU250x

[![My TU250x][DSC00132]{.image-process-inline .right}][DSC00132]
The [Suzuki TU250x] is a 249cc EFI [UJM], produced in Japan and
imported for sale in the United States from 2009 to 2015. It is a very
clean and efficient machine -- I personally have achieved an average
of 72 mpg since I bought mine in April of 2013. It meets stringent EPA
guidelines... with the exception of the venting on the gas tank's cap
which prevents it from being sold as new in the state of California.

[DSC00132]: {static}/photos/DSC00132.JPG

[Suzuki TU250x]: http://www.suzukicycles.com/Product%20Lines/Cycles/Products/TU250X/2013/TU250X.aspx

[UJM]: http://en.wikipedia.org/wiki/Universal_Japanese_motorcycle


## About the PAIR System

[Pulsed Secondary Air Injection][psai] is a system whereby clean air
from the airbox of the motorcycle is allowed to be sucked into the
exhaust valve during a low pressure wave.

It's a two-part emissions system. On one hand, it's mixing clean air
into the exhaust header prior to any kind of measurement being
taken. On the other, this clean air does allow unspent fuel to be
burned before it leaves the exhaust system.

[psai]: http://en.wikipedia.org/wiki/Secondary_air_injection#Aspirated_air_injection

The PAIR valve on a Suzuki has a one-way reed valve which ensures that
no exhaust pressure pushes its way into the air box, and a
solenoid-driven valve which disables the flow entirely in either
direction.

If the ECU detects that the PAIR solenoid is not electrically
connected, it will set an error state and cause the FI light to come
on.

The reed valve needs to be cleaned periodically, as it gets caked with
carbon buildup from the exhaust gasses. Eventually it will no longer
operate correctly, but the ECU will not be able to see the problem.


## Why Would I Remove the PAIR System

[![Face that only a mother could love][DSC00136]{.image-process-inline .right}][DSC00136]
The device does not weigh much, and only draws on the battery in brief
burts at idle RPMs. It is however a tangle of tubes and wires that I
found myself having to fight with during the disassembly process, and
which I was not interested in replacing
[during reassembly][kickstart].  There is no discernable performance
increase. The engine does look less cluttered, from a visual appeal
perspective.

[DSC00136]: {static}/photos/DSC00136.JPG

[kickstart]: {filename}/projects/motorcycle/tu250x-kickstart/index.md


## Patching Things Up

Leaving the PAIR valve out (or removing it) leaves three points in
need of patching.

- The air box needs to be plugged where it would have fed into the
  PAIR valve. Technically the hole is on the rubber tube connecting
  the air box to the throttle body, but "air box" is easier.
- The exhaust side of the cylinder head cover needs a blank covering
  the hole where it would have been fed by the PAIR valve
- The ECU needs to have a voltage available on its PAIR enable pin to
  trick it into behaving as if the PAIR valve were still intact.


### Plug Up the Air Box

Here is a [diagram of the air cleaner on the TU250x][diagram]. We'll
be replacing the part labelled 5 (air cleaner joint, `13858-14D20`)
with a plug of some variety.

[diagram]: http://www.suzukipartshouse.com/oemparts/a/suz/50d330f3f8700232d0b3dbcd/air-cleaner

[![Put a stopper on death][DSC00144]{.image-process-upline .left}][DSC00144]
This is the easiest to patch. Any plug that fits will do, as only
negative pressure will be occurring at this location. If you leave
this spot unplugged it will act like a bypass of the air filter, and
air will be drawn through it and into the throttle body without being
filtered.

[DSC00144]: {static}/photos/DSC00144.JPG

[![Close up][DSC00148]{.image-process-inline .right}][DSC00148]
I originally didn't have much luck finding a plug, so I simply used
the existing clamp to hold two layers of plastic from a zip-lock
baggie over the port. After just under 600 miles my impromptu seal was
still intact, but I stopped by a Home Depot and bought a 1/2 inch
flanged black plastic plug which fit perfectly and looks for all the
world like it belongs there. You can snag the same plug from Amazon -- a <a href="http://www.amazon.com/gp/product/B007AHLVFO/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B007AHLVFO&linkCode=as2&tag=obrieisapileo-20&linkId=Q4GO3AKVHQYUMKMI">SharkBite UP514A, 1/2-Inch Plug</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=obrieisapileo-20&l=as2&o=1&a=B007AHLVFO" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

[DSC00148]: {static}/photos/DSC00148.JPG


### Plug Up the Cylinder Head Cover

[![][DSC00153]{.image-process-inline .right}][DSC00153]
The cylinder head cover is another matter entirely. There will be
significant heat and positive pressure, with moments of negative
pressure as well. I shaped a bit of sheet metal by tracing the
original PAIR attachment, drilling two holes for the mounting
points. I then put a thin bead of liquid gasket around the hole and
attached my blank. I may augment this with a pair of washers (I used
very thin metal) but it does not appear to be leaking.

[DSC00153]: {static}/photos/DSC00153.JPG


### Plug Up the ECU

[![Dummy load][DSC00151]{.image-process-inline .right}][DSC00151]
There are a number of threads regarding how to properly "trick" the
ECU into seeing a false PAIR valve. The original PAIR valve has a
resistance of 22 Ohm. A 12V load on a 22 Ohm resistor would require
the resistor to be capable of dissipating more than 6 Watts of power
without burning up. Automotive resistors do exist with these
attributes, but can be expensive.

[DSC00151]: {static}/photos/DSC00151.JPG

I decided to go with two 1 KOhm 1/4 Watt resistors in parallel. They
are well within their power dissipation rating at 12V, and the
resulting 500 Ohm of resistance is enough to still make the ECU
consider the device to be present and functional.

I purchased the minimum order of the `2P090WP-TS-M` plug from
[Eastern Beaver] (third one down the page, but verify the model
number), and soldered my two resistors directly to the two terminals
before assembling the plug and wrapping the bare resistor leads in a
bit of electrical tape.

I zip-tied the resultant dummy load into a protective area under the
right-side cover, next to the fuse box.

[Eastern Beaver]: http://www.easternbeaver.com/Main/Elec__Products/Connectors/Sealed/SMTS/smts.html


## Done

That's it. Fire up the engine and check that the FI light stays
off. Rev the engine once or twice and check that there's no obvious
blow-out on your cylinder head blank.

As an added bonus I've found that after this modification there was a
reduction in instances of "cold-stop-stalls" that the TU is slightly
infamous for, though I've hardly had enough time to consider this
change in behavior as anything other than a blip of data.

If you enjoyed the photos, here's the [entire album](https://picasaweb.google.com/114793537781613459114/TU250xPAIRValve?authuser=0&authkey=Gv1sRgCJPOlbjdrIi9lgE&feat=directlink). You can read more about the mods I've made to Tux on my [motorcycle projects page]({filename}/projects/motorcycle/index.md)


## Changelog

* 2023-09-25 updated to local photos
* 2014-08-30 added photos, links, etc.
* 2014-08-26 initial write-up. TODO, add pictures and Eastern Beaver
  links to the correct plug.
