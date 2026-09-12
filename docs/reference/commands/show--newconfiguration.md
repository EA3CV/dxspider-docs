# `SHOW/NEWCONFIGURATION`

<div class="command-hero" markdown>

**Show the cluster map**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/NEWCONFIGURATION [token ...]
```

## Command description

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

## Verify on a running node

```text
HELP SHOW/NEWCONFIGURATION
```

Use the node help to check for local overrides or differences in another installed revision.