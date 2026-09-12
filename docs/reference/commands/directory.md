# `DIRECTORY`

<div class="command-hero" markdown>

**Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Messages</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DIRECTORY [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

### Available options and values

`<`, `>`, `ALL`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    DIRECTORY
    ```

    **List messages**


=== "Available form"

    ```text
    DIRECTORY ALL
    ```

    **List all messages**


=== "Available form"

    ```text
    DIRECTORY OWN
    ```

    **List your own messages**


=== "Available form"

    ```text
    DIRECTORY NEW
    ```

    **List all new messages**


=== "Available form"

    ```text
    DIRECTORY TO <call>
    ```

    **List all messages to <call>**


=== "Available form"

    ```text
    DIRECTORY FROM <call>
    ```

    **List all messages from <call>**


=== "Available form"

    ```text
    DIRECTORY SUBJECT <string>
    ```

    **List all messages with <string> in subject**


=== "Available form"

    ```text
    DIRECTORY <nn>
    ```

    **List last <nn> messages**


=== "Available form"

    ```text
    DIRECTORY <from>-<to>
    ```

    **List messages <from> message <to> message**

    List the messages in the messages directory.

    If there is a 'p' one space after the message number then it is a
    personal message. If there is a '-' between the message number and the
    'p' then this indicates that the message has been read.

    You can use shell escape characters such as '*' and '?' in the <call>
    fields.

    You can combine some of the various directory commands together eg:-

    ```text
     DIR TO G1TLH 5
    ```
    or
    ```text
     DIR SUBJECT IOTA 200-250
    ```

    You can abbreviate all the commands to one letter and use ak1a syntax:-

    ```text
     DIR/T G1* 10
     DIR/S QSL 10-100 5
    ```

=== "Available form"

    ```text
    DIRECTORY-
    ```

    ****

    Sysops can see all users' messages.

## When would I use this?

DIRECTORY is the entry point to the message system. Its selectors can be combined instead of scrolling through an undifferentiated list.

## Practical examples

### List messages

```text
DIRECTORY
```

### Your own messages

```text
DIRECTORY OWN
```

### New messages

```text
DIRECTORY NEW
```

### Messages to a callsign

```text
DIRECTORY TO G1TLH 5
```

### Subject search within a range

```text
DIRECTORY SUBJECT IOTA 200-250
```

### Wildcard callsign search

```text
DIR/T G1* 10
```

## Related commands

- [`READ`](read.md)
- [`SEND`](send.md)
- [`REPLY`](reply.md)
- [`KILL`](kill.md)

## Verify on a running node

```text
HELP DIRECTORY
```

Use the node help to check for local overrides or differences in another installed revision.