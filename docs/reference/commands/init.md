# `INIT`

<div class="command-hero" markdown>

**Re-initialise a link to an AK1A compatible node**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
INIT <node>
```

**Re-initialise a link to an AK1A compatible node**

## Details

This command attempts to re-initialise a link to a (usually) AK1A node
that has got confused, usually by a protocol loop of some kind. It may
work - but you usually will be better off simply disconnecting it (or
better, if it is a real AK1A node, doing an RCMD <node> DISC/F <your
node>).

Best of luck - you will need it.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/init.pl){ .md-button }

## Verify on a running node

```text
HELP INIT
```

The built-in help is useful when checking the exact command set installed on a particular node.