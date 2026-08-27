# `RCMD`

<div class="command-hero" markdown>

**Send a command to another DX Cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
RCMD <node call> <cmd>
```

**Send a command to another DX Cluster**

## Details

This command allows you to send nearly any command to another DX Cluster
node that is connected to the system.

Whether you get any output is dependant on a) whether the other system knows
that the node callsign of this cluster is in fact a node b) whether the
other system is allowing RCMDs from this node and c) whether you have
permission to send this command at all.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/rcmd.pl){ .md-button }

## Verify on a running node

```text
HELP RCMD
```

The built-in help is useful when checking the exact command set installed on a particular node.