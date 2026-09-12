# `SET/AGWMONITOR`

<div class="command-hero" markdown>

**Enable Monitoring on the AGW Engine**

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
SET/AGWMONITOR
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`AGWMsg::_sendf()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/agwmonitor.pl` · SHA-256 `598597c54afbc18d3c594e43f6fe69daf6587742c8f2799131eb53db1614064a`

```perl
L7: my $self = shift;
```

### Validation and access evidence

Source: `cmd/set/agwmonitor.pl` · SHA-256 `598597c54afbc18d3c594e43f6fe69daf6587742c8f2799131eb53db1614064a`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return (1, $self->msg('mone'));
```

### Output and error evidence

Source: `cmd/set/agwmonitor.pl` · SHA-256 `598597c54afbc18d3c594e43f6fe69daf6587742c8f2799131eb53db1614064a`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return (1, $self->msg('mone'));
L14: return (1);
```

### Message keys returned

`e5`, `mone`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/AGWMONITOR
```

**Enable Monitoring on the AGW Engine**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/agwmonitor.pl){ .md-button }

## Verify on a running node

```text
HELP SET/AGWMONITOR
```

Compare the installed handler with this page when local overrides or a different revision may be present.