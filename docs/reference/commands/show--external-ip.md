# `SHOW/EXTERNAL_IP`

<div class="command-hero" markdown>

**Source-present command; review implementation evidence.**

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
SHOW/EXTERNAL_IP
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/external_ip.pl` · SHA-256 `e9321c01c34d12c00bb73b2bd48046d6d2f91294626a961566b2e94f422e1531`

```perl
L3: my $self = shift;
```

### Validation and access evidence

Source: `cmd/show/external_ip.pl` · SHA-256 `e9321c01c34d12c00bb73b2bd48046d6d2f91294626a961566b2e94f422e1531`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 8;
```

### Output and error evidence

Source: `cmd/show/external_ip.pl` · SHA-256 `e9321c01c34d12c00bb73b2bd48046d6d2f91294626a961566b2e94f422e1531`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 8;
L9: push @out, "$self->{call}: $self->{hostname} main::me: $main::me->{hostname} node: $chan->{hostname}";
L10: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/external_ip.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/EXTERNAL_IP
```

Compare the installed handler with this page when local overrides or a different revision may be present.