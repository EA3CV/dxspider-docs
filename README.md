# DXSpider Documentation 1.57

Modern, web-first documentation for **DXSpider 1.57**, applicable to **Mojo build 686 and later**.

## What is included

- Clear **User** / **SYSOP** separation.
- Searchable MkDocs Material website.
- **305 public command-reference entries**.
- Root commands plus command families such as `SHOW/`, `SET/`, `UNSET/`, `ACCEPT/`, `REJECT/`, `CLEAR/`, `LOAD/`, `STAT/` and others.
- Modern RBN documentation.
- Current privilege model.
- Legacy protocol material isolated from current-operation guidance.
- Maintainer audit CSV and internal audit notes.
- GitHub Pages workflow.

## Install locally

```bash
unzip dxspider-docs-final.zip
cd dxspider-docs-final

python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

mkdocs serve
```

Browse to:

```text
http://127.0.0.1:8000/
```

## Validate/build

```bash
mkdocs build --strict
```

## Install on GitHub

Create an empty GitHub repository, then:

```bash
git init
git add .
git commit -m "DXSpider 1.57 documentation"
git branch -M main
git remote add origin https://github.com/<owner>/<repository>.git
git push -u origin main
```

The included GitHub Actions workflow publishes the site with `mkdocs gh-deploy`.

If required, open **GitHub → Settings → Pages** and select the `gh-pages` branch.

## Custom domain

Edit:

```yaml
site_url: https://docs.example.org/
```

in `mkdocs.yml`, then configure the same domain in GitHub Pages.

## Source-of-truth policy

Current DXSpider code is authoritative. Historical manuals and wiki pages are secondary sources and are not copied blindly when their protocol or storage descriptions no longer represent current operation.
