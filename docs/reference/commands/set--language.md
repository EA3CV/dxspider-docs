# `SET/LANGUAGE`

<div class="command-hero" markdown>

**Set the language you want to use**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/LANGUAGE [text]
```

### Available options and values

`cz`, `de`, `en`, `es`, `fr`, `it`, `nl`, `pt`

The valid combinations are described in the command forms and examples below.

## Command description

```text
SET/LANGUAGE <lang>
```

**Set the language you want to use**

## Details

You can select the language that you want the cluster to use. Currently
the languages available are en (English), de (German), es (Spanish),
Czech (cz), French (fr), Portuguese (pt), Italian (it) and nl (Dutch).

## Verify on a running node

```text
HELP SET/LANGUAGE
```

Use the node help to check for local overrides or differences in another installed revision.