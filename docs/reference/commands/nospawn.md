# `NOSPAWN`

<div class="command-hero" markdown>

**pretend that you are another user, useful for reseting those silly things that people insist on getting wrong like set/homenode et al**

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
NOSPAWN <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`self->msg()`, `self->run_cmd()`

### Argument parsing evidence

Source: `cmd/nospawn.pl` · SHA-256 `02c6eaeaefea07ceda18681f9165dd871d555ea8ac3d524d42b456a65ecc1eef`

```perl
L9: my ($self, $line) = @_;
L15: Log('DXCommand', "$mycall is trying to nospawn $line locally");
L23: Log('DXCommand', "nospawn '$line' by $mycall");
L25: my @out = $self->run_cmd($line);
```

### Validation and access evidence

Source: `cmd/nospawn.pl` · SHA-256 `02c6eaeaefea07ceda18681f9165dd871d555ea8ac3d524d42b456a65ecc1eef`

```perl
L14: if ($self->priv < 2) {
L16: return (1, $self->msg('e5'));
L18: if ($self->remotecmd || $self->inscript) {
L20: return (1, $self->msg('e5'));
```

### Output and error evidence

Source: `cmd/nospawn.pl` · SHA-256 `02c6eaeaefea07ceda18681f9165dd871d555ea8ac3d524d42b456a65ecc1eef`

```perl
L16: return (1, $self->msg('e5'));
L20: return (1, $self->msg('e5'));
L28: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/nospawn.pl){ .md-button }

## Verify on a running node

```text
HELP NOSPAWN
```

Compare the installed handler with this page when local overrides or a different revision may be present.