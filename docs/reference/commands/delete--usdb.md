# `DELETE/USDB`

<div class="command-hero" markdown>

**Delete this user from the US State Database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DELETE/USDB <callsign> ...
```

**Delete this user from the US State Database**

## Details

This command will completely remove a one or more callsigns
from the US States database.

There is NO SECOND CHANCE.

It goes without saying that you should use this command CAREFULLY!

Note that these callsign may be re-instated by any weekly updates from
the FCC.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/delete/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP DELETE/USDB
```

The built-in help is useful when checking the exact command set installed on a particular node.