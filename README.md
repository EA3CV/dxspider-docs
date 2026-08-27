# DXSpider Documentation

Modern web documentation for **DXSpider 1.57**, applicable to **Mojo build 686 and later**.

## Philosophy

This is not an A–Z list padded with generated one-line descriptions.

The site combines:

- the current `Commands_en.hlp`;
- the current `cmd/` source tree;
- task-oriented guides and recipes;
- a dedicated filter-language guide;
- editorial examples for important workflows;
- separate User and SYSOP navigation;
- a searchable MkDocs Material site.

Internal command authorization levels are intentionally not published.

## Automatic reference build

The GitHub workflow checks out the current DXSpider source, parses its help and command tree, generates the reference, validates the documentation and publishes GitHub Pages.

The generator never invents descriptions from command filenames. If a command lacks useful source/help documentation, that is a documentation gap to fix rather than an excuse to publish filler text.

## Local preview

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./rebuild.sh ../dxspider
mkdocs serve
```

## Publish

```bash
git add -A
git commit -m "Upgrade DXSpider documentation"
git push
```
