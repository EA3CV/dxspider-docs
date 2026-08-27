# `SET/STARTUP`

<div class="command-hero" markdown>

**Create a user startup script**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SET/STARTUP <call>
    ```

    **Create a user startup script**


=== "User form"

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

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/startup.pl){ .md-button }

## Verify on a running node

```text
HELP SET/STARTUP
```

The built-in help is useful when checking the exact command set installed on a particular node.