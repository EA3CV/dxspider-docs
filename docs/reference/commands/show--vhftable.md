# `SHOW/VHFTABLE`

<div class="command-hero" markdown>

**Show the VHF DX Spotter Table**

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
SHOW/VHFTABLE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Reads or changes spot data.

### Recognized tokens, keys or enumerated values in this handler

`ALL`, `Callsign`, `cm`, `m`, `Tot`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Date::Parse::str2time()`, `Day->new()`, `Prefix::to_ciz()`, `Spot::genstats()`, `now->sub()`, `self->msg()`, `self->spawn_cmd()`, `statp->open()`

### Argument parsing evidence

Source: `cmd/show/vhftable.pl` · SHA-256 `442251461987d3a96c68457217eab57990ccc06724b154548c8a6b778e8d6956`

```perl
L21: my ($self, $line) = @_;
L22: my @f = split /\s+/, $line;
L27: my $f = shift @f;
L29: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L78: @out = $self->spawn_cmd("show/vhftable $line", sub {return (generate($self))});
L86: my $self = shift;
L100: my @l = split /\^/;
L126: my @list = (sprintf "%10s", $_);
L136: push @list, $r;
L138: push @out, join('|', @list, "");
```

### Validation and access evidence

Source: `cmd/show/vhftable.pl` · SHA-256 `442251461987d3a96c68457217eab57990ccc06724b154548c8a6b778e8d6956`

```perl
L29: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L40: if (is_callsign($f)) {
```

### Output and error evidence

Source: `cmd/show/vhftable.pl` · SHA-256 `442251461987d3a96c68457217eab57990ccc06724b154548c8a6b778e8d6956`

```perl
L55: push @out, $self->msg('e27', $f);
L61: return (1, @out) if @out;
L78: @out = $self->spawn_cmd("show/vhftable $line", sub {return (generate($self))});
L81: return (1, @out);
L119: push @out, $self->msg('statvhft', $l, $date, $days);
L121: push @out, sprintf "%10s|%4s|%4s|%4s|%4s|%4s|%4s|%4s|%4s|%4s|%4s|", qw(Callsign Tot 6m 4m 2m 70cm 23cm 13cm 9cm 6cm 3cm);
L138: push @out, join('|', @list, "");
L144: push @out, join('|', $nocalls, @tot, "");
```

### Message keys returned

`e27`, `statvhft`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/VHFTABLE [days] [date] [prefix ...]
```

**Show the VHF DX Spotter Table**

## Details

Show the VHF DX Spotter table for the list of prefixes for the last
<days> no of days (default is 31), starting from a date (default: today).

If there are no prefixes then it will show the table for your country.

Remember that some countries have more than one "DXCC country" in them
(eg G :-), to show them (assuming you are not in G already which is
specially treated in the code) you must list all the relevant prefixes

```text
sh/vhftable g gm gd gi gj gw gu
```

Note that the prefixes are converted into country codes so you don't have
to list all possible prefixes for each country.

If you want more or less days than the default simply include the
number you require:-

```text
sh/vhftable 20 pa
```

If you want to start at a different day, simply add the date in some
recognizable form:-

```text
sh/vhftable 2 25nov02
sh/vhftable 2 25-nov-02
sh/vhftable 2 021125
sh/vhftable 2 25/11/02
```

This will show the stats for your DXCC for that CQWW contest weekend.

You can specify either prefixes or full callsigns (so you can see how you
did against all your mates). You can also say 'all' which will then print
the worldwide statistics.

```text
sh/vhftable all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/vhftable.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/VHFTABLE
```

Compare the installed handler with this page when local overrides or a different revision may be present.