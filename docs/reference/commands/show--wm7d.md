# `SHOW/WM7D`

<div class="command-hero" markdown>

**Show callbook details on a US callsigns**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/WM7D <callsign>
```

**Show callbook details on a US callsigns**

## Details

This command queries the WM7D callbook server on the internet
and returns any information available for that US callsign. This service
is provided for users of this software by http://www.wm7d.net.

See also SHOW/QRZ.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/wm7d.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/WM7D
```

The built-in help is useful when checking the exact command set installed on a particular node.