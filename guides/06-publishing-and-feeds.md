# 6. Publishing, feeds and syndication

[Home](../README.md) · [Next: IndieWeb standards](07-indieweb-standards.md)

## Give each post its own URL

Keep posts in HTML or a portable format such as Markdown. Store a publication date and title where applicable. Use a permanent URL and keep it stable when you redesign the site. Back up the original files and media.

## Add a feed

RSS and Atom are machine-readable formats for publishing updates. Feed readers periodically check the feed, allowing people to follow your writing without an account on your site. [JSON Feed](https://www.jsonfeed.org/) is another format, though reader support varies.

Many blogs and generators create a feed automatically. Check that its URL works and that it contains the correct titles, dates and permanent links. Add a visible Subscribe link and advertise the feed in the HTML head. For RSS:

```html
<link rel="alternate" type="application/rss+xml"
      title="My blog" href="/feed.xml">
```

Use the actual path for your site, particularly if it's hosted under a subdirectory. Verify it with the [W3C Feed Validation Service](https://validator.w3.org/feed/). For more details, see [IndieWeb's feed page](https://indieweb.org/feed).

## Follow other people

Try [Feedly](https://feedly.com/), [Inoreader](https://www.inoreader.com/), [NewsBlur](https://newsblur.com/) or a self-managed reader such as [FreshRSS](https://freshrss.org/) or [Miniflux](https://miniflux.app/). Check support for OPML import and export so you can move your subscription list.

Subscribe to five personal blogs you really want to read. Add some to your own blogroll, and send a thoughtful reply when a post resonates.

## POSSE: publish on your own site, syndicate elsewhere

1. Put the original post on your site.
2. Share a link, excerpt or copy to the social services you use.
3. Include a link back to the original page where practical.
4. Optionally record the URL of the syndicated copy on your original post.

Read [POSSE](https://indieweb.org/POSSE). You can do this manually. Automation is useful only when it saves you effort, and platform APIs change.

**PESOS** is publishing on another service first and copying it to your own site. It can be handy if your existing workflow is easier to keep. **Backfeed** means bringing reactions from syndicated copies back to the original post, where supported.

Read [PESOS](https://indieweb.org/PESOS) and [backfeed](https://indieweb.org/backfeed). [Bridgy](https://brid.gy/) supports certain connections between sites and social services. Review its current supported services and privacy model. [Bridgy Fed](https://fed.brid.gy/) is a separate federation bridge. Neither is required to participate.
