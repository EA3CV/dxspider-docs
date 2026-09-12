# `SEND`

<div class="command-hero" markdown>

**Send a message to one or more callsigns**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SEND <structured arguments>
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Available options and values

`.#`, `<`, `B`, `C`, `CC`, `COPY`, `P`, `RR`, `SYSOP`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    SEND <call> [<call> ...]
    ```

    **Send a message to one or more callsigns**


=== "Available form"

    ```text
    SEND RR <call>
    ```

    **Send a message and ask for a read receipt**


=== "Available form"

    ```text
    SEND COPY <msgno> <call>
    ```

    **Send a copy of a  message to someone**


=== "Available form"

    ```text
    SEND PRIVATE <call>
    ```

    **Send a personal message**


=== "Available form"

    ```text
    SEND NOPRIVATE <call>
    ```

    **Send a message to all stations**

    All the SEND commands will create a message which will be sent either to
    an individual callsign or to one of the 'bulletin' addresses.

    SEND <call> on its own acts as though you had typed SEND PRIVATE, that is
    it will mark the message as personal and send it to the cluster node that
    that callsign is connected to. If the <call> you have specified is in fact
    a known bulletin category on your node (eg: ALL) then the message should
    automatically become a bulletin.

    You can have more than one callsign in all of the SEND commands.

    You can have multiple qualifiers so that you can have for example:-

    ```text
    SEND RR COPY 123 PRIVATE G1TLH G0RDI
    ```

    which should send a copy of message 123 to G1TLH and G0RDI and you will
    receive a read receipt when they have read the message.

    SB is an alias for SEND NOPRIVATE (or send a bulletin in BBS speak)
    SP is an alias for SEND PRIVATE

    The system will ask you for a subject. Conventionally this should be
    no longer than 29 characters for compatibility. Most modern cluster
    software should accept more.

    You will now be prompted to start entering your text.

    You finish the message by entering '/EX' on a new line. For instance:

    ```text
    ...
    bye then Jim
    73 Dirk
    /ex
    ```

    If you have started a message and you don't want to keep it then you
    can abandon the message with '/ABORT' on a new line, like:-

    ```text
    line 1
    line 2
    oh I just can't be bothered with this
    /abort
    ```

    If you abort the message it will NOT be sent.

    When you are entering the text of your message, most normal output (such
    as DX announcements and so on are suppressed and stored for latter display
    (upto 20 such lines are stored, as new ones come along, so the oldest
    lines are dropped).

    Also, you can enter normal commands commands (and get the output
    immediately) whilst in the middle of a message. You do this by typing
    the command preceeded by a '/' character on a new line, so:-

    ```text
    /dx g1tlh 144010 strong signal
    ```

    Will issue a dx annoucement to the rest of the cluster.

    Also, you can add the output of a command to your message by preceeding
    the command with '//', thus :-

    ```text
    //sh/vhftable
    ```

    This will show YOU the output from SH/VHFTABLE and also store it in the
    message.

    You can carry on with the message until you are ready to send it.

## Verify on a running node

```text
HELP SEND
```

Use the node help to check for local overrides or differences in another installed revision.