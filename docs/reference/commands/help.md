# `HELP`

<div class="command-hero" markdown>

**The HELP Command**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
HELP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.

### Important calls

`CmdAlias::get_hlp()`, `defh->open()`, `h->open()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/help.pl` · SHA-256 `d64bbf17633776b677811f47bf093816b4b3a3113b7135ba7bfc45adf482f128`

```perl
L13: my ($self, $line) = @_;
L59: $line =~ s{[^\w/]}{}g;
L60: $line =~ s{/}{.*/}g;
L61: $line =~ s/^\s+//g;
L62: $line =~ s/[\s\r]+$//g;
L63: $line = "help" if $line =~ /^\s*$/;
L66: my $alias = CmdAlias::get_hlp($line);
L67: $line = $alias if $alias;
L73: next if $in =~ /^\#/;
L75: $in =~ s/\r$//;
L76: if ($in =~ /^===/) {
L78: $in =~ s/=== //;
L79: my ($priv, $cmd, $desc) = split /\^/, $in;
L81: next unless $cmd =~ /^$line/i;
L82: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
L100: next if $in =~ /^\#/;
L102: if ($in =~ /^===/) {
L104: $in =~ s/=== //;
L105: my ($priv, $cmd, $desc) = split /\^/, $in;
L107: next unless $cmd =~ /^$line/i;
L108: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
L119: push @out, $self->msg('helpe2', $line) if @out == 0;
```

### Validation and access evidence

Source: `cmd/help.pl` · SHA-256 `d64bbf17633776b677811f47bf093816b4b3a3113b7135ba7bfc45adf482f128`

```perl
L40: return (1, $self->msg('helpe1'));
L63: $line = "help" if $line =~ /^\s*$/;
L73: next if $in =~ /^\#/;
L76: if ($in =~ /^===/) {
L80: next if $priv > $self->priv; # ignore subcommands that are of no concern
L81: next unless $cmd =~ /^$line/i;
L82: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
L100: next if $in =~ /^\#/;
L102: if ($in =~ /^===/) {
L106: next if $priv > $self->priv; # ignore subcommands that are of no concern
L107: next unless $cmd =~ /^$line/i;
L108: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
```

### Output and error evidence

Source: `cmd/help.pl` · SHA-256 `d64bbf17633776b677811f47bf093816b4b3a3113b7135ba7bfc45adf482f128`

```perl
L40: return (1, $self->msg('helpe1'));
L82: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
L87: push @out, " $in";
L94: return (1, @out) if @out && $state == 2;
L108: push @out, "$cmd $desc" unless $cmd =~ /-$/o;
L113: push @out, " $in";
L119: push @out, $self->msg('helpe2', $line) if @out == 0;
L120: return (1, @out);
```

### Message keys returned

`helpe1`, `helpe2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
HELP
```

**The HELP Command**

## Details

HELP is available for a number of commands. The syntax is:-

```text
HELP <cmd>
```

Where <cmd> is the name of the command you want help on.

All commands can be abbreviated, so SHOW/DX can be abbreviated
to SH/DX, ANNOUNCE can be shortened to AN and so on.

Look at the APROPOS <string> command which will search the help database
for the <string> you specify and give you a list of likely commands
to look at with HELP.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/help.pl){ .md-button }

## Verify on a running node

```text
HELP HELP
```

Compare the installed handler with this page when local overrides or a different revision may be present.