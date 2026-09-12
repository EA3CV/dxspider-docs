# `SHOW/PROGRAM`

<div class="command-hero" markdown>

**Show the locations of all the included program modules**

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
SHOW/PROGRAM
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/program.pl` · SHA-256 `13f3cea4ad0954af6c7d397c4b14a6d998a74afff3e321cb9b9bc0c37bc69383`

```perl
L8: my $self = shift;
L13: push @out, "$_ => $INC{$_}" if $INC{$_} =~ /spider/o;
```

### Validation and access evidence

Source: `cmd/show/program.pl` · SHA-256 `13f3cea4ad0954af6c7d397c4b14a6d998a74afff3e321cb9b9bc0c37bc69383`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 5;
L13: push @out, "$_ => $INC{$_}" if $INC{$_} =~ /spider/o;
```

### Output and error evidence

Source: `cmd/show/program.pl` · SHA-256 `13f3cea4ad0954af6c7d397c4b14a6d998a74afff3e321cb9b9bc0c37bc69383`

```perl
L9: return (1, $self->msg('e5')) if $self->priv < 5;
L13: push @out, "$_ => $INC{$_}" if $INC{$_} =~ /spider/o;
L16: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/PROGRAM
```

**Show the locations of all the included program modules**

## Details

Show the name and location where every program module was load from. This
is useful for checking where you think you have loaded a .pm file from.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/program.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/PROGRAM
```

Compare the installed handler with this page when local overrides or a different revision may be present.