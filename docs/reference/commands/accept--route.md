# `ACCEPT/ROUTE`

<div class="command-hero" markdown>

**Set an 'accept' filter line for routing**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
ACCEPT/ROUTE <call> [0-9] <pattern>
```

**Set an 'accept' filter line for routing**

## Details

Create an 'accept this routing PC Protocol' line for a filter.

An accept filter line means that if a PC16/17/19/21/24/41/50 matches this filter
it is passed thru that interface. See HELP FILTERING for more info. Please read this
to understand how filters work - it will save a lot of grief later on.

You can use any of the following things in this line:-

```text
call <prefixes>        the callsign of the thingy
call_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
call_itu <prefixes or numbers>     or: G,GM,GW
call_zone <prefixes or numbers>
call_state <states>                eg: VA,NH,RI,NH
origin <prefixes>      really the interface it came in on
origin_dxcc <prefixes or numbers>    eg: 61,62 (from eg: sh/pre G)
origin_itu <prefixes or numbers>     or: G,GM,GW
origin_zone <prefixes or numbers>
origin_state <states>                eg: VA,NH,RI,NH
```

some examples:-

```text
acc/route gb7djk call_dxcc 61,38 (send only UK+EIRE nodes)
acc/route gb7djk call gb7djk     (equiv to SET/ISOLATE)
```

you can now use 'by' as a synonym for 'call' so:

```text
by = call
by_dxcc = call_dxcc
```

and so on

You can use the tag 'all' to accept everything eg:

```text
acc/route all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/accept/route.pl){ .md-button }

## Verify on a running node

```text
HELP ACCEPT/ROUTE
```

The built-in help is useful when checking the exact command set installed on a particular node.