# `REJECT/WCY`

<div class="command-hero" markdown>

**set a 'reject' WCY filter**

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
REJECT/WCY <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/reject/wcy.pl` · SHA-256 `34d771de353fc700bbdab6ab96064a9a54b6a66b30c0fa07a2739012f813951a`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $WCY::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/reject/wcy.pl` · SHA-256 `34d771de353fc700bbdab6ab96064a9a54b6a66b30c0fa07a2739012f813951a`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/reject/wcy.pl` · SHA-256 `34d771de353fc700bbdab6ab96064a9a54b6a66b30c0fa07a2739012f813951a`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    REJECT/WCY [0-9] <pattern>
    ```

    **set a 'reject' WCY filter**

    It is unlikely that you will want to do this, but if you do then you can
    filter on the following fields:-

    ```text
    by <prefixes>            eg: G,M,2
    origin <prefixes>
    origin_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
    origin_itu <prefixes or numbers>     or: G,GM,GW
    origin_zone <prefixes or numbers>
    by_dxcc <prefixes or numbers>
    by_itu <prefixes or numbers>
    by_zone <prefixes or numbers>
    channel <prefixes>
    ```

    There are no examples because WCY Broadcasts only come from one place and
    you either want them or not (see UNSET/WCY if you don't want them).

    This command is really provided for future use.

    See HELP FILTER for information.

=== "Help variant"

    ```text
    REJECT/WCY <call> [input] [0-9] <pattern>
    ```

    **WCY filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/wcy gb7djk all
    ```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/reject/wcy.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/WCY
```

Compare the installed handler with this page when local overrides or a different revision may be present.