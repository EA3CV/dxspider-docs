# Messages

DXSpider includes a message system for personal messages and bulletins.

```text
DIRECTORY
READ
READ <message-number>
SEND <callsign>
REPLY
KILL <message-number>
```

`SEND` supports qualifiers for personal messages, bulletins, copies and read receipts. Common aliases such as `SP` and `SB` may also be available.

A normal user can only read or delete messages permitted by the message rules. SYSOP commands have broader scope and are documented separately.
