# `SET/LOCKOUT`

<div class="command-hero" markdown>

**Stop a callsign connecting to the cluster**

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
SET/LOCKOUT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser->new()`, `DXUser::get_current()`, `ref->lockout()`, `ref->put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/lockout.pl` · SHA-256 `ca6eb75725ad4d21295560c102eb9b75c1a23a999779fe59e72972e0613edd78`

```perl
L11: my $self = shift;
L12: my $ref = shift;
L20: my $self = shift;
L21: my $call = shift;
L31: my ($self, $line) = @_;
L32: my @args = split /\s+/, $line;
L40: Log('DXCommand', $self->call . " attempted to lockout @args");
L44: foreach $call (@args) {
L47: if ($call =~ /-\d{1,2}$/) { # This is a call + ssid, just do this exact call
L48: $call =~ s/-0$//; # this means just the base callsignx
```

### Validation and access evidence

Source: `cmd/set/lockout.pl` · SHA-256 `ca6eb75725ad4d21295560c102eb9b75c1a23a999779fe59e72972e0613edd78`

```perl
L15: return $self->msg("lockout", $ref->call);
L26: return $self->msg("lockoutc", $call);
L39: if ($self->priv < 9) {
L41: return (1, $self->msg('e5'));
L46: unless ($self->remotecmd || $self->inscript) {
L47: if ($call =~ /-\d{1,2}$/) { # This is a call + ssid, just do this exact call
```

### Output and error evidence

Source: `cmd/set/lockout.pl` · SHA-256 `ca6eb75725ad4d21295560c102eb9b75c1a23a999779fe59e72972e0613edd78`

```perl
L15: return $self->msg("lockout", $ref->call);
L26: return $self->msg("lockoutc", $call);
L41: return (1, $self->msg('e5'));
L50: push @out, mod_existing($self, $ref);
L52: push @out, add_new($self, $call);
L60: push @out, mod_existing($self, $ref); # lock the base call
L64: push @out, mod_existing($self, $ref) if $ref;
L67: push @out, add_new($self, $call);
L74: push @out, $self->msg('sorry');
L77: return (1, @out);
```

### Message keys returned

`e5`, `lockout`, `lockoutc`, `sorry`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/LOCKOUT <call>
```

**Stop a callsign connecting to the cluster**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/lockout.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LOCKOUT
```

Compare the installed handler with this page when local overrides or a different revision may be present.