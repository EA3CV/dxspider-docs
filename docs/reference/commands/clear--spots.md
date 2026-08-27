# `CLEAR/SPOTS`

<div class="command-hero" markdown>

**Remove one line or the complete DX spot filter.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    CLEAR/SPOTS [0-9|all]
    ```

    **Clear a spot filter line**

    This command allows you to clear (remove) a line in a spot filter or to
    remove the whole filter.

    If you have a filter:-

    ```text
    acc/spot 1 on hf/cw
    acc/spot 2 on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
    ```

    and you say:-

    ```text
    clear/spot 1
    ```

    you will be left with:-

    ```text
    acc/spot 2 on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
    ```

    If you do:

    ```text
    clear/spot all
    ```

    the filter will be completely removed.

=== "SYSOP form"

    ```text
    CLEAR/SPOTS <callsign> [input] [0-9|all]
    ```

    **Clear a spot filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

## Practical examples

### Remove line 1

```text
CLEAR/SPOTS 1
```

### Remove the complete filter

```text
CLEAR/SPOTS ALL
```

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/clear/spots.pl){ .md-button }

## Related commands

- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP CLEAR/SPOTS
```

The built-in help is useful when checking the exact command set installed on a particular node.