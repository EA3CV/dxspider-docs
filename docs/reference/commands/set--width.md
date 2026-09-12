# `SET/WIDTH`

<div class="command-hero" markdown>

**Set terminal width for the live session and stored user profile.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Personal settings</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SET/WIDTH
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `self->width()`, `user->width()`

### Argument parsing evidence

Source: `cmd/set/width.pl` · SHA-256 `cd133eb909da110a5b9fd6444ba844dcdbfae14a7bc1ebab60ef2c33482b0cec`

```perl
L8: my $self = shift;
L9: my $l = shift;
```

### Validation and access evidence

Source: `cmd/set/width.pl` · SHA-256 `cd133eb909da110a5b9fd6444ba844dcdbfae14a7bc1ebab60ef2c33482b0cec`

```perl
L13: return (1, $self->msg('pagewidth', $l));
```

### Output and error evidence

Source: `cmd/set/width.pl` · SHA-256 `cd133eb909da110a5b9fd6444ba844dcdbfae14a7bc1ebab60ef2c33482b0cec`

```perl
L13: return (1, $self->msg('pagewidth', $l));
```

### Message keys returned

`pagewidth`

## Practical examples

### 120-column terminal

```text
SET/WIDTH 120
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/width.pl){ .md-button }

## Related commands

- [`SET/PAGE`](set--page.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP SET/WIDTH
```

Compare the installed handler with this page when local overrides or a different revision may be present.