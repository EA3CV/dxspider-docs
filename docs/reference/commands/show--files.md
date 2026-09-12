# `SHOW/FILES`

<div class="command-hero" markdown>

**List the contents of a filearea**

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
SHOW/FILES [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/files.pl` · SHA-256 `8c96cf3ab153f8470eeab8c24dc1b9ead74fdfd895114e0b4ab766e64cd5a0c8`

```perl
L11: my ($self, $line) = @_;
L12: my @f = split /\s+/, $line;
L22: $fn =~ s/\\/\//og;
L23: $fn =~ s/\.//og;
L24: $fn =~ s/^\///og;
```

### Validation and access evidence

Source: `cmd/show/files.pl` · SHA-256 `8c96cf3ab153f8470eeab8c24dc1b9ead74fdfd895114e0b4ab766e64cd5a0c8`

```perl
L27: $patt = shellregex(lc $f[1]) if defined $f[1];
L30: opendir(DIR, $root) or return (1, $self->msg('e3', 'show/files', $f[0]));
```

### Output and error evidence

Source: `cmd/show/files.pl` · SHA-256 `8c96cf3ab153f8470eeab8c24dc1b9ead74fdfd895114e0b4ab766e64cd5a0c8`

```perl
L30: opendir(DIR, $root) or return (1, $self->msg('e3', 'show/files', $f[0]));
L50: push @out, "$slot[0] $slot[1]";
L53: push @out, $slot[0] if $flag;
L54: return (1, @out);
```

### Message keys returned

`e3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/files.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/FILES
```

Compare the installed handler with this page when local overrides or a different revision may be present.