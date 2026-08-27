# `SHOW/PREFIX`

<div class="command-hero" markdown>

**Interrogate the prefix database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/PREFIX <callsign>
```

**Interrogate the prefix database**

## Details

This command takes the <callsign> (which can be a full or partial
callsign or a prefix), looks up which internal country number
it is and then displays all the relevant prefixes for that country
together with the internal country no, the CQ and ITU regions.

See also SHOW/DXCC

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/prefix.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/PREFIX
```

The built-in help is useful when checking the exact command set installed on a particular node.