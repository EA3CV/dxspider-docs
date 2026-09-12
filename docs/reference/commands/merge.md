# `MERGE`

<div class="command-hero" markdown>

**Ask for the latest spots and WWV**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
MERGE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
MERGE <node> [<no spots>/<no wwv>]
```

**Ask for the latest spots and WWV**

## Details

MERGE allows you to bring your spot and wwv database up to date. By default
it will request the last 10 spots and 5 WWVs from the node you select. The
node must be connected locally.

You can request any number of spots or wwv and although they will be appended
to your databases they will not duplicate any that have recently been added
(the last 2 days for spots and last month for WWV data).

## Verify on a running node

```text
HELP MERGE
```

Use the node help to check for local overrides or differences in another installed revision.