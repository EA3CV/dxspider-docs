# `UNSET/WCY`

<div class="command-hero" markdown>

**Stop WCY messages coming out on your terminal**

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
UNSET/WCY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `DXChannel::wcy()`, `self->msg()`, `user->wantwcy()`

### Argument parsing evidence

Source: `cmd/unset/wcy.pl` · SHA-256 `22bbfe57c9de3f590a390826f67447d484e9a62cd99de4b559fb3d97b5e34f21`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/wcy.pl` · SHA-256 `22bbfe57c9de3f590a390826f67447d484e9a62cd99de4b559fb3d97b5e34f21`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/unset/wcy.pl` · SHA-256 `22bbfe57c9de3f590a390826f67447d484e9a62cd99de4b559fb3d97b5e34f21`

```perl
L22: push @out, $self->msg('wcyu', $call);
L24: push @out, $self->msg('e3', "Unset WCY", $call);
L27: return (1, @out);
```

### Message keys returned

`e3`, `wcyu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/WCY
```

**Stop WCY messages coming out on your terminal**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/wcy.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/WCY
```

Compare the installed handler with this page when local overrides or a different revision may be present.