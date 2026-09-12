# `ANNOUNCE`

<div class="command-hero" markdown>

**Send local, cluster-wide or SYSOP-only announcements.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Communications</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
ANNOUNCE [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

### Available options and values

`FULL`, `LOCAL`, `SYSOP`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    ANNOUNCE <text>
    ```

    **Send an announcement to LOCAL users only**

    <text> is the text of the announcement you wish to broadcast

=== "Available form"

    ```text
    ANNOUNCE FULL <text>
    ```

    **Send an announcement cluster wide**

    This will send your announcement cluster wide

=== "Available form"

    ```text
    ANNOUNCE SYSOP <text>
    ```

    **Send an announcement to Sysops only**


## Practical examples

### Local users only

```text
ANNOUNCE Local net starts at 20:00Z
```

### Cluster-wide

```text
ANNOUNCE FULL Contest starts in 10 minutes
```

### SYSOP audience

```text
ANNOUNCE SYSOP Link maintenance at 22:00Z
```

## Related commands

- [`SHOW/ANNOUNCE`](show--announce.md)
- [`ACCEPT/ANNOUNCE`](accept--announce.md)
- [`REJECT/ANNOUNCE`](reject--announce.md)

## Verify on a running node

```text
HELP ANNOUNCE
```

Use the node help to check for local overrides or differences in another installed revision.