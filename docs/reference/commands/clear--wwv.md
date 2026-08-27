# `CLEAR/WWV`

<div class="command-hero" markdown>

**Clear a WWV filter line**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    CLEAR/WWV [1|all]
    ```

    **Clear a WWV filter line**

    This command allows you to clear (remove) a line in a WWV filter or to
    remove the whole filter.

    see CLEAR/SPOTS for a more detailed explanation.

=== "SYSOP form"

    ```text
    CLEAR/WWV <callsign> [input] [0-9|all]
    ```

    **Clear a WWV filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/clear/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/WWV
```

The built-in help is useful when checking the exact command set installed on a particular node.