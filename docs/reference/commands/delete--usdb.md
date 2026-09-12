# `DELETE/USDB`

<div class="command-hero" markdown>

**Delete this user from the US State Database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DELETE/USDB [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
DELETE/USDB <callsign> ...
```

**Delete this user from the US State Database**

## Details

This command will completely remove a one or more callsigns
from the US States database.

There is NO SECOND CHANCE.

It goes without saying that you should use this command CAREFULLY!

Note that these callsign may be re-instated by any weekly updates from
the FCC.

## Verify on a running node

```text
HELP DELETE/USDB
```

Use the node help to check for local overrides or differences in another installed revision.