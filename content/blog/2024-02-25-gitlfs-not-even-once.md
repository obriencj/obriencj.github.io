---
title: Git LFS
subtitle: not even once
date: 2024-02-25
status: published

category: hosting
tags:
  - git
  - git-lfs
  - github
  - opinion

---

<!-- summary -->

Ever eager to poke at features of technology as they catch my eye, I
stumbled upon a fascinating addition to Git recently: Git LFS.

What a travesty that turned out to be.

<!-- more -->

This post will not include any form of instruction on how to migrate
to using git LFS, because I strongly discourage its use.

[Git LFS][gitlfs] (Large File Support) is a method for storing large
files separately from the normal Git repository storage backend. In
effect, a lookaside is engaged to hold the large file content, and
[JSON references] are put into their place. A convoluted form of a
symbolic link, in essence.

[gitlfs]: https://git-lfs.com/

[JSON references]: https://github.com/git-lfs/git-lfs/blob/main/docs/spec.md#the-pointer

I [host this site][host] via [github pages] (née github.io). Its
content source holds a few images, which I've always felt a little bit
odd about committing directly into git. I had heard that Github
supported LFS, so I thought to myself that this would be an
interesting opportunity to try the feature out!

[host]: https://github.com/obriencj/obriencj.github.io

[github pages]: https://pages.github.com/

There are a few facets to Github's implementation of Git LFS that I
was woefully unaware of, which I feel are extremely important to note
here.

Github's LFS support is metered. There are two values which come into
play to measure the usage of LFS. There is a "storage" number which is
updated whenever new files are pushed into LFS. Then there is a
"bandwidth" number, which is updated whenever new files are pulled
from LFS. The metering totals are counted against the owner of the
repositories. In my case this meant my user account. The free tier
monthly allocations for both values are a paltry 1GB. There are some
huge, gigantic, major problems that arise from these metering methods.

The bandwidth value is consumed by any and all downloaders. If your
repository is public this means any random person or bot can (and
will) consume your resources. I personally experienced this when two
unknown users performed clones on the 2nd and then 5th of
February 2024. I received an email alert from Github stating that I
had consumed 86% of my bandwidth allotment for the month. This was
quite the surprise, as I had done nothing with my blog at that point
in time for over two months.

When I noted above that bandwidth is consumed by any and all
downloaders, this also includes Github's own runners. The workflow for
building these pages means checking it out and then running pelican to
produce the static site for upload. That checkout process needs to
pull from LFS to fetch the images, and Github didn't deem it necessary
to grant its own builders unfettered access.

Two random, anonymous clones meant that I no longer had the resources
necessary to checkout the site sources for the rest of the month of
February.  Unless, of course, I were to buy a 5GB resource pack from
Github to temporarily grant more bandwidth to my account. Bandwidth
which could then be against consumed by anonymous checkouts.

Even if the bandwidth metering hadn't been impacted by anonymous
clones, the fact that Github's own action runners count against that
number means that I would likely run afoul of this any time I was
feeling slightly prolific.

There are other well-documented complaints against Git LFS that I've
come to realize. Most of these I would have probably ignored, as they
weren't particularly pertinent to my use case. I would not be worried
about how it don't operate well (or at all) with multiple remotes for
example. I didn't mind that it required having a separate package
installed in all the places I wanted to work.

Github's absolutely ridiculous [metering] and billing rules around the
use of LFS is the real and definite pain point. I've since migrated
the site back to just storing the original photos directly in git.

[metering]: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage

[billing]: https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/upgrading-git-large-file-storage#purchasing-additional-storage-and-bandwidth-for-a-personal-account

I feel that it is completely unreasonable that Github's action workers
consume project owner bandwidth numbers.

Thankfully I never *needed* to use LFS for this site. I simply thought
that perhaps the technology would be sensible for storage of static
binary content like source images. I doubt that I will ever find
myself in a position where I need large files support in git. If I do
there are two mandatory caveats. Firstly, I will absolutely ensure
that the project is configured to be owned by a dedicated organization
rather than by my user account. Secondly I will make the repository
private to prevent anonymous clones.

Github's LFS metering is an anti-feature. It is anti-open-source, and
should not be used excepting in extremely niche situations, and then
it must be heavily restrticted.
