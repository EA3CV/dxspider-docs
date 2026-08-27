# `SHOW/TIME`

<div class="command-hero" markdown>

**Show the local time**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/TIME [<prefix>|<callsign>]
```

**Show the local time**

## Details

If no prefixes or callsigns are given then this command returns the local
time and UTC as the computer has it right now. If you give some prefixes
then it will show UTC and UTC + the local offset (not including DST) at
the prefixes or callsigns that you specify.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/time.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/TIME
```

The built-in help is useful when checking the exact command set installed on a particular node.