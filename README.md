# DXSpider Documentation

Modern web documentation for **DXSpider 1.57**, applicable to **Mojo build 686 and later**.

## Philosophy

This is not an A–Z list padded with generated one-line descriptions.

The site combines, in this order of authority:

- the current `cmd/` source tree as the executable inventory and source of truth;
- implementation-derived argument, validation, restriction, effect and output evidence;
- the current `Commands_en.hlp` as secondary text that may lag the code;
- task-oriented guides and recipes;
- a dedicated filter-language guide;
- editorial examples for important workflows;
- separate User and SYSOP navigation;
- a searchable MkDocs Material site.

Internal command authorization levels are intentionally not published.

## Automatic reference build

The GitHub workflow checks out the current DXSpider source, parses its help and command tree, generates the reference, validates the documentation and publishes GitHub Pages.

Every executable `cmd/*.pl` handler receives a page, including commands missing from help. The generator never invents behaviour from a filename: uncertain or delegated semantics remain explicitly marked and are accompanied by exact source-line evidence.

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
