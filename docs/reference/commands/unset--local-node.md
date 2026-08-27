# `UNSET/LOCAL_NODE`

<div class="command-hero" markdown>

**Remove node from the local_node group**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/local_node.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/LOCAL_NODE
```

The built-in help is useful when checking the exact command set installed on a particular node.