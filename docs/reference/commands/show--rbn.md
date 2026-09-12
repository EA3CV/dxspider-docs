# `SHOW/RBN`

<div class="command-hero" markdown>

**Show which connected users want RBN spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/RBN [token ...]
```

## Command forms and examples

=== "Available form"

    ```text
    SHOW/RBN [<callsign> ...]
    ```

    **Show which connected users want RBN spots**


=== "Available form"

    ```text
    SHOW/RBN ALL
    ```

    **Show ALL users that want RBN spots**

    Show a list of the users that want RBN spots of any the callsigns
    specified on the command line. If no callsigns are specified then a
    sorted list of all connected users wanting RBN spots will be displayed

    SHOW/RBN ALL

    will go through the user file and display ALL users that want RBN spots.

## Verify on a running node

```text
HELP SHOW/RBN
```

Use the node help to check for local overrides or differences in another installed revision.