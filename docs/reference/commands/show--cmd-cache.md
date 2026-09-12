# `SHOW/CMD_CACHE`

<div class="command-hero" markdown>

**Show the real source path of commands**

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
SHOW/CMD_CACHE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/cmd_cache.pl` · SHA-256 `664a4a11dd2d41c356cb9d5fd8746c1a5a593805ed8308f70c228d37a67b246d`

```perl
L10: my $self = shift;
L11: my $line = shift;
L16: next if $line && $_ !~ m|\Q$line|i;
L18: $v =~ s|,|/|g;
```

### Validation and access evidence

Source: `cmd/show/cmd_cache.pl` · SHA-256 `664a4a11dd2d41c356cb9d5fd8746c1a5a593805ed8308f70c228d37a67b246d`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L16: next if $line && $_ !~ m|\Q$line|i;
```

### Output and error evidence

Source: `cmd/show/cmd_cache.pl` · SHA-256 `664a4a11dd2d41c356cb9d5fd8746c1a5a593805ed8308f70c228d37a67b246d`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9;
L19: push @out, sprintf "%-20s %s", $_, "$v.pl";
L22: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/CMD_CACHE [pattern]
```

**Show the real source path of commands**

## Details

It is possible in DXSpider to define local versions of commands.
Sometimes one forgets that one has these. This command will show you
the source path where the node is getting each one of its commands.

If you find a local command that you don't want then then simply
delete it, run LOAD/CMD_CACHE to clear out the command cache and
try again. You will now be using the standard version.

If you are looking for information on a specific command then
just add a string, eg:

```text
sh/cmd dx
```

might give you:

```text
Command              Path
set/dxgrid           /spider/cmd/set/dxgrid.pl
sh/dx                /spider/cmd/show/dx.pl
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/cmd_cache.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CMD_CACHE
```

Compare the installed handler with this page when local overrides or a different revision may be present.