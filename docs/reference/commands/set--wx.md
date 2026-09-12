# `SET/WX`

<div class="command-hero" markdown>

**Allow WX messages to come out on your terminal**

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
SET/WX [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `chan->wx()`, `self->msg()`, `user->wantwx()`

### Argument parsing evidence

Source: `cmd/set/wx.pl` · SHA-256 `8e97eeb80d3a0fad41e72b7a9613df4b71888700000b59e14d5c70f9feda0be1`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/wx.pl` · SHA-256 `8e97eeb80d3a0fad41e72b7a9613df4b71888700000b59e14d5c70f9feda0be1`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/wx.pl` · SHA-256 `8e97eeb80d3a0fad41e72b7a9613df4b71888700000b59e14d5c70f9feda0be1`

```perl
L22: push @out, $self->msg('wxs', $call);
L24: push @out, $self->msg('e3', "Set WX Spots", $call);
L27: return (1, @out);
```

### Message keys returned

`e3`, `wxs`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/WX
```

**Allow WX messages to come out on your terminal**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/wx.pl){ .md-button }

## Verify on a running node

```text
HELP SET/WX
```

Compare the installed handler with this page when local overrides or a different revision may be present.