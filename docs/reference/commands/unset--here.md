# `UNSET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are absent from your terminal.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Presence</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
UNSET/HERE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXChannel::broadcast_all_nodes()`, `DXChannel::get()`, `DXProt::eph_dup()`, `DXProt::pc24()`, `Route::Node::get()`, `Route::User::get()`, `dxchan->here()`, `ref->here()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/here.pl` · SHA-256 `51a95123adc2464f3786d83a59f9f72836caa7bd554a864501f8696852836071`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/here.pl` · SHA-256 `51a95123adc2464f3786d83a59f9f72836caa7bd554a864501f8696852836071`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/unset/here.pl` · SHA-256 `51a95123adc2464f3786d83a59f9f72836caa7bd554a864501f8696852836071`

```perl
L21: push @out, $self->msg('hereu', $call);
L31: push @out, $self->msg('e3', "Unset Here", $call);
L35: return (1, @out);
```

### Message keys returned

`e3`, `hereu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/HERE
```

**Tell the system you are absent from your terminal**

## When would I use this?

This is the opposite of SET/HERE. It marks your session as away without disconnecting you.

## Practical examples

### Mark yourself away

```text
UNSET/HERE
```

### Mark yourself present again

```text
SET/HERE
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/here.pl){ .md-button }

## Related commands

- [`SET/HERE`](set--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP UNSET/HERE
```

Compare the installed handler with this page when local overrides or a different revision may be present.