# `SET/PINGINTERVAL`

<div class="command-hero" markdown>

**Set ping time to neighbouring nodes**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SET/PINGINTERVAL <time> <nodecall>
```

**Set ping time to neighbouring nodes**

## Details

As from release 1.35 all neighbouring nodes are pinged at regular intervals
in order to determine the rolling quality of the link and, in future, to
affect routing decisions. The default interval is 300 secs or 5 minutes.

You can use this command to set a different interval. Please don't.

But if you do the value you enter is treated as minutes up 30 and seconds
for numbers greater than that.

This is used also to help determine when a link is down at the far end
(as certain cluster software doesn't always notice), see SET/OBSCOUNT
for more information.

If you must change it (and it may be useful for internet connected nodes
on dynamic IP addresses that go away after a set time of usage) the time
can be specified as:-

```text
5      which if less than 30 is converted to minutes otherwise is
       taken as the no of seconds between pings.
120s   120 seconds
5m     5 minutes
1h     1 hour
```

Please be aware that this causes traffic to occur on the link, setting
this value too low may annoy your neighbours beyond the point of
endurance!

You can switch this off by setting it to 0.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/pinginterval.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PINGINTERVAL
```

The built-in help is useful when checking the exact command set installed on a particular node.