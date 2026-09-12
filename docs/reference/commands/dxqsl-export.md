# `DXQSL_EXPORT`

<div class="command-hero" markdown>

**Export SH/DXSQL information to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DXQSL_EXPORT [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Verify on a running node

```text
HELP DXQSL_EXPORT
```

Use the node help to check for local overrides or differences in another installed revision.