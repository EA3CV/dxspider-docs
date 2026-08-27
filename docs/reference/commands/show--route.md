# `SHOW/ROUTE`

<div class="command-hero" markdown>

**Show the route to the callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/ROUTE <callsign> ...
```

**Show the route to the callsign**

## Details

This command allows you to see to which node the callsigns specified are
connected. It is a sort of inverse sh/config.

 sh/route n2tly

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/route.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/ROUTE
```

The built-in help is useful when checking the exact command set installed on a particular node.