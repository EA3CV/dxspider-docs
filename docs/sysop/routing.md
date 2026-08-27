# Routing and protocol compatibility

DXSpider contains both modern routing behaviour and compatibility mechanisms accumulated over many years.

## PC92

PC92 is used for modern cluster configuration/user routing exchange. `SEND_CONFIG` can broadcast fresh PC92 C configuration records.

## Legacy compatibility

The command set still contains options such as:

```text
SET/SENDPC16
SET/WANTPC16
SET/WANTPC9X
SET/ROUTEPC19
```

These are compatibility controls, not recommendations for designing new systems.

!!! note "Historical help text"
    Some built-in help still describes routing filters using PC16/17/19/21/24/41/50 terminology. The new manual preserves those commands where they still exist but separates **current operation** from **legacy protocol background** instead of presenting old protocol descriptions as the modern architecture.

## Route filters

SYSOP route filters can be set for callsigns/defaults and input/output contexts with `ACCEPT/ROUTE`, `REJECT/ROUTE` and `CLEAR/ROUTE`.
