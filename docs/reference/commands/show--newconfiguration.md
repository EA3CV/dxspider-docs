# `SHOW/NEWCONFIGURATION`

<div class="command-hero" markdown>

**Show the cluster map**

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
SHOW/NEWCONFIGURATION [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`routeroot->config()`

### Argument parsing evidence

Source: `cmd/show/newconfiguration.pl` · SHA-256 `71784d7fa136316e373a7259c1ea9667f1e735872505b426bced4343fe520b91`

```perl
L9: my ($self, $line) = @_;
L10: my @list = map { uc } split /\s+/, $line; # list of callsigns of nodes
L14: if (@list && $list[0] =~ /^USE/) {
L16: shift @list;
L19: push @out, $main::routeroot->config($nodes_only, $self->width, 0, {}, @list);
```

### Validation and access evidence

Source: `cmd/show/newconfiguration.pl` · SHA-256 `71784d7fa136316e373a7259c1ea9667f1e735872505b426bced4343fe520b91`

```perl
L14: if (@list && $list[0] =~ /^USE/) {
```

### Output and error evidence

Source: `cmd/show/newconfiguration.pl` · SHA-256 `71784d7fa136316e373a7259c1ea9667f1e735872505b426bced4343fe520b91`

```perl
L19: push @out, $main::routeroot->config($nodes_only, $self->width, 0, {}, @list);
L20: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/newconfiguration.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/NEWCONFIGURATION
```

Compare the installed handler with this page when local overrides or a different revision may be present.