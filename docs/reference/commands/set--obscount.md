# `SET/OBSCOUNT`

<div class="command-hero" markdown>

**Set the 'pump-up' obscelence PING counter**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/OBSCOUNT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SET/OBSCOUNT <count> <call>
```

**Set the 'pump-up' obscelence PING counter**

## Details

From 1.35 onwards neighbouring nodes are pinged at regular intervals (see
SET/PINGINTERVAL), usually 300 seconds or 5 minutes. There is a 'pump-up'
counter which is decremented on every outgoing ping and then reset to
the 'obscount' value on every incoming ping. The default value of this
parameter is 2.

What this means is that a neighbouring node will be pinged twice at
(default) 300 second intervals and if no reply has been heard just before
what would be the third attempt, that node is disconnected.

If a ping is heard then the obscount is reset to the full value. Using
default values, if a node has not responded to a ping within 15 minutes,
it is disconnected.

You can set this parameter between 1 and 9.

It is STRONGLY recommended that you don't change the default.

## Verify on a running node

```text
HELP SET/OBSCOUNT
```

Use the node help to check for local overrides or differences in another installed revision.