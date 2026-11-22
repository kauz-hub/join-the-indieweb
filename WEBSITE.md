# Companion website

The website is contained in `docs/`. It is a static site designed to live alongside the original Markdown guide.

## Preview locally

Open `docs/index.html` in a browser. There is no server, installation, or build needed for the published site.

## Publish on GitHub Pages

1. Add the `docs/` directory, including its `.nojekyll` file, to the root of `join-the-indieweb`.
2. In the repository, go to **Settings → Pages**.
3. Under Build and deployment, choose **Deploy from a branch**.
4. Select `main` and `/docs`, then save.
5. Open the URL that GitHub Pages provides once deployment completes.

You may also upload only the contents of `docs/` to your own static host. Every internal link is relative, so the site works both at a domain root and in a project subdirectory.

## Updating the website

The existing Markdown files in `guides/`, `RESOURCES.md`, `INSPIRATION.md`, `CONTRIBUTING.md` and `LICENSE.md` are the source of truth for the reading pages. After editing them, run `python3 build_website.py` from the repository root with [Pandoc](https://pandoc.org/installing.html) installed. Commit the regenerated `docs/` files. The homepage and chapter summaries are defined in that script. Styles and interactions are in `docs/style.css` and `docs/site.js`.

The website links back to the original GitHub repository. If you move or fork it, change the repository URL in `build_website.py` and regenerate the HTML.

The site makes no analytics requests. The color theme and checklist preferences are stored only in the reader's browser, when local storage is available.

The theme is initialized in the document head before external stylesheets load, with a CSS fallback that honors the system preference when scripting is unavailable. Keep that early initialization in every page to prevent a saved dark theme from briefly rendering in light mode. The site uses no animated transitions or smooth scrolling. Run `node test-theme.cjs` after rebuilding to check theme initialization across all pages. The test covers saved preferences, system preferences and unavailable browser storage; it is a logic check, not a browser video or photosensitivity certification.
