# `SET/VAR`

<div class="command-hero" markdown>

**set any variable Rape me!**

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
SET/VAR <structured arguments>
```

The handler parses a structured list (for example comma-separated or key/value input). See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Named fields consumed by the parser

`var`, `rest`

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/set/var.pl` · SHA-256 `4b38b2f7d8c7e96a2447f663d3efaea8d9f2b4cbcd685b04e96520e807042781`

```perl
L11: my ($self, $line) = @_;
L13: return (1, $self->msg('e9')) unless $line;
L15: my ($var, $rest) = split /=|\s+/, $line, 2;
L16: $rest =~ s/^=\s*//;
```

### Validation and access evidence

Source: `cmd/set/var.pl` · SHA-256 `4b38b2f7d8c7e96a2447f663d3efaea8d9f2b4cbcd685b04e96520e807042781`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
L13: return (1, $self->msg('e9')) unless $line;
```

### Output and error evidence

Source: `cmd/set/var.pl` · SHA-256 `4b38b2f7d8c7e96a2447f663d3efaea8d9f2b4cbcd685b04e96520e807042781`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
L13: return (1, $self->msg('e9')) unless $line;
L19: return (1, $@ ? $@ : "Ok, $var = " . dd($rest) );
```

### Message keys returned

`e5`, `e9`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/var.pl){ .md-button }

## Verify on a running node

```text
HELP SET/VAR
```

Compare the installed handler with this page when local overrides or a different revision may be present.