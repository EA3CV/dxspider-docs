# `DXQSL_EXPORT`

<div class="command-hero" markdown>

**Export SH/DXSQL information to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
DXQSL_EXPORT [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`File->new()`, `QSL::get()`, `dbm->seq()`, `of->print()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dxqsl_export.pl` · SHA-256 `a33d72fabde70210f28a9df3a8cd0f22f99dee8149e26b1b37dca02995568801`

```perl
L7: my ($self, $line) = @_;
L8: my ($fn) = $line;
```

### Validation and access evidence

Source: `cmd/dxqsl_export.pl` · SHA-256 `a33d72fabde70210f28a9df3a8cd0f22f99dee8149e26b1b37dca02995568801`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L14: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
L16: my $of = IO::File->new(">$fn") or return(1, $self->msg('e30', $fn));
L32: return(0, $self->msg("db13", $count, 'dxqsl', $fn));
```

### Output and error evidence

Source: `cmd/dxqsl_export.pl` · SHA-256 `a33d72fabde70210f28a9df3a8cd0f22f99dee8149e26b1b37dca02995568801`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L10: return (1, "export_dxqsl: <pathname to export to>") unless $fn;
L14: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
L16: my $of = IO::File->new(">$fn") or return(1, $self->msg('e30', $fn));
L32: return(0, $self->msg("db13", $count, 'dxqsl', $fn));
```

### Message keys returned

`db13`, `db3`, `e30`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DXQSL_EXPORT <filename>
```

**Export SH/DXSQL information to a file**

## Details

The SHOW/DXQSL command shows any QSL managers that have been extracted
from comments on a DX spot.

Use this command to export the current state of the information to
a CSV style text file. For example:

```text
 DXQSL_EXPORT /tmp/qsl.csv
```

NOTE: this command will overwrite any file that you have write
permission for.

See also DXQSL_IMPORT to import one of these files.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dxqsl_export.pl){ .md-button }

## Verify on a running node

```text
HELP DXQSL_EXPORT
```

Compare the installed handler with this page when local overrides or a different revision may be present.