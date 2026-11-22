# 7. Connect your site: IndieWeb standards

[Home](../README.md) · [Next: community](08-community.md)

This chapter is optional. You can own your site and publish for years without implementing every protocol.

| Technology | What it enables | When to add it |
|---|---|---|
| [Microformats2](https://microformats.org/wiki/microformats2) | Structured information inside HTML | Once your homepage or blog exists |
| [rel-me](https://indieweb.org/rel-me) | Relationships between your own profiles | When identifying accounts you control |
| [Webmention](https://www.w3.org/TR/webmention/) | Notify another site that you linked to it | When you want cross-site replies and mentions |
| [IndieAuth](https://indieauth.spec.indieweb.org/) | Use your web address in a sign-in flow | When a service or publishing client needs it |
| [Micropub](https://www.w3.org/TR/micropub/) | Publish from compatible third-party apps | When you want more ways to write |
| [Microsub](https://microsub.spec.indieweb.org/) | Separate feed-reader clients and subscription servers | When you want an interoperable reader |
| [WebSub](https://www.w3.org/TR/websub/) | Push updates to subscribers | When low-latency feed delivery matters |

## Step 1: mark up your profile

Microformats add class names to visible HTML. An `h-card` describes a person or organization. An `h-entry` describes a post or similar entry. The `p-` prefix describes plain text, `u-` a URL, `dt-` a date/time, and `e-` embedded markup.

```html
<div class="h-card">
  <a class="p-name u-url" href="https://example.com/">Your name</a>
  <p class="p-note">I write about books and the web.</p>
</div>
```

Only expose information you actually want public. See [h-card](https://microformats.org/wiki/h-card), [h-entry](https://microformats.org/wiki/h-entry) and [h-feed](https://microformats.org/wiki/h-feed).

## Step 2: give a post useful metadata

```html
<article class="h-entry">
  <h1 class="p-name">My first post</h1>
  <a class="p-author h-card" href="https://example.com/">Your name</a>
  <a class="u-url" href="https://example.com/blog/first/">
    <time class="dt-published" datetime="2026-11-21">21 Nov 2026</time>
  </a>
  <div class="e-content"><p>Hello, web.</p></div>
</article>
```

Replace example URLs and names with your own. Use [IndieWebify.me](https://indiewebify.me/) or [microformats.io](https://microformats.io/) to inspect your markup.

## Step 3: link your identities

Add `rel="me"` to links to profiles that you control, and where supported, link back to your homepage from those profiles. This helps establish relationships, but a rel-me link alone does not create an IndieAuth server or guarantee that every service will accept it. See [web sign-in](https://indieweb.org/How_to_set_up_web_sign-in) and your actual authentication provider's setup instructions.

## Step 4: try Webmentions

A Webmention sender notifies the target site of a source URL that links to it. The receiver checks that relationship. It can choose to display the mention, extract a reply or ignore it.

On a static site, you can use [Webmention.io](https://webmention.io/) as an external receiving service. Follow its setup instructions and publish the endpoint it assigns you. Use compatible tooling to send mentions, and display approved mentions from cached or retrieved data. Receiving and displaying are separate tasks. [IndieWeb's Webmention page](https://indieweb.org/Webmention) has examples for many stacks.

Moderate incoming messages. Render untrusted names, content and URLs safely. Keep private API tokens in server or build secrets, never HTML, JavaScript shipped to browsers or public Git commits.

## Step 5: advanced publishing and reading

Micropub is an API for creating and managing posts using authorized clients. Try a compatible CMS or publishing service before building an endpoint yourself. [Quill](https://quill.p3k.io/) is an example client. Microsub provides an architectural separation between subscription backends and reader interfaces. Pick an existing implementation and check current support.

Full reference: [IndieWeb specifications](https://indieweb.org/specifications) and [spec.indieweb.org](https://spec.indieweb.org/).
