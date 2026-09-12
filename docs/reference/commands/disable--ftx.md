# `DISABLE/FTX`

<div class="command-hero" markdown>

**Suppress all spots whose comment contains FT4 or FT8.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>DX spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
DISABLE/FTX
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->ftx()`

### Argument parsing evidence

Source: `cmd/disable/ftx.pl` · SHA-256 `7a205a77f4d06826b473259c9e612c621c76bff3d873fe9fcd842bb704a4185d`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/disable/ftx.pl` · SHA-256 `7a205a77f4d06826b473259c9e612c621c76bff3d873fe9fcd842bb704a4185d`

```perl
L14: return (1, $self->msg('ftxd'));
L16: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/disable/ftx.pl` · SHA-256 `7a205a77f4d06826b473259c9e612c621c76bff3d873fe9fcd842bb704a4185d`

```perl
L14: return (1, $self->msg('ftxd'));
L16: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`ftxd`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DISABLE/FTX
```

**Disable ALL FT4/8 spots**

## When would I use this?

Use this only when you do not want FT4/FT8 spots at all. For a less aggressive option, keep FTX enabled and disable AUTOFTX instead.

## Practical examples

### Block all FT4/FT8 spots

```text
DISABLE/FTX
```

### Allow FT4/FT8 again

```text
ENABLE/FTX
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/disable/ftx.pl){ .md-button }

## Related commands

- [`ENABLE/FTX`](enable--ftx.md)
- [`DISABLE/AUTOFTX`](disable--autoftx.md)
- [`ENABLE/AUTOFTX`](enable--autoftx.md)

## Verify on a running node

```text
HELP DISABLE/FTX
```

Compare the installed handler with this page when local overrides or a different revision may be present.