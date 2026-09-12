# `SET/SYS_LOCATION`

<div class="command-hero" markdown>

**Set your cluster latitude and longitude**

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
SET/SYS_LOCATION [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXBearing::lltos()`, `DXBearing::stoll()`, `DXChannel::broadcast_all_nodes()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->lat()`, `user->long()`, `user->put()`, `user->qra()`

### Argument parsing evidence

Source: `cmd/set/sys_location.pl` · SHA-256 `5cd5c9a6a8f8cb1b27ff9dfd23ceef55eb3d8a9617a85fb2b53f855f75c5cfb9`

```perl
L9: my ($self, $line) = @_;
L16: $line =~ s/^\s+//;
L17: $line =~ s/\s+$//;
L19: return (1, $self->msg('loce1')) if !$line;
L20: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L21: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L25: $line = uc $line;
L26: my ($lat, $long) = DXBearing::stoll($line);
L29: DXChannel::broadcast_all_nodes(DXProt::pc41($call, 3, $line), $main::me);
```

### Validation and access evidence

Source: `cmd/set/sys_location.pl` · SHA-256 `5cd5c9a6a8f8cb1b27ff9dfd23ceef55eb3d8a9617a85fb2b53f855f75c5cfb9`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
L19: return (1, $self->msg('loce1')) if !$line;
L20: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L21: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L36: return (1, $self->msg('sloc', $lat, $long));
L38: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/sys_location.pl` · SHA-256 `5cd5c9a6a8f8cb1b27ff9dfd23ceef55eb3d8a9617a85fb2b53f855f75c5cfb9`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
L19: return (1, $self->msg('loce1')) if !$line;
L20: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L21: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L36: return (1, $self->msg('sloc', $lat, $long));
L38: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`e5`, `loce1`, `loce2`, `loce3`, `namee2`, `sloc`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/SYS_LOCATION <lat & long>
```

**Set your cluster latitude and longitude**

## Details

In order to get accurate headings and such like you must tell the system
what your latitude and longitude is. If you have not yet done a SET/QRA
then this command will set your QRA locator for you. For example:-
```text
SET/LOCATION 52 22 N 0 57 E
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/sys_location.pl){ .md-button }

## Verify on a running node

```text
HELP SET/SYS_LOCATION
```

Compare the installed handler with this page when local overrides or a different revision may be present.