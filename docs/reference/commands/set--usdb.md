# `SET/USDB`

<div class="command-hero" markdown>

**add/update a US DB callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/USDB [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

### Arguments

`call`, `state`, `city`

## Command description

```text
SET/USDB <call> <state> <city>
```

**add/update a US DB callsign**

## Details

This command allows you to add or alter a callsign in the US state
database. Use with extreme caution. Anything you do here will be
overwritten by any weekly updates that affect this callsign

```text
set/usdb g1tlh nh downtown rindge
```

see also DELETE/USDB

## Verify on a running node

```text
HELP SET/USDB
```

Use the node help to check for local overrides or differences in another installed revision.