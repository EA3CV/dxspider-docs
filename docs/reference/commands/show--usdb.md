# `SHOW/USDB`

<div class="command-hero" markdown>

**Show information held on the FCC Call database**

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
SHOW/USDB [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`USDB::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/usdb.pl` · SHA-256 `3c042cd66268674eb98ed9b75148e79a58a0d95085ebcd36a868104898f41426`

```perl
L9: my ($self, $line) = @_;
L10: my @list = split /\s+/, $line; # generate a list of callsigns
L18: foreach $l (@list) {
L23: join (' ', map {ucfirst} split(/\s+/, lc $city)), $state;
```

### Validation and access evidence

Source: `cmd/show/usdb.pl` · SHA-256 `3c042cd66268674eb98ed9b75148e79a58a0d95085ebcd36a868104898f41426`

```perl
L15: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
```

### Output and error evidence

Source: `cmd/show/usdb.pl` · SHA-256 `3c042cd66268674eb98ed9b75148e79a58a0d95085ebcd36a868104898f41426`

```perl
L15: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
L22: push @out, sprintf "%-7s -> %s, %s", $l,
L25: push @out, sprintf "%-7s -> Not Found", $l;
L29: return (1, @out);
```

### Message keys returned

`db3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/USDB [call ..]
```

**Show information held on the FCC Call database**

## Details

Show the City and State of a Callsign held on the FCC database if
his is being run on this system, eg:-

```text
sh/usdb k1xx
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/USDB
```

Compare the installed handler with this page when local overrides or a different revision may be present.