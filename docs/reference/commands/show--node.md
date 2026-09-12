# `SHOW/NODE`

<div class="command-hero" markdown>

**Show the type and version number of nodes**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/NODE [token ...]
```

### Available options and values

`Spider`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    SHOW/NODE [<callsign> ...]
    ```

    **Show the type and version number of nodes**


=== "Available form"

    ```text
    SHOW/NODE ALL
    ```

    **Show the type,version number of ALL known nodes**

    Show the type and version (if connected) of the nodes specified on the
    command line. If no callsigns are specified then a sorted list of all
    the non-user callsigns connected to node will be displayed.

## Verify on a running node

```text
HELP SHOW/NODE
```

Use the node help to check for local overrides or differences in another installed revision.