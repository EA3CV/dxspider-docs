# `UNSET/STARTUP`

<div class="command-hero" markdown>

**Remove a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/STARTUP [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

    ```text
    UNSET/STARTUP <call>
    ```

    **Remove a user startup script**


=== "Available form"

    ```text
    UNSET/STARTUP
    ```

    **Remove your own startup script**

    You can remove your startup script with UNSET/STARTUP.

## Verify on a running node

```text
HELP UNSET/STARTUP
```

Use the node help to check for local overrides or differences in another installed revision.