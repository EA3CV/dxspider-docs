# `SET/ISOLATE`

<div class="command-hero" markdown>

**Isolate a node from the rest of the network**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/ISOLATE
```

**Isolate a node from the rest of the network**

## Details

Connect a node to your system in such a way that you are a full protocol
member of its network and can see all spots on it, but nothing either leaks
out from it nor goes back into from the rest of the nodes connected to you.

You can potentially connect several nodes in this way.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/isolate.pl){ .md-button }

## Verify on a running node

```text
HELP SET/ISOLATE
```

The built-in help is useful when checking the exact command set installed on a particular node.