# `UNSET/BADDX`

<div class="command-hero" markdown>

**Propagate a dx spot with this callsign again**

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
UNSET/BADDX [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`baddx->unset()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/baddx.pl` · SHA-256 `fc51f8c65a0d3ccfcc9398c03a0adaba0b0a61b06756893b3a4bbfce5e28fefe`

```perl
L8: my ($self, $line) = @_;
L12: $line = join(' ', map {s|[/-]\d+$||; $_} split(/\s+/, $line));
L13: return $DXProt::baddx->unset(8, $self->msg('e6'), $self, $line);
```

### Validation and access evidence

Source: `cmd/unset/baddx.pl` · SHA-256 `fc51f8c65a0d3ccfcc9398c03a0adaba0b0a61b06756893b3a4bbfce5e28fefe`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::baddx->unset(8, $self->msg('e6'), $self, $line);
```

### Output and error evidence

Source: `cmd/unset/baddx.pl` · SHA-256 `fc51f8c65a0d3ccfcc9398c03a0adaba0b0a61b06756893b3a4bbfce5e28fefe`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L13: return $DXProt::baddx->unset(8, $self->msg('e6'), $self, $line);
```

### Message keys returned

`e5`, `e6`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BADDX <call>..
```

**Propagate a dx spot with this callsign again**

## Details

Setting a word as 'baddx' will prevent spots with that word in the
'spotted' field (as in: DX 14001.1 FR0G)of a DX spot from going any
further. They will not be displayed and they will not be sent onto
other nodes.

The word must be written in full, no wild cards are allowed eg:-

```text
set/baddx FORSALE VIDEO FR0G
```

To allow a word again, use the following command ...

```text
unset/baddx VIDEO
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/baddx.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADDX
```

Compare the installed handler with this page when local overrides or a different revision may be present.