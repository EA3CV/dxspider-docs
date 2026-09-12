# `SAVE`

<div class="command-hero" markdown>

**Save command output to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SAVE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Named fields consumed by the parser

`fn`, `rest`

### Important calls

`self->msg()`, `self->run_cmd()`

### Argument parsing evidence

Source: `cmd/save.pl` · SHA-256 `84035b04b5b5e7a2c0f263a792d4579a125a5c0eefa3a5f517433308a99ef002`

```perl
L11: my ($self, $line) = @_;
L16: if ($line =~ /-d/) { # add a date to the end of the filename
L17: $line =~ s/\s*-d\s*//;
L20: if ($line =~ /-t/) { # add a time to the end of the filename
L21: $line =~ s/\s*-t\s*//;
L24: if ($line =~ /-a/) { # append to the file
L25: $line =~ s/\s*-a\s*//;
L31: my ($fn, $rest) = split /\s+/, $line, 2;
L32: $fn = "$main::root/packclus/$fn" unless $fn =~ m|^/|;
L33: $fn =~ s/\.\.//g;
L34: $fn =~ s|/+|/|g;
L37: $fn =~ s/\s+//g;
L40: if ($rest =~ /^\s*\"/) {
L41: @cmd = split /\s*\"[\s,]?\"?/, $rest;
```

### Validation and access evidence

Source: `cmd/save.pl` · SHA-256 `84035b04b5b5e7a2c0f263a792d4579a125a5c0eefa3a5f517433308a99ef002`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
L16: if ($line =~ /-d/) { # add a date to the end of the filename
L20: if ($line =~ /-t/) { # add a time to the end of the filename
L24: if ($line =~ /-a/) { # append to the file
L32: $fn = "$main::root/packclus/$fn" unless $fn =~ m|^/|;
L40: if ($rest =~ /^\s*\"/) {
L45: open OF, "$app_req$fn" or return (1, $self->msg('e30', $fn));
L52: return (1, $self->msg('ok'));
```

### Output and error evidence

Source: `cmd/save.pl` · SHA-256 `84035b04b5b5e7a2c0f263a792d4579a125a5c0eefa3a5f517433308a99ef002`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
L45: open OF, "$app_req$fn" or return (1, $self->msg('e30', $fn));
L52: return (1, $self->msg('ok'));
```

### Message keys returned

`e30`, `e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/save.pl){ .md-button }

## Verify on a running node

```text
HELP SAVE
```

Compare the installed handler with this page when local overrides or a different revision may be present.