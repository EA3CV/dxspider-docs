# `HELP`

<div class="command-hero" markdown>

**The HELP Command**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
HELP
```

**The HELP Command**

## Details

HELP is available for a number of commands. The syntax is:-

```text
HELP <cmd>
```

Where <cmd> is the name of the command you want help on.

All commands can be abbreviated, so SHOW/DX can be abbreviated
to SH/DX, ANNOUNCE can be shortened to AN and so on.

Look at the APROPOS <string> command which will search the help database
for the <string> you specify and give you a list of likely commands
to look at with HELP.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/help.pl){ .md-button }

## Verify on a running node

```text
HELP HELP
```

The built-in help is useful when checking the exact command set installed on a particular node.