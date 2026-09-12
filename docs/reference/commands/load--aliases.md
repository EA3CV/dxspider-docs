# `LOAD/ALIASES`

<div class="command-hero" markdown>

**Reload the command alias table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/ALIASES
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
LOAD/ALIASES
```

**Reload the command alias table**

## Details

Reload the /spider/cmd/Aliases file after you have editted it. You
will need to do this if you change this file whilst the cluster is
running in order for the changes to take effect.

## Verify on a running node

```text
HELP LOAD/ALIASES
```

Use the node help to check for local overrides or differences in another installed revision.