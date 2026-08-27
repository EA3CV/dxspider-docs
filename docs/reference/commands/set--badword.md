# `SET/BADWORD`

<div class="command-hero" markdown>

**Stop things like this word being propagated**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/BADWORD <word>..
```

**Stop things like this word being propagated**

## Details

Setting a word as a 'badword' will prevent things like spots,
announces or talks with this word in the the text part from going any
further. They will not be displayed and they will not be sent onto
other nodes.

This has changed its meaning from the master release. All words entered
are reduced to the minimum regex that will match words starting like
this one:

```text
set/badword annihilate
```

will stop anything that starts with these words in the text
like this:

```text
annihilate annihilated
```

but it will also stop things like this:

```text
anihilate annni11ihhh ii lllattt eee
```

A few common 'leet' substitutions are automatically matched:

```text
b0ll0cks bo0lll0ccckks fr1iigging
```

and so on

It will not stop some things like:

```text
The base word FRIG will stop 'friiigging' but not 'friiig ging'
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/badword.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BADWORD
```

The built-in help is useful when checking the exact command set installed on a particular node.