# Maintenance

Current DXSpider includes reload and asynchronous retrieval commands suitable for operational maintenance.

## Reload configuration/data

Examples:

```text
LOAD/ALIASES
LOAD/BADIP
LOAD/BANDS
LOAD/CMD_CACHE
LOAD/FORWARD
LOAD/HOPS
LOAD/KEPS
LOAD/MESSAGES
LOAD/PREFIXES
LOAD/USDB
```

## Download external data

```text
DOWNLOAD <url>
```

`DOWNLOAD` is asynchronous and is suitable for use from the DXSpider crontab. When scheduling downloads from shared public resources, spread requests across different minutes rather than causing every node to fetch at the same instant.

## Satellite data

```text
GET/KEPS
LOAD/KEPS
```

`GET/KEPS` fetches current data and, after a successful download, loads it.

## Duplicate state

`CLEAR/DUPEFILE` is a recovery tool, not routine maintenance. Repeatedly clearing duplicate state can cause additional network duplicates.
