# `MSG`

<div class="command-hero" markdown>

**Alter various message parameters**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
MSG <cmd> <msgno> [data ... ]
```

**Alter various message parameters**

## Details

Alter message parameters like To, From, Subject, whether private or bulletin
or return receipt (RR) is required or whether to keep this message from timing
out.

```text
MSG TO <msgno> <call>     - change TO callsign to <call>
MSG FRom <msgno> <call>   - change FROM callsign to <call>
MSG PRrivate <msgno>      - set private flag
MSG NOPRrivate <msgno>    - unset private flag
MSG RR <msgno>            - set RR flag
MSG NORR <msgno>          - unset RR flag
MSG KEep <msgno>          - set the keep flag (message won't be deleted ever)
MSG NOKEep <msgno>        - unset the keep flag
MSG SUbject <msgno> <new> - change the subject to <new>
MSG WAittime <msgno>      - remove any waitting time for this message
MSG NOREad <msgno>        - mark message as unread
MSG REad <msgno>          - mark message as read
MSG QUeue                 - queue any outstanding bulletins
MSG QUeue 1               - queue any outstanding private messages
```

You can look at the status of a message by using:-

```text
STAT/MSG <msgno>
```

This will display more information on the message than DIR does.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/msg.pl){ .md-button }

## Verify on a running node

```text
HELP MSG
```

The built-in help is useful when checking the exact command set installed on a particular node.