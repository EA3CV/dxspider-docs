# `SEND_CONFIG`

<div class="command-hero" markdown>

**Broadcast PC92 C records**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SEND_CONFIG
```

**Broadcast PC92 C records**

## Details

This is the PC92 equivalent of INIT. In that it will send out a new
PC92 C record to all interfaces. This can be used to bring other nodes
up to date quicker after a restart.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/send_config.pl){ .md-button }

## Verify on a running node

```text
HELP SEND_CONFIG
```

The built-in help is useful when checking the exact command set installed on a particular node.