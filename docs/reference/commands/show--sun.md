# `SHOW/SUN`

<div class="command-hero" markdown>

**Show sun rise and set times**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/SUN [ndays] [<prefix>|<callsign>]
```

**Show sun rise and set times**

## Details

Show the sun rise and set times for a (list of) prefixes or callsigns,
together with the azimuth and elevation of the sun currently at those
locations.

If you don't specify any prefixes or callsigns, it will show the times for
your QTH (assuming you have set it with either SET/LOCATION or SET/QRA),
together with the current azimuth and elevation.

If all else fails it will show the sunrise and set times for the node
that you are connected to.

For example:-

```text
SH/SUN
SH/SUN G1TLH K9CW ZS
```

You can also use this command to see into the past or the future, so
if you want to see yesterday's times then do:-

```text
SH/SUN -1
```

or in three days time:-

```text
SH/SUN +3 W9
```

Upto 366 days can be checked both in the past and in the future.

Please note that the rise and set times are given as the UTC times of rise and
set on the requested UTC day UNLESS you add the keyword 'local' (without quotes)
to the list of callsigns e.g:

```text
SH/SUN G1TLH W5UN local
SH/SUN  LOCAL G1TLH W5UN
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/sun.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SUN
```

The built-in help is useful when checking the exact command set installed on a particular node.