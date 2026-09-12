# `SET/NODE`

<div class="command-hero" markdown>

**Make the callsign an AK1A cluster**

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
SET/NODE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser->new()`, `DXUser::get()`, `self->msg()`, `user->homenode()`, `user->lockout()`, `user->priv()`, `user->put()`, `user->sort()`

### Argument parsing evidence

Source: `cmd/set/node.pl` · SHA-256 `306df3c1ed26f4158961b6f675047825e1f0b862f40dddae0c9b0a914e6e6871`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/node.pl` · SHA-256 `306df3c1ed26f4158961b6f675047825e1f0b862f40dddae0c9b0a914e6e6871`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L41: $user->priv(1) unless $user->priv;
```

### Output and error evidence

Source: `cmd/set/node.pl` · SHA-256 `306df3c1ed26f4158961b6f675047825e1f0b862f40dddae0c9b0a914e6e6871`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L23: push @out, $self->msg('e11', $call);
L27: push @out, $self->msg('e11', $call);
L32: push @out, $self->msg('nodee1', $call);
L43: push @out, $self->msg($create ? 'nodeac' : 'nodea', $call);
L45: push @out, $self->msg('e3', "Set Node", $call);
L49: return (1, @out);
```

### Message keys returned

`e11`, `e3`, `e5`, `nodee1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/NODE <call> [<call>..]
```

**Make the callsign an AK1A cluster**

## Details

Tell the system that the call(s) are to be treated as AK1A cluster and
fed PC Protocol rather normal user commands.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/node.pl){ .md-button }

## Verify on a running node

```text
HELP SET/NODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.