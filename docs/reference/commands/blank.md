# `BLANK`

<div class="command-hero" markdown>

**Print nn (default 1) blank lines (or strings)**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
BLANK [<string>] [<nn>]
```

**Print nn (default 1) blank lines (or strings)**

## Details

In its basic form this command prints one or more blank lines. However if
you pass it a string it will replicate the string for the width of the
screen (default 80) and then print that one or more times, so:

```text
blank 2
```

prints two blank lines

```text
blank -
```

prints a row of - characters once.

```text
blank abc
```

prints 'abcabcabcabcabcabc....'

This is really only of any use in a script file and you can print a maximum
of 9 lines.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/blank.pl){ .md-button }

## Verify on a running node

```text
HELP BLANK
```

The built-in help is useful when checking the exact command set installed on a particular node.