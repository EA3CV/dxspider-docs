# `ENABLE/FTX`

<div class="command-hero" markdown>

**Enable ALL FT4/8 Spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
ENABLE/FTX
```

**Enable ALL FT4/8 Spots**

## Details

If disabled, stops ALL spots with "FT4" or "FT8" in the comment string.

NOTE: if enabled, with disable/autoftx command means that you STILL
get all non-automated FT4/8 spots.

Default is enabled.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/enable/ftx.pl){ .md-button }

## Verify on a running node

```text
HELP ENABLE/FTX
```

The built-in help is useful when checking the exact command set installed on a particular node.