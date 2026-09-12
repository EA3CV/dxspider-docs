# `STAT/DB`

<div class="command-hero" markdown>

**Show the status of a database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
STAT/DB [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
STAT/DB <dbname>
```

**Show the status of a database**

## Details

Show the internal status of a database descriptor.

Depending on your privilege level you will see more or less information.
This command is unlikely to be of much use to anyone other than a sysop.

## Verify on a running node

```text
HELP STAT/DB
```

Use the node help to check for local overrides or differences in another installed revision.