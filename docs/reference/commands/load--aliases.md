# `LOAD/ALIASES`

<div class="command-hero" markdown>

**Reload the command alias table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
LOAD/ALIASES
```

**Reload the command alias table**

## Details

Reload the /spider/cmd/Aliases file after you have editted it. You
will need to do this if you change this file whilst the cluster is
running in order for the changes to take effect.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/aliases.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/ALIASES
```

The built-in help is useful when checking the exact command set installed on a particular node.