# `SHOW/HOPS`

<div class="command-hero" markdown>

**Show the hop counts for a node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/HOPS [token ...]
```

### Available options and values

`ann`, `route`, `spots`, `wcy`, `wwv`

The valid combinations are described in the command forms and examples below.

## Command description

```text
SHOW/HOPS <call> [ann|spots|route|wcy|wwv]
```

**Show the hop counts for a node**

## Details

This command shows the hop counts set up for a node. You can specify
which category you want to see. If you leave the category out then
all the categories will be listed.

## Verify on a running node

```text
HELP SHOW/HOPS
```

Use the node help to check for local overrides or differences in another installed revision.