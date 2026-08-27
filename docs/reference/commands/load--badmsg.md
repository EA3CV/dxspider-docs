# `LOAD/BADMSG`

<div class="command-hero" markdown>

**Reload the bad msg table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
LOAD/BADMSG
```

**Reload the bad msg table**

## Details

Reload the /spider/msg/badmsg.pl file if you have changed it manually whilst
the cluster is running. This table contains a number of perl regular
expressions which are searched for in the fields targetted of each message.
If any of them match then that message is immediately deleted on receipt.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/badmsg.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BADMSG
```

The built-in help is useful when checking the exact command set installed on a particular node.