# `LOAD/BADWORDS`

<div class="command-hero" markdown>

**Reload the bad words table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/BADWORDS
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
LOAD/BADWORDS
```

**Reload the bad words table**

## Details

Reload the /spider/data/badwords file if you have changed it manually whilst
the cluster is running. This file contains a list of words which, if found
on certain text portions of PC protocol, will cause those protocol frames
to be rejected. It will all put out a message if any of these words are
used on the announce, dx and talk commands. The words can be one or
more on a line, lines starting with '#' are ignored.

## Verify on a running node

```text
HELP LOAD/BADWORDS
```

Use the node help to check for local overrides or differences in another installed revision.