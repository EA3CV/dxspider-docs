# `SET/PASSWORD`

<div class="command-meta" markdown>
<div>**Audience**  
<span class="badge-dual">User + SYSOP</span></div>
<div>**authorization **  
`0 / 9`</div>
<div>**DXSpider**  
1.57 / Mojo ≥ 686</div>
</div>

## Purpose

Own-password form is user-level; targeted form requires authorization .

## Syntax

```text
SET/PASSWORD  |  SET/PASSWORD <callsign> <password>
```


## Audience-specific behaviour

This command has more than one access form. The normal-user and authorization d forms are deliberately treated separately in this manual. Check the syntax shown by the running node with `HELP` before using the administrative form.

## Built-in help

On a running node, use:

```text
HELP SET/PASSWORD
```

The built-in help reflects the exact command set installed on that node.
