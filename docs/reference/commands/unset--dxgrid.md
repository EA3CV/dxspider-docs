# `UNSET/DXGRID`

<div class="command-hero" markdown>

**Stop QRA Grid Squares on the end of DX announcements**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/DXGRID [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
UNSET/DXGRID
```

**Stop QRA Grid Squares on the end of DX announcements**

## Details

A standard feature which is enabled in version 1.43 and above is
that if the spotter's grid square is known it is output on the end
of a DX announcement (there is just enough room). Some user programs
cannot cope with this. You can use this command to reset (or set)
this feature.

Conflicts with: SET/DXCQ, SET/DXITU

Do a STAT/USER to see which flags you have set if you are confused.

## Verify on a running node

```text
HELP UNSET/DXGRID
```

Use the node help to check for local overrides or differences in another installed revision.