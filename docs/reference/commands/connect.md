# `CONNECT`

<div class="command-hero" markdown>

**Start a connection to another DX Cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
CONNECT <callsign>
```

**Start a connection to another DX Cluster**

## Details

Start a connection process that will culminate in a new connection to the
DX cluster <callsign>. This process creates a new 'client' process which will
use the script in /spider/connect/<callsign> to effect the 'chat' exchange
necessary to traverse the network(s) to logon to the cluster <callsign>.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/connect.pl){ .md-button }

## Verify on a running node

```text
HELP CONNECT
```

The built-in help is useful when checking the exact command set installed on a particular node.