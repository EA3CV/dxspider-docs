# `UNSET/AGWENGINE`

<div class="command-hero" markdown>

**Disable the AGW Engine**

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
UNSET/AGWENGINE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`AGWMsg::finish()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/agwengine.pl` · SHA-256 `fe9680f5245ed242ed0cde3b63681d266bd95df8ad807b7ed6caaf136e4f1924`

```perl
L7: my $self = shift;
```

### Validation and access evidence

Source: `cmd/unset/agwengine.pl` · SHA-256 `fe9680f5245ed242ed0cde3b63681d266bd95df8ad807b7ed6caaf136e4f1924`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return (1, $self->msg('agwu'));
```

### Output and error evidence

Source: `cmd/unset/agwengine.pl` · SHA-256 `fe9680f5245ed242ed0cde3b63681d266bd95df8ad807b7ed6caaf136e4f1924`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return (1, $self->msg('agwu'));
L14: return (1);
```

### Message keys returned

`agwu`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/AGWENGINE
```

**Disable the AGW Engine**

## Details

These commands assume that /spider/local/AGWConnect.pm has been setup
correctly and you wish to do some testing or otherwise want to alter
the default state of your connection to the AGW Engine.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/agwengine.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/AGWENGINE
```

Compare the installed handler with this page when local overrides or a different revision may be present.