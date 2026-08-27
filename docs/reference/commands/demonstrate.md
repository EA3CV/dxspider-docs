# `DEMONSTRATE`

<div class="command-hero" markdown>

**Demonstrate a command to another user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DEMONSTRATE <call> <command>
```

**Demonstrate a command to another user**

## Details

This command is provided so that sysops can demonstrate commands to
other users. It runs a command as though that user had typed it in and
then sends the output to that user, together with the command that
caused it.

```text
DEMO g7brn sh/dx iota oc209
DEMO g1tlh set/here
```

Note that this command is similar to SPOOF and will have the same side
effects. Commands are run at the privilege of the user which is being
demonstrated to.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/demonstrate.pl){ .md-button }

## Verify on a running node

```text
HELP DEMONSTRATE
```

The built-in help is useful when checking the exact command set installed on a particular node.