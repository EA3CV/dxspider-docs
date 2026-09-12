# `CREATE/USER`

<div class="command-hero" markdown>

**Create this user from the User Database**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
CREATE/USER [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

```text
CREATE/USER <callsign> ...
```

**Create this user from the User Database**

## Details

This command will create one or more new users. None of the fields
like name, qth etc will be filled in. It is just a new entry in the user
database to which one can add more stuff like SET/PASSWORD or by SPOOF.

## Verify on a running node

```text
HELP CREATE/USER
```

Use the node help to check for local overrides or differences in another installed revision.