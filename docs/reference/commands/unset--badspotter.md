# `UNSET/BADSPOTTER`

<div class="command-hero" markdown>

**Allow spots from this callsign again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/BADSPOTTER <call>..
```

**Allow spots from this callsign again**

## Details

Setting a callsign as a 'badspotter' will prevent spots from this callsign
going any further. They will not be displayed and they will not be
sent onto other nodes.

The call must be written in full, no wild cards are allowed eg:-

```text
set/badspotter VE2STN
```

will stop anything from VE2STN. This command will automatically
stop spots from this user, regardless of whether or which SSID
he uses. DO NOT USE SSIDs in the callsign, just use the callsign
as above or below.

```text
unset/badspotter VE2STN
```

will allow spots from him again.

Use with extreme care. This command may well be superceded by FILTERing.

This command will also stop TALK and ANNOUNCE/FULL from any user marked
as a BADSPOTTER.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/badspotter.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADSPOTTER
```

The built-in help is useful when checking the exact command set installed on a particular node.