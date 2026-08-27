# `UNSET/DXCQ`

<div class="command-hero" markdown>

**Stop CQ Zones on the end of DX announcements**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/DXCQ
```

**Stop CQ Zones on the end of DX announcements**

## Details

Display both the Spotter's and the Spotted's CQ Zone on the end
of a DX announcement (there is just enough room). Some user programs
cannot cope with this. The Spotter's CQ is on the RHS of the
time, the Spotted's CQ is on the LHS.

Conflicts with: SET/DXGRID, SET/DXITU, SHOW/USSTATE

Do a STAT/USER to see which flags you have set if you are confused.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/dxcq.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/DXCQ
```

The built-in help is useful when checking the exact command set installed on a particular node.