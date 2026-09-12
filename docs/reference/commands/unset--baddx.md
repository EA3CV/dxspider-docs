# `UNSET/BADDX`

<div class="command-hero" markdown>

**Propagate a dx spot with this callsign again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/BADDX [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

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

## Verify on a running node

```text
HELP UNSET/BADDX
```

Use the node help to check for local overrides or differences in another installed revision.