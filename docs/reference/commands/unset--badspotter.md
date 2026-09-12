# `UNSET/BADSPOTTER`

<div class="command-hero" markdown>

**Allow spots from this callsign again**

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
UNSET/BADSPOTTER [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`badspotter->unset()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/badspotter.pl` · SHA-256 `94ec09f5e009741f64a19d1638615efa63d8bcd2dcfc07258c2634bd2d2ee8f2`

```perl
L8: my ($self, $line) = @_;
L12: $line = join(' ', map {s|[/-]\d+$||; $_} split(/\s+/, $line));
L13: $line = join(' ', map {s|[/-]\d+$||; $_} split(/\s+/, $line));
L14: return $DXProt::badspotter->unset(8, $self->msg('e6'), $self, $line);
```

### Validation and access evidence

Source: `cmd/unset/badspotter.pl` · SHA-256 `94ec09f5e009741f64a19d1638615efa63d8bcd2dcfc07258c2634bd2d2ee8f2`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L14: return $DXProt::badspotter->unset(8, $self->msg('e6'), $self, $line);
```

### Output and error evidence

Source: `cmd/unset/badspotter.pl` · SHA-256 `94ec09f5e009741f64a19d1638615efa63d8bcd2dcfc07258c2634bd2d2ee8f2`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L14: return $DXProt::badspotter->unset(8, $self->msg('e6'), $self, $line);
```

### Message keys returned

`e5`, `e6`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BADSPOTTER <call>..
```

**Allow spots from this callsign again**

## Details

Setting a callsign as a 'badspotter' will prevent spots from this callsign
going any further. They will not be displayed and they will not be
sent onto other nodes.

The call must be written in full, no wild cards are allowed eg:-

```text
set/badspotter VE2STN
```

will stop anything from VE2STN. This command will automatically
stop spots from this user, regardless of whether or which SSID
he uses. DO NOT USE SSIDs in the callsign, just use the callsign
as above or below.

```text
unset/badspotter VE2STN
```

will allow spots from him again.

Use with extreme care. This command may well be superceded by FILTERing.

This command will also stop TALK and ANNOUNCE/FULL from any user marked
as a BADSPOTTER.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/badspotter.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADSPOTTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.