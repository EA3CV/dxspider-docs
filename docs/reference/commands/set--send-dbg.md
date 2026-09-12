# `SET/SEND_DBG`

<div class="command-hero" markdown>

**send debug information to this connection**

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
SET/SEND_DBG [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`, `self->senddbg()`

### Argument parsing evidence

Source: `cmd/set/send_dbg.pl` · SHA-256 `164e533feab17453a08e7f3480cbf898294ffe48e62b0cb4e33e827c1963a3cb`

```perl
L9: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/set/send_dbg.pl` · SHA-256 `164e533feab17453a08e7f3480cbf898294ffe48e62b0cb4e33e827c1963a3cb`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 8;
L12: return (1, $self->msg('done'));
```

### Output and error evidence

Source: `cmd/set/send_dbg.pl` · SHA-256 `164e533feab17453a08e7f3480cbf898294ffe48e62b0cb4e33e827c1963a3cb`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 8;
L12: return (1, $self->msg('done'));
```

### Message keys returned

`done`, `e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/send_dbg.pl){ .md-button }

## Verify on a running node

```text
HELP SET/SEND_DBG
```

Compare the installed handler with this page when local overrides or a different revision may be present.