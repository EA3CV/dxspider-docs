# `FORWARD/OPERNAM`

<div class="command-hero" markdown>

**Send out information on this <call> to all clusters**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
FORWARD/OPERNAM <call>
```

**Send out information on this <call> to all clusters**

## Details

This command sends out any information held in the user file which can
be broadcast in PC41 protocol packets. This information is Name, QTH, Location
and Homenode. PC41s are only sent for the information that is available.

## Verify on a running node

```text
HELP FORWARD/OPERNAM
```

The built-in help is useful when checking the exact command set installed on a particular node.