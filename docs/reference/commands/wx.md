# `WX`

<div class="command-hero" markdown>

**Send a weather message to local users**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    WX <text>
    ```

    **Send a weather message to local users**


=== "User form"

    ```text
    WX FULL <text>
    ```

    **Send a weather message to all cluster users**


=== "SYSOP form"

    ```text
    WX SYSOP <text>
    ```

    **Send a weather message to other clusters only**

    Weather messages can sometimes be useful if you are experiencing an extreme
    that may indicate enhanced conditions

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/wx.pl){ .md-button }

## Verify on a running node

```text
HELP WX
```

The built-in help is useful when checking the exact command set installed on a particular node.