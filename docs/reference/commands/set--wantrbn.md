# `SET/WANTRBN`

<div class="command-hero" markdown>

**Choose which curated RBN/Skimmer categories are delivered to the user.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>RBN</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/WANTRBN [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command forms and examples

=== "Available form"

    ```text
    SET/WANTRBN
    ```

    **[category ..]^Allow (some) RBN/Skimmer spots**


=== "Available form"

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

## Related commands

- [`UNSET/WANTRBN`](unset--wantrbn.md)
- [`ACCEPT/RBN`](accept--rbn.md)
- [`REJECT/RBN`](reject--rbn.md)
- [`CLEAR/RBN`](clear--rbn.md)

## Verify on a running node

```text
HELP SET/WANTRBN
```

Use the node help to check for local overrides or differences in another installed revision.