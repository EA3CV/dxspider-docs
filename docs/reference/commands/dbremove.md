# `DBREMOVE`

<div class="command-hero" markdown>

**Delete a database**

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
DBREMOVE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Named fields consumed by the parser

`name`

### Important calls

`DXDb::getdesc()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dbremove.pl` · SHA-256 `69a9976bc509518e0ed37117365a3457ac75eec632b5e2c449b8a2fc4773f626`

```perl
L7: my ($self, $line) = @_;
L8: my ($name) = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/dbremove.pl` · SHA-256 `69a9976bc509518e0ed37117365a3457ac75eec632b5e2c449b8a2fc4773f626`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 9;
L19: return (1, $self->msg('db3', $name)) unless $db;
```

### Output and error evidence

Source: `cmd/dbremove.pl` · SHA-256 `69a9976bc509518e0ed37117365a3457ac75eec632b5e2c449b8a2fc4773f626`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 9;
L12: return(1, "usage: dbremove <database name>" ) unless $name;
L17: push @out, $self->msg('db9', $name);
L19: return (1, $self->msg('db3', $name)) unless $db;
L22: return (1, @out);
```

### Message keys returned

`db3`, `db9`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DBREMOVE <dbname>
```

**Delete a database**

## Details

DBREMOVE will completely remove a database entry and also delete any data
file that is associated with it.

There is no warning, no comeback, no safety net.

For example:

```text
DBREMOVE oblast
```

will remove the oblast database from the system and it will also remove
the associated datafile.

I repeat:

There is no warning, no comeback, no safety net.

You have been warned.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbremove.pl){ .md-button }

## Verify on a running node

```text
HELP DBREMOVE
```

Compare the installed handler with this page when local overrides or a different revision may be present.