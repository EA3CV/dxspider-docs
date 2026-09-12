# `SET/HOMENODE`

<div class="command-hero" markdown>

**Set your normal cluster callsign**

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
SET/HOMENODE [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->homenode()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/homenode.pl` · SHA-256 `4f8b272a059ed82ec883de1e01697ebc274176a2bf01205a642465501ea77c76`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L16: $line =~ s/[{}]//g; # no braces allowed
L18: return (1, $self->msg('hnodee1')) if !$line;
L22: $line = uc unpad($line);
L23: if ($user->homenode && $line ne $user->homenode) {
L24: $user->homenode($line);
L26: my $s = DXProt::pc41($call, 4, $line);
L30: return (1, $self->msg('hnode', $line));
```

### Validation and access evidence

Source: `cmd/set/homenode.pl` · SHA-256 `4f8b272a059ed82ec883de1e01697ebc274176a2bf01205a642465501ea77c76`

```perl
L18: return (1, $self->msg('hnodee1')) if !$line;
L30: return (1, $self->msg('hnode', $line));
L32: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/homenode.pl` · SHA-256 `4f8b272a059ed82ec883de1e01697ebc274176a2bf01205a642465501ea77c76`

```perl
L18: return (1, $self->msg('hnodee1')) if !$line;
L30: return (1, $self->msg('hnode', $line));
L32: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`hnode`, `hnodee1`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/HOMENODE <node>
```

**Set your normal cluster callsign**

## Details

Tell the cluster system where you normally connect to. Any Messages sent
to you will normally find their way there should you not be connected.
eg:-
```text
SET/HOMENODE gb7djk
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/homenode.pl){ .md-button }

## Verify on a running node

```text
HELP SET/HOMENODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.