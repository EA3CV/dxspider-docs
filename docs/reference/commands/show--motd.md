# `SHOW/MOTD`

<div class="command-hero" markdown>

**Show your MOTD (the Message of the Day)**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/MOTD
```

**Show your MOTD (the Message of the Day)**

## Details

The Message of the Day is normally printed whenever one logs on. However
many people now login using logging programs or something other than plain
telnet or ax25 connections. This command allows the user (or the program)
to see what is in the MOTD.

The actual MOTD that you are shown depends on what carrier you are logged
on via, whether you are registered and some other factors that your sysop
may have thrown in.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/motd.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MOTD
```

The built-in help is useful when checking the exact command set installed on a particular node.