# `SHOW/CONFIGURATION`

<div class="command-hero" markdown>

**Show all the nodes and users visible**

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
SHOW/CONFIGURATION [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXChannel::get()`, `Route::Node::get_all()`, `Route::User::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/configuration.pl` · SHA-256 `43a00f496047ea7704df605a542e12635099e2989c13e707008524f99c5f2e00`

```perl
L9: my ($self, $line) = @_;
L10: my @list = map { uc } split /\s+/, $line; # list of callsigns of nodes
L18: if ($list[0] && $list[0] =~ /^NOD/) {
L50: $printall = 1 if @list && $list[0] =~ /^ALL/i;
L55: if (@list) {
L56: next unless grep $node->call =~ /^$_/, @list;
```

### Validation and access evidence

Source: `cmd/show/configuration.pl` · SHA-256 `43a00f496047ea7704df605a542e12635099e2989c13e707008524f99c5f2e00`

```perl
L18: if ($list[0] && $list[0] =~ /^NOD/) {
L50: $printall = 1 if @list && $list[0] =~ /^ALL/i;
L56: next unless grep $node->call =~ /^$_/, @list;
```

### Output and error evidence

Source: `cmd/show/configuration.pl` · SHA-256 `43a00f496047ea7704df605a542e12635099e2989c13e707008524f99c5f2e00`

```perl
L17: push @out, $self->msg('showconf');
L35: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s %-12s", @l;
L45: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s %-12s", @l;
L73: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s %-12s", @l;
L87: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s %-12s", @l;
L93: return (1, @out);
```

### Message keys returned

`showconf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/configuration.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CONFIGURATION
```

Compare the installed handler with this page when local overrides or a different revision may be present.