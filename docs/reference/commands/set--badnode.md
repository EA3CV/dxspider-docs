# `SET/BADNODE`

<div class="command-hero" markdown>

**Stop spots from this node being propagated**

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
SET/BADNODE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`badnode->set()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/badnode.pl` · SHA-256 `10da9ea9025db6ca2869dc2d452bb2690aa935c0b8bc28592dbb075c25940e0d`

```perl
L8: my ($self, $line) = @_;
L13: return $DXProt::badnode->set(8, $self->msg('e12'), $self, $line);
```

### Validation and access evidence

Source: `cmd/set/badnode.pl` · SHA-256 `10da9ea9025db6ca2869dc2d452bb2690aa935c0b8bc28592dbb075c25940e0d`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::badnode->set(8, $self->msg('e12'), $self, $line);
```

### Output and error evidence

Source: `cmd/set/badnode.pl` · SHA-256 `10da9ea9025db6ca2869dc2d452bb2690aa935c0b8bc28592dbb075c25940e0d`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::badnode->set(8, $self->msg('e12'), $self, $line);
```

### Message keys returned

`e12`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/BADNODE <call>..
```

**Stop spots from this node being propagated**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/badnode.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BADNODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.