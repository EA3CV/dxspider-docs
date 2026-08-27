# `SET/USDB`

<div class="command-hero" markdown>

**add/update a US DB callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/USDB <call> <state> <city>
```

**add/update a US DB callsign**

## Details

This command allows you to add or alter a callsign in the US state
database. Use with extreme caution. Anything you do here will be
overwritten by any weekly updates that affect this callsign

```text
set/usdb g1tlh nh downtown rindge
```

see also DELETE/USDB

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP SET/USDB
```

The built-in help is useful when checking the exact command set installed on a particular node.