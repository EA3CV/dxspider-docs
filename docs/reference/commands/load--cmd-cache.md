# `LOAD/CMD_CACHE`

<div class="command-hero" markdown>

**Reload the automatic command cache**

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
LOAD/CMD_CACHE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXCommandmode::clear_cmd_cache()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L12: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L16: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/load/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L16: return (1, $self->msg('ok'));
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/CMD_CACHE
```

**Reload the automatic command cache**

## Details

Normally, if you change a command file in the cmd or local_cmd tree it
will automatially be picked up by the cluster program. Sometimes it
can get confused if you are doing a lot of moving commands about or
delete a command in the local_cmd tree and want to use the normal one
again. Execute this command to reset everything back to the state it
was just after a cluster restart. To see what is in the command cache
see SHOW/CMD_CACHE.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/cmd_cache.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/CMD_CACHE
```

Compare the installed handler with this page when local overrides or a different revision may be present.