# `SET/NODE`

<div class="command-hero" markdown>

**Make the callsign an AK1A cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/NODE <call> [<call>..]
```

**Make the callsign an AK1A cluster**

## Details

Tell the system that the call(s) are to be treated as AK1A cluster and
fed PC Protocol rather normal user commands.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/node.pl){ .md-button }

## Verify on a running node

```text
HELP SET/NODE
```

The built-in help is useful when checking the exact command set installed on a particular node.