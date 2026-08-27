# `READ`

<div class="command-hero" markdown>

**Read the next unread personal message addressed to you**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    READ
    ```

    **Read the next unread personal message addressed to you**


=== "User form"

    ```text
    READ <msgno>
    ```

    **Read the specified message**

    You can read any messages that are sent as 'non-personal' and also any
    message either sent by or sent to your callsign.

=== "SYSOP form"

    ```text
    READ-
    ```

    ****

    As a sysop you may read any message on the system

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/read.pl){ .md-button }

## Verify on a running node

```text
HELP READ
```

The built-in help is useful when checking the exact command set installed on a particular node.