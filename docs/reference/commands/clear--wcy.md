# `CLEAR/WCY`

<div class="command-hero" markdown>

**Clear a WCY filter line**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
CLEAR/WCY [token ...]
```

## Command forms and examples

=== "Available form"

    ```text
    CLEAR/WCY [1|all]
    ```

    **Clear a WCY filter line**

    This command allows you to clear (remove) a line in a WCY filter or to
    remove the whole filter.

    see CLEAR/SPOTS for a more detailed explanation.

=== "Available form"

    ```text
    CLEAR/WCY <callsign> [input] [0-9|all]
    ```

    **Clear a WCY filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

## Verify on a running node

```text
HELP CLEAR/WCY
```

Use the node help to check for local overrides or differences in another installed revision.