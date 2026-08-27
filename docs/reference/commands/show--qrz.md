# `SHOW/QRZ`

<div class="command-hero" markdown>

**Show any callbook details on a callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/QRZ <callsign>
```

**Show any callbook details on a callsign**

## Details

This command queries the QRZ callbook server on the internet
and returns any information available for that callsign. This service
is provided for users of this software by http://www.qrz.com

See also SHOW/WM7D for an alternative.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/qrz.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/QRZ
```

The built-in help is useful when checking the exact command set installed on a particular node.