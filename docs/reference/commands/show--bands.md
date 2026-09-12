# `SHOW/BANDS`

<div class="command-hero" markdown>

**Show the list of bands and regions**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/BANDS [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`band`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Bands::get()`, `Bands::get_keys()`, `Bands::get_region()`, `Bands::get_region_keys()`

### Argument parsing evidence

Source: `cmd/show/bands.pl` · SHA-256 `3e04a5a0b4dd252f3f41f7f85ea51fc071ba7b6af9b372771f2e09149003481d`

```perl
L11: my $name = shift;
L12: my $ref = shift;
L13: my $level = shift || '';
L27: my ($self, $line) = @_;
L30: my @f = split m|[\s,]|, $line;
```

### Output and error evidence

Source: `cmd/show/bands.pl` · SHA-256 `3e04a5a0b4dd252f3f41f7f85ea51fc071ba7b6af9b372771f2e09149003481d`

```perl
L43: push @out, @f ? "Band:-" : "Bands Available:-";
L48: push @out, $s;
L57: push @out, $s;
L64: push @out, "Regions Available:-";
L69: push @out, $s;
L73: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/bands.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BANDS
```

Compare the installed handler with this page when local overrides or a different revision may be present.