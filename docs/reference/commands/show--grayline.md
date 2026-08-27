# `SHOW/GRAYLINE`

<div class="command-hero" markdown>

**Show Civil dawn/dusk times**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/grayline.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/GRAYLINE
```

The built-in help is useful when checking the exact command set installed on a particular node.