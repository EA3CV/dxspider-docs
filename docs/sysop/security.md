# Privileges and security

DXSpider command help defines the traditional privilege levels used by the command dispatcher:

| Level | Meaning |
|---:|---|
| 0 | Normal user |
| 1 | Limited privileged/remote-node operations |
| 5 | Common node/SYSOP operations |
| 8 | Higher administrative operations |
| 9 | Local full SYSOP |

A remote login normally starts with reduced privilege. The `SYSOP` challenge command is used to regain configured privileges.

```text
SYSOP
```

Manage stored privilege levels with:

```text
SET/PRIVILEGE <level> <callsign>
```

Drop privilege for the current session with:

```text
UNSET/PRIVILEGE
```

!!! danger
    Do not assign privilege 9 to remote users or nodes. Commands at this level include operations that can change files, internal state or execute highly privileged administrative actions.

## Internal commands

A small number of source-tree commands are intentionally **not** presented as normal supported administration commands. This includes no-op placeholders and commands whose implementation exposes raw internal execution/state. They remain listed in the maintainer audit but are hidden from the public command indexes.
