# `DBCREATE`

<div class="command-hero" markdown>

**Create a database entry**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    DBCREATE <name>
    ```

    **Create a database entry**


=== "SYSOP form"

    ```text
    DBCREATE <name> chain <name> [<name>..]
    ```

    **Create a chained database entry**


=== "SYSOP form"

    ```text
    DBCREATE <name> remote <node>
    ```

    **Create a remote database entry**


=== "SYSOP form"

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/dbcreate.pl){ .md-button }

## Verify on a running node

```text
HELP DBCREATE
```

The built-in help is useful when checking the exact command set installed on a particular node.