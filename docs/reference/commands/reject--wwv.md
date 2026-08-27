# `REJECT/WWV`

<div class="command-hero" markdown>

**set a 'reject' WWV filter**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    REJECT/WWV [0-9] <pattern>
    ```

    **set a 'reject' WWV filter**

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
    reject/wwv by_zone 14,15,16
    ```

    is probably the only useful thing to do (which will only show WWV broadcasts
    by stations in the US).

    See HELP FILTER for information.

=== "SYSOP form"

    ```text
    REJECT/WWV <call> [input] [0-9] <pattern>
    ```

    **WWV filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/wwv db0sue-7 1 by_zone 4
    reject/wwv node_default all
    ```

    ```text
    reject/wwv user_default by W
    ```

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reject/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/WWV
```

The built-in help is useful when checking the exact command set installed on a particular node.