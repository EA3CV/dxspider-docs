# `STAT/DB`

<div class="command-hero" markdown>

**Show the status of a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
STAT/DB <dbname>
```

**Show the status of a database**

## Details

Show the internal status of a database descriptor.

Depending on your privilege level you will see more or less information.
This command is unlikely to be of much use to anyone other than a sysop.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/stat/db.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/DB
```

The built-in help is useful when checking the exact command set installed on a particular node.