# `STAT/MSG`

<div class="command-hero" markdown>

**Show the status of the message system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
STAT/MSG [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command forms and examples

=== "Available form"

    ```text
    STAT/MSG
    ```

    **Show the status of the message system**


=== "Available form"

    ```text
    STAT/MSG <msgno>
    ```

    **Show the status of a message**

    This command shows the internal status of a message and includes information
    such as to whom it has been forwarded, its size, origin etc etc.

    If no message number is given then the status of the message system is
    displayed.

## Verify on a running node

```text
HELP STAT/MSG
```

Use the node help to check for local overrides or differences in another installed revision.