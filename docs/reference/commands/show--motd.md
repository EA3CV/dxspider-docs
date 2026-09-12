# `SHOW/MOTD`

<div class="command-hero" markdown>

**Show your MOTD (the Message of the Day)**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/MOTD [arguments; see parser evidence]
```

## Command description

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

## Verify on a running node

```text
HELP SHOW/MOTD
```

Use the node help to check for local overrides or differences in another installed revision.