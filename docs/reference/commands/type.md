# `TYPE`

<div class="command-hero" markdown>

**Look at the contents of a file in one of the fileareas**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
TYPE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/type.pl` · SHA-256 `c0fc438150f4cdeadd6ca66426306f0c8b6a719f8fb541debd0ee808485fcf2c`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/type.pl` · SHA-256 `c0fc438150f4cdeadd6ca66426306f0c8b6a719f8fb541debd0ee808485fcf2c`

```perl
L24: open(INP, $root) or return (1, $self->msg('e3', 'type', $f[0]));
```

### Output and error evidence

Source: `cmd/type.pl` · SHA-256 `c0fc438150f4cdeadd6ca66426306f0c8b6a719f8fb541debd0ee808485fcf2c`

```perl
L24: open(INP, $root) or return (1, $self->msg('e3', 'type', $f[0]));
L28: return (1, @out);
```

### Message keys returned

`e3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/type.pl){ .md-button }

## Verify on a running node

```text
HELP TYPE
```

Compare the installed handler with this page when local overrides or a different revision may be present.