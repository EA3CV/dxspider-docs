# `SET/PRIVILEGE`

<div class="command-hero" markdown>

**Set privilege level on a call**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/PRIVILEGE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command description

```text
SET/PRIVILEGE <n> <call> [<call..]
```

**Set privilege level on a call**

## Details

Set the privilege level on a callsign. The privilege levels that pertain
to commands are as default:-
```text
0 - normal user
1 - allow remote nodes normal user RCMDs
5 - various privileged commands (including shutdown, but not disc-
    connect), the normal level for another node.
8 - more privileged commands (including disconnect)
9 - local sysop privilege. DO NOT SET ANY REMOTE USER OR NODE TO THIS
    LEVEL.
```
If you are a sysop and you come in as a normal user on a remote connection
your privilege will automatically be set to 0.

## Verify on a running node

```text
HELP SET/PRIVILEGE
```

Use the node help to check for local overrides or differences in another installed revision.