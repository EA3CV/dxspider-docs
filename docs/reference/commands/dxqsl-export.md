# `DXQSL_EXPORT`

<div class="command-hero" markdown>

**Export SH/DXSQL information to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DXQSL_EXPORT <filename>
```

**Export SH/DXSQL information to a file**

## Details

The SHOW/DXQSL command shows any QSL managers that have been extracted
from comments on a DX spot.

Use this command to export the current state of the information to
a CSV style text file. For example:

```text
 DXQSL_EXPORT /tmp/qsl.csv
```

NOTE: this command will overwrite any file that you have write
permission for.

See also DXQSL_IMPORT to import one of these files.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/dxqsl_export.pl){ .md-button }

## Verify on a running node

```text
HELP DXQSL_EXPORT
```

The built-in help is useful when checking the exact command set installed on a particular node.