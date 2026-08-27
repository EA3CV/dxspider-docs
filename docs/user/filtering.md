# Filtering

DXSpider uses **accept** and **reject** filters. Filters can contain numbered lines and can match fields such as callsign, origin, zone, DXCC entity, state, frequency/band and other fields supported by the relevant filter family.

## Main user filter families

| Traffic | Accept | Reject | Clear |
|---|---|---|---|
| DX spots | `ACCEPT/SPOTS` | `REJECT/SPOTS` | `CLEAR/SPOTS` |
| RBN spots | `ACCEPT/RBN` | `REJECT/RBN` | `CLEAR/RBN` |
| Announcements | `ACCEPT/ANNOUNCE` | `REJECT/ANNOUNCE` | `CLEAR/ANNOUNCE` |
| WWV | `ACCEPT/WWV` | `REJECT/WWV` | `CLEAR/WWV` |
| WCY | `ACCEPT/WCY` | `REJECT/WCY` | `CLEAR/WCY` |

Example:

```text
ACCEPT/SPOTS 1 ON HF/CW
ACCEPT/SPOTS 2 ON VHF AND (BY_ZONE 14,15,16 OR CALL_ZONE 14,15,16)
```

Remove one line:

```text
CLEAR/SPOTS 1
```

Remove the complete filter:

```text
CLEAR/SPOTS ALL
```

!!! warning "Routing filters"
    Route filters also exist, including administrative forms. Historical help text describes parts of route filtering using legacy PC records. The modern manual therefore treats routing filters as an administration topic rather than copying that historical explanation unchanged.
