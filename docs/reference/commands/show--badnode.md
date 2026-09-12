# `SHOW/BADNODE`

<div class="command-hero" markdown>

**Show all the bad nodes in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/BADNODE [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

```text
SHOW/BADNODE
```

**Show all the bad nodes in the system**

## Details

Display all the bad node callsigns in the system, see SET/BADNODE
for more information.

## Verify on a running node

```text
HELP SHOW/BADNODE
```

Use the node help to check for local overrides or differences in another installed revision.