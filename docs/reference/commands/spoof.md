# `SPOOF`

<div class="command-hero" markdown>

**Do a command as though you are another user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/spoof.pl){ .md-button }

## Verify on a running node

```text
HELP SPOOF
```

The built-in help is useful when checking the exact command set installed on a particular node.