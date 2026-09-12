# `SET/WANTPC9X`

<div class="command-hero" markdown>

**set the wantPC9x flag**

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
SET/WANTPC9X [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantpc9x()`

### Argument parsing evidence

Source: `cmd/set/wantpc9x.pl` · SHA-256 `af08b2576d4aa090be94f3d2e0c2088964e9116401a8858dece827ccf99bf208`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/wantpc9x.pl` · SHA-256 `af08b2576d4aa090be94f3d2e0c2088964e9116401a8858dece827ccf99bf208`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L17: return (1, $self->msg('e12')) unless is_callsign($call);
```

### Output and error evidence

Source: `cmd/set/wantpc9x.pl` · SHA-256 `af08b2576d4aa090be94f3d2e0c2088964e9116401a8858dece827ccf99bf208`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L17: return (1, $self->msg('e12')) unless is_callsign($call);
L23: push @out, $self->msg('wpc9xs', $call);
L25: push @out, $self->msg('e3', "set/wantpc9x", $call);
L28: return (1, @out);
```

### Message keys returned

`e12`, `e3`, `e5`, `wpc9xs`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/wantpc9x.pl){ .md-button }

## Verify on a running node

```text
HELP SET/WANTPC9X
```

Compare the installed handler with this page when local overrides or a different revision may be present.