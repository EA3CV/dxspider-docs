# `SET/WWV`

<div class="command-hero" markdown>

**Allow WWV messages to come out on your terminal**

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
SET/WWV [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `DXChannel::wwv()`, `self->msg()`, `user->wantwwv()`

### Argument parsing evidence

Source: `cmd/set/wwv.pl` · SHA-256 `69c5e7f9b1289d4177688859d15cf08b8b8a8aec062c3cf1cc1138ad8f8f22df`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/wwv.pl` · SHA-256 `69c5e7f9b1289d4177688859d15cf08b8b8a8aec062c3cf1cc1138ad8f8f22df`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/wwv.pl` · SHA-256 `69c5e7f9b1289d4177688859d15cf08b8b8a8aec062c3cf1cc1138ad8f8f22df`

```perl
L22: push @out, $self->msg('wwvs', $call);
L24: push @out, $self->msg('e3', "Set WWV", $call);
L27: return (1, @out);
```

### Message keys returned

`e3`, `wwvs`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/WWV
```

**Allow WWV messages to come out on your terminal**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP SET/WWV
```

Compare the installed handler with this page when local overrides or a different revision may be present.