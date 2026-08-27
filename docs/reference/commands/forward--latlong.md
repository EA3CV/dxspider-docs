# `FORWARD/LATLONG`

<div class="command-hero" markdown>

**Send latitude and longitude information to another cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
FORWARD/LATLONG <node_call>
```

**Send latitude and longitude information to another cluster**

## Details

This command sends all the latitude and longitude information that your
cluster is holding against callsigns.  One advantage of recieving this
information is that more locator information is held by you.  This
means that more locators are given on the DX line assuming you have
SET/DXGRID enabled.  This could be a LOT of information though, so
it is not recommended on slow links.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/forward/latlong.pl){ .md-button }

## Verify on a running node

```text
HELP FORWARD/LATLONG
```

The built-in help is useful when checking the exact command set installed on a particular node.