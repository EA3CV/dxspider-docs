# `REJECT/ROUTE`

<div class="command-hero" markdown>

**Set an 'reject' filter line for routing**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reject/route.pl){ .md-button }

## Verify on a running node

```text
HELP REJECT/ROUTE
```

The built-in help is useful when checking the exact command set installed on a particular node.