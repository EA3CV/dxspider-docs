# Diagnostics

DXSpider exposes several levels of operational diagnostics.

## Connection and routing views

```text
SHOW/CONNECT
SHOW/NODE
SHOW/ROUTE
SHOW/PROGRAM
SHOW/DATA_STATS
```

## Internal state

```text
STAT/CHANNEL
STAT/DB
STAT/MSG
STAT/ROUTE_NODE
STAT/ROUTE_USER
STAT/USER
```

## Debug state

```text
SHOW/DEBUG_RING
SHOW/DUP_SPOTS
SHOW/DUP_ANN
SHOW/DUP_WWV
SHOW/DUP_WCY
```

Most internal diagnostics are privileged because they expose implementation state rather than normal user information.
