# DXSpider Documentation

Modern web documentation for **DXSpider 1.57**, applicable to **Mojo build 686 and later**.

## Philosophy

This is not an A–Z list padded with generated one-line descriptions.

The site combines:

- the commands actually available in the current DXSpider version;
- arguments, accepted options and access restrictions verified against current behaviour;
- the current English help as an editorial starting point, never as the sole authority;
- task-oriented guides and recipes;
- a dedicated filter-language guide;
- practical command forms and realistic examples;
- separate User and SYSOP navigation;
- a searchable MkDocs Material site.

The implementation is inspected only during generation and verification. Source code,
internal routines, file paths, line-level evidence and internal authorization levels
are intentionally not published on command-guide pages.

## Automatic reference build

The GitHub workflow checks out the current DXSpider source, parses its help and command tree, generates the reference, validates the documentation and publishes GitHub Pages.

Every available command receives a page, including commands missing from the old help.
The generator does not invent behaviour from command names. When the available evidence
is insufficient, the page says so and recommends checking the running node instead of
presenting an assumption as fact.

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
