# `REJECT/RBN`

<div class="command-hero" markdown>

**Set a 'reject' filter line for RBN spots**

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
REJECT/RBN <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/reject/rbn.pl` · SHA-256 `50723f5af3652f62953a856454be6e53f88da3ae5983b8a33d51d08fc87db25d`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $RBN::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/reject/rbn.pl` · SHA-256 `50723f5af3652f62953a856454be6e53f88da3ae5983b8a33d51d08fc87db25d`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/reject/rbn.pl` · SHA-256 `50723f5af3652f62953a856454be6e53f88da3ae5983b8a33d51d08fc87db25d`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
REJECT/RBN [0-9] <pattern>
```

**Set a 'reject' filter line for RBN spots**

## Details

Create a 'reject this spot' line for a filter.

A reject filter line means that if the spot matches this filter it is
dumped (not passed on). See HELP FILTERING for more info. Please read this
to understand how filters work - it will save a lot of grief later on.

You can use any of the following things in this line:-

```text
freq <range>           eg: 0/30000 or hf or hf/cw or 6m,4m,2m
on <range>             same as 'freq'
call <prefixes>        eg: G,PA,HB9
info <string>          eg: iota or qsl
by <prefixes>
call_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
call_itu <prefixes or numbers>     or: G,GM,GW
call_zone <prefixes or numbers>
call_state <states>                eg: VA,NH,RI,ME
by_dxcc <prefixes or numbers>
by_itu <prefixes or numbers>
by_zone <prefixes or numbers>
by_state <states>                eg: VA,NH,RI,ME
origin <prefixes>
channel <prefixes>
```

'call' means the callsign that has spotted 'by' whoever.

For frequencies, you can use any of the band names defined in
SHOW/BANDS and you can use a subband name like: cw, rtty, data, ssb -
thus: hf/ssb. You can also just have a simple range like: 0/30000 -
this is more efficient than saying simply: on HF (but don't get
too hung up about that)

some examples:-

```text
rej/spot 1 on hf
rej/spot 2 on vhf and not (by_zone 14,15,16 or call_zone 14,15,16)
```

You can use the tag 'all' to reject everything eg:

```text
rej/spot 3 all
```

but this probably for advanced users...

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/reject/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/RBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.