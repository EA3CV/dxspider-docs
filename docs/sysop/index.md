# SYSOP / Administration

This section is for DXSpider node administrators.

## Administration topics

- [Installation and web documentation deployment](installation.md)
- [authorization model and security](security.md)
- [Users and node types](users-nodes.md)
- [Connections](connections.md)
- [Routing and protocol compatibility](routing.md)
- [RBN administration](rbn.md)
- [Maintenance and reload operations](maintenance.md)
- [Diagnostics](diagnostics.md)
- [SYSOP command reference](commands/index.md)

!!! warning
    authorization is part of the command contract. A command with authorization is not automatically “non-administrative”; for example, `SYSOP` is invoked from a remote login at authorization specifically to regain configured authorization s after authentication.
