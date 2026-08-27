# `ANNOUNCE`

<div class="command-hero" markdown>

**Send local, cluster-wide or SYSOP-only announcements.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Communications</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    ANNOUNCE <text>
    ```

    **Send an announcement to LOCAL users only**

    <text> is the text of the announcement you wish to broadcast

=== "User form"

    ```text
    ANNOUNCE FULL <text>
    ```

    **Send an announcement cluster wide**

    This will send your announcement cluster wide

=== "SYSOP form"

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

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/announce.pl){ .md-button }

## Related commands

- [`SHOW/ANNOUNCE`](show--announce.md)
- [`ACCEPT/ANNOUNCE`](accept--announce.md)
- [`REJECT/ANNOUNCE`](reject--announce.md)

## Verify on a running node

```text
HELP ANNOUNCE
```

The built-in help is useful when checking the exact command set installed on a particular node.