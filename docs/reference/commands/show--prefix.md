# `SHOW/PREFIX`

<div class="command-hero" markdown>

**Interrogate the prefix database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/PREFIX [token ...]
```

## Command description

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

## Verify on a running node

```text
HELP SHOW/PREFIX
```

Use the node help to check for local overrides or differences in another installed revision.