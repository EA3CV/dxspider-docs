# `LOAD/CMD_CACHE`

<div class="command-hero" markdown>

**Reload the automatic command cache**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/cmd_cache.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/CMD_CACHE
```

The built-in help is useful when checking the exact command set installed on a particular node.