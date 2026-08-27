# RBN administration

RBN support is a first-class part of current DXSpider.

Useful administration commands include:

```text
SET/RBN <callsign>
SHOW/RBN [ALL]
SET/WANTRBN <callsign> ...
```

Normal users select the RBN categories they want and may maintain separate RBN filters. The administration forms allow a SYSOP to inspect or configure relevant state for other callsigns.

Keep HUMAN and RBN traffic conceptually distinct when designing external applications: RBN is a continuous data feed, not a reason to repeatedly log in, issue `SHOW/DX`, disconnect and reconnect.
