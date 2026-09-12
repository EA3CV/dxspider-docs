# `LOAD/FORWARD`

<div class="command-hero" markdown>

**Reload the msg forwarding routing table**

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
LOAD/FORWARD
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::load_forward()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/forward.pl` · SHA-256 `a4328fe3fc2e1208b445a9616d09bd320085c7a3d859139c9ba96d297b8ef0ea`

```perl
L2: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/forward.pl` · SHA-256 `a4328fe3fc2e1208b445a9616d09bd320085c7a3d859139c9ba96d297b8ef0ea`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/forward.pl` · SHA-256 `a4328fe3fc2e1208b445a9616d09bd320085c7a3d859139c9ba96d297b8ef0ea`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
L5: push @out, (DXMsg::load_forward());
L6: @out = ($self->msg('ok')) unless @out;
L7: return (1, @out);
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/FORWARD
```

**Reload the msg forwarding routing table**

## Details

Reload the /spider/msg/forward.pl file if you have changed it
manually whilst the cluster is running.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/forward.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/FORWARD
```

Compare the installed handler with this page when local overrides or a different revision may be present.