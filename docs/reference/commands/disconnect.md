# `DISCONNECT`

<div class="command-hero" markdown>

**Disconnect user(s) or node(s)**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DISCONNECT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
DISCONNECT <call> [<call> ...]
```

**Disconnect user(s) or node(s)**

## Details

Disconnect any <call> connected locally.

In addition you can disconnect all users (except yourself) with

```text
DISC users
```

or all nodes with:

```text
DISC nodes
```

or everything (except yourself) with

```text
DISC all
```

## Verify on a running node

```text
HELP DISCONNECT
```

Use the node help to check for local overrides or differences in another installed revision.