# `DEBUG`

<div class="command-hero" markdown>

**Set the cluster program into debug mode**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DEBUG
```

**Set the cluster program into debug mode**

## Details

Executing this command will only have an effect if you are running the cluster
in debug mode i.e.

```text
	perl -d cluster.pl
```

It will interrupt the cluster just after the debug command has finished.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/debug.pl){ .md-button }

## Verify on a running node

```text
HELP DEBUG
```

The built-in help is useful when checking the exact command set installed on a particular node.