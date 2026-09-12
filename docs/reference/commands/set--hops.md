# `SET/HOPS`

<div class="command-hero" markdown>

**Set hop count**

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
SET/HOPS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`Filter->new()`, `Filter::read_in()`, `ref->isa()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/hops.pl` · SHA-256 `737a8ee2df22229029dcdbb37ef75f6de131c7aaaf32dd9381e50119adde03c1`

```perl
L8: my ($self, $line) = @_;
L11: my @f = split /\s+/, $line;
L16: $call = uc shift @f;
L18: $call = shift @f;
L21: my $sort = lc shift @f if $f[0] =~ /^ann|spots|wwv|wcy|route$/i;
L22: my $hops = shift @f if $f[0] =~ /^\d+$/;
```

### Validation and access evidence

Source: `cmd/set/hops.pl` · SHA-256 `737a8ee2df22229029dcdbb37ef75f6de131c7aaaf32dd9381e50119adde03c1`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 8;
L15: if (is_callsign(uc $f[0])) {
L21: my $sort = lc shift @f if $f[0] =~ /^ann|spots|wwv|wcy|route$/i;
L22: my $hops = shift @f if $f[0] =~ /^\d+$/;
L24: return (0, $self->msg('sethop1')) unless $call && $sort && defined $hops;
L28: return (0, $self->msg('filter5', '', $sort, $call)) unless $ref;
L35: return (0, $self->msg('sethop2', $hops, '', $sort, $call));
```

### Output and error evidence

Source: `cmd/set/hops.pl` · SHA-256 `737a8ee2df22229029dcdbb37ef75f6de131c7aaaf32dd9381e50119adde03c1`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 8;
L24: return (0, $self->msg('sethop1')) unless $call && $sort && defined $hops;
L28: return (0, $self->msg('filter5', '', $sort, $call)) unless $ref;
L35: return (0, $self->msg('sethop2', $hops, '', $sort, $call));
```

### Message keys returned

`e5`, `filter5`, `sethop1`, `sethop2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/HOPS <call> ann|spots|route|wwv|wcy <n>
```

**Set hop count**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/hops.pl){ .md-button }

## Verify on a running node

```text
HELP SET/HOPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.