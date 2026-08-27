# `TYPE`

<div class="command-hero" markdown>

**Look at the contents of a file in one of the fileareas**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
TYPE <filearea>/<name>
```

**Look at the contents of a file in one of the fileareas**

## Details

Type out the contents of a file in a filearea. So, for example, in
filearea 'bulletins' you want to look at file 'arld051' you would
enter:-
```text
 TYPE bulletins/arld051
```

See also SHOW/FILES to see what fileareas are available and a
list of content.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/type.pl){ .md-button }

## Verify on a running node

```text
HELP TYPE
```

The built-in help is useful when checking the exact command set installed on a particular node.