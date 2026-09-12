# `SET/PAGE`

<div class="command-hero" markdown>

**Set the lines per page**

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
SET/PAGE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `self->pagelth()`, `user->pagelth()`

### Argument parsing evidence

Source: `cmd/set/page.pl` · SHA-256 `13285dc714a8bcdb1189def5a2ac7a6246816c66cb01df074be7469301f16198`

```perl
L8: my $self = shift;
L9: my $l = shift;
```

### Validation and access evidence

Source: `cmd/set/page.pl` · SHA-256 `13285dc714a8bcdb1189def5a2ac7a6246816c66cb01df074be7469301f16198`

```perl
L13: return (1, $self->msg('pagelth', $l));
```

### Output and error evidence

Source: `cmd/set/page.pl` · SHA-256 `13285dc714a8bcdb1189def5a2ac7a6246816c66cb01df074be7469301f16198`

```perl
L13: return (1, $self->msg('pagelth', $l));
```

### Message keys returned

`pagelth`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/PAGE <lines per page>
```

**Set the lines per page**

## Details

Tell the system how many lines you wish on a page when the number of line
of output from a command is more than this. The default is 20. Setting it
explicitly to 0 will disable paging.
```text
SET/PAGE 30
SET/PAGE 0
```

The setting is stored in your user profile.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/page.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PAGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.