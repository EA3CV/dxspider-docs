# `DXQSL_IMPORT`

<div class="command-hero" markdown>

**Import SH/DXSQL information from a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DXQSL_IMPORT <structured arguments>
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Verify on a running node

```text
HELP DXQSL_IMPORT
```

Use the node help to check for local overrides or differences in another installed revision.