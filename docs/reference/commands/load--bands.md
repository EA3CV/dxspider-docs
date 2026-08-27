# `LOAD/BANDS`

<div class="command-hero" markdown>

**Reload the band limits table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
LOAD/BANDS
```

**Reload the band limits table**

## Details

Reload the /spider/data/bands.pl file if you have changed it manually whilst
the cluster is running.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/bands.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BANDS
```

The built-in help is useful when checking the exact command set installed on a particular node.