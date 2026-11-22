# 9. Care for your site

[Home](../README.md) · [Resource directory](../RESOURCES.md)

The goal is a website you can maintain for years. A few basic habits go a long way.

## Privacy

- Decide whether to publish your real name, an alias, photos, email address or location. A personal site can be pseudonymous.
- Remove sensitive metadata from photos before publishing, especially GPS coordinates. Avoid sharing other people's personal details without consent.
- Remember that public pages can be indexed, copied and archived. `robots.txt` is not access control. Use actual authentication for private pages.
- Choose third-party embeds with care. They can collect visitor information, add dependencies or break later.
- If you collect comments or analytics, explain what you collect, why and how you handle it. Review the requirements applicable to you.

## Accessibility and performance

- Use semantic HTML, descriptive titles, clear links and meaningful alternative text.
- Ensure text and controls have sufficient contrast and can be enlarged without breaking the layout.
- Test using only a keyboard, with visible focus, and on small screens.
- Provide controls for media and respect reduced-motion preferences.
- Compress large images and avoid unnecessary JavaScript.

Read [W3C WAI's accessibility introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/) and [MDN accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility). Automated checks help, but they do not replace manual testing.

## Security and continuity

- Use HTTPS and enable multifactor authentication at your registrar, host and Git provider.
- Keep recovery codes offline. Never publish credentials or private API tokens.
- If you run a CMS, promptly install supported software updates and remove unused plugins.
- Moderate guestbooks, comments and mentions before publishing untrusted submissions.
- Export posts, images, database content when applicable, redirects and source files. Test that you can restore them somewhere else.
- Document how you deploy the site and where domain renewal happens.

## A maintenance checklist

| When | Task |
|---|---|
| After publishing | Check links, mobile view, media, post URL and feed |
| Monthly | Update maintained dependencies and export recent content |
| Quarterly | Test backups, review broken links and contact information |
| Annually | Review domain renewal, service costs, ownership details and recovery options |
| Before migrating | Export everything and preserve URLs |

## Common problems

| Problem | Things to check |
|---|---|
| Homepage shows 404 | Is `index.html` in the published root? Is the correct branch deployed? |
| Images missing | Verify case-sensitive paths and project base URL. |
| Custom domain fails | Check host verification, DNS records, certificate state and DNS propagation. |
| Feed doesn't update | Check build settings, cached output and feed validation. |
| Webmentions don't show | Check endpoint discovery, source links, receiving service, moderation and rendering. |
| Can't update the site easily | Simplify your workflow or consider a static generator or hosted CMS. |

If you stop using a site, consider leaving a readable archive and redirecting important URLs. You don't have to keep posting forever.
