# `SET/PAGE`

<div class="command-hero" markdown>

**Set the lines per page**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/page.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PAGE
```

The built-in help is useful when checking the exact command set installed on a particular node.