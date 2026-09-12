# `LOAD/SWOP`

<div class="command-hero" markdown>

**reload the swop file**

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
LOAD/SWOP
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::load_swop()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/swop.pl` · SHA-256 `2c49db48afb1b4f1f98eff8bb5a3133051e611fc9da8a8dd67ee92823574b5f0`

```perl
L2: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/swop.pl` · SHA-256 `2c49db48afb1b4f1f98eff8bb5a3133051e611fc9da8a8dd67ee92823574b5f0`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/swop.pl` · SHA-256 `2c49db48afb1b4f1f98eff8bb5a3133051e611fc9da8a8dd67ee92823574b5f0`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
L5: push @out, (DXMsg::load_swop());
L6: @out = ($self->msg('ok')) unless @out;
L7: return (1, @out);
```

### Message keys returned

`e5`, `ok`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/swop.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/SWOP
```

Compare the installed handler with this page when local overrides or a different revision may be present.