# `SAVE`

<div class="command-hero" markdown>

**Save command output to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SAVE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Arguments

`fn`, `rest`

## Command description

```text
SAVE [-d -t -a] <filename> "<cmd>" [...]
```

**Save command output to a file**

## Details

This sysop only cammand allows you to save the output of one or more
commands to a file. For example:-

```text
save /spider/packclus/dxstats show/dxstat
```

will save the output of the normal command "show/dxstat" to the file
"dxstats" in the files area.

You can have some extra flags to the save which will either
date stamp or time stamp or both the filename so:-

```text
save -d /tmp/a <cmd> creates /tmp/a_6-Jan-2002
save -t /tmp/a <cmd> creates /tmp/a_2301Z
save -d -t /tmp/a <cmd> creates /tmp/a_6-Jan-2002_2301Z
```

The -a flag means append to the file instead of overwriting it.

You can have more than one command on the line, to do this you MUST
enclose each command in double quotes (") eg:-

```text
save /tmp/a "sh/hfstats" "blank +" "sh/vhfstats"
```

or

```text
save /tmp/a "sh/hfstats","blank +","sh/vhfstats"
```

You can only write into places that the cluster has permission for (which
is that of the "sysop" user [which had BETTER NOT BE "root"]), you will
need to create any directories you want to put stuff in beforehand as well.

It is likely that you will want to run these commands in a crontab type
situation. You would do that something like:-

```text
0 0 * * * run_cmd('save /tmp/dxstats "echo DXStat Table", "sh/dxstats"')
```

Note that you still enclose each command with (") characters but you must
enclose the entire save command in (') characters.

Now in fact, this can be varied if you know what you are doing. See the
admin manual for more details.

## Verify on a running node

```text
HELP SAVE
```

Use the node help to check for local overrides or differences in another installed revision.