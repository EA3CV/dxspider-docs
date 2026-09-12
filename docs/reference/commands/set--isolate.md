# `SET/ISOLATE`

<div class="command-hero" markdown>

**Isolate a node from the rest of the network**

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
SET/ISOLATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.
- Reads or modifies filter state/files.

### Important calls

`DXChannel::get()`, `DXUser->new()`, `DXUser::get()`, `Filter::getfn()`, `self->msg()`, `user->isolate()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/isolate.pl` · SHA-256 `be5291ad7d0ffbf925f97495bc4f348d9117866cb84b7d5897f9ad027af2e162`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/isolate.pl` · SHA-256 `be5291ad7d0ffbf925f97495bc4f348d9117866cb84b7d5897f9ad027af2e162`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/set/isolate.pl` · SHA-256 `be5291ad7d0ffbf925f97495bc4f348d9117866cb84b7d5897f9ad027af2e162`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9;
L24: push @out, $self->msg('nodee1', $call);
L30: push(@out, $self->msg('isoari', $call)), $f++ if Filter::getfn('route', $call, 1);
L31: push(@out, $self->msg('isoaro', $call)), $f++ if Filter::getfn('route', $call, 0);
L36: push @out, $self->msg($create ? 'isoc' : 'iso', $call);
L37: Log('DXCommand', $self->msg($create ? 'isoc' : 'iso', $call));
L40: push @out, $self->msg('e3', "Set/Isolate", $call);
L44: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `isoari`, `isoaro`, `nodee1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/ISOLATE
```

**Isolate a node from the rest of the network**

## Details

Connect a node to your system in such a way that you are a full protocol
member of its network and can see all spots on it, but nothing either leaks
out from it nor goes back into from the rest of the nodes connected to you.

You can potentially connect several nodes in this way.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/isolate.pl){ .md-button }

## Verify on a running node

```text
HELP SET/ISOLATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.