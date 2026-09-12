# `SET/BADIP`

<div class="command-hero" markdown>

**Stop logins and spots with this IP address**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/BADIP [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

```text
SET/BADIP <ip address>..
```

**Stop logins and spots with this IP address**

## Details

This command will prevent logins to this node from this IP address.
It will also drop spots (PC61) from this address thus preventing them
from being propagated.

```text
set/badip 217.61.58.23
```

## Verify on a running node

```text
HELP SET/BADIP
```

Use the node help to check for local overrides or differences in another installed revision.