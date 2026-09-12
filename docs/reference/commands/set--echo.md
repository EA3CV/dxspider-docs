# `SET/ECHO`

<div class="command-hero" markdown>

**Make the cluster echo your input**

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
SET/ECHO
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `self->send_now()`, `user->wantecho()`

### Argument parsing evidence

Source: `cmd/set/echo.pl` · SHA-256 `4343dd8b521cb9fb39a77ec5f413d9411d0459e0a5cbbc78d0a5a066eb5c578e`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/set/echo.pl` · SHA-256 `4343dd8b521cb9fb39a77ec5f413d9411d0459e0a5cbbc78d0a5a066eb5c578e`

```perl
L11: return (1, $self->msg('echoon'));
```

### Output and error evidence

Source: `cmd/set/echo.pl` · SHA-256 `4343dd8b521cb9fb39a77ec5f413d9411d0459e0a5cbbc78d0a5a066eb5c578e`

```perl
L11: return (1, $self->msg('echoon'));
```

### Message keys returned

`echoon`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/ECHO
```

**Make the cluster echo your input**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/echo.pl){ .md-button }

## Verify on a running node

```text
HELP SET/ECHO
```

Compare the installed handler with this page when local overrides or a different revision may be present.