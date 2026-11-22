# 3. Domains, DNS and hosting

[Home](../README.md) · [Next: learn the web](04-learn-the-web.md)

A domain is your address (`example.com`). Hosting is where your website lives. DNS tells browsers which host serves your address. You can buy a domain from one company and host your site with another.

## Register a domain

1. Choose a name you can keep for years. An alias is fine.
2. Compare the renewal price, transfer policy, privacy options and supported extensions. Registrars include [Porkbun](https://porkbun.com/), [Namecheap](https://www.namecheap.com/) and [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/).
3. Register in an account you control using accurate required details. Review what the registry makes public, since policies differ by extension.
4. Enable multifactor authentication, keep recovery information offline and set renewal reminders. A lapse can cost you your address.
5. Keep the receipt and record your registrar, host and DNS provider.

You can start without purchasing anything. A provider subdomain is suitable for learning, but a registered domain is more portable.

## Connect your domain

Follow the documentation for your actual host. Don't copy DNS values from an unrelated tutorial.

| DNS record | Common purpose |
|---|---|
| A / AAAA | Point a name to an IPv4 / IPv6 address. |
| CNAME | Alias a name to another hostname, commonly for `www`. |
| TXT | Ownership verification and other text-based records. |
| MX | Mail delivery. Keep existing mail records when moving a website. |
| NS | Identify authoritative DNS servers. |

1. Add and verify the custom domain with the host.
2. Enter only the records required by that host in your DNS dashboard.
3. Wait for the host to verify DNS and issue its HTTPS certificate.
4. Open your address with HTTPS and test the `www` and non-`www` versions. Pick one canonical address and redirect the other when supported.

## Publish with GitHub Pages

For a free public personal site, create a repository named `YOUR-USERNAME.github.io`. Add `index.html`, images and CSS as needed. Open repository **Settings → Pages** and choose the source branch and folder, following the [official quickstart](https://docs.github.com/en/pages/quickstart).

Use the [official custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) to configure records. Verify domain ownership and avoid wildcard records. [Enable HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

Project sites may live below a path such as `username.github.io/project/`. Use correct relative asset paths and check your generator's base URL setting.

## Publish by uploading files

On a host such as Neocities or Nekoweb, create a site, open its file manager and upload `index.html` plus your CSS and assets. Keep the folder layout intact. You can usually preview locally first by opening the HTML file in a browser.

## Move hosts without breaking your site

- Back up content, images, feeds and configuration before migration.
- Deploy to the new host and test its temporary address.
- Maintain old URLs or configure permanent redirects.
- Update necessary DNS records, preserve mail settings and verify HTTPS.
- Keep the old hosting until the new site works and DNS has settled.

Read [MDN's publishing guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website) for the basics.
