# RBN / Skimmer

DXSpider can deliver curated Reverse Beacon Network / Skimmer spots separately from ordinary human-originated spots.

## Select RBN categories

```text
SET/WANTRBN
SET/WANTRBN CW
SET/WANTRBN PSK FT
UNSET/WANTRBN
```

The current command help recognises the principal categories:

```text
CW  BEACON  PSK  RTTY  FT
```

and synonyms including `BCN`, `DXF`, `FSK`, `MSK`, `FT8` and `FT4`.

`SET/SKIMMER` is an equivalent user-facing command name where that alias is installed.

## Filter RBN independently

```text
ACCEPT/RBN ...
REJECT/RBN ...
CLEAR/RBN ...
```

When a dedicated RBN filter exists, it is used for RBN traffic instead of the normal spot filter. If no dedicated RBN filter exists, normal spot filtering applies.

!!! note
    The SYSOP form of `SET/WANTRBN` can target another callsign. That syntax is documented only in the administration reference.
