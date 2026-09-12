# `SET/ISOLATE`

<div class="command-hero" markdown>

**Isolate a node from the rest of the network**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/ISOLATE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SET/ISOLATE
```

**Isolate a node from the rest of the network**

## Details

Connect a node to your system in such a way that you are a full protocol
member of its network and can see all spots on it, but nothing either leaks
out from it nor goes back into from the rest of the nodes connected to you.

You can potentially connect several nodes in this way.

## Verify on a running node

```text
HELP SET/ISOLATE
```

Use the node help to check for local overrides or differences in another installed revision.