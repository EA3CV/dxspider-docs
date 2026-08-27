# `ACCEPT/SPOTS`

<div class="command-hero" markdown>

**Allow only DX spots that match one or more filter rules.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    ACCEPT/SPOTS [0-9] <pattern>
    ```

    **Set an 'accept' filter line for spots**


=== "SYSOP form"

    ```text
    ACCEPT/SPOTS <call> [input] [0-9] <pattern>
    ```

    **Spot filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    accept/spot db0sue-7 1 by_zone 14,15,16
    accept/spot node_default all
    set/hops node_default 10
    ```

    ```text
    accept/spot user_default by G,M,2
    ```

## Practical examples

### Accept CW spots on HF

```text
ACCEPT/SPOTS 1 ON HF/CW
```

### Accept VHF spots from or for CQ zones 14–16

```text
ACCEPT/SPOTS 2 ON VHF AND (BY_ZONE 14,15,16 OR CALL_ZONE 14,15,16)
```

### Accept spots reported by US states

```text
ACCEPT/SPOTS BY_STATE VA,NH,RI,MA,ME
```

### Accept everything

```text
ACCEPT/SPOTS 3 ALL
```

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/accept/spots.pl){ .md-button }

## Related commands

- [`REJECT/SPOTS`](reject--spots.md)
- [`CLEAR/SPOTS`](clear--spots.md)
- [`SHOW/FILTER`](show--filter.md)
- [`SHOW/BANDS`](show--bands.md)

## Verify on a running node

```text
HELP ACCEPT/SPOTS
```

The built-in help is useful when checking the exact command set installed on a particular node.