# `DBIMPORT`

<div class="command-hero" markdown>

**Import AK1A data into a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DBIMPORT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

### Arguments

`name`, `fn`

## Command description

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

## Verify on a running node

```text
HELP DBIMPORT
```

Use the node help to check for local overrides or differences in another installed revision.