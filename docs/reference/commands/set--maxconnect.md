# `SET/MAXCONNECT`

<div class="command-hero" markdown>

**Set max incoming connections for user/node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/MAXCONNECT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SET/MAXCONNECT <value> [<call> ..]
```

**Set max incoming connections for user/node**

## Details

Set the maximum no of connections (parents) an incoming user or node is
allowed to have. If this incoming connection takes it over the separate
limits for users and nodes (defaults: 3 and 8 respectively), then the
connection is refused (with a polite message).

The idea behind this to limit the number of copies of messages that
are sent to users (and nodes). Nodes really don't need to have more than
5 or 6 partners and users don't need more than two connections into the
cluster cloud.

This check is only for INCOMING connections, no check is performed for
outgoing connections.

## Verify on a running node

```text
HELP SET/MAXCONNECT
```

Use the node help to check for local overrides or differences in another installed revision.