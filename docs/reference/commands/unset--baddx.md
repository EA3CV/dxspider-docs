# `UNSET/BADDX`

<div class="command-hero" markdown>

**Propagate a dx spot with this callsign again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/BADDX <call>..
```

**Propagate a dx spot with this callsign again**

## Details

Setting a word as 'baddx' will prevent spots with that word in the
'spotted' field (as in: DX 14001.1 FR0G)of a DX spot from going any
further. They will not be displayed and they will not be sent onto
other nodes.

The word must be written in full, no wild cards are allowed eg:-

```text
set/baddx FORSALE VIDEO FR0G
```

To allow a word again, use the following command ...

```text
unset/baddx VIDEO
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/baddx.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADDX
```

The built-in help is useful when checking the exact command set installed on a particular node.