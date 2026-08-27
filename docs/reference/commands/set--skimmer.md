# `SET/SKIMMER`

<div class="command-hero" markdown>

**[category ..]^Allow (some) RBN/Skimmer spotsT**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    SET/SKIMMER
    ```

    **[category ..]^Allow (some) RBN/Skimmer spotsT**


=== "SYSOP form"

    ```text
    SET/SKIMMER
    ```

    **<call> [category ..]^Allow (some) RBN/Skimmer spots**

    This command allows curated Reverse Beacon Spots to come out on your
    terminal (or not).

    If you want everything just type:

    ```text
     set/wantrbn
    ```
    or
    ```text
     set/skimmer
    ```

    Either command will do.

    If you want it all to just stop type:

    ```text
     unset/skimmer        (or unset/wantrbn)
    ```
    or
    ```text
     set/skimmer none
    ```

    There five categories (or modes) of RBN/Skimmer spot available and one
    can limit the spots to one or more of these categories/modes:

    ```text
     CW BEACON PSK RTTY FT
    ```

    together with a load of synonyms

    ```text
     BEACON BCN DXF
     PSK FSK MSK
     FT FT8 FT4
    ```

    if you use

    ```text
     set/skimmer psk ft8
    ```

    you will get psk, fsk, msk, ft4 and ft8 spots. if you want to break
    that down, then you will need to set filters accordingly - but your
    filter will only be offered spots from the categories that you have
    selected.

    If you get into a muddle with this you can simply reset 'all on'
    with SET/SKIMMER or 'all off' with UNSET/SKIMMER.

    By default any filters that you have for "manual" spots will be
    automatically applied to your RBN/Skimmer feed. However it is possible
    to filter RBN/Skimmer spots differently by use ACCEPT/RBN and/or
    REJECT/RBN filters.

    The RBN filters completely override any spot filters for these
    spots. But the spot filters will continue to filter "manual" spots as
    before.

    NOTE: Filters and this command CAN interact with each other. If you
    don't get the results that you expect, check your filters with
    SHOW/FILTER.

    Please see HELP RBN for an explanation of the spot format. It is NOT
    the same as one would get directly from the RBN/Skimmers. But it is
    recommended that you SET/DXCQ and UNSET/DXITU and UNSET/DXGRID (unless
    latter in more important to you with, for example, FT4/8 spots).

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Verify on a running node

```text
HELP SET/SKIMMER
```

The built-in help is useful when checking the exact command set installed on a particular node.