# `UNSET/LOCAL_NODE`

<div class="command-hero" markdown>

**Remove node from the local_node group**

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
UNSET/LOCAL_NODE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXChannel::get()`, `DXUser::get_current()`, `dxchan->group()`, `self->msg()`, `user->group()`

### Argument parsing evidence

Source: `cmd/unset/local_node.pl` · SHA-256 `64ecd7f47b5675630adaf28cbc12668f86e943083841c5f416c576c48f65c5b9`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L15: foreach my $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/local_node.pl` · SHA-256 `64ecd7f47b5675630adaf28cbc12668f86e943083841c5f416c576c48f65c5b9`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 5;
```

### Output and error evidence

Source: `cmd/unset/local_node.pl` · SHA-256 `64ecd7f47b5675630adaf28cbc12668f86e943083841c5f416c576c48f65c5b9`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 5;
L17: push(@out, $self->msg('e3', 'set/localnode', $call)), next unless $user;
L18: push(@out, $self->msg('e13', $call)), next unless $user->is_node;
L24: push @out, $self->msg('lgunset', $call);
L28: return (1, @out);
```

### Message keys returned

`e13`, `e3`, `e5`, `lgunset`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/LOCAL_NODE
```

**Remove node from the local_node group**

## Details

The 'local_node' group is a group of nodes that you want a user
to perceive as effectively one big node. At the moment, this extends
only to announcing whenever a user is logging in or out of one of
the nodes in the group (if those users have SET/LOGININFO).

The local node group is as setup on this node. If you want the other
nodes to also include this node and all the other nodes specified, then
you must get those nodes to also run this command (or rcmd them to do
so).

In principle, therefore, each node determines its own local node group
and these can overlap with other nodes' views.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/local_node.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/LOCAL_NODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.