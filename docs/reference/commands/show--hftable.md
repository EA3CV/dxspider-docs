# `SHOW/HFTABLE`

<div class="command-hero" markdown>

**Show the HF DX Spotter Table**

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
SHOW/HFTABLE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Reads or changes spot data.

### Recognized tokens, keys or enumerated values in this handler

`ALL`, `Callsign`, `m`, `Tot`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Date::Parse::str2time()`, `Day->new()`, `Prefix::to_ciz()`, `Spot::genstats()`, `now->sub()`, `self->msg()`, `self->spawn_cmd()`, `statp->open()`

### Argument parsing evidence

Source: `cmd/show/hftable.pl` · SHA-256 `8d930426610a6ec608a3028b125c32082c8b0c8762c2c9347bc7d90f7365ac49`

```perl
L48: my ($self, $line) = @_;
L52: my @f = split /\s+/, $line;
L57: my $f = shift @f;
L59: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L109: @out = $self->spawn_cmd("show/hftable $line", sub { return (generate($self)); });
L117: my $self = shift;
L132: my @l = split /\^/;
L157: my @list = (sprintf "%9s", $_);
L167: push @list, $r;
L169: push @out, join('|', @list);
```

### Validation and access evidence

Source: `cmd/show/hftable.pl` · SHA-256 `8d930426610a6ec608a3028b125c32082c8b0c8762c2c9347bc7d90f7365ac49`

```perl
L59: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L70: if (is_callsign($f)) {
```

### Output and error evidence

Source: `cmd/show/hftable.pl` · SHA-256 `8d930426610a6ec608a3028b125c32082c8b0c8762c2c9347bc7d90f7365ac49`

```perl
L85: push @out, $self->msg('e27', $f);
L91: return (1, @out) if @out;
L109: @out = $self->spawn_cmd("show/hftable $line", sub { return (generate($self)); });
L112: return (1, @out);
L151: push @out, $self->msg('stathft', $l, $date, $days);
L152: push @out, sprintf "%9s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|%5s|", qw(Callsign Tot 160m 80m 60m 40m 30m 20m 17m 15m 12m 10m);
L169: push @out, join('|', @list);
L175: push @out, join('|', $nocalls, @tot,"");
```

### Message keys returned

`e27`, `stathft`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/HFTABLE [days] [date] [prefix ...]
```

**Show the HF DX Spotter Table**

## Details

Show the HF DX Spotter table for the list of prefixes for the last
<days> no of days (default is 31), starting from a <date> (default: today).

If there are no prefixes then it will show the table for your country.

Remember that some countries have more than one "DXCC country" in them
(eg G :-), to show them (assuming you are not in G already which is
specially treated in the code) you must list all the relevant prefixes

```text
sh/hftable g gm gd gi gj gw gu
```

Note that the prefixes are converted into country codes so you don't have
to list all possible prefixes for each country.

If you want more or less days than the default simply include the
number you require:-

```text
sh/hftable 20 pa
```

If you want to start at a different day, simply add the date in some
recognizable form:-

```text
sh/hftable 2 25nov02
sh/hftable 2 25-nov-02
sh/hftable 2 021125
sh/hftable 2 25/11/02
```

This will show the stats for your DXCC for that CQWW contest weekend.

You can specify either prefixes or full callsigns (so you can see how you
did against all your mates). You can also say 'all' which will then print
the worldwide statistics.

```text
sh/hftable all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/hftable.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/HFTABLE
```

Compare the installed handler with this page when local overrides or a different revision may be present.