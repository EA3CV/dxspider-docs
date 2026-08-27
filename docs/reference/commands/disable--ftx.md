# `DISABLE/FTX`

<div class="command-hero" markdown>

**Suppress all spots whose comment contains FT4 or FT8.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>DX spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DISABLE/FTX
```

**Disable ALL FT4/8 spots**

## When would I use this?

Use this only when you do not want FT4/FT8 spots at all. For a less aggressive option, keep FTX enabled and disable AUTOFTX instead.

## Practical examples

### Block all FT4/FT8 spots

```text
DISABLE/FTX
```

### Allow FT4/FT8 again

```text
ENABLE/FTX
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/disable/ftx.pl){ .md-button }

## Related commands

- [`ENABLE/FTX`](enable--ftx.md)
- [`DISABLE/AUTOFTX`](disable--autoftx.md)
- [`ENABLE/AUTOFTX`](enable--autoftx.md)

## Verify on a running node

```text
HELP DISABLE/FTX
```

The built-in help is useful when checking the exact command set installed on a particular node.