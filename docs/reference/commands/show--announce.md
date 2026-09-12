# `SHOW/ANNOUNCE`

<div class="command-hero" markdown>

**Show log of announces**

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
SHOW/ANNOUNCE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `DXLog::print_item()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/announce.pl` · SHA-256 `9cca0642748aff3db6fc2556568f679b574a74158be30b4d3c9b9525309bdc93`

```perl
L8: my $self = shift;
L13: my $cmdline = shift;
L14: my @f = split /\s+/, $cmdline;
L20: while ($f = shift @f) { # next field
L23: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L27: ($to) = $f =~ /^(\d+)$/o if !$to; # is it a to count?
```

### Validation and access evidence

Source: `cmd/show/announce.pl` · SHA-256 `9cca0642748aff3db6fc2556568f679b574a74158be30b4d3c9b9525309bdc93`

```perl
L31: if ($f !~ /^\d+/) {
L34: if ($f !~ /^\d+/) {
```

### Output and error evidence

Source: `cmd/show/announce.pl` · SHA-256 `9cca0642748aff3db6fc2556568f679b574a74158be30b4d3c9b9525309bdc93`

```perl
L47: push @out, DXLog::print_item($_);
L49: return (1, @out);
L52: return (1, DXLog::print($from, $to, $main::systime, 'ann', $who)) if ($self->{_nospawn} || $main::is_win == 1) || $DB::VERSION;
L53: return (1, $self->spawn_cmd("show/announce $cmdline", \&DXLog::print, args => [$from, $to, $main::systime, 'ann', $who]));
L55: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/ANNOUNCE [<n>][<from>-<to>][<call>] ...
```

**Show log of announces**

## Details

Show announcements that have come in.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/announce.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/ANNOUNCE
```

Compare the installed handler with this page when local overrides or a different revision may be present.