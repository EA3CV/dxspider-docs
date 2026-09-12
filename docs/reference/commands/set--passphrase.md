# `SET/PASSPHRASE`

<div class="command-hero" markdown>

**set a user's passphrase Syntax: set/passphrase <callsign> <password>**

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
SET/PASSPHRASE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `ref->passphrase()`, `ref->put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/passphrase.pl` · SHA-256 `ceb86f1a01c199cb872cabec8fcf06cd3dc11c03ca1261c8ccd4336c6e1285a1`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line, 2;
L11: my $call = shift @args;
L27: return (1, $self->msg('e29')) unless @args;
```

### Validation and access evidence

Source: `cmd/set/passphrase.pl` · SHA-256 `ceb86f1a01c199cb872cabec8fcf06cd3dc11c03ca1261c8ccd4336c6e1285a1`

```perl
L16: if ($self->remotecmd || $self->inscript) {
L19: return (1, $self->msg('e5'));
L23: if ($self->priv < 9) {
L25: return (1, $self->msg('e5'));
L27: return (1, $self->msg('e29')) unless @args;
```

### Output and error evidence

Source: `cmd/set/passphrase.pl` · SHA-256 `ceb86f1a01c199cb872cabec8fcf06cd3dc11c03ca1261c8ccd4336c6e1285a1`

```perl
L19: return (1, $self->msg('e5'));
L25: return (1, $self->msg('e5'));
L27: return (1, $self->msg('e29')) unless @args;
L31: push @out, $self->msg("passphrase", $call);
L34: push @out, $self->msg('e3', 'User record for', $call);
L38: return (1, @out);
```

### Message keys returned

`e29`, `e3`, `e5`, `passphrase`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/passphrase.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PASSPHRASE
```

Compare the installed handler with this page when local overrides or a different revision may be present.