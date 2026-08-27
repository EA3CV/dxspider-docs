# `SET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are present at your terminal.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Presence</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/HERE
```

**Tell the system you are present at your terminal**

## When would I use this?

Use this when you want your current session to advertise that you are actively present rather than away.

## Practical examples

### Mark yourself present

```text
SET/HERE
```

### Later, mark yourself away

```text
UNSET/HERE
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/here.pl){ .md-button }

## Related commands

- [`UNSET/HERE`](unset--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP SET/HERE
```

The built-in help is useful when checking the exact command set installed on a particular node.