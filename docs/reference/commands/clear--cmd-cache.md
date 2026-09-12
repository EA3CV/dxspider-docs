# `CLEAR/CMD_CACHE`

<div class="command-hero" markdown>

**reset/reload the short name command cache you may need to do this if you remove files or the system gets confused about where it should be loading its cmd files**

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
CLEAR/CMD_CACHE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXCommandmode::clear_cmd_cache()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/clear/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L12: my $self = shift;
```

### Validation and access evidence

Source: `cmd/clear/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L16: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/clear/cmd_cache.pl` · SHA-256 `a60c0434853027a55736894ac9b2c373a5d0c0e4f08c1e0a52aa0d570ac2a105`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L16: return (1, $self->msg('ok'));
```

### Message keys returned

`e5`, `ok`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/clear/cmd_cache.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/CMD_CACHE
```

Compare the installed handler with this page when local overrides or a different revision may be present.