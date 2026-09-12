# `SHOW/MOON`

<div class="command-hero" markdown>

**Show Moon rise and set times**

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
SHOW/MOON [token ...]
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

Source: `cmd/show/moon.pl` · SHA-256 `6ec4e1df6e54c98e4ec883c878cee9b5f7bd407a1e595b056251b050b26d490a`

```perl
L17: my ($self, $line) = @_;
L18: my @l = split /\s+/, $line;
L25: my @list;
L38: while ($f = shift @f) {
L40: ($n_offset) = $f =~ /^([-+]?\d+)$/;
L43: push @list, $f;
L58: my $call = shift;
L64: shift @ans;
L65: my $a = shift @ans;
L80: return undef unless $time =~ /^(\d{2}):(\d{2})Z$/;
L105: if (@list) {
L106: foreach $l (@list) {
L119: my $pre = shift @ans;
L191: $l->[3] =~ s{(-\d+|/\w+)$}{};
```

### Validation and access evidence

Source: `cmd/show/moon.pl` · SHA-256 `6ec4e1df6e54c98e4ec883c878cee9b5f7bd407a1e595b056251b050b26d490a`

```perl
L39: if (!defined $n_offset) {
L41: next if defined $n_offset;
L46: $n_offset = 0 unless defined $n_offset;
L59: return 0 unless defined $call && length $call;
L69: return 0 unless defined $off;
L79: return undef unless defined $time;
L80: return undef unless $time =~ /^(\d{2}):(\d{2})Z$/;
L89: return $time unless defined $epoch;
L126: if (defined $off) {
L175: if (defined $rise_epoch && defined $set_epoch && $set_epoch <= $rise_epoch) {
L185: if (defined $next_set_epoch) {
L210: if defined $ifrac;
```

### Output and error evidence

Source: `cmd/show/moon.pl` · SHA-256 `6ec4e1df6e54c98e4ec883c878cee9b5f7bd407a1e595b056251b050b26d490a`

```perl
L158: push @out, $want_local
L162: push @out, $want_local
L197: push @out, sprintf(
L202: push @out, sprintf(
L209: push @out, sprintf("Illuminated fraction of the Moon's disk is %4.2f", $ifrac)
L212: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/MOON [ndays] [<prefix>|<callsign> | local]
```

**Show Moon rise and set times**

## Details

Show the Moon rise and set times for a (list of) prefixes or callsigns,
together with the azimuth and elevation of the sun currently at those
locations.

If you don't specify any prefixes or callsigns, it will show the times for
your QTH (assuming you have set it with either SET/LOCATION or SET/QRA),
together with the current azimuth and elevation.

In addition, it will show the illuminated fraction of the moons disk.

If all else fails it will show the Moonrise and set times for the node
that you are connected to.

For example:-

```text
SH/MOON
SH/MOON G1TLH W5UN
```

You can also use this command to see into the past or the future, so
if you want to see yesterday's times then do:-

```text
SH/MOON -1
```

or in three days time:-

```text
SH/MOON +3 W9
```

Upto 366 days can be checked both in the past and in the future.

Please note that the rise and set times are given as the UTC times of rise and
set on the requested UTC day UNLESS you add the keyword 'local' (without quotes)
to the list of callsigns e.g:

```text
SH/MOON G1TLH W5UN local
SH/MOON LOCAL G1TLH W5UN
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/moon.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MOON
```

Compare the installed handler with this page when local overrides or a different revision may be present.