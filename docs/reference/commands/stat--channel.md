# `STAT/CHANNEL`

<div class="command-hero" markdown>

**Show the status of a channel on the cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
STAT/CHANNEL [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
STAT/CHANNEL [<callsign>]
```

**Show the status of a channel on the cluster**

## Details

Show the internal status of the channel object either for the channel that
you are on or else for the callsign that you asked for.

Only the fields that are defined (in perl term) will be displayed.

## Verify on a running node

```text
HELP STAT/CHANNEL
```

Use the node help to check for local overrides or differences in another installed revision.