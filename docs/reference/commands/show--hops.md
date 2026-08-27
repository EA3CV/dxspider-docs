# `SHOW/HOPS`

<div class="command-hero" markdown>

**Show the hop counts for a node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/HOPS <call> [ann|spots|route|wcy|wwv]
```

**Show the hop counts for a node**

## Details

This command shows the hop counts set up for a node. You can specify
which category you want to see. If you leave the category out then
all the categories will be listed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/hops.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/HOPS
```

The built-in help is useful when checking the exact command set installed on a particular node.