# Documentation deployment

This repository is a static MkDocs Material site designed to live in GitHub.

## Local preview

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000/
```

## Build

```bash
mkdocs build --strict
```

## GitHub Pages

Push the repository to GitHub with `main` as the default branch. The included workflow publishes the generated site to the `gh-pages` branch.

```bash
git init
git add .
git commit -m "Initial DXSpider 1.57 documentation"
git branch -M main
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
```

In GitHub, configure **Settings → Pages** to deploy from the `gh-pages` branch if it is not selected automatically.

For a custom domain, set the final `site_url` in `mkdocs.yml` and configure the domain in GitHub Pages.
