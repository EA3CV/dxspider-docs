# `LOAD/HOPS`

<div class="command-hero" markdown>

**load the node hop count table after changing it**

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
LOAD/HOPS
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXProt::load_hops()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/hops.pl` · SHA-256 `ac3aa082d754e84a50a4cf71b1019469118ef93ca6a417be25cf7cdb7704a226`

```perl
L4: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/hops.pl` · SHA-256 `ac3aa082d754e84a50a4cf71b1019469118ef93ca6a417be25cf7cdb7704a226`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/hops.pl` · SHA-256 `ac3aa082d754e84a50a4cf71b1019469118ef93ca6a417be25cf7cdb7704a226`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
L7: @out = ($self->msg('ok')) if !@out;
L8: return (1, @out);
```

### Message keys returned

`e5`, `ok`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/hops.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/HOPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.