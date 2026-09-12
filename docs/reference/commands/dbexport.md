# `DBEXPORT`

<div class="command-hero" markdown>

**Export an AK1A data to a file**

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
DBEXPORT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Named fields consumed by the parser

`name`, `fn`

### Important calls

`DXDb::getdesc()`, `File->new()`, `of->print()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dbexport.pl` · SHA-256 `9257e0f805e4ada3c322d7d814515b8a737f4919159ed6074db4c1f9e9b64d86`

```perl
L7: my ($self, $line) = @_;
L8: my ($name, $fn) = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/dbexport.pl` · SHA-256 `9257e0f805e4ada3c322d7d814515b8a737f4919159ed6074db4c1f9e9b64d86`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L15: return (1, $self->msg('db3', $name)) unless $db;
L16: return (1, $self->msg('db1', $db->remote )) if $db->remote;
L17: my $of = IO::File->new(">$fn") or return(1, $self->msg('e30', $fn));
L26: return(0, $self->msg("db13", $count, $name, $fn));
```

### Output and error evidence

Source: `cmd/dbexport.pl` · SHA-256 `9257e0f805e4ada3c322d7d814515b8a737f4919159ed6074db4c1f9e9b64d86`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 9;
L10: return (1, "dbexport: <database name> <pathname to export to>") unless $name && $fn;
L15: return (1, $self->msg('db3', $name)) unless $db;
L16: return (1, $self->msg('db1', $db->remote )) if $db->remote;
L17: my $of = IO::File->new(">$fn") or return(1, $self->msg('e30', $fn));
L26: return(0, $self->msg("db13", $count, $name, $fn));
```

### Message keys returned

`db1`, `db13`, `db3`, `e30`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DBEXPORT <dbname> <filename>
```

**Export an AK1A data to a file**

## Details

Sometimes one needs to export the data from an existing database file,
maybe for a backup or to send to another node.

```text
DBEXPORT oblast /tmp/OBLAST.FUL
```

will export the OBLAST database to /tmp/OBLAST.FUL

There is no protection, it is up to you not to overwrite a file that
is important to you.

See DBIMPORT for the importing of existing AK1A format data to databases.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbexport.pl){ .md-button }

## Verify on a running node

```text
HELP DBEXPORT
```

Compare the installed handler with this page when local overrides or a different revision may be present.