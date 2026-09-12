# `SHOW/SATELLITE`

<div class="command-hero" markdown>

**Show tracking data**

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
SHOW/SATELLITE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Sun::Calendar_date_and_time_from_JD()`, `Sun::Julian_Date_of_Epoch()`, `Sun::Julian_Day()`, `Sun::get_satellite_pos()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/satellite.pl` · SHA-256 `bdaf05a11fedccc5fa03cafb739386f92ecb062e4bda72c5bb33e31e9347c575`

```perl
L15: my ($self, $line) = @_;
L18: my @f = split /\s+/, $line;
L19: my $satname = uc shift @f if @f;
L20: my $numhours = shift @f if @f; # the number of hours ahead to print
L21: my $step = shift @f if @f; # tracking table resolution in minutes
L24: $numhours = 3 unless $numhours && $numhours =~ /^\d+$/;
L27: $step = 5 unless $step && $step =~ /^\d+$/;
```

### Validation and access evidence

Source: `cmd/show/satellite.pl` · SHA-256 `bdaf05a11fedccc5fa03cafb739386f92ecb062e4bda72c5bb33e31e9347c575`

```perl
L24: $numhours = 3 unless $numhours && $numhours =~ /^\d+$/;
L27: $step = 5 unless $step && $step =~ /^\d+$/;
```

### Output and error evidence

Source: `cmd/show/satellite.pl` · SHA-256 `bdaf05a11fedccc5fa03cafb739386f92ecb062e4bda72c5bb33e31e9347c575`

```perl
L56: push @out, $self->msg("pos", $call, slat($lat), slong($lon));
L57: push @out, $self->msg("sat1", $satname, $numhours, $step);
L58: push @out, $self->msg("sat2");
L62: push @out,sprintf("Now %2.2d:%2.2d %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f",
L76: push @out, $self->msg("satdisc");
L78: push @out,sprintf("%2.2d/%2.2d %2.2d:%2.2d %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f",
L88: push @out, $self->msg("satnf", $satname) if $satname;
L89: push @out, $self->msg("sat3");
L90: push @out, $self->msg("sat4");
L96: push @out,join ' ', @l;
L106: push @out, join ' ', @l;
L109: return (1,@out);
```

### Message keys returned

`pos`, `sat1`, `sat2`, `sat3`, `sat4`, `satdisc`, `satnf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/SATELLITE <name> [<hours> <interval>]
```

**Show tracking data**

## Details

Show the tracking data from your location to the satellite of your choice
from now on for the next few hours.

If you use this command without a satellite name it will display a list
of all the satellites known currently to the system.

If you give a name then you can obtain tracking data of all the passes
that start and finish 5 degrees below the horizon. As default it will
give information for the next three hours for every five minute period.

You can alter the number of hours and the step size, within certain
limits.

Each pass in a period is separated with a row of '-----' characters

So for example:-

 SH/SAT AO-10
 SH/SAT FENGYUN1 12 2

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/satellite.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SATELLITE
```

Compare the installed handler with this page when local overrides or a different revision may be present.