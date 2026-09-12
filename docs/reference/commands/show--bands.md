# `SHOW/BANDS`

<div class="command-hero" markdown>

**Show the list of bands and regions**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/BANDS [arguments; see parser evidence]
```

### Available options and values

`band`

The valid combinations are described in the command forms and examples below.

## Command description

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

## Verify on a running node

```text
HELP SHOW/BANDS
```

Use the node help to check for local overrides or differences in another installed revision.