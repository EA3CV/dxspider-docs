# `SHOW/VHFSTATS`

<div class="command-hero" markdown>

**Show the VHF DX Statistics**

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
SHOW/VHFSTATS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Reads or changes spot data.

### Recognized tokens, keys or enumerated values in this handler

`cm`, `Date`, `m`, `mm`, `Total`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Date::Parse::str2time()`, `Day->new()`, `Spot::genstats()`, `now->add()`, `now->sub()`, `self->msg()`, `self->spawn_cmd()`, `statp->open()`

### Argument parsing evidence

Source: `cmd/show/vhfstats.pl` · SHA-256 `bedcb68ddd5a2f2a563ce09bf810f8018e11ccad57497b3c42bcccc29593665d`

```perl
L31: my ($self, $line) = @_;
L32: my @f = split /\s+/, $line;
L39: my $f = shift @f;
L41: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L64: return (1, $self->spawn_cmd("show/vhfstats $line", sub { (generate($self, $days, $now, $today )); }));
L86: my @l = split /\^/;
L110: $today =~ s/-\d+$//;
```

### Validation and access evidence

Source: `cmd/show/vhfstats.pl` · SHA-256 `bedcb68ddd5a2f2a563ce09bf810f8018e11ccad57497b3c42bcccc29593665d`

```perl
L41: if ($f =~ /^\d+$/ && $f < 366) { # no of days
```

### Output and error evidence

Source: `cmd/show/vhfstats.pl` · SHA-256 `bedcb68ddd5a2f2a563ce09bf810f8018e11ccad57497b3c42bcccc29593665d`

```perl
L48: push @out, $self->msg('e33', $f);
L51: return (1, @out) if @out;
L61: return (1, generate($self, $days, $now, $today));
L64: return (1, $self->spawn_cmd("show/vhfstats $line", sub { (generate($self, $days, $now, $today )); }));
L98: push @out, $self->msg('statvhf', $today, $days);
L99: push @out, sprintf "%6s|%6s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|", qw(Date Total 6m 4m 2m 70cm 23cm 13cm 9cm 6cm 3cm 12mm);
L111: push @out, join '|', sprintf("%6s|%6d", $today, $linetot), map {$_ ? sprintf("%5d", $_) : ' '} @$ref[14..16,18..24], "";
L113: push @out, join '|', sprintf("%6s|%6d", 'Total', $tot[0]), map {$_ ? sprintf("%5d", $_) : ' '} @tot[14..16,18..24], "";
```

### Message keys returned

`e33`, `statvhf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/VHFSTATS [days] [date]
```

**Show the VHF DX Statistics**

## Details

Show the VHF DX spots breakdown by band for the last
<days> no of days (default is 31), starting from a date (default: today).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/vhfstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/VHFSTATS
```

Compare the installed handler with this page when local overrides or a different revision may be present.