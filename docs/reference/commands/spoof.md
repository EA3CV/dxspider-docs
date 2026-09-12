# `SPOOF`

<div class="command-hero" markdown>

**Do a command as though you are another user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SPOOF [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Arguments

`call`, `newline`

## Command description

```text
SPOOF <call> <command>
```

**Do a command as though you are another user**

## Details

This command is provided so that sysops can set a user's parameters without
me having to write a special 'sysop' version for every user command. It
allows you to pretend that you are doing the command as the user you specify.

eg:-

```text
 SPOOF G1TLH set/name Dirk
 SPOOF G1TLH set/qra JO02LQ
```

## Verify on a running node

```text
HELP SPOOF
```

Use the node help to check for local overrides or differences in another installed revision.