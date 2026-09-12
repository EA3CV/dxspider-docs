# `READ`

<div class="command-hero" markdown>

**Read the next unread personal message addressed to you**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
READ [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command forms and examples

=== "Available form"

    ```text
    READ
    ```

    **Read the next unread personal message addressed to you**


=== "Available form"

    ```text
    READ <msgno>
    ```

    **Read the specified message**

    You can read any messages that are sent as 'non-personal' and also any
    message either sent by or sent to your callsign.

=== "Available form"

    ```text
    READ-
    ```

    ****

    As a sysop you may read any message on the system

## Verify on a running node

```text
HELP READ
```

Use the node help to check for local overrides or differences in another installed revision.