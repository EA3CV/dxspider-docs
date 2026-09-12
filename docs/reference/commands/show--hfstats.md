# `SHOW/HFSTATS`

<div class="command-hero" markdown>

**Show the HF DX Statistics**

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
SHOW/HFSTATS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Reads or changes spot data.

### Recognized tokens, keys or enumerated values in this handler

`Date`, `m`, `Total`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Date::Parse::str2time()`, `Day->new()`, `Spot::genstats()`, `now->add()`, `now->sub()`, `self->msg()`, `self->spawn_cmd()`, `statp->open()`

### Argument parsing evidence

Source: `cmd/show/hfstats.pl` · SHA-256 `45bc87fbc48a7071b2c22ee6a1f1a834885c29fc8c6e5cfbe60be136f24cc000`

```perl
L31: my ($self, $line) = @_;
L32: my @f = split /\s+/, $line;
L39: my $f = shift @f;
L41: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L64: return (1, $self->spawn_cmd("show/hfstats $line", sub { (generate($self, $days, $now, $today )); }));
L86: my @l = split /\^/;
L108: $today =~ s/-\d+$//;
```

### Validation and access evidence

Source: `cmd/show/hfstats.pl` · SHA-256 `45bc87fbc48a7071b2c22ee6a1f1a834885c29fc8c6e5cfbe60be136f24cc000`

```perl
L41: if ($f =~ /^\d+$/ && $f < 366) { # no of days
```

### Output and error evidence

Source: `cmd/show/hfstats.pl` · SHA-256 `45bc87fbc48a7071b2c22ee6a1f1a834885c29fc8c6e5cfbe60be136f24cc000`

```perl
L48: push @out, $self->msg('e33', $f);
L51: return (1, @out) if @out;
L61: return (1, generate($self, $days, $now, $today));
L64: return (1, $self->spawn_cmd("show/hfstats $line", sub { (generate($self, $days, $now, $today )); }));
L98: push @out, $self->msg('stathf', $today, $days);
L99: push @out, sprintf "%6s|%6s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|", qw(Date Total 160m 80m 60m 40m 30m 20m 17m 15m 12m 10m);
L109: push @out, join '|', sprintf("%6s|%6d", $today, $linetot), map {$_ ? sprintf("%5d", $_) : ' '} @$ref[4..13], "";
L111: push @out, join '|', sprintf("%6s|%6d", 'Total', $tot[0]), map {$_ ? sprintf("%5d", $_) : ' '} @tot[4..13], "";
```

### Message keys returned

`e33`, `stathf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/HFSTATS [days] [date]
```

**Show the HF DX Statistics**

## Details

Show the HF DX spots breakdown by band for the last <days> no of days
(default is 31), starting from a <date> (default: today).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/hfstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/HFSTATS
```

Compare the installed handler with this page when local overrides or a different revision may be present.