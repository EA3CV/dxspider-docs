# `SHOW/SUN`

<div class="command-hero" markdown>

**Show sun rise and set times**

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
SHOW/SUN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`timegm`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXUser::get_current()`, `Prefix::extract()`, `Prefix::utcoff()`, `Sun::rise_set()`, `a->utcoff()`

### Argument parsing evidence

Source: `cmd/show/sun.pl` · SHA-256 `584a5b7473ce9ee5e0a83c4f08f6f859b9d67dd9424dd7db0951797b1870ebd3`

```perl
L17: my ($self, $line) = @_;
L18: my @l = split /\s+/, $line;
L24: my @list;
L36: while ($f = shift @f) {
L38: ($n_offset) = $f =~ /^([-+]?\d+)$/;
L41: push @list, $f;
L56: my $call = shift;
L62: shift @ans;
L63: my $a = shift @ans;
L78: return undef unless $time =~ /^(\d{2}):(\d{2})Z$/;
L103: if (@list) {
L104: foreach $l (@list) {
L117: my $pre = shift @ans;
L189: $l->[3] =~ s{(-\d+|/\w+)$}{};
```

### Validation and access evidence

Source: `cmd/show/sun.pl` · SHA-256 `584a5b7473ce9ee5e0a83c4f08f6f859b9d67dd9424dd7db0951797b1870ebd3`

```perl
L37: if (!defined $n_offset) {
L39: next if defined $n_offset;
L44: $n_offset = 0 unless defined $n_offset;
L57: return 0 unless defined $call && length $call;
L67: return 0 unless defined $off;
L77: return undef unless defined $time;
L78: return undef unless $time =~ /^(\d{2}):(\d{2})Z$/;
L87: return $time unless defined $epoch;
L124: if (defined $off) {
L173: if (defined $rise_epoch && defined $set_epoch && $set_epoch <= $rise_epoch) {
L183: if (defined $next_set_epoch) {
```

### Output and error evidence

Source: `cmd/show/sun.pl` · SHA-256 `584a5b7473ce9ee5e0a83c4f08f6f859b9d67dd9424dd7db0951797b1870ebd3`

```perl
L156: push @out, $want_local
L160: push @out, $want_local
L195: push @out, sprintf(
L200: push @out, sprintf(
L207: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/SUN [ndays] [<prefix>|<callsign>]
```

**Show sun rise and set times**

## Details

Show the sun rise and set times for a (list of) prefixes or callsigns,
together with the azimuth and elevation of the sun currently at those
locations.

If you don't specify any prefixes or callsigns, it will show the times for
your QTH (assuming you have set it with either SET/LOCATION or SET/QRA),
together with the current azimuth and elevation.

If all else fails it will show the sunrise and set times for the node
that you are connected to.

For example:-

```text
SH/SUN
SH/SUN G1TLH K9CW ZS
```

You can also use this command to see into the past or the future, so
if you want to see yesterday's times then do:-

```text
SH/SUN -1
```

or in three days time:-

```text
SH/SUN +3 W9
```

Upto 366 days can be checked both in the past and in the future.

Please note that the rise and set times are given as the UTC times of rise and
set on the requested UTC day UNLESS you add the keyword 'local' (without quotes)
to the list of callsigns e.g:

```text
SH/SUN G1TLH W5UN local
SH/SUN  LOCAL G1TLH W5UN
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/sun.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SUN
```

Compare the installed handler with this page when local overrides or a different revision may be present.