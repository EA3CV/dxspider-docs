# `UNSET/LOCKOUT`

<div class="command-hero" markdown>

**Allow a callsign to connect to the cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/LOCKOUT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command description

```text
UNSET/LOCKOUT <call>
```

**Allow a callsign to connect to the cluster**

## Details

If <call> is a bare callsign with no SSID, then the command will scan all the
callsigns in the User database that both that AND callsigns-xx and will
(un)lock those records. If a specific callsign-xx is used then only that callsign
will (un)locked.

If you only want to (un)lock a bare callsign then add '-0' e.g G1TLH-0.

## Verify on a running node

```text
HELP UNSET/LOCKOUT
```

Use the node help to check for local overrides or differences in another installed revision.