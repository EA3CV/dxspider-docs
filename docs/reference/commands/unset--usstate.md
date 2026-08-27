# `UNSET/USSTATE`

<div class="command-hero" markdown>

**Stop US State info on the end of DX announcements**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/USSTATE
```

**Stop US State info on the end of DX announcements**

## Details

If the spotter's or spotted's US State is known it is output on the
end of a DX announcement (there is just enough room).

A spotter's state will appear on the RHS of the time (like
SET/DXGRID) and the spotted's State will appear on the LHS of the
time field. Any information found will override any locator
information from SET/DXGRID.

Some user programs cannot cope with this. You can use this command
to reset (or set) this feature.

Conflicts with: SET/DXCQ, SET/DXITU

Do a STAT/USER to see which flags you have set if you are confused.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/usstate.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/USSTATE
```

The built-in help is useful when checking the exact command set installed on a particular node.