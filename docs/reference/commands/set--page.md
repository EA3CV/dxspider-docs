# `SET/PAGE`

<div class="command-hero" markdown>

**Set the lines per page**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/PAGE
```

## Command description

```text
SET/PAGE <lines per page>
```

**Set the lines per page**

## Details

Tell the system how many lines you wish on a page when the number of line
of output from a command is more than this. The default is 20. Setting it
explicitly to 0 will disable paging.
```text
SET/PAGE 30
SET/PAGE 0
```

The setting is stored in your user profile.

## Verify on a running node

```text
HELP SET/PAGE
```

Use the node help to check for local overrides or differences in another installed revision.