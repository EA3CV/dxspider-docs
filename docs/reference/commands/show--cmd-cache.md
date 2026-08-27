# `SHOW/CMD_CACHE`

<div class="command-hero" markdown>

**Show the real source path of commands**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/CMD_CACHE [pattern]
```

**Show the real source path of commands**

## Details

It is possible in DXSpider to define local versions of commands.
Sometimes one forgets that one has these. This command will show you
the source path where the node is getting each one of its commands.

If you find a local command that you don't want then then simply
delete it, run LOAD/CMD_CACHE to clear out the command cache and
try again. You will now be using the standard version.

If you are looking for information on a specific command then
just add a string, eg:

```text
sh/cmd dx
```

might give you:

```text
Command              Path
set/dxgrid           /spider/cmd/set/dxgrid.pl
sh/dx                /spider/cmd/show/dx.pl
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/cmd_cache.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CMD_CACHE
```

The built-in help is useful when checking the exact command set installed on a particular node.