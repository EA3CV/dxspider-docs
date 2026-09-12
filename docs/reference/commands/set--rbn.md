# `SET/RBN`

<div class="command-hero" markdown>

**Mark this call as an RBN node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/RBN [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Verify on a running node

```text
HELP SET/RBN
```

Use the node help to check for local overrides or differences in another installed revision.