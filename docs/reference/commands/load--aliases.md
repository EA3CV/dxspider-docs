# `LOAD/ALIASES`

<div class="command-hero" markdown>

**Reload the command alias table**

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
LOAD/ALIASES
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`CmdAlias::load()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/aliases.pl` · SHA-256 `ed272d9664d9f8383e52a8df882dc5337ad9b00f45c73b492d9e051b629cbffe`

```perl
L4: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/aliases.pl` · SHA-256 `ed272d9664d9f8383e52a8df882dc5337ad9b00f45c73b492d9e051b629cbffe`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/aliases.pl` · SHA-256 `ed272d9664d9f8383e52a8df882dc5337ad9b00f45c73b492d9e051b629cbffe`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
L7: @out = ($self->msg('ok')) if !@out;
L8: return (1, @out);
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/ALIASES
```

**Reload the command alias table**

## Details

Reload the /spider/cmd/Aliases file after you have editted it. You
will need to do this if you change this file whilst the cluster is
running in order for the changes to take effect.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/aliases.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/ALIASES
```

Compare the installed handler with this page when local overrides or a different revision may be present.