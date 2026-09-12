# `SEND_CONFIG`

<div class="command-hero" markdown>

**Broadcast PC92 C records**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SEND_CONFIG
```

## Command description

```text
SEND_CONFIG
```

**Broadcast PC92 C records**

## Details

This is the PC92 equivalent of INIT. In that it will send out a new
PC92 C record to all interfaces. This can be used to bring other nodes
up to date quicker after a restart.

## Verify on a running node

```text
HELP SEND_CONFIG
```

Use the node help to check for local overrides or differences in another installed revision.