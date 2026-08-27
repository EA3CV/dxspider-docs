# `SHOW/LOG`

<div class="command-hero" markdown>

**Show excerpts from the system log**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/LOG [<callsign>]
```

**Show excerpts from the system log**

## Details

This command outputs a short section of the system log.  On its own
it will output a general logfile.  With the optional callsign it will
show output from the log associated with that callsign.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/log.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/LOG
```

The built-in help is useful when checking the exact command set installed on a particular node.