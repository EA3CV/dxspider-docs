# `DELETE/USER`

<div class="command-hero" markdown>

**Delete this user from the User Database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
DELETE/USER <callsign> ...
```

**Delete this user from the User Database**

## Details

This command will completely remove a one or more users from the database.

There is NO SECOND CHANCE.

It goes without saying that you should use this command CAREFULLY!

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/delete/user.pl){ .md-button }

## Verify on a running node

```text
HELP DELETE/USER
```

The built-in help is useful when checking the exact command set installed on a particular node.