# `SHOW/DXSTATS`

<div class="command-hero" markdown>

**Show the DX Statistics**

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
SHOW/DXSTATS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Reads or changes spot data.

### Important calls

`Date::Parse::str2time()`, `Day->new()`, `Spot::genstats()`, `now->add()`, `now->sub()`, `self->msg()`, `statp->open()`

### Argument parsing evidence

Source: `cmd/show/dxstats.pl` · SHA-256 `eb5ec070e4378f343ebb6dd8131a8a7526ff93eeb0d04ed920a2e09270ee2e37`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
L23: my $f = shift @f;
L25: if ($f =~ /^\d+$/ && $f < 366) { # no of days
L51: my @l = split /\^/;
```

### Validation and access evidence

Source: `cmd/show/dxstats.pl` · SHA-256 `eb5ec070e4378f343ebb6dd8131a8a7526ff93eeb0d04ed920a2e09270ee2e37`

```perl
L25: if ($f =~ /^\d+$/ && $f < 366) { # no of days
```

### Output and error evidence

Source: `cmd/show/dxstats.pl` · SHA-256 `eb5ec070e4378f343ebb6dd8131a8a7526ff93eeb0d04ed920a2e09270ee2e37`

```perl
L33: push @out, $self->msg('e33', $f);
L36: return (1, @out) if @out;
L63: push @out, $self->msg('statdx', $date, $days);
L65: push @out, sprintf "%12s: %7d", $ref->[0]->as_string, $ref->[1];
L68: push @out, sprintf "%12s: %7d", "Total", $tot;
L70: return (1, @out);
```

### Message keys returned

`e33`, `statdx`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/DXSTATS [days] [date]
```

**Show the DX Statistics**

## Details

Show the total DX spots for the last <days> no of days (default is 31),
starting from a <date> (default: today).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/dxstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DXSTATS
```

Compare the installed handler with this page when local overrides or a different revision may be present.