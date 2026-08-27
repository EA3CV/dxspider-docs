# DX spots

## Sending a spot

```text
DX <frequency> <callsign> [remarks]
```

Frequency and callsign can be entered in the forms accepted by the node. Remarks are appended to the spot.

## Reviewing spots

```text
SHOW/DX
```

`SHOW/DX` supports additional selectors and limits. Use the command reference or built-in `HELP SHOW/DX` for the full syntax available on the running node.

## Personal filtering

Use `ACCEPT/SPOTS`, `REJECT/SPOTS` and `CLEAR/SPOTS` to control which spots reach your session.

```text
ACCEPT/SPOTS 1 ON HF/CW
REJECT/SPOTS 2 BY_ZONE 14,15,16
CLEAR/SPOTS ALL
```

The filter engine is shared with other DXSpider filter families. See [Filtering](filtering.md).
