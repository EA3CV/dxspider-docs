# `UNSET/ISOLATE`

<div class="command-hero" markdown>

**Stop Isolation of a node from the rest of the network**

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
UNSET/ISOLATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `self->msg()`, `user->isolate()`, `user->put()`

### Argument parsing evidence

Source: `cmd/unset/isolate.pl` · SHA-256 `e16dd2aad2e11f090780be3654bdfe17b5cab2e599e21bda161f5fee65a629c4`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/isolate.pl` · SHA-256 `e16dd2aad2e11f090780be3654bdfe17b5cab2e599e21bda161f5fee65a629c4`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L27: return (1, $self->msg('usernf', $call)) if !$user;
```

### Output and error evidence

Source: `cmd/unset/isolate.pl` · SHA-256 `e16dd2aad2e11f090780be3654bdfe17b5cab2e599e21bda161f5fee65a629c4`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L24: push @out, $self->msg('nodee1', $call);
L27: return (1, $self->msg('usernf', $call)) if !$user;
L30: push @out, $self->msg('isou', $call);
L31: Log('DXCommand', $self->msg('isou', $call));
L34: return (1, @out);
```

### Message keys returned

`e5`, `isou`, `nodee1`, `usernf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/ISOLATE
```

**Stop Isolation of a node from the rest of the network**

## Details

Remove isolation from a node - SET/ISOLATE

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/isolate.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/ISOLATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.