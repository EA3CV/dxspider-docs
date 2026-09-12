# `SHOW/HOPS`

<div class="command-hero" markdown>

**Show the hop counts for a node**

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
SHOW/HOPS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Recognized tokens, keys or enumerated values in this handler

`ann`, `route`, `spots`, `wcy`, `wwv`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Filter::read_in()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/hops.pl` · SHA-256 `3935b76effd4ca4a86a0eeb32439e042c5243ef5e24551f7383c14ab5abb49c1`

```perl
L8: my ($self, $line) = @_;
L9: my @f = split /\s+/, $line;
L15: $call = uc shift @f;
L17: $call = shift @f;
```

### Validation and access evidence

Source: `cmd/show/hops.pl` · SHA-256 `3935b76effd4ca4a86a0eeb32439e042c5243ef5e24551f7383c14ab5abb49c1`

```perl
L13: if (@f && $self->priv >= 8) {
L14: if (is_callsign(uc $f[0])) {
```

### Output and error evidence

Source: `cmd/show/hops.pl` · SHA-256 `3935b76effd4ca4a86a0eeb32439e042c5243ef5e24551f7383c14ab5abb49c1`

```perl
L32: push @out, $self->msg('sethop2', $hops, '', $sort, $call) if $hops;
L34: push @out, $self->msg('sethop3', $call) unless @out;
L35: return (1, @out);
```

### Message keys returned

`sethop2`, `sethop3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/HOPS <call> [ann|spots|route|wcy|wwv]
```

**Show the hop counts for a node**

## Details

This command shows the hop counts set up for a node. You can specify
which category you want to see. If you leave the category out then
all the categories will be listed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/hops.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/HOPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.