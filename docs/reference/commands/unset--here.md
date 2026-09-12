# `UNSET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are absent from your terminal.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Presence</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/HERE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Related commands

- [`SET/HERE`](set--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP UNSET/HERE
```

Use the node help to check for local overrides or differences in another installed revision.