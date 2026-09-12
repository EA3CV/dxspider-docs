# `SHOW/TALK`

<div class="command-hero" markdown>

**print out the general log file for talks only print "f: $f list: ", join(',', @list), "\n"; ($who) = $f =~ /^(\w+)/o;**

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
SHOW/TALK
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/talk.pl` · SHA-256 `88c8167d14c365314d5744e619fc6185ccb894ce07277be9120d03c960e77753`

```perl
L8: my $self = shift;
L10: my $cmdline = shift;
L11: my @f = split /\s+/, $cmdline;
L17: while ($f = shift @f) { # next field
L20: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L24: ($to) = $f =~ /^(\d+)$/o if !$to; # is it a to count?
```

### Validation and access evidence

Source: `cmd/show/talk.pl` · SHA-256 `88c8167d14c365314d5744e619fc6185ccb894ce07277be9120d03c960e77753`

```perl
L28: if ($f !~ /^\d+/) {
L36: if ($self->priv < 6) {
L38: return (1, $self->msg('e5')) if $who ne $self->call;
```

### Output and error evidence

Source: `cmd/show/talk.pl` · SHA-256 `88c8167d14c365314d5744e619fc6185ccb894ce07277be9120d03c960e77753`

```perl
L38: return (1, $self->msg('e5')) if $who ne $self->call;
L41: return (1, DXLog::print($from, $to, $main::systime, 'talk', $who)) if ($self->{_nospawn} || $main::is_win == 1);
L42: return (1, $self->spawn_cmd("show/talk $cmdline", \&DXLog::print, args => [$from, $to, $main::systime, 'talk', $who]));
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/talk.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/TALK
```

Compare the installed handler with this page when local overrides or a different revision may be present.