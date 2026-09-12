# `SET/GTK`

<div class="command-hero" markdown>

**set the gtk flag**

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
SET/GTK [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->enhanced()`, `self->gtk()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/gtk.pl` · SHA-256 `9b5eefd6a74d9948c357d465954f405ef093a2b641b00fe4f29054035a3d14cd`

```perl
L9: my ($self, $line) = @_;
```

### Output and error evidence

Source: `cmd/set/gtk.pl` · SHA-256 `9b5eefd6a74d9948c357d465954f405ef093a2b641b00fe4f29054035a3d14cd`

```perl
L13: push @out, $self->msg('gtks', $self->call);
L14: return (1, @out);
```

### Message keys returned

`gtks`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/gtk.pl){ .md-button }

## Verify on a running node

```text
HELP SET/GTK
```

Compare the installed handler with this page when local overrides or a different revision may be present.