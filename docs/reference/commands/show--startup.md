# `SHOW/STARTUP`

<div class="command-hero" markdown>

**View a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/STARTUP [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

    ```text
    SHOW/STARTUP <call>
    ```

    **View a user startup script**


=== "Available form"

    ```text
    SHOW/STARTUP
    ```

    **View your own startup script**

    View the contents of a startup script created with SET/STARTUP.

## Verify on a running node

```text
HELP SHOW/STARTUP
```

Use the node help to check for local overrides or differences in another installed revision.