# `REPLY`

<div class="command-hero" markdown>

**Reply (privately) to the last message that you have read**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    REPLY
    ```

    **Reply (privately) to the last message that you have read**


=== "User form"

    ```text
    REPLY <msgno>
    ```

    **Reply (privately) to the specified message**


=== "User form"

    ```text
    REPLY B <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "User form"

    ```text
    REPLY NOPrivate <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "User form"

    ```text
    REPLY RR <msgno>
    ```

    **Reply to the specified message with read receipt**

    You can reply to a message and the subject will automatically have
    "Re:" inserted in front of it, if it isn't already present.

    You can also use all the extra qualifiers such as RR, PRIVATE,
    NOPRIVATE, B that you can use with the SEND command (see SEND
    for further details)

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/reply.pl){ .md-button }

## Verify on a running node

```text
HELP REPLY
```

The built-in help is useful when checking the exact command set installed on a particular node.