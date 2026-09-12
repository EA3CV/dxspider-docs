# `SHOW/NODE`

<div class="command-hero" markdown>

**Show the type and version number of nodes**

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
SHOW/NODE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`Spider`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXChannel::get_all_nodes()`, `DXUser::get_current()`, `DXUser::using_database()`, `Route::Node::get()`, `dbh->prepare()`, `dbm->seq()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/node.pl` · SHA-256 `91e6fe54aab24d6fe62c86e7a85d031af68bb8215ab7a1d754c514985c3883c7`

```perl
L17: my ($self, $line) = @_;
L20: my @call = map {uc $_} split /\s+/, $line;
L29: shift @call;
```

### Validation and access evidence

Source: `cmd/show/node.pl` · SHA-256 `91e6fe54aab24d6fe62c86e7a85d031af68bb8215ab7a1d754c514985c3883c7`

```perl
L18: return (1, $self->msg('e5')) unless $self->priv >= 1;
L36: if ($d !~ m{"sort":"U"}) {
L43: if (is_callsign($key)) {
L99: return (1, @out, $self->msg('rec', $count));
```

### Output and error evidence

Source: `cmd/show/node.pl` · SHA-256 `91e6fe54aab24d6fe62c86e7a85d031af68bb8215ab7a1d754c514985c3883c7`

```perl
L18: return (1, $self->msg('e5')) unless $self->priv >= 1;
L56: push @out, $self->msg('snode1') unless @out > 0;
L68: push @out, $self->msg('snode3', $call);
L91: push @out, $self->msg('snode2', $pcall, $sort, "$ver $build");
L94: push @out, $self->msg('snode2', $pcall, $sort, $ver ? "$major\-$minor.$subs" : " ");
L99: return (1, @out, $self->msg('rec', $count));
```

### Message keys returned

`e5`, `rec`, `snode1`, `snode2`, `snode3`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/NODE [<callsign> ...]
    ```

    **Show the type and version number of nodes**


=== "Help variant"

    ```text
    SHOW/NODE ALL
    ```

    **Show the type,version number of ALL known nodes**

    Show the type and version (if connected) of the nodes specified on the
    command line. If no callsigns are specified then a sorted list of all
    the non-user callsigns connected to node will be displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/node.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/NODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.