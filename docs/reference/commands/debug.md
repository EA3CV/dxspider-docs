# `DEBUG`

<div class="command-hero" markdown>

**Set the cluster program into debug mode**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DEBUG
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
DEBUG
```

**Set the cluster program into debug mode**

## Details

Executing this command will only have an effect if you are running the cluster
in debug mode i.e.

```text
	perl -d cluster.pl
```

It will interrupt the cluster just after the debug command has finished.

## Verify on a running node

```text
HELP DEBUG
```

Use the node help to check for local overrides or differences in another installed revision.