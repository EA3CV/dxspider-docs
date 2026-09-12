# `SET/USSTATE`

<div class="command-hero" markdown>

**Allow US State info on the end of DX announcements**

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
SET/USSTATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantdxcq()`, `user->wantdxitu()`, `user->wantusstate()`

### Argument parsing evidence

Source: `cmd/set/usstate.pl` · SHA-256 `e8a01fe0440ecc7d4eb683807f8d3b182fcf9321a5cebd7e3c3e560f0d78a04b`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L16: @args = $self->call if (!@args || $self->priv < 9);
L18: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/usstate.pl` · SHA-256 `e8a01fe0440ecc7d4eb683807f8d3b182fcf9321a5cebd7e3c3e560f0d78a04b`

```perl
L14: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
L16: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/usstate.pl` · SHA-256 `e8a01fe0440ecc7d4eb683807f8d3b182fcf9321a5cebd7e3c3e560f0d78a04b`

```perl
L14: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
L32: push @out, $self->msg('usstates', $call);
L34: push @out, $self->msg('e3', "Set US State", $call);
L37: return (1, @out);
```

### Message keys returned

`db3`, `dxcqu`, `dxituu`, `e3`, `usstates`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/USSTATE
```

**Allow US State info on the end of DX announcements**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/usstate.pl){ .md-button }

## Verify on a running node

```text
HELP SET/USSTATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.