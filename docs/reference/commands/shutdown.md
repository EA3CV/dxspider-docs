# `SHUTDOWN`

<div class="command-hero" markdown>

**Shutdown the cluster**

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
SHUTDOWN
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXChannel::get_all()`, `ref->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/shutdown.pl` · SHA-256 `ff554fc9a3784479dd2a0d6a5c63ee8dfc88b819d1c9adfdec8b083b81a95a38`

```perl
L6: my $self = shift;
```

### Validation and access evidence

Source: `cmd/shutdown.pl` · SHA-256 `ff554fc9a3784479dd2a0d6a5c63ee8dfc88b819d1c9adfdec8b083b81a95a38`

```perl
L9: return (1, $self->msg('e5')) unless $self->priv >= 5;
```

### Output and error evidence

Source: `cmd/shutdown.pl` · SHA-256 `ff554fc9a3784479dd2a0d6a5c63ee8dfc88b819d1c9adfdec8b083b81a95a38`

```perl
L9: return (1, $self->msg('e5')) unless $self->priv >= 5;
L11: $ref->send($self->msg('shutting')) if $ref->is_user;
L16: return (1);
```

### Message keys returned

`e5`, `shutting`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHUTDOWN
```

**Shutdown the cluster**

## Details

Shutdown the cluster and disconnect all the users

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/shutdown.pl){ .md-button }

## Verify on a running node

```text
HELP SHUTDOWN
```

Compare the installed handler with this page when local overrides or a different revision may be present.