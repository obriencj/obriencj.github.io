---
title: Github and Git-LFS
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

I am ever eager to experiment with novel features of technology as
they catch my eye. I recently stumbled upon a fascinating thing named
git LFS which piqued my interest. So I endeavored to try it out on the
content of this site.

What a travesty that turned out to be.

<!-- more -->

*Note: This post will not include any form of instruction on how to
migrate to using git LFS, because I strongly discourage its use. This
is purely an explanation of my complaints with Github's LFS offering.*

[Git LFS][gitlfs] (Large File Support) is a method for storing large
files separately from the normal git repository storage backend. In
effect, a lookaside is engaged to hold the large file content, and
[JSON references] are put into their place. A convoluted form of a
symbolic link, in essence.

[gitlfs]: https://git-lfs.com/

[JSON references]: https://github.com/git-lfs/git-lfs/blob/main/docs/spec.md#the-pointer

I [host this site][host] via [github pages]. Its content [source] holds
a few images, which I've always felt a little bit odd about committing
directly into git. I had heard that Github supported LFS, so I thought
to myself that this would be an interesting opportunity to try the
feature out!

[host]: {filename}/content/blog/2023-09-27-migrating-from-octopress-to-pelican.md

[source]: https://github.com/obriencj/obriencj.github.io

[github pages]: https://pages.github.com/

There are a few facets to Github's implementation of git LFS that I
was woefully unaware of. Had I first read Github's explicit statements
on LFS support, I would likely have never used it. I will elaborate on
those points.

**Github's LFS support is metered**. There are two values which come
into play to measure the usage of LFS. There is a "storage" number
which is updated whenever new files are pushed into LFS. Then there is
a "bandwidth" number, which is updated whenever files are pulled from
LFS.

**The metering totals are spent from the resources of the owner
of the repository**. In this case that meant my own user account. The
free tier monthly allocations for both values are a paltry 1GB. There
are some huge, gigantic, major problems that arise from these metering
methods.

**The bandwidth value is consumed by any and all downloaders**. If
your repository is public this means any random person or bot can (and
will) consume your account's resources. I personally experienced this
when two unknown users performed clones on the 2nd and then 5th of
February 2024. I received an email alert from Github stating that I
had consumed 86% of my bandwidth allotment for the month. This was
quite the surprise, as I had done nothing with my blog at that point
in time for over two months.

**Even Github's own action runners consume bandwidth value**. The
workflow for building these pages means checking it out and then
running pelican to produce the static site for upload. That checkout
process needs to pull from LFS to fetch the images, and Github didn't
deem it necessary to grant its own builders unfettered access.

Two random, anonymous clones meant that I no longer had the resources
necessary to checkout the site sources for the rest of the month of
February.  Unless, of course, I were to buy a 5GB resource pack from
Github to temporarily grant more bandwidth to my account. Bandwidth
which could then be again consumed by anonymous checkouts.

Even if the bandwidth metering hadn't been impacted by anonymous
clones, the fact that Github's own action runners count against that
number means that I would likely run afoul of this any time I was
feeling slightly prolific.

There are other well-documented complaints against git LFS that I've
come to realize. Most of these I would have probably ignored, as they
weren't particularly pertinent to my use case. I would not be worried
about how it don't operate well (or at all) with multiple remotes for
example. I didn't mind that it required having a separate package
installed in all the places I wanted to work.

Github's absolutely ridiculous [metering] and [billing] rules around
the use of LFS is the real and definite pain point. I've since
migrated the site back to storing the original photos directly in git.

[metering]: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage

[billing]: https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/upgrading-git-large-file-storage#purchasing-additional-storage-and-bandwidth-for-a-personal-account

I feel that it is completely unreasonable that Github's action workers
consume project owner bandwidth numbers.

Thankfully I never *needed* to use LFS for this site. I simply thought
that perhaps the technology would be sensible for storage of static
binary content like source images. I doubt that I will ever find
myself in a position where I need large files support in git. If I do
there are two mandatory caveats before I would consider using it with
Github. Firstly, it would be necessary that the project is configured
to be owned by a dedicated organization rather than by my user
account. Secondly the repository would need to be made private to
prevent anonymous clones.

**Github's metering alone renders git LFS as an anti-feature**. It is
dangerous to open source projects, and should not be used except in
extremely niche situations.
