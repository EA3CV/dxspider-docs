# `SHOW/DB0SDX`

<div class="command-hero" markdown>

**Show QSL infomation from DB0SDX database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/DB0SDX <callsign>
```

**Show QSL infomation from DB0SDX database**

## Details

This command queries the DB0SDX QSL server on the internet
and returns any information available for that callsign. This service
is provided for users of this software by http://www.qslinfo.de.

See also SHOW/QRZ, SHOW/WM7D.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/db0sdx.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DB0SDX
```

The built-in help is useful when checking the exact command set installed on a particular node.