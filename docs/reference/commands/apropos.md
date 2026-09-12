# `APROPOS`

<div class="command-hero" markdown>

**Search help database for <string>**

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
APROPOS [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.

### Important calls

`defh->open()`, `h->open()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/apropos.pl` · SHA-256 `3b331fa750e349f54c99b20685ec3b3487d0e6f3f77c469d3b8481fad0d494d2`

```perl
L11: my ($self, $line) = @_;
L19: $line = 'help' unless $line;
L20: $line =~ s/\ball\b/.*/;
L21: $line =~ s/\W//g; # remove dubious characters
L22: print "$line\n";
L46: next if $in =~ /^\#/;
L48: $in =~ s/\r$//;
L49: if ($in =~ /^===/) {
L51: ($priv, $cmd, $param, $desc) = $in =~ m{^===\s+(\d)\^(\S+)(\s+[^\^]+)?\^(.*)};
L55: next unless $in =~ /$line/i;
L56: next if $cmd =~ /-$/o;
L67: next if $in =~ /^\#/;
L69: $in =~ s/\r$//;
L70: if ($in =~ /^===/) {
L72: ($priv, $cmd, $param, $desc) = $in =~ m{^===\s+(\d)\^(\S+)(\s+[^\^]+)?\^(.*)};
L76: next unless $in =~ /$line/i;
L77: next if $cmd =~ /-$/o;
L94: push @out, $self->msg('helpe2', $line) if @out == 0;
```

### Validation and access evidence

Source: `cmd/apropos.pl` · SHA-256 `3b331fa750e349f54c99b20685ec3b3487d0e6f3f77c469d3b8481fad0d494d2`

```perl
L30: return (1, $self->msg('helpe1'));
L46: next if $in =~ /^\#/;
L49: if ($in =~ /^===/) {
L54: next if $priv > $self->priv; # ignore subcommands that are of no concern
L55: next unless $in =~ /$line/i;
L56: next if $cmd =~ /-$/o;
L67: next if $in =~ /^\#/;
L70: if ($in =~ /^===/) {
L75: next if $priv > $self->priv; # ignore subcommands that are of no concern
L76: next unless $in =~ /$line/i;
L77: next if $cmd =~ /-$/o;
```

### Output and error evidence

Source: `cmd/apropos.pl` · SHA-256 `3b331fa750e349f54c99b20685ec3b3487d0e6f3f77c469d3b8481fad0d494d2`

```perl
L30: return (1, $self->msg('helpe1'));
L88: push @out, @$v;
L90: push @out, @$v;
L94: push @out, $self->msg('helpe2', $line) if @out == 0;
L96: return (1, @out);
```

### Message keys returned

`helpe1`, `helpe2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
APROPOS <string>
```

**Search help database for <string>**

## Details

Search the help database for <string> (it isn't case sensitive), and print
the names of all the commands that may be relevant.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/apropos.pl){ .md-button }

## Verify on a running node

```text
HELP APROPOS
```

Compare the installed handler with this page when local overrides or a different revision may be present.