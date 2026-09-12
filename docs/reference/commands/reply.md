# `REPLY`

<div class="command-hero" markdown>

**Reply (privately) to the last message that you have read**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
REPLY [token ...]
```

### Available options and values

`RR`

The valid combinations are described in the command forms and examples below.

## Command forms and examples

=== "Available form"

    ```text
    REPLY
    ```

    **Reply (privately) to the last message that you have read**


=== "Available form"

    ```text
    REPLY <msgno>
    ```

    **Reply (privately) to the specified message**


=== "Available form"

    ```text
    REPLY B <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "Available form"

    ```text
    REPLY NOPrivate <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "Available form"

    ```text
    REPLY RR <msgno>
    ```

    **Reply to the specified message with read receipt**

    You can reply to a message and the subject will automatically have
    "Re:" inserted in front of it, if it isn't already present.

    You can also use all the extra qualifiers such as RR, PRIVATE,
    NOPRIVATE, B that you can use with the SEND command (see SEND
    for further details)

## Verify on a running node

```text
HELP REPLY
```

Use the node help to check for local overrides or differences in another installed revision.