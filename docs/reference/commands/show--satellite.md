# `SHOW/SATELLITE`

<div class="command-hero" markdown>

**Show tracking data**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/satellite.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SATELLITE
```

The built-in help is useful when checking the exact command set installed on a particular node.