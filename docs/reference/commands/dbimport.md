# `DBIMPORT`

<div class="command-hero" markdown>

**Import AK1A data into a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DBIMPORT <dbname> <filename>
```

**Import AK1A data into a database**

## Details

If you want to import or update data in bulk to a database you can use
this command. It will either create or update entries into an existing
database. For example:-

```text
DBIMPORT oblast /tmp/OBLAST.FUL
```

will import the standard OBLAST database that comes with AK1A into the
oblast database held locally.

See DBEXPORT for how to export an AK1A database

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/dbimport.pl){ .md-button }

## Verify on a running node

```text
HELP DBIMPORT
```

The built-in help is useful when checking the exact command set installed on a particular node.