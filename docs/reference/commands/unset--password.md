# `UNSET/PASSWORD`

<div class="command-hero" markdown>

**Delete (remove) a user's password**

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
UNSET/PASSWORD [token ...]
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

Source: `cmd/unset/password.pl` · SHA-256 `5961648bb5f5c93234124c42f754541c50dbe5be3c6a71dfb5eb69a33316296e`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L16: Log('DXCommand', $self->call . " attempted to unset password for @args remotely");
L21: Log('DXCommand', $self->call . " attempted to unset password for @args");
L25: for (@args) {
```

### Validation and access evidence

Source: `cmd/unset/password.pl` · SHA-256 `5961648bb5f5c93234124c42f754541c50dbe5be3c6a71dfb5eb69a33316296e`

```perl
L15: if ($self->remotecmd || $self->inscript) {
L17: return (1, $self->msg('e5'));
L20: if ($self->priv < 9) {
L22: return (1, $self->msg('e5'));
```

### Output and error evidence

Source: `cmd/unset/password.pl` · SHA-256 `5961648bb5f5c93234124c42f754541c50dbe5be3c6a71dfb5eb69a33316296e`

```perl
L17: return (1, $self->msg('e5'));
L22: return (1, $self->msg('e5'));
L30: push @out, $self->msg("passwordu", $call);
L33: push @out, $self->msg('e3', 'User record for', $call);
L37: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `passwordu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/PASSWORD <call> ...
```

**Delete (remove) a user's password**

## Details

This command allows the sysop to completely delete and remove a
password for a user.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/password.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PASSWORD
```

Compare the installed handler with this page when local overrides or a different revision may be present.