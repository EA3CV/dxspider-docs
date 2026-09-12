# `ACCEPT/RBN`

<div class="command-hero" markdown>

**Apply an accept filter specifically to RBN/Skimmer spots.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>RBN / Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
ACCEPT/RBN <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/accept/rbn.pl` · SHA-256 `55becc759734314ac219870204b1aed9805308141056fff5affd4e97cae1af19`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $RBN::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/accept/rbn.pl` · SHA-256 `55becc759734314ac219870204b1aed9805308141056fff5affd4e97cae1af19`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/accept/rbn.pl` · SHA-256 `55becc759734314ac219870204b1aed9805308141056fff5affd4e97cae1af19`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
ACCEPT/RBN [0-9] <pattern>
```

**Set an 'accept' filter line for RBN spots**

## Details

Create an 'accept this spot' line for a filter.

An accept filter line means that if the spot matches this filter it is
passed onto the user. See HELP FILTERING for more info. Please read this
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
this is more efficient than saying simply: freq HF (but don't get
too hung up about that)

some examples:-

```text
acc/spot 1 on hf/cw
acc/spot 2 on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
```

You can use the tag 'all' to accept everything, eg:

```text
acc/spot 3 all
```

for US states

```text
acc/spots by_state VA,NH,RI,MA,ME
```

but this probably for advanced users...

## Practical examples

### Accept HF CW RBN spots

```text
ACCEPT/RBN 1 ON HF/CW
```

### Accept RBN spots for selected DXCCs

```text
ACCEPT/RBN 2 CALL_DXCC 230,291
```

### Remove the RBN filter later

```text
CLEAR/RBN ALL
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/accept/rbn.pl){ .md-button }

## Related commands

- [`REJECT/RBN`](reject--rbn.md)
- [`CLEAR/RBN`](clear--rbn.md)
- [`SET/WANTRBN`](set--wantrbn.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP ACCEPT/RBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.