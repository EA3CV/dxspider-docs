# `UNSET/LOGININFO`

<div class="command-hero" markdown>

**No longer inform when a station logs in/out locally**

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
UNSET/LOGININFO
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->logininfo()`, `self->msg()`, `user->wantlogininfo()`

### Argument parsing evidence

Source: `cmd/unset/logininfo.pl` · SHA-256 `da74d58c5cc822c66dd015b06b9abe508d4815c6ebd8d55ad785ae63db2ec9e3`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/unset/logininfo.pl` · SHA-256 `da74d58c5cc822c66dd015b06b9abe508d4815c6ebd8d55ad785ae63db2ec9e3`

```perl
L11: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/unset/logininfo.pl` · SHA-256 `da74d58c5cc822c66dd015b06b9abe508d4815c6ebd8d55ad785ae63db2ec9e3`

```perl
L11: return (1, $self->msg('ok'));
```

### Message keys returned

`ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/LOGININFO
```

**No longer inform when a station logs in/out locally**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/logininfo.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/LOGININFO
```

Compare the installed handler with this page when local overrides or a different revision may be present.