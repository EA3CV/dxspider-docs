# `DBIMPORT`

<div class="command-hero" markdown>

**Import AK1A data into a database**

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
DBIMPORT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Performs file I/O.

### Named fields consumed by the parser

`name`, `fn`

### Important calls

`DXDb::getdesc()`, `db->putkey()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dbimport.pl` · SHA-256 `c31d0232e6a64dadb876e5ac0760ede06c4b58ed65ad11f7cdb4773a04333c3b`

```perl
L7: my ($self, $line) = @_;
L8: my ($name, $fn) = split /\s+/, $line;
L36: if ($key =~ /^#/) {
```

### Validation and access evidence

Source: `cmd/dbimport.pl` · SHA-256 `c31d0232e6a64dadb876e5ac0760ede06c4b58ed65ad11f7cdb4773a04333c3b`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 9;
L14: return (1, $self->msg('db3', $name)) unless $db;
L15: return (1, $self->msg('db1', $db->remote )) if $db->remote;
L16: return (1, $self->msg('e3', 'dbimport', $fn)) unless -e $fn;
L36: if ($key =~ /^#/) {
```

### Output and error evidence

Source: `cmd/dbimport.pl` · SHA-256 `c31d0232e6a64dadb876e5ac0760ede06c4b58ed65ad11f7cdb4773a04333c3b`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 9;
L14: return (1, $self->msg('db3', $name)) unless $db;
L15: return (1, $self->msg('db1', $db->remote )) if $db->remote;
L16: return (1, $self->msg('e3', 'dbimport', $fn)) unless -e $fn;
L23: open(IMP, $fn) or return (1, "Cannot open $fn $!");
L52: push @out, $self->msg('db10', $count, $fn, $db->name);
L53: return (1, @out);
```

### Message keys returned

`db1`, `db10`, `db3`, `e3`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DBIMPORT <dbname> <filename>
```

**Import AK1A data into a database**

## Details

If you want to import or update data in bulk to a database you can use
this command. It will either create or update entries into an existing
database. For example:-

```text
DBIMPORT oblast /tmp/OBLAST.FUL
```

will import the standard OBLAST database that comes with AK1A into the
oblast database held locally.

See DBEXPORT for how to export an AK1A database

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbimport.pl){ .md-button }

## Verify on a running node

```text
HELP DBIMPORT
```

Compare the installed handler with this page when local overrides or a different revision may be present.