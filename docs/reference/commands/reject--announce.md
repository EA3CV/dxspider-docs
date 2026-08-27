# `REJECT/ANNOUNCE`

<div class="command-hero" markdown>

**Set a 'reject' filter line for announce**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

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

=== "SYSOP form"

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

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reject/announce.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/ANNOUNCE
```

The built-in help is useful when checking the exact command set installed on a particular node.