# `SHOW/DXCC`

<div class="command-hero" markdown>

**Interrogate the spot database by country**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/DXCC <prefix>
```

**Interrogate the spot database by country**

## Details

This command takes the <prefix> (which can be a full or partial
callsign if desired), looks up which internal country number it is
and then displays all the spots as per SH/DX for that country.

This is now an alias for 'SHOW/DX DXCC'

The options for SHOW/DX also apply to this command.
e.g.

```text
 SH/DXCC G
 SH/DXCC W on 20m iota
```

This can be done with the SHOW/DX command like this:-

```text
 SH/DX dxcc g
 SH/DX dxcc w on 20m iota
```

This is an alias for: SH/DX dxcc

## Verify on a running node

```text
HELP SHOW/DXCC
```

The built-in help is useful when checking the exact command set installed on a particular node.