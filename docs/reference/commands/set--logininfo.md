# `SET/LOGININFO`

<div class="command-hero" markdown>

**Inform when a station logs in/out locally**

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
SET/LOGININFO
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->logininfo()`, `self->msg()`, `user->wantlogininfo()`

### Argument parsing evidence

Source: `cmd/set/logininfo.pl` · SHA-256 `090230fa5c9323f1f1c17d8e103c2c1376732ab049b6a2ec20e08baa226a4dd1`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/set/logininfo.pl` · SHA-256 `090230fa5c9323f1f1c17d8e103c2c1376732ab049b6a2ec20e08baa226a4dd1`

```perl
L11: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/set/logininfo.pl` · SHA-256 `090230fa5c9323f1f1c17d8e103c2c1376732ab049b6a2ec20e08baa226a4dd1`

```perl
L11: return (1, $self->msg('ok'));
```

### Message keys returned

`ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/LOGININFO
```

**Inform when a station logs in/out locally**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/logininfo.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LOGININFO
```

Compare the installed handler with this page when local overrides or a different revision may be present.