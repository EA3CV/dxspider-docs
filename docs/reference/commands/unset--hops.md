# `UNSET/HOPS`

<div class="command-hero" markdown>

**Unset hop count**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/HOPS <call> ann|spots|route|wwv|wcy
```

**Unset hop count**

## Details

Set the hop count for a particular type of broadcast for a node.

This command allows you to set up special hop counts for a node
for currently: announce, spots, wwv and wcy broadcasts.

eg:
```text
set/hops gb7djk ann 10
set/hops gb7mbc spots 20
```

Set SHOW/HOPS for information on what is already set. This command
creates a filter and works in conjunction with the filter system.

You can unset the hops with command UNSET/HOPS. For example:-

```text
unset/hops gb7djk ann
unset/hops gb7mbc spots
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/hops.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/HOPS
```

The built-in help is useful when checking the exact command set installed on a particular node.