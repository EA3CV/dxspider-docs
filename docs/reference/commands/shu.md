# `SHU`

<div class="command-hero" markdown>

**Command to force people to type at least 'shut' to shutdown**

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
SHU
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/shu.pl` · SHA-256 `035c2f9aef9b9d70e7cc32f361bf187c48885d7d53603046ad93e22b414ef565`

```perl
L9: my $self = shift;
```

### Validation and access evidence

Source: `cmd/shu.pl` · SHA-256 `035c2f9aef9b9d70e7cc32f361bf187c48885d7d53603046ad93e22b414ef565`

```perl
L11: if ($self->priv >= 5) {
L12: return (1, $self->msg('shu'))
L14: return (1, $self->msg('e1'));
```

### Output and error evidence

Source: `cmd/shu.pl` · SHA-256 `035c2f9aef9b9d70e7cc32f361bf187c48885d7d53603046ad93e22b414ef565`

```perl
L12: return (1, $self->msg('shu'))
L14: return (1, $self->msg('e1'));
```

### Message keys returned

`e1`, `shu`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/shu.pl){ .md-button }

## Verify on a running node

```text
HELP SHU
```

Compare the installed handler with this page when local overrides or a different revision may be present.