# `DIRECTORY`

<div class="command-hero" markdown>

**Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Messages</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    DIRECTORY
    ```

    **List messages**


=== "User form"

    ```text
    DIRECTORY ALL
    ```

    **List all messages**


=== "User form"

    ```text
    DIRECTORY OWN
    ```

    **List your own messages**


=== "User form"

    ```text
    DIRECTORY NEW
    ```

    **List all new messages**


=== "User form"

    ```text
    DIRECTORY TO <call>
    ```

    **List all messages to <call>**


=== "User form"

    ```text
    DIRECTORY FROM <call>
    ```

    **List all messages from <call>**


=== "User form"

    ```text
    DIRECTORY SUBJECT <string>
    ```

    **List all messages with <string> in subject**


=== "User form"

    ```text
    DIRECTORY <nn>
    ```

    **List last <nn> messages**


=== "User form"

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

=== "SYSOP form"

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

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/directory.pl){ .md-button }

## Related commands

- [`READ`](read.md)
- [`SEND`](send.md)
- [`REPLY`](reply.md)
- [`KILL`](kill.md)

## Verify on a running node

```text
HELP DIRECTORY
```

The built-in help is useful when checking the exact command set installed on a particular node.