# `SET/QTH`

<div class="command-hero" markdown>

**Set your QTH**

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
SET/QTH [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->put()`, `user->qth()`

### Argument parsing evidence

Source: `cmd/set/qth.pl` · SHA-256 `2f61e0396a79c8495d5446608a783cfecce2a30799338c36a342a9d2d47e3355`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L16: $line =~ s/[{}]//g; # no braces allowed
L18: return (1, $self->msg('qthe1')) if !$line;
L22: $user->qth($line);
L24: my $s = DXProt::pc41($call, 2, $line);
L27: return (1, $self->msg('qth', $line));
```

### Validation and access evidence

Source: `cmd/set/qth.pl` · SHA-256 `2f61e0396a79c8495d5446608a783cfecce2a30799338c36a342a9d2d47e3355`

```perl
L18: return (1, $self->msg('qthe1')) if !$line;
L27: return (1, $self->msg('qth', $line));
L29: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/qth.pl` · SHA-256 `2f61e0396a79c8495d5446608a783cfecce2a30799338c36a342a9d2d47e3355`

```perl
L18: return (1, $self->msg('qthe1')) if !$line;
L27: return (1, $self->msg('qth', $line));
L29: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`namee2`, `qth`, `qthe1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/QTH <your qth>
```

**Set your QTH**

## Details

Tell the system where you are. For example:-
```text
SET/QTH East Dereham, Norfolk
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/qth.pl){ .md-button }

## Verify on a running node

```text
HELP SET/QTH
```

Compare the installed handler with this page when local overrides or a different revision may be present.