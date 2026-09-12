# `UNSET/DXCQ`

<div class="command-hero" markdown>

**Stop CQ Zones on the end of DX announcements**

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
UNSET/DXCQ [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantdxcq()`

### Argument parsing evidence

Source: `cmd/unset/dxcq.pl` · SHA-256 `51e4742475c60b7f69fe50058bb63e0fbb91665735ae01ed7d22a2ac25fd65fb`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/dxcq.pl` · SHA-256 `51e4742475c60b7f69fe50058bb63e0fbb91665735ae01ed7d22a2ac25fd65fb`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/unset/dxcq.pl` · SHA-256 `51e4742475c60b7f69fe50058bb63e0fbb91665735ae01ed7d22a2ac25fd65fb`

```perl
L22: push @out, $self->msg('dxcqu', $call);
L24: push @out, $self->msg('e3', "Unset DX CQ", $call);
L27: return (1, @out);
```

### Message keys returned

`dxcqu`, `e3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/DXCQ
```

**Stop CQ Zones on the end of DX announcements**

## Details

Display both the Spotter's and the Spotted's CQ Zone on the end
of a DX announcement (there is just enough room). Some user programs
cannot cope with this. The Spotter's CQ is on the RHS of the
time, the Spotted's CQ is on the LHS.

Conflicts with: SET/DXGRID, SET/DXITU, SHOW/USSTATE

Do a STAT/USER to see which flags you have set if you are confused.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/dxcq.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/DXCQ
```

Compare the installed handler with this page when local overrides or a different revision may be present.