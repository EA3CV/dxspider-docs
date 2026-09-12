# `SET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are present at your terminal.**

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
SET/HERE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXChannel::broadcast_all_nodes()`, `DXChannel::get()`, `DXProt::eph_dup()`, `DXProt::pc24()`, `Route::Node::get()`, `Route::User::get()`, `dxchan->here()`, `ref->here()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/here.pl` · SHA-256 `5a0fd54b849196b36e4c41fa854b24c6c7e8f59cdc1e3c0ad12d06ddb52784cb`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/here.pl` · SHA-256 `5a0fd54b849196b36e4c41fa854b24c6c7e8f59cdc1e3c0ad12d06ddb52784cb`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/here.pl` · SHA-256 `5a0fd54b849196b36e4c41fa854b24c6c7e8f59cdc1e3c0ad12d06ddb52784cb`

```perl
L21: push @out, $self->msg('heres', $call);
L31: push @out, $self->msg('e3', "Set Here", $call);
L35: return (1, @out);
```

### Message keys returned

`e3`, `heres`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/HERE
```

**Tell the system you are present at your terminal**

## When would I use this?

Use this when you want your current session to advertise that you are actively present rather than away.

## Practical examples

### Mark yourself present

```text
SET/HERE
```

### Later, mark yourself away

```text
UNSET/HERE
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/here.pl){ .md-button }

## Related commands

- [`UNSET/HERE`](unset--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP SET/HERE
```

Compare the installed handler with this page when local overrides or a different revision may be present.