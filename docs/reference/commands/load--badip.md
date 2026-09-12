# `LOAD/BADIP`

<div class="command-hero" markdown>

**Reload the bad IP address table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/BADIP [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

```text
LOAD/BADIP
```

**Reload the bad IP address table**

## Details

Reload the badip address file(s) if you have changed any of them  manually
whilst the cluster is running.

You can edit the badip.* files manually in local_data or (for instance)
obtain some bad IP addresses from the web to replace badip.base for TOR
IP addresses (this filename may change).

There is (currently) no UNSET/BADIP command so you will need to edit
the badip.local file to remove IP addresses.

After modification, you can reload the database with:

```text
LOAD/BADIP
```

## Verify on a running node

```text
HELP LOAD/BADIP
```

Use the node help to check for local overrides or differences in another installed revision.