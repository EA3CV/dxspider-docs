# `SET/USDB`

<div class="command-hero" markdown>

**add/update a US DB callsign**

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
SET/USDB [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Named fields consumed by the parser

`call`, `state`, `city`

### Important calls

`USDB::add()`, `USDB::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/usdb.pl` · SHA-256 `0d2ec5e3a950a4866181bf42e78f64d84c0b6b856f66fd8af503dcc03e0c6cdb`

```perl
L11: my ($self, $line) = @_;
L14: my ($call, $state, $city) = split /\s+/, uc $line, 3;
```

### Validation and access evidence

Source: `cmd/set/usdb.pl` · SHA-256 `0d2ec5e3a950a4866181bf42e78f64d84c0b6b856f66fd8af503dcc03e0c6cdb`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L15: return (1, $self->msg('susdb1')) if length $state != 2 || !is_callsign($call);
```

### Output and error evidence

Source: `cmd/set/usdb.pl` · SHA-256 `0d2ec5e3a950a4866181bf42e78f64d84c0b6b856f66fd8af503dcc03e0c6cdb`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L15: return (1, $self->msg('susdb1')) if length $state != 2 || !is_callsign($call);
L19: push @out, $self->msg('susdb2', $call, $ocity, $ostate ) if $ocity;
L21: push @out, $self->msg('susdb3', $call, $city, $state );
L22: Log('DXCommand', $self->msg('susdb3', $call, $city, $state));
L23: return (1, @out);
```

### Message keys returned

`e5`, `susdb1`, `susdb2`, `susdb3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/USDB <call> <state> <city>
```

**add/update a US DB callsign**

## Details

This command allows you to add or alter a callsign in the US state
database. Use with extreme caution. Anything you do here will be
overwritten by any weekly updates that affect this callsign

```text
set/usdb g1tlh nh downtown rindge
```

see also DELETE/USDB

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP SET/USDB
```

Compare the installed handler with this page when local overrides or a different revision may be present.