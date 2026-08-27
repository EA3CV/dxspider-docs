# `SHOW/MYDX`

<div class="command-hero" markdown>

**Search the spot database after applying your personal spot filter.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>DX spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/MYDX
```

**Show the DX data filtered with your spot filter.**

## Details

SHOW/DX potentially shows all the spots available in the system. Using
SHOW/MYDX will, instead, filter the availble spots using any spot filter
that you have set, first.

This command, together with ACCEPT/SPOT or REJECT/SPOT, will allow
you to customise the spots that you receive.

So if you have said: ACC/SPOT on hf

Doing a SHOW/MYDX will now only, ever, show HF spots. All the other
options on SH/DX can still be used.

## When would I use this?

Use SHOW/MYDX when you want historical/query results to follow the same spot-selection rules you configured for incoming spots.

## Practical examples

### Create an HF-only personal filter

```text
ACCEPT/SPOTS 1 ON HF
```

### Query using that filter

```text
SHOW/MYDX
```

### Add the normal SHOW/DX selectors

```text
SHOW/MYDX ON 20M INFO IOTA
```

## Related commands

- [`SHOW/DX`](show--dx.md)
- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)
- [`CLEAR/SPOTS`](clear--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP SHOW/MYDX
```

The built-in help is useful when checking the exact command set installed on a particular node.