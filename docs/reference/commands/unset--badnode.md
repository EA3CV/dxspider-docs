# `UNSET/BADNODE`

<div class="command-hero" markdown>

**Allow spots from this node again**

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
UNSET/BADNODE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`badnode->unset()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/badnode.pl` · SHA-256 `b73cb269b94669b1ef48e75f72290271acb51e376238f2a94c2c0d209fb1e127`

```perl
L8: my ($self, $line) = @_;
L13: return $DXProt::badnode->unset(8, $self->msg('e12'), $self, $line);
```

### Validation and access evidence

Source: `cmd/unset/badnode.pl` · SHA-256 `b73cb269b94669b1ef48e75f72290271acb51e376238f2a94c2c0d209fb1e127`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::badnode->unset(8, $self->msg('e12'), $self, $line);
```

### Output and error evidence

Source: `cmd/unset/badnode.pl` · SHA-256 `b73cb269b94669b1ef48e75f72290271acb51e376238f2a94c2c0d209fb1e127`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::badnode->unset(8, $self->msg('e12'), $self, $line);
```

### Message keys returned

`e12`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BADNODE <call>..
```

**Allow spots from this node again**

## Details

Setting a callsign as a 'badnode' will prevent spots from that node
going any further. They will not be displayed and they will not be
sent onto other nodes.

The call must be a full eg:-

```text
set/badnode K1TTT
```

will stop anything from K1TTT. If you want SSIDs as well then you must
enter them specifically.

```text
unset/badnode K1TTT
```

will allow spots from him again.

Use with extreme care. This command may well be superceeded by FILTERing.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/badnode.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADNODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.