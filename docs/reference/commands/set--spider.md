# `SET/SPIDER`

<div class="command-hero" markdown>

**Make the callsign an DXSpider node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/SPIDER [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SET/SPIDER <call> [<call>..]
```

**Make the callsign an DXSpider node**

## Details

Tell the system that the call(s) are to be treated as DXSpider node and
fed new style DX Protocol rather normal user commands.

## Verify on a running node

```text
HELP SET/SPIDER
```

Use the node help to check for local overrides or differences in another installed revision.