# `FORWARD/OPERNAME`

<div class="command-hero" markdown>

**Cause node to send PC41 info frames Mods by Dirk Koopman G1TLH 12Dec98**

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
FORWARD/OPERNAME [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXBearing::lltos()`, `DXChannel::broadcast_all_nodes()`, `DXProt::eph_dup()`, `DXProt::pc41()`, `DXUser::get_current()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/forward/opername.pl` · SHA-256 `6e59bba096fca51f22be91f823121996dbbf93198b1d1774e82df17319100567`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, uc $line;
```

### Validation and access evidence

Source: `cmd/forward/opername.pl` · SHA-256 `6e59bba096fca51f22be91f823121996dbbf93198b1d1774e82df17319100567`

```perl
L13: if ($self->priv < 1) {
L17: return (1, $self->msg('e5'));
L20: return (1, $self->msg('e6'));
```

### Output and error evidence

Source: `cmd/forward/opername.pl` · SHA-256 `6e59bba096fca51f22be91f823121996dbbf93198b1d1774e82df17319100567`

```perl
L17: return (1, $self->msg('e5'));
L20: return (1, $self->msg('e6'));
L62: return (1, @out);
```

### Message keys returned

`e5`, `e6`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/forward/opername.pl){ .md-button }

## Verify on a running node

```text
HELP FORWARD/OPERNAME
```

Compare the installed handler with this page when local overrides or a different revision may be present.