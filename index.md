---
layout : page
title : "Christopher O'Brien"
tagline : "is a pile of bits"

---
{% include JB/setup %}

{% for post in site.posts reversed limit:3 %}
## {{ post.title }}
 __posted [{{ post.date | date_to_string }}]({{ post.url }})__

{{ post.content }}

___
{% endfor %}

Older posts are in the [Archive](/archive)

[Contact](contact) | [Projects](projects) | [GPG Public Key][gpgkey]

[gpgkey]: /gpg/52829C5C.asc
"ASCII-armored public key 52829C5C"
