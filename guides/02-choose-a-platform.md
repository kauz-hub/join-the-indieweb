# 2. Choose a platform

[Home](../README.md) · [Next: domains and hosting](03-domains-and-hosting.md)

Pick the platform that makes publishing easiest for you. You can move later if your content and domain are portable.

## Hosted writing platforms

| Option | Best for | Before choosing |
|---|---|---|
| [Bear Blog](https://bearblog.dev/) | Minimal text-focused blogging | Review [customization and domain docs](https://docs.bearblog.dev/) |
| [Pika](https://pika.page/) | A simple managed blog | Review [manual](https://pika.page/manual), including export and Micropub |
| [Micro.blog](https://micro.blog/) | Blogging with community and cross-posting features | Review [help](https://help.micro.blog/) and plans |
| [Write.as](https://write.as/) | Writing with a minimal interface | Compare domain and export features |
| [WordPress.com](https://wordpress.com/) | Managed CMS with editing tools | Check domain, plugin and export limits by plan |
| [Ghost](https://ghost.org/) | Publication and newsletter workflows | Compare hosted and self-managed editions |
| [omg.lol](https://omg.lol/) | Personal identity, profile and small-site services | Review [documentation](https://omg.lol/info) |

## Static hosting

Static hosts serve HTML, CSS, JavaScript and images. They usually don't run a database or server-side scripts for you.

| Option | Workflow |
|---|---|
| [Neocities](https://neocities.org/) | Edit or upload files through a web interface. Great for handmade homepages. |
| [Nekoweb](https://nekoweb.org/) | Small-web-focused static hosting. |
| [GitHub Pages](https://pages.github.com/) | Store files in Git and publish from a repository. |
| [Codeberg Pages](https://docs.codeberg.org/codeberg-pages/) | Static publishing with the nonprofit Codeberg forge. Read current git-pages setup instructions and eligibility. |
| [GitLab Pages](https://docs.gitlab.com/user/project/pages/) | Publish from a GitLab project using CI. |
| [Cloudflare Pages](https://pages.cloudflare.com/) | Upload or build a static project with Git integration. |
| [Netlify](https://www.netlify.com/) | Git deployments or manual uploads. |

Check current limits on bandwidth, storage, custom domains, build minutes and acceptable use. Some free tiers are enough for a personal site, while custom domains or added features may require payment.

## Static site generators

Once copying HTML for each post becomes tedious, a generator can turn Markdown and shared layouts into HTML files.

- [Eleventy](https://www.11ty.dev/): flexible JavaScript-based generator.
- [Hugo](https://gohugo.io/): standalone binary, themes and Go templates.
- [Jekyll](https://jekyllrb.com/): Markdown, Liquid and Ruby, with a long history on GitHub Pages.
- [Astro](https://docs.astro.build/): component-based content sites with optional interactivity.
- [Zola](https://www.getzola.org/): standalone Rust-based generator.

Generators are not hosting services. Keep source content and build configuration as well as published output.

## Dynamic CMS and self-hosting

[WordPress.org](https://wordpress.org/), [Ghost](https://ghost.org/) and [Known](https://withknown.com/) can manage posts and dynamic features. Managed hosting reduces operational work. A VPS gives more control but requires keeping the OS, applications, certificates and backups healthy.

For WordPress, read the [IndieWeb WordPress walkthrough](https://indieweb.org/Getting_Started_on_WordPress). Check plugin and theme compatibility before installing anything.

## Decision checklist

Before paying for anything, ask:

- Can I use a domain I control? Can I export posts, images and redirects?
- Can readers subscribe without an account?
- Can I publish what matters to me without changing my workflow every month?
- Is the price sustainable after any introductory offer?
- Can I leave without losing my address or years of work?

If you're still unsure, try a free hosted page or blog and publish something before researching more platforms.

For detailed starting paths, see [Neocities, Nekoweb and Bear Blog](11-three-ways-to-start.md).
