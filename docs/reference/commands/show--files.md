# `SHOW/FILES`

<div class="command-hero" markdown>

**List the contents of a filearea**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/FILES [token ...]
```

## Command description

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

## Verify on a running node

```text
HELP SHOW/FILES
```

Use the node help to check for local overrides or differences in another installed revision.