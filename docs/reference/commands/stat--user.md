# `STAT/USER`

<div class="command-hero" markdown>

**Show the full status of a user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
STAT/USER [<callsign>]
```

**Show the full status of a user**

## Details

Shows the full contents of a user record including all the secret flags
and stuff.

Only the fields that are defined (in perl term) will be displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/stat/user.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/USER
```

The built-in help is useful when checking the exact command set installed on a particular node.