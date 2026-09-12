# `LOAD/BADMSG`

<div class="command-hero" markdown>

**Reload the bad msg table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/BADMSG
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
LOAD/BADMSG
```

**Reload the bad msg table**

## Details

Reload the /spider/msg/badmsg.pl file if you have changed it manually whilst
the cluster is running. This table contains a number of perl regular
expressions which are searched for in the fields targetted of each message.
If any of them match then that message is immediately deleted on receipt.

## Verify on a running node

```text
HELP LOAD/BADMSG
```

Use the node help to check for local overrides or differences in another installed revision.