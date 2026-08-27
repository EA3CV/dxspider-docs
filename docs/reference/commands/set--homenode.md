# `SET/HOMENODE`

<div class="command-hero" markdown>

**Set your normal cluster callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/HOMENODE <node>
```

**Set your normal cluster callsign**

## Details

Tell the cluster system where you normally connect to. Any Messages sent
to you will normally find their way there should you not be connected.
eg:-
```text
SET/HOMENODE gb7djk
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/homenode.pl){ .md-button }

## Verify on a running node

```text
HELP SET/HOMENODE
```

The built-in help is useful when checking the exact command set installed on a particular node.