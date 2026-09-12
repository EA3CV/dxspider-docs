# `SHOW/MUF`

<div class="command-hero" markdown>

**Show the likely propagation to a prefix**

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
SHOW/MUF [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXBearing::bdist()`, `DXBearing::lltos()`, `Minimuf::ds()`, `Minimuf::ion()`, `Minimuf::minimuf()`, `Minimuf::pathloss()`, `Minimuf::spots()`, `Minimuf::zenith()`, `Prefix::extract()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/muf.pl` · SHA-256 `9a94c33e3e31c1a6213dde2a57b53d6383ec77acf548e550b92221258e5b1cc2`

```perl
L14: my ($self, $line) = @_;
L15: my @f = split /\s+/, $line;
L17: my $prefix = uc shift @f;
L23: my $f = shift @f;
L24: $lp++ if $f =~ /^l/;
L25: $hr2 = $f if $f =~ /^\d+$/;
L192: $out =~ s/\s+$//;
```

### Validation and access evidence

Source: `cmd/show/muf.pl` · SHA-256 `9a94c33e3e31c1a6213dde2a57b53d6383ec77acf548e550b92221258e5b1cc2`

```perl
L18: return (1, $self->msg('e4')) unless $prefix;
L24: $lp++ if $f =~ /^l/;
L25: $hr2 = $f if $f =~ /^\d+$/;
```

### Output and error evidence

Source: `cmd/show/muf.pl` · SHA-256 `9a94c33e3e31c1a6213dde2a57b53d6383ec77acf548e550b92221258e5b1cc2`

```perl
L18: return (1, $self->msg('e4')) unless $prefix;
L44: push @out, $self->msg('heade1');
L124: push @out, sprintf("RxSens: $rsens dBM SFI:%4.0f R:%4.0f Month: $month Day: $day", $flux, $ssn);
L125: push @out, sprintf("Power : %3.0f dBW Distance:%6.0f km Delay:%5.1f ms", $dB1, $d * $R, $delay);
L126: push @out, sprintf("Location Lat / Long Azim");
L127: push @out, sprintf("%-30.30s %-18s %3.0f", $loc1, DXBearing::lltos($lat1*$r2d, -$lon1*$r2d), $b1 * $r2d);
L128: push @out, sprintf("%-30.30s %-18s %3.0f", $a->name, DXBearing::lltos($lat2*$r2d, -$lon2*$r2d), $b2 * $r2d);
L133: push @out, $head;
L193: push @out, $out;
L196: return (1, @out);
```

### Message keys returned

`e4`, `heade1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/MUF <prefix> [<hours>][long]
```

**Show the likely propagation to a prefix**

## Details

This command allow you to estimate the likelihood of you contacting
a station with the prefix you have specified. The output assumes a modest
power of 20dBW and receiver sensitivity of -123dBm (about 0.15muV/10dB SINAD)

The result predicts the most likely operating frequencies and signal
levels for high frequency (shortwave) radio propagation paths on
specified days of the year and hours of the day. It is most useful for
paths between 250 km and 6000 km, but can be used with reduced accuracy
for paths shorter or longer than this.

The command uses a routine MINIMUF 3.5 developed by the U.S. Navy and
used to predict the MUF given the predicted flux, day of the year,
hour of the day and geographic coordinates of the transmitter and
receiver. This routine is reasonably accurate for the purposes here,
with a claimed RMS error of 3.8 MHz, but much smaller and less complex
than the programs used by major shortwave broadcasting organizations,
such as the Voice of America.

The command will display some header information detailing its
assumptions, together with the locations, latitude and longitudes and
bearings. It will then show UTC (UT), local time at the other end
(LT), calculate the MUFs, Sun zenith angle at the midpoint of the path
(Zen) and the likely signal strengths. Then for each frequency for which
the system thinks there is a likelihood of a circuit it prints a value.

The value is currently a likely S meter reading based on the conventional
6dB / S point scale. If the value has a '+' appended it means that it is
1/2 an S point stronger. If the value is preceeded by an 'm' it means that
there is likely to be much fading and by an 's' that the signal is likely
to be noisy.

By default SHOW/MUF will show the next two hours worth of data. You
can specify anything up to 24 hours worth of data by appending the no of
hours required after the prefix. For example:-

```text
SH/MUF W
```

produces:

```text
RxSens: -123 dBM SFI: 159   R: 193   Month: 10   Day: 21
Power :   20 dBW    Distance:  6283 km    Delay: 22.4 ms
Location                       Lat / Long           Azim
East Dereham, Norfolk          52 41 N 0 57 E         47
United-States-W                43 0 N 87 54 W        299
UT LT  MUF Zen  1.8  3.5  7.0 10.1 14.0 18.1 21.0 24.9 28.0 50.0
18 23 11.5 -35  mS0+ mS2   S3
19  0 11.2 -41  mS0+ mS2   S3
```

indicating that you will have weak, fading circuits on top band and
80m but usable signals on 40m (about S3).

inputing:-

```text
SH/MUF W 24
```

will get you the above display, but with the next 24 hours worth of
propagation data.

```text
SH/MUF W L 24
SH/MUF W 24 Long
```

Gives you an estimate of the long path propagation characterics. It
should be noted that the figures will probably not be very useful, nor
terrible accurate, but it is included for completeness.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/muf.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MUF
```

Compare the installed handler with this page when local overrides or a different revision may be present.