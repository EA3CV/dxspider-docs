# `SHOW/SPOTSTATS`

<div class="command-hero" markdown>

**Show the current Spot statistics**

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
SHOW/SPOTSTATS
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXProt::get_pc11_61_stats()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/spotstats.pl` · SHA-256 `eacda3f300bd3757d7a36797d5c7ff45027b92eb45eb9ece4a10146e1f28a8bc`

```perl
L10: my $self = shift;
```

### Validation and access evidence

Source: `cmd/show/spotstats.pl` · SHA-256 `eacda3f300bd3757d7a36797d5c7ff45027b92eb45eb9ece4a10146e1f28a8bc`

```perl
L11: return (1, $self->msg('e5')) unless $self->priv >= 1;
```

### Output and error evidence

Source: `cmd/show/spotstats.pl` · SHA-256 `eacda3f300bd3757d7a36797d5c7ff45027b92eb45eb9ece4a10146e1f28a8bc`

```perl
L11: return (1, $self->msg('e5')) unless $self->priv >= 1;
L19: push @out, $stats;
L21: push @out, qq{pc11 stats not available};
L23: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/SPOTSTATS
```

**Show the current Spot statistics**

## Details

View the current unique spot sentences seen since the last restart.

It shows the number of PC11 and PC61 sentences and the percentage
of PC11s received of the total of both. It also shows the number
of PC11s that have been promoted to PC61 before being passed on
plus a total percentage of incoming PC11 that have been promoted.

A PC11 can be promoted to PC61 by a stored IP address in the routing
table or it can be promoted by being delayed to a short for any
passing PC61 from another node.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/spotstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SPOTSTATS
```

Compare the installed handler with this page when local overrides or a different revision may be present.