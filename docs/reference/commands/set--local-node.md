# `SET/LOCAL_NODE`

<div class="command-hero" markdown>

**Add node to the local_node group**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SET/LOCAL_NODE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`local_node`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXChannel::get()`, `DXUser::get_current()`, `dxchan->group()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/local_node.pl` · SHA-256 `e0a478eb18dadabaeeab6abed40ff0a2b690357ef3d804a58a1bb3eba98fd352`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L15: foreach my $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/local_node.pl` · SHA-256 `e0a478eb18dadabaeeab6abed40ff0a2b690357ef3d804a58a1bb3eba98fd352`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 5;
```

### Output and error evidence

Source: `cmd/set/local_node.pl` · SHA-256 `e0a478eb18dadabaeeab6abed40ff0a2b690357ef3d804a58a1bb3eba98fd352`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 5;
L17: push(@out, $self->msg('e3', 'set/localnode', $call)), next unless $user;
L18: push(@out, $self->msg('e13', $call)), next unless $user->is_node;
L23: push @out, $self->msg('lgset', $call);
L27: return (1, @out);
```

### Message keys returned

`e13`, `e3`, `e5`, `lgset`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/LOCAL_NODE
```

**Add node to the local_node group**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/local_node.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LOCAL_NODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.