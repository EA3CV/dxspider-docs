# `SET/SYS_QRA`

<div class="command-hero" markdown>

**Set your cluster QRA Grid locator**

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
SET/SYS_QRA [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/set/sys_qra.pl` · SHA-256 `433400d081e980e32f30ab483c0546795c57b1fb87a608bbee56f60e25b44ed1`

```perl
L9: my ($self, $line) = @_;
L11: my @out = run_cmd($self, "set/qra $line");
L12: return (1, run_cmd($main::me, "set/qra $line"));
```

### Validation and access evidence

Source: `cmd/set/sys_qra.pl` · SHA-256 `433400d081e980e32f30ab483c0546795c57b1fb87a608bbee56f60e25b44ed1`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/set/sys_qra.pl` · SHA-256 `433400d081e980e32f30ab483c0546795c57b1fb87a608bbee56f60e25b44ed1`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return (1, run_cmd($main::me, "set/qra $line"));
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/SYS_QRA <locator>
```

**Set your cluster QRA Grid locator**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/sys_qra.pl){ .md-button }

## Verify on a running node

```text
HELP SET/SYS_QRA
```

Compare the installed handler with this page when local overrides or a different revision may be present.