# `SHOW/HEADING`

<div class="command-hero" markdown>

**show the heading and distance for each callsign or prefix entered AK1A-compatible output Iain Philipps, G0RDI 16-Dec-1998 prefixes --->**

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
SHOW/HEADING [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXBearing::bdist()`, `Prefix::extract()`, `a->name()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/heading.pl` · SHA-256 `86077a7e48fedd7be4e406bd87d97dabb2020ad864c2728482861177e2bcf6fd`

```perl
L8: my ($self, $line) = @_;
L9: my @list = split /\s+/, $line; # generate a list of callsigns
L21: foreach $l (@list) {
L25: my $pre = shift @ans;
```

### Output and error evidence

Source: `cmd/show/heading.pl` · SHA-256 `86077a7e48fedd7be4e406bd87d97dabb2020ad864c2728482861177e2bcf6fd`

```perl
L16: push @out, $self->msg('heade1');
L30: push @out, sprintf "%-2s %s: %.0f degs - dist: %.0f mi, %.0f km Reciprocal heading: %.0f degs", $pre, $a->name(), $b, $dx * 0.62133785, $dx, $r;
L35: return (1, @out);
```

### Message keys returned

`heade1`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/heading.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/HEADING
```

Compare the installed handler with this page when local overrides or a different revision may be present.