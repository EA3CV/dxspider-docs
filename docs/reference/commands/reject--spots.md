# `REJECT/SPOTS`

<div class="command-hero" markdown>

**Reject DX spots that match one or more filter rules.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
REJECT/SPOTS <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.
- Reads or changes spot data.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/reject/spots.pl` · SHA-256 `fa79dfaa93a20cd145ef9dcd4448734ccceafcbdb06e260848013dbcfdbf35b8`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $Spot::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/reject/spots.pl` · SHA-256 `fa79dfaa93a20cd145ef9dcd4448734ccceafcbdb06e260848013dbcfdbf35b8`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/reject/spots.pl` · SHA-256 `fa79dfaa93a20cd145ef9dcd4448734ccceafcbdb06e260848013dbcfdbf35b8`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    REJECT/SPOTS [0-9] <pattern>
    ```

    **Set a 'reject' filter line for spots**


=== "Help variant"

    ```text
    REJECT/SPOTS <call> [input] [0-9] <pattern>
    ```

    **Spot filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/spot db0sue-7 1 by_zone 14,15,16
    reject/spot node_default all
    set/hops node_default 10
    ```

    ```text
    reject/spot user_default by G,M,2
    ```

## Practical examples

### Reject a band

```text
REJECT/SPOTS 1 ON 160M
```

### Reject selected origins

```text
REJECT/SPOTS 2 ORIGIN BADNODE1,BADNODE2
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/reject/spots.pl){ .md-button }

## Related commands

- [`ACCEPT/SPOTS`](accept--spots.md)
- [`CLEAR/SPOTS`](clear--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP REJECT/SPOTS
```

Compare the installed handler with this page when local overrides or a different revision may be present.