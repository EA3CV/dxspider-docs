# `DMESG`

<div class="command-hero" markdown>

**Log the current values of the DXDebug dbgring butter**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
DMESG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXDebug::dbgclearring()`, `DXDebug::dbgprintring()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dmesg.pl` · SHA-256 `3e41c91d237fbd7fe0ae29bb0e169a532cd52f317457fbf0c28e9c8cd7d58fd0`

```perl
L6: my $self = shift;
L7: my $line = shift;;
L10: my @args = split /\s+/, $line;
L14: for (@args) {
```

### Validation and access evidence

Source: `cmd/dmesg.pl` · SHA-256 `3e41c91d237fbd7fe0ae29bb0e169a532cd52f317457fbf0c28e9c8cd7d58fd0`

```perl
L8: return (1, $self->msg('e5')) unless $self->priv >= 9;
```

### Output and error evidence

Source: `cmd/dmesg.pl` · SHA-256 `3e41c91d237fbd7fe0ae29bb0e169a532cd52f317457fbf0c28e9c8cd7d58fd0`

```perl
L8: return (1, $self->msg('e5')) unless $self->priv >= 9;
L22: return (1, qq{Contents of $lines lines of debug ring buffer logged. View with watchdbg.});
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dmesg.pl){ .md-button }

## Verify on a running node

```text
HELP DMESG
```

Compare the installed handler with this page when local overrides or a different revision may be present.