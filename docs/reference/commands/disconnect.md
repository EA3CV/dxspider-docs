# `DISCONNECT`

<div class="command-hero" markdown>

**Disconnect user(s) or node(s)**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DISCONNECT <call> [<call> ...]
```

**Disconnect user(s) or node(s)**

## Details

Disconnect any <call> connected locally.

In addition you can disconnect all users (except yourself) with

```text
DISC users
```

or all nodes with:

```text
DISC nodes
```

or everything (except yourself) with

```text
DISC all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/disconnect.pl){ .md-button }

## Verify on a running node

```text
HELP DISCONNECT
```

The built-in help is useful when checking the exact command set installed on a particular node.