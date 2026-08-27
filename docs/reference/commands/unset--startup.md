# `UNSET/STARTUP`

<div class="command-hero" markdown>

**Remove a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    UNSET/STARTUP <call>
    ```

    **Remove a user startup script**


=== "User form"

    ```text
    UNSET/STARTUP
    ```

    **Remove your own startup script**

    You can remove your startup script with UNSET/STARTUP.

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/startup.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/STARTUP
```

The built-in help is useful when checking the exact command set installed on a particular node.