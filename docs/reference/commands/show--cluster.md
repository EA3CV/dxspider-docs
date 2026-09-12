# `SHOW/CLUSTER`

<div class="command-hero" markdown>

**show some statistics**

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
SHOW/CLUSTER
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Route::cluster()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/cluster.pl` · SHA-256 `dd4c515ee04489fac47106983cc8589ddf7f14edad55f6c7af13c25a367abf7c`

```perl
L5: my $self = shift;
```

### Validation and access evidence

Source: `cmd/show/cluster.pl` · SHA-256 `dd4c515ee04489fac47106983cc8589ddf7f14edad55f6c7af13c25a367abf7c`

```perl
L13: return (1, $self->msg('cluster', $localnodes, $nodes, $users, $tot, $maxlocalusers, $maxusers, $uptime));
```

### Output and error evidence

Source: `cmd/show/cluster.pl` · SHA-256 `dd4c515ee04489fac47106983cc8589ddf7f14edad55f6c7af13c25a367abf7c`

```perl
L13: return (1, $self->msg('cluster', $localnodes, $nodes, $users, $tot, $maxlocalusers, $maxusers, $uptime));
```

### Message keys returned

`cluster`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/cluster.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CLUSTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.