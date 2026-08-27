# Filter language

DXSpider filters are ordered rule sets. A rule can **accept** or **reject** traffic and can be placed on a numbered line, normally `0`–`9`.

## The mental model

```text
traffic → rule 1 → rule 2 → ... → accept/reject
```

A filter expression combines fields with boolean operators:

```text
AND
OR
(...)
```

For example:

```text
ACCEPT/SPOTS 1 ON HF/CW
ACCEPT/SPOTS 2 ON VHF AND (BY_ZONE 14,15,16 OR CALL_ZONE 14,15,16)
```

## Spot / RBN fields

| Field | Meaning | Example |
|---|---|---|
| `freq` / `on` | Frequency range, band or sub-band | `ON HF/CW`, `ON 6M`, `FREQ 0/30000` |
| `call` | Spotted callsign/prefix | `CALL G,PA,HB9` |
| `info` | Text in the spot information/comment | `INFO IOTA` |
| `by` | Spotter callsign/prefix | `BY G,M,2` |
| `call_dxcc` | DXCC of spotted station | `CALL_DXCC 61,62` |
| `call_itu` | ITU zone of spotted station | `CALL_ITU 27,28` |
| `call_zone` | CQ zone of spotted station | `CALL_ZONE 14,15,16` |
| `call_state` | US state of spotted station | `CALL_STATE VA,NH,RI` |
| `by_dxcc` | DXCC of spotter | `BY_DXCC 223` |
| `by_itu` | ITU zone of spotter | `BY_ITU 27` |
| `by_zone` | CQ zone of spotter | `BY_ZONE 14,15,16` |
| `by_state` | US state of spotter | `BY_STATE VA,NH,RI,MA,ME` |
| `origin` | Node/interface from which traffic arrived | `ORIGIN GB7DJK` |
| `channel` | Input channel/source | `CHANNEL ...` |
| `all` | Match everything | `ALL` |

Band names come from `SHOW/BANDS`; sub-band notation such as `HF/CW`, `HF/SSB`, `RTTY` and `DATA` can be used where defined by the installed band data.

## Announce fields

Announcement filters support fields including:

```text
INFO
BY
ORIGIN
ORIGIN_DXCC
ORIGIN_ITU
ORIGIN_ZONE
ORIGIN_STATE
BY_DXCC
BY_ITU
BY_ZONE
BY_STATE
CHANNEL
WX
DEST
```

Example:

```text
ACCEPT/ANNOUNCE DEST 6MUK
ACCEPT/ANNOUNCE 2 BY_ZONE 14,15,16
```

## Numbered lines

Rules can be maintained individually:

```text
ACCEPT/SPOTS 1 ON HF/CW
ACCEPT/SPOTS 2 ON VHF
CLEAR/SPOTS 1
```

After the clear, line 2 remains.

To remove the whole filter:

```text
CLEAR/SPOTS ALL
```

## Accept versus reject

An **accept** filter expresses what should pass; a **reject** filter expresses what should be blocked. Keep rules small and explicit. Complex filters are easier to maintain when split across numbered lines rather than compressed into one opaque expression.

## RBN filters

RBN has its own `ACCEPT/RBN`, `REJECT/RBN` and `CLEAR/RBN` family. A dedicated RBN filter takes precedence for RBN traffic; if no RBN-specific filter exists, normal spot filtering applies.

!!! tip "Debugging a filter"
    Build the filter one rule at a time, then use `SHOW/FILTER` to inspect the installed result. If a rule behaves unexpectedly, simplify the expression before adding additional `AND`/`OR` clauses.
