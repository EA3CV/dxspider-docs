# `SHOW/LOG`

<div class="command-hero" markdown>

**Show excerpts from the system log**

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
SHOW/LOG
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/log.pl` · SHA-256 `73708cfa06749821cf3aa7835d3c7a2fb4e583ef033f23aad9ceb7f69deb7517`

```perl
L11: my $self = shift;
L13: my $cmdline = shift;
L14: my @f = split /\s+/, $cmdline;
L20: while ($f = shift @f) { # next field
L23: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L27: ($to) = $f =~ /^(\d+)$/ if !$to; # is it a to count?
L30: unless ($f =~ /^\d+$/) {
```

### Validation and access evidence

Source: `cmd/show/log.pl` · SHA-256 `73708cfa06749821cf3aa7835d3c7a2fb4e583ef033f23aad9ceb7f69deb7517`

```perl
L30: unless ($f =~ /^\d+$/) {
L39: if ($self->priv < 6) {
L40: return (1, $self->msg('e5')) if defined $who && $who ne $self->call;
```

### Output and error evidence

Source: `cmd/show/log.pl` · SHA-256 `73708cfa06749821cf3aa7835d3c7a2fb4e583ef033f23aad9ceb7f69deb7517`

```perl
L40: return (1, $self->msg('e5')) if defined $who && $who ne $self->call;
L44: return (1, DXLog::print($from, $to, $main::systime, undef, $who)) if ($self->{_nospawn} || $main::is_win == 1);
L45: return (1, $self->spawn_cmd("show/log $cmdline", \&DXLog::print, args => [$from, $to, $main::systime, undef, $who]));
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/LOG [<callsign>]
```

**Show excerpts from the system log**

## Details

This command outputs a short section of the system log.  On its own
it will output a general logfile.  With the optional callsign it will
show output from the log associated with that callsign.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/log.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/LOG
```

Compare the installed handler with this page when local overrides or a different revision may be present.