# `CLEAR/ANNOUNCE`

<div class="command-hero" markdown>

**Clear a announce filter line**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
CLEAR/ANNOUNCE [token ...]
```

## Command forms and examples

=== "Available form"

    ```text
    CLEAR/ANNOUNCE [1|all]
    ```

    **Clear a announce filter line**

    This command allows you to clear (remove) a line in a annouce filter or to
    remove the whole filter.

    see CLEAR/SPOTS for a more detailed explanation.

=== "Available form"

    ```text
    CLEAR/ANNOUNCE <callsign> [input] [0-9|all]
    ```

    **Clear a announce filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

## Verify on a running node

```text
HELP CLEAR/ANNOUNCE
```

Use the node help to check for local overrides or differences in another installed revision.