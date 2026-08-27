# `SHOW/FILES`

<div class="command-hero" markdown>

**List the contents of a filearea**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/FILES [<filearea> [<string>]]
```

**List the contents of a filearea**

## Details

SHOW/FILES on its own will show you a list of the various fileareas
available on the system. To see the contents of a particular file
area type:-
```text
 SH/FILES <filearea>
```
where <filearea> is the name of the filearea you want to see the
contents of.

You can also use shell globbing characters like '*' and '?' in a
string to see a selection of files in a filearea eg:-
```text
 SH/FILES bulletins arld*
```

See also TYPE - to see the contents of a file.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/files.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/FILES
```

The built-in help is useful when checking the exact command set installed on a particular node.