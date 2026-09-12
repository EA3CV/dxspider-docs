# `SET/LOCATION`

<div class="command-hero" markdown>

**Set your latitude and longitude**

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
SET/LOCATION [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXBearing::lltoqra()`, `DXBearing::lltos()`, `DXBearing::stoll()`, `DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->lat()`, `user->long()`, `user->put()`, `user->qra()`

### Argument parsing evidence

Source: `cmd/set/location.pl` · SHA-256 `25045e57635223a35fc83ab0e346f739b8cfa3ba055a74b38394b462f8b7ee89`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L17: return (1, $self->msg('loce1')) if !$line;
L18: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L19: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L23: $line = uc $line;
L24: my ($lat, $long) = DXBearing::stoll($line);
L45: return (1, $self->msg('loc', $line));
```

### Validation and access evidence

Source: `cmd/set/location.pl` · SHA-256 `25045e57635223a35fc83ab0e346f739b8cfa3ba055a74b38394b462f8b7ee89`

```perl
L17: return (1, $self->msg('loce1')) if !$line;
L18: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L19: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L45: return (1, $self->msg('loc', $line));
L47: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/location.pl` · SHA-256 `25045e57635223a35fc83ab0e346f739b8cfa3ba055a74b38394b462f8b7ee89`

```perl
L17: return (1, $self->msg('loce1')) if !$line;
L18: return (1, $self->msg('loce3', uc $line)) if is_qra($line);
L19: return (1, $self->msg('loce2', $line)) unless is_latlong($line);
L45: return (1, $self->msg('loc', $line));
L47: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`loc`, `loce1`, `loce2`, `loce3`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/LOCATION <lat & long>
```

**Set your latitude and longitude**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/location.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LOCATION
```

Compare the installed handler with this page when local overrides or a different revision may be present.