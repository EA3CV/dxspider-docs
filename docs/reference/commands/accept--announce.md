# `ACCEPT/ANNOUNCE`

<div class="command-hero" markdown>

**Set an 'accept' filter line for announce**

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
ACCEPT/ANNOUNCE <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/accept/announce.pl` · SHA-256 `c4ebf887061f03b59a560872911f6b3523653f1a62d20253ab53c8324c4f4688`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $AnnTalk::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/accept/announce.pl` · SHA-256 `c4ebf887061f03b59a560872911f6b3523653f1a62d20253ab53c8324c4f4688`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/accept/announce.pl` · SHA-256 `c4ebf887061f03b59a560872911f6b3523653f1a62d20253ab53c8324c4f4688`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    ACCEPT/ANNOUNCE [0-9] <pattern>
    ```

    **Set an 'accept' filter line for announce**

    Create an 'accept this announce' line for a filter.

    An accept filter line means that if the announce matches this filter it is
    passed onto the user. See HELP FILTERING for more info. Please read this
    to understand how filters work - it will save a lot of grief later on.

    You can use any of the following things in this line:-

    ```text
    info <string>            eg: iota or qsl
    by <prefixes>            eg: G,M,2
    origin <prefixes>
    origin_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
    origin_itu <prefixes or numbers>     or: G,GM,GW
    origin_zone <prefixes or numbers>
    origin_state <states>                eg: VA,NH,RI,NH
    by_dxcc <prefixes or numbers>
    by_itu <prefixes or numbers>
    by_zone <prefixes or numbers>
    by_state <states>
    channel <prefixes>
    wx 1                     filter WX announces
    dest <prefixes>          eg: 6MUK,WDX      (distros)
    ```

    some examples:-

    ```text
    acc/ann dest 6MUK
    acc/ann 2 by_zone 14,15,16
    (this could be all on one line: acc/ann dest 6MUK or by_zone 14,15,16)
    ```
    or
    ```text
    acc/ann by G,M,2
    ```

    for american states

    ```text
    acc/ann by_state va,nh,ri,nh
    ```

    You can use the tag 'all' to accept everything eg:

    ```text
    acc/ann all
    ```

    but this probably for advanced users...

=== "Help variant"

    ```text
    ACCEPT/ANNOUNCE <call> [input] [0-9] <pattern>
    ```

    **Announce filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    accept/ann by G,M,2
    accept/ann input node_default by G,M,2
    accept/ann user_default by G,M,2
    ```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/accept/announce.pl){ .md-button }

## Verify on a running node

```text
HELP ACCEPT/ANNOUNCE
```

Compare the installed handler with this page when local overrides or a different revision may be present.