# `UNSET/BADWORD`

<div class="command-hero" markdown>

**Propagate things like this word again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/BADWORD <word>..
```

**Propagate things like this word again**

## Details

This is the opposite of set/badword <word>

```text
unset/badword fred
```

will allow text with this word again (if it has been set as a bad word.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/badword.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADWORD
```

The built-in help is useful when checking the exact command set installed on a particular node.