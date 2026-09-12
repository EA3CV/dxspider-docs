# `LOAD/PREFIXES`

<div class="command-hero" markdown>

**Reload the prefix table**

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
LOAD/PREFIXES
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`Prefix::load()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/prefixes.pl` · SHA-256 `837edd47e3ec9823205c39644e43d164677dc12850c0f7d0c0cb5734c73e4782`

```perl
L4: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/prefixes.pl` · SHA-256 `837edd47e3ec9823205c39644e43d164677dc12850c0f7d0c0cb5734c73e4782`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
L7: return (1, $out ? $out : $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/load/prefixes.pl` · SHA-256 `837edd47e3ec9823205c39644e43d164677dc12850c0f7d0c0cb5734c73e4782`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
L7: return (1, $out ? $out : $self->msg('ok'));
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/PREFIXES
```

**Reload the prefix table**

## Details

Reload the /spider/data/prefix_data.pl file if you have changed it
manually whilst the cluster is running.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/prefixes.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/PREFIXES
```

Compare the installed handler with this page when local overrides or a different revision may be present.