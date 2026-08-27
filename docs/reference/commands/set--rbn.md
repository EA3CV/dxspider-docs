# `SET/RBN`

<div class="command-hero" markdown>

**Mark this call as an RBN node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/RBN <call> ...
```

**Mark this call as an RBN node**

## Details

This will mark this callsign as a Reverse Beacon
Network client. It's not a node in the normal sense of that word
in DXSpider. But it will generate spots from the RBN/Skimmers and
will act like a specialised node just for RBN spots.

You will need to use this command to create your skimmer node
connections. Normally one per RBN port (7000, 7001) but, in principle
you could connect to any skimmer that uses the same spot format.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP SET/RBN
```

The built-in help is useful when checking the exact command set installed on a particular node.