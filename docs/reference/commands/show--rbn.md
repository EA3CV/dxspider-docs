# `SHOW/RBN`

<div class="command-hero" markdown>

**Show which connected users want RBN spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SHOW/RBN [<callsign> ...]
    ```

    **Show which connected users want RBN spots**


=== "SYSOP form"

    ```text
    SHOW/RBN ALL
    ```

    **Show ALL users that want RBN spots**

    Show a list of the users that want RBN spots of any the callsigns
    specified on the command line. If no callsigns are specified then a
    sorted list of all connected users wanting RBN spots will be displayed

    SHOW/RBN ALL

    will go through the user file and display ALL users that want RBN spots.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/RBN
```

The built-in help is useful when checking the exact command set installed on a particular node.