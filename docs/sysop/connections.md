# Connections

## Connect

```text
CONNECT <callsign>
```

Starts the configured outbound connection procedure for a node.

## Disconnect

```text
DISCONNECT <callsign>
DISCONNECT USERS
DISCONNECT NODES
DISCONNECT ALL
```

`DISCONNECT` requires higher administrative authorization than `CONNECT`.

## Link recovery

`INIT`, `RINIT` and `SEND_CONFIG` are recovery/resynchronisation tools for specific protocol/link situations.

```text
INIT <node>
RINIT <node>
SEND_CONFIG
```

`SEND_CONFIG` broadcasts PC92 C configuration records and is the PC92-oriented resynchronisation operation.
