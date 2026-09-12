# `SHOW/GRAYLINE`

<div class="command-hero" markdown>

**Show Civil dawn/dusk times**

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
SHOW/GRAYLINE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `Prefix::extract()`, `Sun::rise_set()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/grayline.pl` · SHA-256 `beadcef0d33e84bd5c6e275f28c26171e344ddbd852605996e989d5a42ed07dc`

```perl
L6: my ($self, $line) = @_;
L7: my @f = split /\s+/, $line;
L13: my @list;
L15: while ($f = shift @f){
L17: ($n_offset) = $f =~ /^([-+]?\d+)$/;
L20: push @list, $f;
L34: if (@list) {
L35: foreach $l (@list) {
L43: my $pre = shift @ans;
L65: $l->[3] =~ s{(-\d+|/\w+)$}{};
```

### Validation and access evidence

Source: `cmd/show/grayline.pl` · SHA-256 `beadcef0d33e84bd5c6e275f28c26171e344ddbd852605996e989d5a42ed07dc`

```perl
L22: $n_offset = 0 unless defined $n_offset;
```

### Output and error evidence

Source: `cmd/show/grayline.pl` · SHA-256 `beadcef0d33e84bd5c6e275f28c26171e344ddbd852605996e989d5a42ed07dc`

```perl
L60: push @out, $self->msg('grayline1');
L61: push @out, $self->msg('grayline2');
L66: push @out,sprintf("%-6.6s %-30.30s %02d/%02d/%4d %s %s %s %s", $l->[3], $l->[0], $day, $month, $yr, $dawn, $rise, $set, $dusk);
L70: return (1, @out);
```

### Message keys returned

`grayline1`, `grayline2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/GRAYLINE [ndays] [<prefix>|<callsign>]
```

**Show Civil dawn/dusk times**

## Details

This command is very similar to SHOW/SUN except that it shows the
start and end of "Official" or "Civil" Dawn and Dusk. This is defined
as when the Sun is 6 degrees below the horizon.

If you don't specify any prefixes or callsigns, it will show the
times for your QTH (assuming you have set it with either SET/LOCATION
or SET/QRA), together with the current azimuth and elevation.

If all else fails it will show the civil dawn and dusk times for
the node that you are connected to.

For example:-

```text
SH/GRAYLINE
SH/GRAYLINE G1TLH W5UN
```

You can also use this command to see into the past or the future, so
if you want to see yesterday's times then do:-

```text
SH/GRAYLINE -1
```

or in three days time:-

```text
SH/GRAYLINE +3 W9
```

Upto 366 days can be checked both in the past and in the future.

Please note that the times are given as the UT times of the requested
UT day.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/grayline.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/GRAYLINE
```

Compare the installed handler with this page when local overrides or a different revision may be present.