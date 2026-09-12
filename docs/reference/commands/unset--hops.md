# `UNSET/HOPS`

<div class="command-hero" markdown>

**Unset hop count**

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
UNSET/HOPS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`Filter->new()`, `Filter::read_in()`, `ref->isa()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/hops.pl` · SHA-256 `c0ff60e3809177a4a8410295a14023f7f02b44e80f4c753e92e9192284d7fe6d`

```perl
L8: my ($self, $line) = @_;
L11: my @f = split /\s+/, $line;
L16: $call = uc shift @f;
L18: $call = shift @f;
L21: my $sort = lc shift @f if $f[0] =~ /^ann|spots|wwv|wcy|route$/i;
```

### Validation and access evidence

Source: `cmd/unset/hops.pl` · SHA-256 `c0ff60e3809177a4a8410295a14023f7f02b44e80f4c753e92e9192284d7fe6d`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 8;
L15: if (is_callsign(uc $f[0])) {
L21: my $sort = lc shift @f if $f[0] =~ /^ann|spots|wwv|wcy|route$/i;
L23: return (0, $self->msg('unsethop1')) unless $call && $sort;
L27: return (0, $self->msg('filter5', '', $sort, $call)) unless $ref;
L33: return (0, $self->msg('unsethop2', $sort, $call));
```

### Output and error evidence

Source: `cmd/unset/hops.pl` · SHA-256 `c0ff60e3809177a4a8410295a14023f7f02b44e80f4c753e92e9192284d7fe6d`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 8;
L23: return (0, $self->msg('unsethop1')) unless $call && $sort;
L27: return (0, $self->msg('filter5', '', $sort, $call)) unless $ref;
L33: return (0, $self->msg('unsethop2', $sort, $call));
```

### Message keys returned

`e5`, `filter5`, `unsethop1`, `unsethop2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/HOPS <call> ann|spots|route|wwv|wcy
```

**Unset hop count**

## Details

Set the hop count for a particular type of broadcast for a node.

This command allows you to set up special hop counts for a node
for currently: announce, spots, wwv and wcy broadcasts.

eg:
```text
set/hops gb7djk ann 10
set/hops gb7mbc spots 20
```

Set SHOW/HOPS for information on what is already set. This command
creates a filter and works in conjunction with the filter system.

You can unset the hops with command UNSET/HOPS. For example:-

```text
unset/hops gb7djk ann
unset/hops gb7mbc spots
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/hops.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/HOPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.