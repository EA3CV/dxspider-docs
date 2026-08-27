# `SET/LANGUAGE`

<div class="command-hero" markdown>

**Set the language you want to use**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/LANGUAGE <lang>
```

**Set the language you want to use**

## Details

You can select the language that you want the cluster to use. Currently
the languages available are en (English), de (German), es (Spanish),
Czech (cz), French (fr), Portuguese (pt), Italian (it) and nl (Dutch).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/language.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LANGUAGE
```

The built-in help is useful when checking the exact command set installed on a particular node.