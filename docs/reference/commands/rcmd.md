# `RCMD`

<div class="command-hero" markdown>

**Send a command to another DX Cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
RCMD [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`DXProt::addrcmd()`, `Route::Node::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/rcmd.pl` · SHA-256 `858828c073a46c8b2026d31ee830c8c2f238812fd7ef0b98727133c2d0f0311b`

```perl
L9: my $self = shift;
L10: my $line = shift;
L11: my ($call) = $line =~ /^\s*(\S+)/;
L21: $line =~ s/^\s*$call\s+//;
L29: DXProt::addrcmd($self, $call, $line);
L31: return (1, $self->msg('rcmdo', $line, $call));
```

### Validation and access evidence

Source: `cmd/rcmd.pl` · SHA-256 `858828c073a46c8b2026d31ee830c8c2f238812fd7ef0b98727133c2d0f0311b`

```perl
L12: return (1, $self->msg('e5')) if $self->remotecmd;
L15: return (1, $self->msg('e5')) if $self->priv < 6;
L18: return (1, $self->msg('e6')) unless $call;
L26: return (1, $self->msg('e7', $call)) unless $noderef;
L31: return (1, $self->msg('rcmdo', $line, $call));
```

### Output and error evidence

Source: `cmd/rcmd.pl` · SHA-256 `858828c073a46c8b2026d31ee830c8c2f238812fd7ef0b98727133c2d0f0311b`

```perl
L12: return (1, $self->msg('e5')) if $self->remotecmd;
L15: return (1, $self->msg('e5')) if $self->priv < 6;
L18: return (1, $self->msg('e6')) unless $call;
L26: return (1, $self->msg('e7', $call)) unless $noderef;
L31: return (1, $self->msg('rcmdo', $line, $call));
```

### Message keys returned

`e5`, `e6`, `e7`, `rcmdo`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
RCMD <node call> <cmd>
```

**Send a command to another DX Cluster**

## Details

This command allows you to send nearly any command to another DX Cluster
node that is connected to the system.

Whether you get any output is dependant on a) whether the other system knows
that the node callsign of this cluster is in fact a node b) whether the
other system is allowing RCMDs from this node and c) whether you have
permission to send this command at all.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/rcmd.pl){ .md-button }

## Verify on a running node

```text
HELP RCMD
```

Compare the installed handler with this page when local overrides or a different revision may be present.