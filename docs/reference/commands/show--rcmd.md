# `SHOW/RCMD`

<div class="command-hero" markdown>

**Show log of rcmds**

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
SHOW/RCMD
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/rcmd.pl` · SHA-256 `542d49ffe22e5ad597ba79f962ff3727f5051f2e7ffc057908e9ce6a094466aa`

```perl
L8: my $self = shift;
L12: my $cmdline = shift;
L13: my @f = split /\s+/, $cmdline;
L19: while ($f = shift @f) { # next field
L22: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L26: ($to) = $f =~ /^(\d+)$/o if !$to; # is it a to count?
```

### Validation and access evidence

Source: `cmd/show/rcmd.pl` · SHA-256 `542d49ffe22e5ad597ba79f962ff3727f5051f2e7ffc057908e9ce6a094466aa`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
L30: if ($f !~ /^\d+$/) {
```

### Output and error evidence

Source: `cmd/show/rcmd.pl` · SHA-256 `542d49ffe22e5ad597ba79f962ff3727f5051f2e7ffc057908e9ce6a094466aa`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 9;
L38: return (1, DXLog::print($from, $to, $main::systime, 'rcmd', $who)) if ($self->{_nospawn} || $main::is_win == 1);
L39: return (1, $self->spawn_cmd("show/rcmd $cmdline", \&DXLog::print, args => [$from, $to, $main::systime, 'rcmd', $who]));
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/RCMD [<n>][<from>-<to>][<call>] ...
```

**Show log of rcmds**

## Details

Show the rcmds that have come in and their replies.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/rcmd.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/RCMD
```

Compare the installed handler with this page when local overrides or a different revision may be present.