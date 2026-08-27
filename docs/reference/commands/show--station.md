# `SHOW/STATION`

<div class="command-meta" markdown>
<div>**Audience**  
<span class="badge-dual">User + SYSOP</span></div>
<div>**authorization **  
`0 / 6`</div>
<div>**DXSpider**  
1.57 / Mojo ≥ 686</div>
</div>

## Purpose

Normal lookup is user-level; SHOW/STATION ALL requires authorization .

## Syntax

```text
SHOW/STATION [<callsign> ...]
```


## Audience-specific behaviour

This command has more than one access form. The normal-user and authorization d forms are deliberately treated separately in this manual. Check the syntax shown by the running node with `HELP` before using the administrative form.

## Built-in help

On a running node, use:

```text
HELP SHOW/STATION
```

The built-in help reflects the exact command set installed on that node.
