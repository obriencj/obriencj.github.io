---
title: The eero6 Mistake
subtitle: Someone Else's WiFi
date: 2020-11-27
category: technology
tags:
  - eero
  - wifi6
  - zigbee

---

I made a mistake. I'm rectifying the mistake now, but I want to share
my experiences with you in the hopes that the information I gained
while sorting through my folly may be interesting or enlightening in
some way.

I bought into the [eero6].

[eero6]: https://eero.com/shop/eero-6

<!-- more -->

Let's backtrack a bit. My home network is what I'd imagine the average
mid-nerd level setup to be. ISP (ATT Fiber in this case) provides
their hardware, and I immediately get it set to bridge mode. I connect
my own hardware to act as router and firewall, I run my own caching
nameserver and my own timeserver, and have a mix of static and dynamic
addresses on two subnets (let's call them "user" for user devices and
"core" for persistent services). It's nothing particularly intense but
it's also not the consumer plug-and-play.

My user network had been providing wireless connectivity via a trio of
old 802.11g access points, each acting as simple bridges, and all
sharing the same SSID. Roaming connectivity was good, but bandwidth
was very dated (54Mbps max, yikes). I've got wired gigabit to my desk
and the spots that the access points were located in, and it was well
past time to start trying to actually use some of that. I started to
think about upgrading.

At the same time I'd been fostering a growing interest in home
automation. I wasn't sure at the time what technology I'd settle on,
but zigbee and wifi both seemed reasonable.

So when I saw this new eero6 thing announced, I was very excited. A
[wifi6] router (802.11ax) with integrated [zigbee] hub! I could go from
extremely dated tech to the cutting edge. It also had a lovely sleek
aesthetic, so it wouldn't look like a big spiky pile of junk when
stationed around the house. I quickly looked over a few reviews and
ordered a pair!

[wifi6]: https://www.cisco.com/c/en/us/products/collateral/wireless/nb-06-preparing-for-wifi-6-ebook-cte-en.html
[zigbee]: https://zigbeealliance.org/

I didn't research deeply enough.

Here's what I discovered after having the eeros in service for a few
weeks.

* management is cloud-based only. There's no local management
  interface on the eeros, they connect out to api-user.e2ro.com and
  that's what you have to talk to in order to check the device status
  or change settings. There is a [python package] which can
  authenticate against this REST endpoint in order to query the device
  status.
* the eeros have an undocumented MAC address that they use when in
  bridge mode to get an IP for themselves. I watched my dhcpd logs to
  discover this, and subsequently assigned them specific IPs. There is
  no way to configure an IP from the eero itself when it's in bridge
  mode.
* the eeros use dhcp to get an IP, but do not honor the dns or ntp
  options. Instead they have hard-coded lists of name and time servers
  and will use those directly. I discovered this watching iptables
  logs, and added some pre-routing rules to dnat to my own name and
  time services.
* the eeros run [samknows1 speedtests] nightly, and this cannot be
  disabled. This uses TCP ports 6004 and 6500, and UDP port 6003
* the eeros perform software updates automatically, and this cannot be
  disabled. I noticed this when my wireless network just decided to
  reboot one day. This is considered to be a design feature.
* the eeros determine if the network is up or not by occasionally
  hitting [http://eeroup.com/up.css] but as mentioned previously
  blocking the software update connections will still trigger it to
  start flashing an error. Nonetheless I started hosting my own copy
  of this file and redirect as I was with dns and ntp.
* the eeros get some unknown information via https. Some of this is
  directed at the samknows1 hosts, so is probably for geolocation and
  fetching lists of speedtest servers. The rest is directed to EC2
  which is probably where the cloud control lives. I did attempted to
  mitm these connections, but it's set to validate the certificate so
  it wasn't fooled.
* the much anticipated zigbee bridge requires you to link the eero to
  an [amazon alexa] account. Devices it discovers are only available via
  alexa integration, which means control leaves the house.
* nothing I own can take advantage of wifi6. At best I get 400Mb/s
  from my most modern wireless devices.

[python package]: https://github.com/343max/eero-client
[samknows1 speedtests]: https://samknows.com/technology/tests/speed-tests
[amazon alexa]: https://alexa.amazon.com/

In short, the eero6 is really more like an amazon service than an
access point. You're very limited in what you're allowed to do with
it, and support is negligible. If you are already invested in alexa
and the idea of your wireless access being a service provided by
someone else seems appealing, this may be a great product for you. But
if you are someone who tinkers with your network and has it set up the
way you like it, and above all want to be the one in control, this is
absolutely not the device you want.

To celebrate [Buy Nothing Day] I've also decided that today is the best
time to file a return! I had already ordered replacement devices. This
time I'm going with Cisco [CBW140AC]. Not wifi6, but going from 802.11g
to 802.11ac is a significant upgrade still.

[Buy Nothing Day]: https://en.wikipedia.org/wiki/Buy_Nothing_Day
[CBW140AC]: https://amzn.to/36b0jBk

The home automation problem I solved with a dedicated [RPi4] running a
[containerized] version of [Home Assistant] with a [HUSBZB-1] dongle that
can operate with both zigbee and z-wave devices. More on that another day.

[RPi4]: https://amzn.to/3fTgpTH
[containerized]: https://hub.docker.com/r/homeassistant/raspberrypi4-64-homeassistant
[Home Assistant]: https://www.home-assistant.io/getting-started/
[HUSBZB-1]: https://amzn.to/3fIiBNu
