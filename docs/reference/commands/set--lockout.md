# `SET/LOCKOUT`

<div class="command-hero" markdown>

**Stop a callsign connecting to the cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/LOCKOUT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command description

```text
SET/LOCKOUT <call>
```

**Stop a callsign connecting to the cluster**

## Verify on a running node

```text
HELP SET/LOCKOUT
```

Use the node help to check for local overrides or differences in another installed revision.