# `REJECT/RBN`

<div class="command-hero" markdown>

**Set a 'reject' filter line for RBN spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reject/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/RBN
```

The built-in help is useful when checking the exact command set installed on a particular node.