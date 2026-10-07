# Publish your portfolio and README

This package contains:
- `README.md` — GitHub profile README with a visual portfolio preview and project links.
- `index.html` — your single-file interactive portfolio (HTML, CSS and JavaScript in one file).
- `assets/portfolio-preview.png` and `assets/portfolio-preview.svg` — static preview assets displayed by the README.

## Upload to your repository

1. Open your profile repository: https://github.com/VASANI007/VASANI007
2. Replace the repository's `README.md` with this package's `README.md`.
3. Upload `index.html` to the repository root (same level as `README.md`).
4. Upload the `assets` folder including `portfolio-preview.svg`.
5. Commit the changes. The README preview will display on your profile.

## Enable GitHub Pages for the interactive website

1. In the repository, open **Settings → Pages**.
2. Under Build and deployment, select **Deploy from a branch**.
3. Choose branch `main` and folder `/ (root)`, then save.
4. Wait for GitHub Pages to publish. The project-site URL for a repository named `VASANI007` is normally `https://vasani007.github.io/VASANI007/`.
5. Once the site loads successfully, the README's **Open Live Portfolio** button will link to it.

GitHub README sanitizes HTML and does not run `<script>` or page-wide CSS from Markdown. Use Pages for the interactive site; use README for the preview, skills, projects, stats and links.
