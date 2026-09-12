# `ENABLE/FTX`

<div class="command-hero" markdown>

**Enable ALL FT4/8 Spots**

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
ENABLE/FTX
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->ftx()`

### Argument parsing evidence

Source: `cmd/enable/ftx.pl` · SHA-256 `175b71b1e718a5618673f828ac94688b0d7cf9a357a8ac586917a3ed2a1ccf44`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/enable/ftx.pl` · SHA-256 `175b71b1e718a5618673f828ac94688b0d7cf9a357a8ac586917a3ed2a1ccf44`

```perl
L14: return (1, $self->msg('ftxe'));
L16: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/enable/ftx.pl` · SHA-256 `175b71b1e718a5618673f828ac94688b0d7cf9a357a8ac586917a3ed2a1ccf44`

```perl
L14: return (1, $self->msg('ftxe'));
L16: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`ftxe`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
ENABLE/FTX
```

**Enable ALL FT4/8 Spots**

## Details

If disabled, stops ALL spots with "FT4" or "FT8" in the comment string.

NOTE: if enabled, with disable/autoftx command means that you STILL
get all non-automated FT4/8 spots.

Default is enabled.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/enable/ftx.pl){ .md-button }

## Verify on a running node

```text
HELP ENABLE/FTX
```

Compare the installed handler with this page when local overrides or a different revision may be present.