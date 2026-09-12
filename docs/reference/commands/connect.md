# `CONNECT`

<div class="command-hero" markdown>

**Start a connection to another DX Cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
CONNECT
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
CONNECT <callsign>
```

**Start a connection to another DX Cluster**

## Details

Start a connection process that will culminate in a new connection to the
DX cluster <callsign>. This process creates a new 'client' process which will
use the script in /spider/connect/<callsign> to effect the 'chat' exchange
necessary to traverse the network(s) to logon to the cluster <callsign>.

## Verify on a running node

```text
HELP CONNECT
```

Use the node help to check for local overrides or differences in another installed revision.