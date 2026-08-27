# `SHOW/STARTUP`

<div class="command-hero" markdown>

**View a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SHOW/STARTUP <call>
    ```

    **View a user startup script**


=== "User form"

    ```text
    SHOW/STARTUP
    ```

    **View your own startup script**

    View the contents of a startup script created with SET/STARTUP.

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/startup.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/STARTUP
```

The built-in help is useful when checking the exact command set installed on a particular node.