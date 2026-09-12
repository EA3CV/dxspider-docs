# `SEND_CONFIG`

<div class="command-hero" markdown>

**Broadcast PC92 C records**

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
SEND_CONFIG
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`me->broadcast_pc92_update()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/send_config.pl` · SHA-256 `283df2c2f998585bd50af14d54a2bc5addf9d0fa79c7cdf406f7d67356ff0416`

```perl
L5: my $self = shift;
```

### Validation and access evidence

Source: `cmd/send_config.pl` · SHA-256 `283df2c2f998585bd50af14d54a2bc5addf9d0fa79c7cdf406f7d67356ff0416`

```perl
L6: return (1, $self->msg('e5')) unless $self->priv > 5;
L10: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/send_config.pl` · SHA-256 `283df2c2f998585bd50af14d54a2bc5addf9d0fa79c7cdf406f7d67356ff0416`

```perl
L6: return (1, $self->msg('e5')) unless $self->priv > 5;
L10: return (1, $self->msg('ok'));
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SEND_CONFIG
```

**Broadcast PC92 C records**

## Details

This is the PC92 equivalent of INIT. In that it will send out a new
PC92 C record to all interfaces. This can be used to bring other nodes
up to date quicker after a restart.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/send_config.pl){ .md-button }

## Verify on a running node

```text
HELP SEND_CONFIG
```

Compare the installed handler with this page when local overrides or a different revision may be present.