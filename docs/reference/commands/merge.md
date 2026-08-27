# `MERGE`

<div class="command-hero" markdown>

**Ask for the latest spots and WWV**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
MERGE <node> [<no spots>/<no wwv>]
```

**Ask for the latest spots and WWV**

## Details

MERGE allows you to bring your spot and wwv database up to date. By default
it will request the last 10 spots and 5 WWVs from the node you select. The
node must be connected locally.

You can request any number of spots or wwv and although they will be appended
to your databases they will not duplicate any that have recently been added
(the last 2 days for spots and last month for WWV data).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/merge.pl){ .md-button }

## Verify on a running node

```text
HELP MERGE
```

The built-in help is useful when checking the exact command set installed on a particular node.