# `UNSET/DXITU`

<div class="command-hero" markdown>

**Stop ITU Zones on the end of DX announcements**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/DXITU [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
UNSET/DXITU
```

**Stop ITU Zones on the end of DX announcements**

## Details

Display both the Spotter's and the Spotted's ITU Zone on the end
of a DX announcement (there is just enough room). Some user programs
cannot cope with this. The Spotter's ITU is on the RHS of the
time, the Spotted's ITU is on the LHS.

Conflicts with: SET/DXGRID, SET/DXCQ, SHOW/USSTATE

Do a STAT/USER to see which flags you have set if you are confused.

## Verify on a running node

```text
HELP UNSET/DXITU
```

Use the node help to check for local overrides or differences in another installed revision.