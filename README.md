# DXSpider Documentation

Web-first documentation for **DXSpider 1.57**, applicable to **Mojo build 686 and later**.

The goal is not to reproduce the old manual. The site combines:

1. **Current `Commands_en.hlp`** — authoritative syntax, options, explanations and examples.
2. **Current `cmd/` source tree** — detects real commands and documentation gaps.
3. **Editorial guides** — task-oriented explanations, filter grammar, RBN workflows, administration and practical examples.
4. **GitHub Pages** — searchable, responsive web publication.

## Automatic command reference

`tools/generate_reference.py` parses the current DXSpider source and generates the command reference.

Every generated command page includes:

- USER / SYSOP / DUAL audience;
- all help-defined privilege variants;
- exact syntax;
- the current built-in help text;
- examples;
- links to related commands;
- a link to the current command source when available.

The GitHub workflow checks out the current documentation source revision, generates the reference, validates links, performs a strict MkDocs build and publishes to `gh-pages`.

## Preview locally

If DXSpider is checked out at `../dxspider`:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./rebuild.sh ../dxspider
mkdocs serve
```

## Publish

```bash
git add .
git commit -m "Rebuild DXSpider documentation"
git push
```

GitHub Actions performs the source checkout and reference generation automatically.

## Important maintenance rule

Do not hand-copy hundreds of command pages. Improve the DXSpider help or the generator/curated notes instead. That way the web reference follows the actual command set instead of slowly becoming another stale manual.
