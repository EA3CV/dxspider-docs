# `UNSET/BADNODE`

<div class="command-hero" markdown>

**Allow spots from this node again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/BADNODE <call>..
```

**Allow spots from this node again**

## Details

Setting a callsign as a 'badnode' will prevent spots from that node
going any further. They will not be displayed and they will not be
sent onto other nodes.

The call must be a full eg:-

```text
set/badnode K1TTT
```

will stop anything from K1TTT. If you want SSIDs as well then you must
enter them specifically.

```text
unset/badnode K1TTT
```

will allow spots from him again.

Use with extreme care. This command may well be superceeded by FILTERing.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/badnode.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADNODE
```

The built-in help is useful when checking the exact command set installed on a particular node.