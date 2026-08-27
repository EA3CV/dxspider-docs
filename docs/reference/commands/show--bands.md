# `SHOW/BANDS`

<div class="command-hero" markdown>

**Show the list of bands and regions**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/BANDS [band|region names]
```

**Show the list of bands and regions**

## Details

Display the bands and regions (collections of bands) known to
the system. If you supply band or region names to SHOW/BANDS,
the command will display just those bands or regions, e.g.:

```text
	sh/bands
	sh/bands 2m
	sh/bands hf
```

If you specify one or more specific bands then you will get a list of
sub bands as well as the extent of that band.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/bands.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BANDS
```

The built-in help is useful when checking the exact command set installed on a particular node.