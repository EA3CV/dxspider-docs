# `DXQSL_IMPORT`

<div class="command-hero" markdown>

**Import SH/DXSQL information from a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DXQSL_IMPORT <filename>
```

**Import SH/DXSQL information from a file**

## Details

The SHOW/DXQSL command shows any QSL managers that have been extracted
from comments on a DX spot.

Use this command to restore a file created by the DXSQL_EXPORT command.
For example:

```text
 DXQSL_IMPORT /tmp/qsl.csv
```

The data in this file will UPDATE any information that may already be
present. This may not be what you want. To make the data the same as
the import file then you must:

* stop the node
* remove /spider/data/qsl.v1
* restart the node
* login as sysop
* do the import

Preferably before too many DX spots with qsl manager info come in.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/dxqsl_import.pl){ .md-button }

## Verify on a running node

```text
HELP DXQSL_IMPORT
```

The built-in help is useful when checking the exact command set installed on a particular node.