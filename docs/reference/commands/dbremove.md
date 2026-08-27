# `DBREMOVE`

<div class="command-hero" markdown>

**Delete a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DBREMOVE <dbname>
```

**Delete a database**

## Details

DBREMOVE will completely remove a database entry and also delete any data
file that is associated with it.

There is no warning, no comeback, no safety net.

For example:

```text
DBREMOVE oblast
```

will remove the oblast database from the system and it will also remove
the associated datafile.

I repeat:

There is no warning, no comeback, no safety net.

You have been warned.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/dbremove.pl){ .md-button }

## Verify on a running node

```text
HELP DBREMOVE
```

The built-in help is useful when checking the exact command set installed on a particular node.