# `RCMD`

<div class="command-hero" markdown>

**Send a command to another DX Cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
RCMD [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

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

## Verify on a running node

```text
HELP RCMD
```

Use the node help to check for local overrides or differences in another installed revision.