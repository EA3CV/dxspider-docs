# `DBEXPORT`

<div class="command-hero" markdown>

**Export an AK1A data to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DBEXPORT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

### Arguments

`name`, `fn`

## Command description

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

## Verify on a running node

```text
HELP DBEXPORT
```

Use the node help to check for local overrides or differences in another installed revision.