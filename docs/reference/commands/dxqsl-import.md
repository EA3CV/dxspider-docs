# `DXQSL_IMPORT`

<div class="command-hero" markdown>

**Import SH/DXSQL information from a file**

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
DXQSL_IMPORT <structured arguments>
```

The handler parses a structured list (for example comma-separated or key/value input). See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`File->new()`, `QSL->new()`, `QSL::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dxqsl_import.pl` · SHA-256 `834feba17fac757793c54981f2eff8db45d08073f158c58bb4d0ef36fe17ae7f`

```perl
L7: my ($self, $line) = @_;
L8: my ($fn) = $line;
L21: my ($call, $manager, $c, $t, $by) = split /\s*,\s*/;
```

### Validation and access evidence

Source: `cmd/dxqsl_import.pl` · SHA-256 `834feba17fac757793c54981f2eff8db45d08073f158c58bb4d0ef36fe17ae7f`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L14: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
L16: my $if = IO::File->new("$fn") or return(1, $self->msg('e30', $fn));
L42: return(0, $self->msg("db10", $count, $fn, 'dxqsl'));
```

### Output and error evidence

Source: `cmd/dxqsl_import.pl` · SHA-256 `834feba17fac757793c54981f2eff8db45d08073f158c58bb4d0ef36fe17ae7f`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L10: return (1, "import_dxqsl: <pathname to import from>") unless $fn;
L14: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
L16: my $if = IO::File->new("$fn") or return(1, $self->msg('e30', $fn));
L42: return(0, $self->msg("db10", $count, $fn, 'dxqsl'));
```

### Message keys returned

`db10`, `db3`, `e30`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DXQSL_IMPORT <filename>
```

**Import SH/DXSQL information from a file**

## Details

The SHOW/DXQSL command shows any QSL managers that have been extracted
from comments on a DX spot.

Use this command to restore a file created by the DXSQL_EXPORT command.
For example:

```text
 DXQSL_IMPORT /tmp/qsl.csv
```

The data in this file will UPDATE any information that may already be
present. This may not be what you want. To make the data the same as
the import file then you must:

* stop the node
* remove /spider/data/qsl.v1
* restart the node
* login as sysop
* do the import

Preferably before too many DX spots with qsl manager info come in.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dxqsl_import.pl){ .md-button }

## Verify on a running node

```text
HELP DXQSL_IMPORT
```

Compare the installed handler with this page when local overrides or a different revision may be present.