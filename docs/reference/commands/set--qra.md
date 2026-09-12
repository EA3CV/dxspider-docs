# `SET/QRA`

<div class="command-hero" markdown>

**Set your QRA Grid locator**

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
SET/QRA [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Uses or emits DX protocol data.

### Important calls

`DXBearing::lltos()`, `DXBearing::qratoll()`, `DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`, `user->lat()`, `user->long()`, `user->put()`, `user->qra()`

### Argument parsing evidence

Source: `cmd/set/qra.pl` · SHA-256 `d70e82eaec4a00e61040713d95ca76488606e9f2ae82d4fe6fb99f318dd1ac13`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L17: return (1, $self->msg('qrae1')) if !$line;
L18: return (1, $self->msg('qrae2', $line)) unless is_qra($line);
L22: my $qra = uc $line;
L43: return (1, $self->msg('qra', $line));
```

### Validation and access evidence

Source: `cmd/set/qra.pl` · SHA-256 `d70e82eaec4a00e61040713d95ca76488606e9f2ae82d4fe6fb99f318dd1ac13`

```perl
L17: return (1, $self->msg('qrae1')) if !$line;
L18: return (1, $self->msg('qrae2', $line)) unless is_qra($line);
L43: return (1, $self->msg('qra', $line));
L45: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/qra.pl` · SHA-256 `d70e82eaec4a00e61040713d95ca76488606e9f2ae82d4fe6fb99f318dd1ac13`

```perl
L17: return (1, $self->msg('qrae1')) if !$line;
L18: return (1, $self->msg('qrae2', $line)) unless is_qra($line);
L43: return (1, $self->msg('qra', $line));
L45: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`namee2`, `qra`, `qrae1`, `qrae2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/QRA <locator>
```

**Set your QRA Grid locator**

## Details

Tell the system what your QRA (or Maidenhead) locator is. If you have not
done a SET/LOCATION then your latitude and longitude will be set roughly
correctly (assuming your locator is correct ;-). For example:-
```text
SET/QRA JO02LQ
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/qra.pl){ .md-button }

## Verify on a running node

```text
HELP SET/QRA
```

Compare the installed handler with this page when local overrides or a different revision may be present.