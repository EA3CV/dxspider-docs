# `SHOW/FDX`

<div class="command-hero" markdown>

**Show the DX data in realtime format.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/FDX
```

**Show the DX data in realtime format.**

## Details

Normally SHOW/DX outputs spot data in a different format to the
realtime data. This is a deliberate policy (so you can tell the
difference between the two). Some logging programs cannot handle
this so SHOW/FDX outputs historical data in real time format.

This is an alias for: SHOW/DX real

## Verify on a running node

```text
HELP SHOW/FDX
```

The built-in help is useful when checking the exact command set installed on a particular node.