# `SET/STARTUP`

<div class="command-hero" markdown>

**Create a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/STARTUP [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

    ```text
    SET/STARTUP <call>
    ```

    **Create a user startup script**


=== "Available form"

    ```text
    SET/STARTUP
    ```

    **Create your own startup script**

    Create a startup script of DXSpider commands which will be executed
    everytime that you login into this node. You can only input the whole
    script afresh, it is not possible to 'edit' it. Inputting a new script is
    just like typing in a message using SEND. To finish inputting type: /EX
    on a newline, to abandon the script type: /ABORT.

    You may find the (curiously named) command BLANK useful to break
    up the output. If you simply want a blank line, it is easier to
    input one or more spaces and press the <return> key.

    See UNSET/STARTUP to remove a script.

## Verify on a running node

```text
HELP SET/STARTUP
```

Use the node help to check for local overrides or differences in another installed revision.