# `SHOW/NODE`

<div class="command-hero" markdown>

**Show the type and version number of nodes**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SHOW/NODE [<callsign> ...]
    ```

    **Show the type and version number of nodes**


=== "SYSOP form"

    ```text
    SHOW/NODE ALL
    ```

    **Show the type,version number of ALL known nodes**

    Show the type and version (if connected) of the nodes specified on the
    command line. If no callsigns are specified then a sorted list of all
    the non-user callsigns connected to node will be displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/node.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/NODE
```

The built-in help is useful when checking the exact command set installed on a particular node.