# `LOAD/BADIP`

<div class="command-hero" markdown>

**Reload the bad IP address table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/badip.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BADIP
```

The built-in help is useful when checking the exact command set installed on a particular node.