# `SHOW/PROGRAM`

<div class="command-hero" markdown>

**Show the locations of all the included program modules**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/PROGRAM
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SHOW/PROGRAM
```

**Show the locations of all the included program modules**

## Details

Show the name and location where every program module was load from. This
is useful for checking where you think you have loaded a .pm file from.

## Verify on a running node

```text
HELP SHOW/PROGRAM
```

Use the node help to check for local overrides or differences in another installed revision.