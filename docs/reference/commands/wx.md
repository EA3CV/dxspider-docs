# `WX`

<div class="command-hero" markdown>

**Send a weather message to local users**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
WX [token ...]
```

### Who can use it

- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Available options and values

`FULL`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    WX <text>
    ```

    **Send a weather message to local users**


=== "Available form"

    ```text
    WX FULL <text>
    ```

    **Send a weather message to all cluster users**


=== "Available form"

    ```text
    WX SYSOP <text>
    ```

    **Send a weather message to other clusters only**

    Weather messages can sometimes be useful if you are experiencing an extreme
    that may indicate enhanced conditions

## Verify on a running node

```text
HELP WX
```

Use the node help to check for local overrides or differences in another installed revision.