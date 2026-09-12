# `SET/REGISTER`

<div class="command-hero" markdown>

**Mark a user as registered**

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
SET/REGISTER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser->new()`, `DXUser::get_current()`, `dxchan->registered()`, `ref->put()`, `ref->registered()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/register.pl` · SHA-256 `6c3920ab64dbafce075d0241f6812c54dd12610ef59200cb11320bf8305a6b34`

```perl
L8: my ($self, $line) = @_;
L9: my @args = split /\s+/, $line;
L17: Log('DXCommand', $self->call . " attempted to register @args");
L22: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/register.pl` · SHA-256 `6c3920ab64dbafce075d0241f6812c54dd12610ef59200cb11320bf8305a6b34`

```perl
L16: if ($self->priv < 9) {
L18: return (1, $self->msg('e5'));
L24: unless ($self->remotecmd || $self->inscript) {
```

### Output and error evidence

Source: `cmd/set/register.pl` · SHA-256 `6c3920ab64dbafce075d0241f6812c54dd12610ef59200cb11320bf8305a6b34`

```perl
L18: return (1, $self->msg('e5'));
L28: push @out, $self->msg("reg", $call);
L33: push @out, $self->msg("regc", $call);
L40: push @out, $self->msg('sorry');
L43: return (1, @out);
```

### Message keys returned

`e5`, `reg`, `regc`, `reginac`, `sorry`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/REGISTER <call> ...
```

**Mark a user as registered**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/register.pl){ .md-button }

## Verify on a running node

```text
HELP SET/REGISTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.