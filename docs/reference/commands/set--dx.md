# `SET/DX`

<div class="command-hero" markdown>

**Allow DX messages to come out on your terminal**

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
SET/DX [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `chan->dx()`, `self->msg()`, `user->wantdx()`

### Argument parsing evidence

Source: `cmd/set/dx.pl` · SHA-256 `cef680b5655639781bf7e7e2d0b40f7e15fb4dd4ee853982b43a2ec18c71467d`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/dx.pl` · SHA-256 `cef680b5655639781bf7e7e2d0b40f7e15fb4dd4ee853982b43a2ec18c71467d`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/dx.pl` · SHA-256 `cef680b5655639781bf7e7e2d0b40f7e15fb4dd4ee853982b43a2ec18c71467d`

```perl
L22: push @out, $self->msg('dxs', $call);
L24: push @out, $self->msg('e3', "Set DX Spots", $call);
L27: return (1, @out);
```

### Message keys returned

`dxs`, `e3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/DX
```

**Allow DX messages to come out on your terminal**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/dx.pl){ .md-button }

## Verify on a running node

```text
HELP SET/DX
```

Compare the installed handler with this page when local overrides or a different revision may be present.