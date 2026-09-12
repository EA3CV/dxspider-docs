# `UNSET/PASSPHRASE`

<div class="command-hero" markdown>

**unset a user's passphrase Syntax: unset/passphrase <callsign> ...**

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
UNSET/PASSPHRASE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `ref->put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/passphrase.pl` · SHA-256 `9c4759ce4d95ffc6da39009af3932c0326c27ac04b63a3abcc96c7e856aa2ac0`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L16: Log('DXCommand', $self->call . " attempted to unset passphrase for @args remotely");
L21: Log('DXCommand', $self->call . " attempted to unset passphrase for @args");
L25: for (@args) {
```

### Validation and access evidence

Source: `cmd/unset/passphrase.pl` · SHA-256 `9c4759ce4d95ffc6da39009af3932c0326c27ac04b63a3abcc96c7e856aa2ac0`

```perl
L15: if ($self->remotecmd || $self->inscript) {
L17: return (1, $self->msg('e5'));
L20: if ($self->priv < 9) {
L22: return (1, $self->msg('e5'));
```

### Output and error evidence

Source: `cmd/unset/passphrase.pl` · SHA-256 `9c4759ce4d95ffc6da39009af3932c0326c27ac04b63a3abcc96c7e856aa2ac0`

```perl
L17: return (1, $self->msg('e5'));
L22: return (1, $self->msg('e5'));
L30: push @out, $self->msg("passphraseu", $call);
L33: push @out, $self->msg('e3', 'User record for', $call);
L37: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `passphraseu`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/passphrase.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PASSPHRASE
```

Compare the installed handler with this page when local overrides or a different revision may be present.