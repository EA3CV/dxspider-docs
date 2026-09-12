# `REJECT/ROUTE`

<div class="command-hero" markdown>

**Set an 'reject' filter line for routing**

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
REJECT/ROUTE <arguments accepted by delegated parser>
```

The complete argument line is delegated to another parser. Follow the cited call for the final grammar.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`filterdef->cmd()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/reject/route.pl` · SHA-256 `d7237f0d67906ce66d5480b5ccaf8b9f9a97e7f8cfaae43260022dff1f88708a`

```perl
L9: my ($self, $line) = @_;
L13: my ($r, $filter, $fno) = $Route::filterdef->cmd($self, $sort, $type, $line);
```

### Validation and access evidence

Source: `cmd/reject/route.pl` · SHA-256 `d7237f0d67906ce66d5480b5ccaf8b9f9a97e7f8cfaae43260022dff1f88708a`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Output and error evidence

Source: `cmd/reject/route.pl` · SHA-256 `d7237f0d67906ce66d5480b5ccaf8b9f9a97e7f8cfaae43260022dff1f88708a`

```perl
L15: return ($ok, $r ? $filter : $self->msg('filter1', $fno, $filter->{name}));
```

### Message keys returned

`filter1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
REJECT/ROUTE <call> [0-9] <pattern>
```

**Set an 'reject' filter line for routing**

## Details

Create an 'reject this routing PC Protocol' line for a filter.

An reject filter line means that if a PC16/17/19/21/24/41/50 matches this filter
it is NOT passed thru that interface. See HELP FILTERING for more info. Please
read this to understand how filters work - it will save a lot of grief later on.

You can use any of the following things in this line:-

```text
call <prefixes>        the callsign of the thingy
call_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
call_itu <prefixes or numbers>     or: G,GM,GW
call_zone <prefixes or numbers>
call_state <states>                eg: VA,NH,RI,ME
origin <prefixes>      really the interface it came in on
origin_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
origin_itu <prefixes or numbers>     or: G,GM,GW
origin_zone <prefixes or numbers>
origin_state <states>                eg: VA,NH,RI,ME
```

some examples:-

```text
rej/route gb7djk call_dxcc 61,38 (everything except  UK+EIRE nodes)
```

You can use the tag 'all' to reject everything eg:

```text
rej/route all     (equiv to [very] restricted mode)
```

as with ACCEPT/ROUTE 'by' is now a synonym for 'call'.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/reject/route.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/ROUTE
```

Compare the installed handler with this page when local overrides or a different revision may be present.