# `SET/WANTRBN`

<div class="command-hero" markdown>

**Choose which curated RBN/Skimmer categories are delivered to the user.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>RBN</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    SET/WANTRBN
    ```

    **[category ..]^Allow (some) RBN/Skimmer spots**


=== "SYSOP form"

    ```text
    SET/WANTRBN
    ```

    **<call> [category ..]^Allow (some) RBN/Skimmer spots**


## Practical examples

### Enable the default RBN selection

```text
SET/WANTRBN
```

### CW only

```text
SET/WANTRBN CW
```

### Digital categories

```text
SET/WANTRBN PSK RTTY FT
```

### Disable RBN delivery

```text
UNSET/WANTRBN
```

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/wantrbn.pl){ .md-button }

## Related commands

- [`UNSET/WANTRBN`](unset--wantrbn.md)
- [`ACCEPT/RBN`](accept--rbn.md)
- [`REJECT/RBN`](reject--rbn.md)

## Verify on a running node

```text
HELP SET/WANTRBN
```

The built-in help is useful when checking the exact command set installed on a particular node.