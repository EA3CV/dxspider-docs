# `LOAD/BANDS`

<div class="command-hero" markdown>

**Reload the band limits table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/BANDS
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
LOAD/BANDS
```

**Reload the band limits table**

## Details

Reload the /spider/data/bands.pl file if you have changed it manually whilst
the cluster is running.

## Verify on a running node

```text
HELP LOAD/BANDS
```

Use the node help to check for local overrides or differences in another installed revision.