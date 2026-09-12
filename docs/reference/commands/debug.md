# `DEBUG`

<div class="command-hero" markdown>

**Set the cluster program into debug mode**

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
DEBUG
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/debug.pl` · SHA-256 `280a89a59fca1d59a360f67c05e8d227fc811dfefd5ac133ae36fbf20765105e`

```perl
L11: my $self = shift;
```

### Validation and access evidence

Source: `cmd/debug.pl` · SHA-256 `280a89a59fca1d59a360f67c05e8d227fc811dfefd5ac133ae36fbf20765105e`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/debug.pl` · SHA-256 `280a89a59fca1d59a360f67c05e8d227fc811dfefd5ac133ae36fbf20765105e`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DEBUG
```

**Set the cluster program into debug mode**

## Details

Executing this command will only have an effect if you are running the cluster
in debug mode i.e.

```text
	perl -d cluster.pl
```

It will interrupt the cluster just after the debug command has finished.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/debug.pl){ .md-button }

## Verify on a running node

```text
HELP DEBUG
```

Compare the installed handler with this page when local overrides or a different revision may be present.