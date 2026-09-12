# `SET/NAME`

<div class="command-hero" markdown>

**Set your name**

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
SET/NAME [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->name()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/name.pl` · SHA-256 `b5ca995fcb8b9d16dadb54678170c65b813ee899ebf263d6598d8f9c63ecc5e0`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L16: $line =~ s/[{}]//g; # no braces allowed
L18: return (1, $self->msg('namee1')) if !$line;
L22: $user->name($line);
L24: my $s = DXProt::pc41($call, 1, $line);
L27: return (1, $self->msg('name', $line));
```

### Validation and access evidence

Source: `cmd/set/name.pl` · SHA-256 `b5ca995fcb8b9d16dadb54678170c65b813ee899ebf263d6598d8f9c63ecc5e0`

```perl
L18: return (1, $self->msg('namee1')) if !$line;
L27: return (1, $self->msg('name', $line));
L29: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/name.pl` · SHA-256 `b5ca995fcb8b9d16dadb54678170c65b813ee899ebf263d6598d8f9c63ecc5e0`

```perl
L18: return (1, $self->msg('namee1')) if !$line;
L27: return (1, $self->msg('name', $line));
L29: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`name`, `namee1`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/NAME <your name>
```

**Set your name**

## Details

Tell the system what your name is eg:-
```text
SET/NAME Dirk
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/name.pl){ .md-button }

## Verify on a running node

```text
HELP SET/NAME
```

Compare the installed handler with this page when local overrides or a different revision may be present.