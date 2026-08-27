# `SHOW/DXSTATS`

<div class="command-hero" markdown>

**Show the DX Statistics**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/DXSTATS [days] [date]
```

**Show the DX Statistics**

## Details

Show the total DX spots for the last <days> no of days (default is 31),
starting from a <date> (default: today).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/dxstats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DXSTATS
```

The built-in help is useful when checking the exact command set installed on a particular node.