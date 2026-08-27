# `STAT/MSG`

<div class="command-hero" markdown>

**Show the status of the message system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    STAT/MSG
    ```

    **Show the status of the message system**


=== "SYSOP form"

    ```text
    STAT/MSG <msgno>
    ```

    **Show the status of a message**

    This command shows the internal status of a message and includes information
    such as to whom it has been forwarded, its size, origin etc etc.

    If no message number is given then the status of the message system is
    displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/stat/msg.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/MSG
```

The built-in help is useful when checking the exact command set installed on a particular node.