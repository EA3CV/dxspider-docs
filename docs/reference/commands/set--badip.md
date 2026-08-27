# `SET/BADIP`

<div class="command-hero" markdown>

**Stop logins and spots with this IP address**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/BADIP <ip address>..
```

**Stop logins and spots with this IP address**

## Details

This command will prevent logins to this node from this IP address.
It will also drop spots (PC61) from this address thus preventing them
from being propagated.

```text
set/badip 217.61.58.23
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/badip.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BADIP
```

The built-in help is useful when checking the exact command set installed on a particular node.