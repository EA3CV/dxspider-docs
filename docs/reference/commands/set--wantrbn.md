# `SET/WANTRBN`

<div class="command-meta" markdown>
<div>**Audience**  
<span class="badge-dual">User + SYSOP</span></div>
<div>**Privilege**  
`0 / 9`</div>
<div>**DXSpider**  
1.57 / Mojo ≥ 686</div>
</div>

## Purpose

User selects RBN categories; a privilege-9 targeted form is available to SYSOP.

## Syntax

```text
SET/WANTRBN [CW|BEACON|PSK|RTTY|FT|NONE ...]
```


## Audience-specific behaviour

This command has more than one access form. The normal-user and privileged forms are deliberately treated separately in this manual. Check the syntax shown by the running node with `HELP` before using the administrative form.

## Built-in help

On a running node, use:

```text
HELP SET/WANTRBN
```

The built-in help reflects the exact command set installed on that node.
