# `UNSET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are absent from your terminal.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Presence</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/HERE
```

**Tell the system you are absent from your terminal**

## When would I use this?

This is the opposite of SET/HERE. It marks your session as away without disconnecting you.

## Practical examples

### Mark yourself away

```text
UNSET/HERE
```

### Mark yourself present again

```text
SET/HERE
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/here.pl){ .md-button }

## Related commands

- [`SET/HERE`](set--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP UNSET/HERE
```

The built-in help is useful when checking the exact command set installed on a particular node.