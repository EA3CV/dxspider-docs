# `REJECT/WCY`

<div class="command-hero" markdown>

**set a 'reject' WCY filter**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
REJECT/WCY <arguments accepted by delegated parser>
```

## Command forms and examples

=== "Available form"

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

=== "Available form"

    ```text
    REJECT/WCY <call> [input] [0-9] <pattern>
    ```

    **WCY filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/wcy gb7djk all
    ```

## Verify on a running node

```text
HELP REJECT/WCY
```

Use the node help to check for local overrides or differences in another installed revision.