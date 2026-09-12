# `UNSET/LOCKOUT`

<div class="command-hero" markdown>

**Allow a callsign to connect to the cluster**

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
UNSET/LOCKOUT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `ref->lockout()`, `ref->put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/lockout.pl` · SHA-256 `7ce532cd37f2912502e5ce0dca0f51a758f7792bf99667bc353026d952d3fc50`

```perl
L11: my $self = shift;
L12: my $ref = shift;
L21: my ($self, $line) = @_;
L22: my @args = split /\s+/, $line;
L30: Log('DXCommand', $self->call . " attempted to un-lockout @args");
L34: foreach $call (@args) {
L37: if ($call =~ /-\d{1,2}$/) { # This is a call + ssid, just do this exact call
```

### Validation and access evidence

Source: `cmd/unset/lockout.pl` · SHA-256 `7ce532cd37f2912502e5ce0dca0f51a758f7792bf99667bc353026d952d3fc50`

```perl
L15: return $self->msg("lockoutun", $ref->call);
L29: if ($self->priv < 9) {
L31: return (1, $self->msg('e5'));
L36: unless ($self->remotecmd || $self->inscript) {
L37: if ($call =~ /-\d{1,2}$/) { # This is a call + ssid, just do this exact call
```

### Output and error evidence

Source: `cmd/unset/lockout.pl` · SHA-256 `7ce532cd37f2912502e5ce0dca0f51a758f7792bf99667bc353026d952d3fc50`

```perl
L15: return $self->msg("lockoutun", $ref->call);
L31: return (1, $self->msg('e5'));
L39: push @out, mod_existing($self, $ref);
L47: push @out, mod_existing($self, $ref); # lock the base call
L51: push @out, mod_existing($self, $ref) if $ref;
L58: push @out, $self->msg('sorry');
L62: return (1, @out);
```

### Message keys returned

`e5`, `lockoutun`, `sorry`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/LOCKOUT <call>
```

**Allow a callsign to connect to the cluster**

## Details

If <call> is a bare callsign with no SSID, then the command will scan all the
callsigns in the User database that both that AND callsigns-xx and will
(un)lock those records. If a specific callsign-xx is used then only that callsign
will (un)locked.

If you only want to (un)lock a bare callsign then add '-0' e.g G1TLH-0.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/lockout.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/LOCKOUT
```

Compare the installed handler with this page when local overrides or a different revision may be present.