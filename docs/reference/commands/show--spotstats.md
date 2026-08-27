# `SHOW/SPOTSTATS`

<div class="command-hero" markdown>

**Show the current Spot statistics**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/SPOTSTATS
```

**Show the current Spot statistics**

## Details

View the current unique spot sentences seen since the last restart.

It shows the number of PC11 and PC61 sentences and the percentage
of PC11s received of the total of both. It also shows the number
of PC11s that have been promoted to PC61 before being passed on
plus a total percentage of incoming PC11 that have been promoted.

A PC11 can be promoted to PC61 by a stored IP address in the routing
table or it can be promoted by being delayed to a short for any
passing PC61 from another node.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/spotstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SPOTSTATS
```

The built-in help is useful when checking the exact command set installed on a particular node.