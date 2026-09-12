# `DELETE/USDB`

<div class="command-hero" markdown>

**Delete this user from the US State Database**

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
DELETE/USDB [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`USDB::del()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/delete/usdb.pl` · SHA-256 `bfa50d0e376390b1fc6a7d3a68878ff4b28f6d5d5fd8587a42f2fa0243a6495b`

```perl
L12: my ($self, $line) = @_;
L13: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/delete/usdb.pl` · SHA-256 `bfa50d0e376390b1fc6a7d3a68878ff4b28f6d5d5fd8587a42f2fa0243a6495b`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/delete/usdb.pl` · SHA-256 `bfa50d0e376390b1fc6a7d3a68878ff4b28f6d5d5fd8587a42f2fa0243a6495b`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9;
L22: push @out, $self->msg('susdb4', $call);
L23: Log('DXCommand', $self->msg('susdb4', $call));
L25: return (1, @out);
```

### Message keys returned

`e5`, `susdb4`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DELETE/USDB <callsign> ...
```

**Delete this user from the US State Database**

## Details

This command will completely remove a one or more callsigns
from the US States database.

There is NO SECOND CHANCE.

It goes without saying that you should use this command CAREFULLY!

Note that these callsign may be re-instated by any weekly updates from
the FCC.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/delete/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP DELETE/USDB
```

Compare the installed handler with this page when local overrides or a different revision may be present.