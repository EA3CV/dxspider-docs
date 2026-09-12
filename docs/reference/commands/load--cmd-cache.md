# `LOAD/CMD_CACHE`

<div class="command-hero" markdown>

**Reload the automatic command cache**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/CMD_CACHE
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
LOAD/CMD_CACHE
```

**Reload the automatic command cache**

## Details

Normally, if you change a command file in the cmd or local_cmd tree it
will automatially be picked up by the cluster program. Sometimes it
can get confused if you are doing a lot of moving commands about or
delete a command in the local_cmd tree and want to use the normal one
again. Execute this command to reset everything back to the state it
was just after a cluster restart. To see what is in the command cache
see SHOW/CMD_CACHE.

## Verify on a running node

```text
HELP LOAD/CMD_CACHE
```

Use the node help to check for local overrides or differences in another installed revision.