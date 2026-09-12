# `ACCEPT/WWV`

<div class="command-hero" markdown>

**set an 'accept' WWV filter**

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
ACCEPT/WWV <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/accept/wwv.pl` · SHA-256 `b6587ec8a7145212ef36e232238dd99d36489a8bd5b7596bb25c107cf57f257e`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $Geomag::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/accept/wwv.pl` · SHA-256 `b6587ec8a7145212ef36e232238dd99d36489a8bd5b7596bb25c107cf57f257e`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/accept/wwv.pl` · SHA-256 `b6587ec8a7145212ef36e232238dd99d36489a8bd5b7596bb25c107cf57f257e`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    ACCEPT/WWV [0-9] <pattern>
    ```

    **set an 'accept' WWV filter**

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

    for example

    ```text
    accept/wwv by_zone 4
    ```

    is probably the only useful thing to do (which will only show WWV broadcasts
    by stations in the US).

    See HELP FILTER for information.

=== "Help variant"

    ```text
    ACCEPT/WWV <call> [input] [0-9] <pattern>
    ```

    **WWV filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    accept/wwv db0sue-7 1 by_zone 4
    accept/wwv node_default all
    set/hops node_default 10
    ```

    ```text
    accept/wwv user_default by W,K
    ```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/accept/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP ACCEPT/WWV
```

Compare the installed handler with this page when local overrides or a different revision may be present.