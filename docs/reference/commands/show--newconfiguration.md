# `SHOW/NEWCONFIGURATION`

<div class="command-hero" markdown>

**Show the cluster map**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/NEWCONFIGURATION [USERS|<node call>]
```

**Show the cluster map**

## Details

Show the map of the whole cluster.

This shows the structure of the cluster that you are connected to. By
default it will only show the nodes that are known. By adding the keyword
USER to the command it will show all the users as well.

As there will be loops, you will see '...', this means that the information
is as printed earlier and that is a looped connection from here on.

BE WARNED: the list that is returned can be VERY long (particularly
with the USER keyword)

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/newconfiguration.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/NEWCONFIGURATION
```

The built-in help is useful when checking the exact command set installed on a particular node.