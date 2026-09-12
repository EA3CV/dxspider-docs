# `SHOW/LOG`

<div class="command-hero" markdown>

**Show excerpts from the system log**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/LOG
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SHOW/LOG [<callsign>]
```

**Show excerpts from the system log**

## Details

This command outputs a short section of the system log.  On its own
it will output a general logfile.  With the optional callsign it will
show output from the log associated with that callsign.

## Verify on a running node

```text
HELP SHOW/LOG
```

Use the node help to check for local overrides or differences in another installed revision.