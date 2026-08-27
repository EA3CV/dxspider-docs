# `UNSET/DEBUG`

<div class="command-hero" markdown>

**Remove a debug level from the debug set**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/DEBUG <name>
```

**Remove a debug level from the debug set**

## Details

You can choose to log several different levels.  The levels are

 chan
 state
 msg
 cron
 connect

You can show what levels you are logging with SHOW/DEBUG

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/debug.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/DEBUG
```

The built-in help is useful when checking the exact command set installed on a particular node.