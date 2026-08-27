# `CREATE/USER`

<div class="command-hero" markdown>

**Create this user from the User Database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
CREATE/USER <callsign> ...
```

**Create this user from the User Database**

## Details

This command will create one or more new users. None of the fields
like name, qth etc will be filled in. It is just a new entry in the user
database to which one can add more stuff like SET/PASSWORD or by SPOOF.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/create/user.pl){ .md-button }

## Verify on a running node

```text
HELP CREATE/USER
```

The built-in help is useful when checking the exact command set installed on a particular node.