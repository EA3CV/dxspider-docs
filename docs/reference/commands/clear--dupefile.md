# `CLEAR/DUPEFILE`

<div class="command-hero" markdown>

**Clear out the dupefile completely**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
CLEAR/DUPEFILE
```

**Clear out the dupefile completely**

## Details

The system maintains a list of duplicate announces and spots (amongst many
other things). Sometimes this file gets corrupted during operation
(although not very often). This command will remove the file and start
again from scratch.

Try this if you get several duplicate DX Spots, one after another.

Please ONLY use this command if you have a problem. And then only once.
If it does not cure your problem, then repeating the command won't help.
Get onto the dxspider-support list and let us try to help.

If you use this command frequently then you will cause other people, as
well as yourself, a lot of problems with duplicates.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/clear/dupefile.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/DUPEFILE
```

The built-in help is useful when checking the exact command set installed on a particular node.