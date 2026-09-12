# `SHOW/LOCKOUT`

<div class="command-hero" markdown>

**Show the list of locked out or excluded callsigns**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/LOCKOUT [token ...]
```

### Available options and values

`ALL`

The valid combinations are described in the command forms and examples below.

## Command description

```text
SHOW/LOCKOUT <prefix>|ALL
```

**Show the list of locked out or excluded callsigns**

## Details

This command works in the same general way as SET/LOCKOUT, in that using a bare
callsign without ssid will show all the callsign + ssid users as well as the bare callsign. In
order to just see the base callsign's lock status, use the ssid '-0'. E.g. G1TLH-0.

The ALL keyword will search through the user database for callsigns that are locked.

## Verify on a running node

```text
HELP SHOW/LOCKOUT
```

Use the node help to check for local overrides or differences in another installed revision.