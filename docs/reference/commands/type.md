# `TYPE`

<div class="command-hero" markdown>

**Look at the contents of a file in one of the fileareas**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
TYPE [token ...]
```

## Command description

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

## Verify on a running node

```text
HELP TYPE
```

Use the node help to check for local overrides or differences in another installed revision.