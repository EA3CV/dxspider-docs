# `ACCEPT/WWV`

<div class="command-hero" markdown>

**set an 'accept' WWV filter**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
ACCEPT/WWV <arguments accepted by delegated parser>
```

## Command forms and examples

=== "Available form"

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

=== "Available form"

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

## Verify on a running node

```text
HELP ACCEPT/WWV
```

Use the node help to check for local overrides or differences in another installed revision.