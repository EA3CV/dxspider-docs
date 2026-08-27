# Users and node types

Administrative commands define or change how a callsign is represented by DXSpider.

Common operations include:

```text
CREATE/USER <callsign>
DELETE/USER <callsign>
SET/USER <callsign>
SET/NODE <callsign>
SET/SPIDER <callsign>
SET/DXNET <callsign>
SET/ARCLUSTER <callsign>
SET/CCLUSTER <callsign>
SET/CLX <callsign>
SET/BBS <callsign>
SET/RBN <callsign>
```

The exact node type is operationally significant: neighbours can change protocol behaviour based on the type/capabilities advertised. Do not mark software as a node type whose protocol behaviour it does not implement.

Use `SHOW/NODE`, `SHOW/CONFIGURATION`, `SHOW/ROUTE` and the diagnostic `STAT/*` commands to inspect the resulting state.
