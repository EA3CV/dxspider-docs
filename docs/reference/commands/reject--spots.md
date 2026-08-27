# `REJECT/SPOTS`

<div class="command-hero" markdown>

**Reject DX spots that match one or more filter rules.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    REJECT/SPOTS [0-9] <pattern>
    ```

    **Set a 'reject' filter line for spots**


=== "SYSOP form"

    ```text
    REJECT/SPOTS <call> [input] [0-9] <pattern>
    ```

    **Spot filter sysop version**

    This version allows a sysop to set a filter for a callsign as well as the
    default for nodes and users eg:-

    ```text
    reject/spot db0sue-7 1 by_zone 14,15,16
    reject/spot node_default all
    set/hops node_default 10
    ```

    ```text
    reject/spot user_default by G,M,2
    ```

## Practical examples

### Reject a band

```text
REJECT/SPOTS 1 ON 160M
```

### Reject selected origins

```text
REJECT/SPOTS 2 ORIGIN BADNODE1,BADNODE2
```

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reject/spots.pl){ .md-button }

## Related commands

- [`ACCEPT/SPOTS`](accept--spots.md)
- [`CLEAR/SPOTS`](clear--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP REJECT/SPOTS
```

The built-in help is useful when checking the exact command set installed on a particular node.