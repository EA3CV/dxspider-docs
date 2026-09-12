# `SET/HERE`

<div class="command-hero" markdown>

**Tell DXSpider that you are present at your terminal.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Presence</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/HERE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Related commands

- [`UNSET/HERE`](unset--here.md)
- [`SHOW/CONFIGURATION`](show--configuration.md)

## Verify on a running node

```text
HELP SET/HERE
```

Use the node help to check for local overrides or differences in another installed revision.