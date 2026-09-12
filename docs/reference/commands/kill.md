# `KILL`

<div class="command-hero" markdown>

**Delete a message from the local system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
KILL [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command forms and examples

=== "Available form"

    ```text
    KILL <msgno> [<msgno..]
    ```

    **Delete a message from the local system**


=== "Available form"

    ```text
    KILL <from msgno>-<to msgno>
    ```

    **Delete a range of messages**


=== "Available form"

    ```text
    KILL from <regex>
    ```

    **Delete messages FROM a callsign or pattern**


=== "Available form"

    ```text
    KILL to <regex>
    ```

    **Delete messages TO a callsign or pattern**


=== "Available form"

    ```text
    KILL FULL <msgno> [<msgno..]
    ```

    **Delete a message from the whole cluster**

    Delete a message from the local system. You will only be able to
    delete messages that you have originated or been sent (unless you are
    the sysop).

    ```text
    KILL 1234-1255
    ```

    Will delete all the messages that you own between msgnos 1234 and 1255.

    ```text
    KILL from g1tlh
    ```

    will delete all the messages from g1tlh (if you are g1tlh). Similarly:

    ```text
    KILL to g1tlh
    ```

    will delete all messages to g1tlh.

    ```text
    KILL FULL 1234
    ```

    will delete a message (usually a 'bulletin') from the whole cluster system.

    This uses the subject field, so any messages that have exactly the
    same subject will be deleted. Beware!

=== "Available form"

    ```text
    KILL EXPunge <msgno> [<msgno..]
    ```

    **Expunge a message**

    Deleting a message using the normal KILL commands only marks that message
    for deletion. The actual deletion only happens later (usually two days later).

    The KILL EXPUNGE command causes the message to be truly deleted more or less
    immediately.

    It otherwise is used in the same way as the KILL command.

=== "Available form"

    ```text
    KILL <msgno> [<msgno> ...]
    ```

    **Remove or erase a message from the system**

    You can get rid of any message to or originating from your callsign using
    this command. You can remove more than one message at a time.

=== "Available form"

    ```text
    KILL <from>-<to>
    ```

    **Remove a range of messages from the system**


=== "Available form"

    ```text
    KILL FROM <call>
    ```

    **Remove all messages from a callsign**


=== "Available form"

    ```text
    KILL TO <call>
    ```

    **Remove all messages to a callsign**


=== "Available form"

    ```text
    KILL FULL <msgno> [<msgno]
    ```

    **Remove a message from the entire cluster**

    Remove this message from the entire cluster system as well as your node.

=== "Available form"

    ```text
    KILL
    ```

    ****

    As a sysop you can kill any message on the system.

## Verify on a running node

```text
HELP KILL
```

Use the node help to check for local overrides or differences in another installed revision.