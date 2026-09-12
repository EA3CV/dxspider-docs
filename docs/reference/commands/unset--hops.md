# `UNSET/HOPS`

<div class="command-hero" markdown>

**Unset hop count**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/HOPS [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
UNSET/HOPS <call> ann|spots|route|wwv|wcy
```

**Unset hop count**

## Details

Set the hop count for a particular type of broadcast for a node.

This command allows you to set up special hop counts for a node
for currently: announce, spots, wwv and wcy broadcasts.

eg:
```text
set/hops gb7djk ann 10
set/hops gb7mbc spots 20
```

Set SHOW/HOPS for information on what is already set. This command
creates a filter and works in conjunction with the filter system.

You can unset the hops with command UNSET/HOPS. For example:-

```text
unset/hops gb7djk ann
unset/hops gb7mbc spots
```

## Verify on a running node

```text
HELP UNSET/HOPS
```

Use the node help to check for local overrides or differences in another installed revision.