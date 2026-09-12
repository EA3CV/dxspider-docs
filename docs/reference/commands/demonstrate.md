# `DEMONSTRATE`

<div class="command-hero" markdown>

**Demonstrate a command to another user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DEMONSTRATE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Arguments

`call`, `newline`

## Command description

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

## Verify on a running node

```text
HELP DEMONSTRATE
```

Use the node help to check for local overrides or differences in another installed revision.