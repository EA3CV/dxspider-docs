# `DBSHOW`

<div class="command-hero" markdown>

**Display an entry, if it exists, in a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DBSHOW [token ...]
```

## Command description

```text
DBSHOW <dbname> <key>
```

**Display an entry, if it exists, in a database**

## Details

This is the generic user interface to the database to the database system.
It is expected that the sysop will add an entry to the local Aliases file
so that users can use the more familiar AK1A style of enquiry such as:

```text
SH/BUCK G1TLH
```

but if he hasn't and the database really does exist (use DBAVAIL or
SHOW/COMMAND to find out) you can do the same thing with:

```text
DBSHOW buck G1TLH
```

## Verify on a running node

```text
HELP DBSHOW
```

Use the node help to check for local overrides or differences in another installed revision.