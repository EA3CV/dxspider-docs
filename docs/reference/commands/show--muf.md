# `SHOW/MUF`

<div class="command-hero" markdown>

**Show the likely propagation to a prefix**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/muf.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MUF
```

The built-in help is useful when checking the exact command set installed on a particular node.