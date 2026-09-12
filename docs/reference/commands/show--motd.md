# `SHOW/MOTD`

<div class="command-hero" markdown>

**Show your MOTD (the Message of the Day)**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/MOTD [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Argument parsing evidence

Source: `cmd/show/motd.pl` · SHA-256 `0de802b5715c57c46bd7c9f9c088e7ceb61177c81a90938ae505b67ca85061b8`

```perl
L5: my ($self, $line) = @_;
```

### Output and error evidence

Source: `cmd/show/motd.pl` · SHA-256 `0de802b5715c57c46bd7c9f9c088e7ceb61177c81a90938ae505b67ca85061b8`

```perl
L9: return (1);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/motd.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MOTD
```

Compare the installed handler with this page when local overrides or a different revision may be present.