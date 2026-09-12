# `PC`

<div class="command-hero" markdown>

**Send text (eg PC Protocol) to <call>**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
PC [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

    ```text
    PC <call> <text>
    ```

    **Send text (eg PC Protocol) to <call>**

    Send some arbitrary text to a locally connected callsign. No
    processing is done on the text. This command allows you to send PC
    Protocol to unstick things if problems arise (messages get stuck
    etc). eg:-

    ```text
     pc gb7djk PC33^GB7TLH^GB7DJK^400^
    ```
    or
    ```text
     pc G1TLH Try doing that properly!!!
    ```

=== "Available form"

    ```text
    PC <call> <text>
    ```

    **Send arbitrary text to a connected callsign**

    Send any text you like to the callsign requested. This is used mainly to send
    PC protocol to connected nodes either for testing or to unstick things.

    You can also use in the same way as a talk command to a connected user but
    without any processing, added of "from <blah> to <blah" or whatever.

## Verify on a running node

```text
HELP PC
```

Use the node help to check for local overrides or differences in another installed revision.