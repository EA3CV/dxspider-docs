# `DBREMOVE`

<div class="command-hero" markdown>

**Delete a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DBREMOVE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

### Arguments

`name`

## Command description

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

## Verify on a running node

```text
HELP DBREMOVE
```

Use the node help to check for local overrides or differences in another installed revision.