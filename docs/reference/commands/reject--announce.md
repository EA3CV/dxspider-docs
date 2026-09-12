# `REJECT/ANNOUNCE`

<div class="command-hero" markdown>

**Set a 'reject' filter line for announce**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
REJECT/ANNOUNCE <arguments accepted by delegated parser>
```

## Command forms and examples

=== "Available form"

    ```text
    REJECT/ANNOUNCE [0-9] <pattern>
    ```

    **Set a 'reject' filter line for announce**

    Create an 'reject this announce' line for a filter.

    A reject filter line means that if the announce matches this filter it is
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
    origin_state <states>                eg: VA,NH,RI,ME
    by_dxcc <prefixes or numbers>
    by_itu <prefixes or numbers>
    by_zone <prefixes or numbers>
    by_state <states>                eg: VA,NH,RI,ME
    channel <prefixes>
    wx 1                     filter WX announces
    dest <prefixes>          eg: 6MUK,WDX      (distros)
    ```

    some examples:-

    ```text
    rej/ann by_zone 14,15,16 and not by G,M,2
    ```

    You can use the tag 'all' to reject everything eg:

    ```text
    rej/ann all
    ```

    but this probably for advanced users...

=== "Available form"

    ```text
    REJECT/ANNOUNCE <call> [input] [0-9] <pattern>
    ```

    **Announce filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/ann by G,M,2
    reject/ann input node_default by G,M,2
    reject/ann user_default by G,M,2
    ```

## Verify on a running node

```text
HELP REJECT/ANNOUNCE
```

Use the node help to check for local overrides or differences in another installed revision.