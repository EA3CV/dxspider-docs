# `DBCREATE`

<div class="command-hero" markdown>

**Create a database entry**

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
DBCREATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Recognized tokens, keys or enumerated values in this handler

`chain`, `cmd`, `remote`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXDb::getdesc()`, `DXDb::new()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dbcreate.pl` · SHA-256 `a35a6fb95afe7ddf8bd45c1b7cc01320936cd419674aec5daa9a9a520559af69`

```perl
L7: my ($self, $line) = @_;
L8: my @f = split /\s+/, $line;
L9: my $name = shift @f if @f;
L19: my $f = lc shift @f;
L21: $remote = uc shift @f if @f;
L25: $cmd = lc shift @f if @f;
```

### Validation and access evidence

Source: `cmd/dbcreate.pl` · SHA-256 `a35a6fb95afe7ddf8bd45c1b7cc01320936cd419674aec5daa9a9a520559af69`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L13: return (1, $self->msg('db6', $name)) if DXDb::getdesc($name);
```

### Output and error evidence

Source: `cmd/dbcreate.pl` · SHA-256 `a35a6fb95afe7ddf8bd45c1b7cc01320936cd419674aec5daa9a9a520559af69`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L13: return (1, $self->msg('db6', $name)) if DXDb::getdesc($name);
L36: push @out, $self->msg($remote ? 'db7' : 'db8', $name, $remote);
L37: return (1, @out);
```

### Message keys returned

`db6`, `e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    DBCREATE <name>
    ```

    **Create a database entry**


=== "Help variant"

    ```text
    DBCREATE <name> chain <name> [<name>..]
    ```

    **Create a chained database entry**


=== "Help variant"

    ```text
    DBCREATE <name> remote <node>
    ```

    **Create a remote database entry**


=== "Help variant"

    ```text
    DBCREATE <name> cmd <dxspider command>
    ```

    **make a local command available as a DB**

    DBCREATE allows you to define a database in the system. It doesn't actually
    create anything, just defines it.

    The databases that are created are simple DB_File hash databases, they are
    therefore already 'indexed'.

    You can define a local database with the first form of the command eg:

    ```text
    DBCREATE oblast
    ```

    You can also chain databases with the addition of the 'chain' keyword.
    This will search each database one after the other. A typical example
    is:

    ```text
    DBCREATE sdx_qsl chain sql_ad
    ```

    No checking is done to see if the any of the chained databases exist, in
    fact it is usually better to do the above staement first then do each of
    the chained databases.

    Databases can exist offsite. To define a database that lives on another
    node do:

    ```text
    DBCREATE buckmaster remote gb7dxc
    ```

    Remote databases cannot be chained; however, the last database in a
    a chain can be a remote database eg:

    ```text
    DBCREATE qsl chain gb7dxc
    ```

    To see what databases have been defined do:

    ```text
    DBAVAIL (or it will have been aliased to SHOW/COMMAND)
    ```

    It would be normal for you to add an entry into your local Aliases file
    to allow people to use the 'SHOW/<dbname>' style syntax. So you would
    need to add a line like:-

    ```text
    's' => [
      ..
      ..
      '^sh\w*/buc', 'dbshow buckmaster', 'dbshow',
      ..
      ..
     ],
    ```

    to allow

    ```text
    SH/BUCK g1tlh
    ```

    to work as they may be used to.

    You can also make local commands available as 'pseudo' databases. You
    can therefore make spider special commands available as a database. I
    imagine that this will be primarily useful for remote access from
    legacy nodes. For example:-

    ```text
    DBCREATE dxqsl cmd show/dxqsl
    ```

    You also use one of these databases in a chain. This may be useful
    locally.

    See DBIMPORT for the importing of existing AK1A format data to databases.
    See DXEXPORT for how to export an AK1A data in a form able to be imported.
    See DBSHOW for generic database enquiry

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbcreate.pl){ .md-button }

## Verify on a running node

```text
HELP DBCREATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.