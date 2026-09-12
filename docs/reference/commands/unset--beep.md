# `UNSET/BEEP`

<div class="command-hero" markdown>

**Stop beeps for DX and other messages on your terminal**

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
UNSET/BEEP
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->beep()`, `self->msg()`, `user->wantbeep()`

### Argument parsing evidence

Source: `cmd/unset/beep.pl` · SHA-256 `cca805af30a8dc0221db8fc9ffd48c0d65ed5a4bd7dd974f739c063e52f05057`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/unset/beep.pl` · SHA-256 `cca805af30a8dc0221db8fc9ffd48c0d65ed5a4bd7dd974f739c063e52f05057`

```perl
L11: return (1, $self->msg('beepoff'));
```

### Output and error evidence

Source: `cmd/unset/beep.pl` · SHA-256 `cca805af30a8dc0221db8fc9ffd48c0d65ed5a4bd7dd974f739c063e52f05057`

```perl
L11: return (1, $self->msg('beepoff'));
```

### Message keys returned

`beepoff`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BEEP
```

**Stop beeps for DX and other messages on your terminal**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/beep.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BEEP
```

Compare the installed handler with this page when local overrides or a different revision may be present.