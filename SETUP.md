# Setup: Profile README + interactive portfolio

## Files in this package

- `README.md` — text/Markdown profile README; does not depend on SVG or image files.
- `index.html` — the complete single-file portfolio with its CSS and JavaScript embedded.

## Add these files to your profile repository

1. Open `https://github.com/VASANI007/VASANI007`.
2. Upload/replace `README.md` and upload `index.html` at the repository root (same level as README.md).
3. Commit the changes.
4. In the repository, open **Settings → Pages**.
5. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/(root)`, then Save.
6. After GitHub Pages deploys, the project site should be available at `https://vasani007.github.io/VASANI007/`.
7. Open that site once. If Pages uses a different URL in repository settings, update the portfolio link at the top of `README.md` to match it.

## Important limitation

GitHub renders README as Markdown with a restricted set of HTML. It does not run the page's custom CSS or JavaScript inside README, nor allow the full interactive page to be embedded there. This setup keeps the README itself image-free and uses a link to the full working website for animations and interactive features.

The portfolio uses Google Fonts, Lucide icons, and GitHub's public API; an internet connection is needed for those external services and live statistics.
