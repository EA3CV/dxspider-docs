# `SHOW/DEBUG`

<div class="command-hero" markdown>

**Show what levels of debug information you are logging**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/DEBUG
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Argument parsing evidence

Source: `cmd/show/debug.pl` · SHA-256 `41e548d1a50f133dbad65626586cb3ac9d92e5ef617ecb1fa20f89523f036522`

```perl
L9: my $self = shift;
```

### Validation and access evidence

Source: `cmd/show/debug.pl` · SHA-256 `41e548d1a50f133dbad65626586cb3ac9d92e5ef617ecb1fa20f89523f036522`

```perl
L10: return (0) if ($self->priv < 9); # only console users allowed
```

### Output and error evidence

Source: `cmd/show/debug.pl` · SHA-256 `41e548d1a50f133dbad65626586cb3ac9d92e5ef617ecb1fa20f89523f036522`

```perl
L10: return (0) if ($self->priv < 9); # only console users allowed
L14: return (1, "debug levels: $set");
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/DEBUG
```

**Show what levels of debug information you are logging**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/debug.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DEBUG
```

Compare the installed handler with this page when local overrides or a different revision may be present.