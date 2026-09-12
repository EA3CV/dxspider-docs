# `REJECT/SPOTS`

<div class="command-hero" markdown>

**Reject DX spots that match one or more filter rules.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
REJECT/SPOTS <arguments accepted by delegated parser>
```

## Command forms and examples

=== "Available form"

    ```text
    REJECT/SPOTS [0-9] <pattern>
    ```

    **Set a 'reject' filter line for spots**


=== "Available form"

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

## Related commands

- [`ACCEPT/SPOTS`](accept--spots.md)
- [`CLEAR/SPOTS`](clear--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP REJECT/SPOTS
```

Use the node help to check for local overrides or differences in another installed revision.