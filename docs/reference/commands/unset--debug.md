# `UNSET/DEBUG`

<div class="command-hero" markdown>

**Remove a debug level from the debug set**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/DEBUG [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
UNSET/DEBUG <name>
```

**Remove a debug level from the debug set**

## Details

You can choose to log several different levels.  The levels are

 chan
 state
 msg
 cron
 connect

You can show what levels you are logging with SHOW/DEBUG

## Verify on a running node

```text
HELP UNSET/DEBUG
```

Use the node help to check for local overrides or differences in another installed revision.