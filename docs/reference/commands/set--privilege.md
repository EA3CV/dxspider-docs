# `SET/PRIVILEGE`

<div class="command-hero" markdown>

**Set privilege level on a call**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/privilege.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PRIVILEGE
```

The built-in help is useful when checking the exact command set installed on a particular node.