# `SHOW/CONFIGURATION`

<div class="command-hero" markdown>

**Show all the nodes and users visible**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/CONFIGURATION [<node>]
```

**Show all the nodes and users visible**

## Details

This command allows you to see all the users that can be seen
and the nodes to which they are connected.

This command is normally abbreviated to: sh/c

Normally, the list returned will be just for the nodes from your
country (because the list otherwise will be very long).

```text
SH/C ALL
```

will produce a complete list of all nodes.

BE WARNED: the list that is returned can be VERY long

It is possible to supply a node or part of a prefix and you will get
a list of the users for that node or list of nodes starting with
that prefix.

```text
SH/C GB7DJK
```

```text
SH/C SK
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/configuration.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CONFIGURATION
```

The built-in help is useful when checking the exact command set installed on a particular node.