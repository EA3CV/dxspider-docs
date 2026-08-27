# `PING`

<div class="command-hero" markdown>

**User level link check command**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    PING [argument]
    ```

    **User level link check command**

    At the user level, this command allows the user to check that they
    are still connected to a functioning node. If the command is
    issued with no arguments it will return string 'PONG 123' where
    '123' is a node global counter starting at 1. This number cannot
    be relied to run consecutively as it is shared by all users.

    If an argument is supplied then the return is 'PONG ARGUMENT'. So it
    you are a client program and you need a counter or some other unique
    string to satisfy yourself that you are not being spoofed, then you
    will need to supply the argument and check that reply is what you
    expect:

    ping 23 or ping xyzzy

    will return

    PONG 23 or PONG XYZZY

    respectively.

=== "SYSOP form"

    ```text
    PING <node call>
    ```

    **Check the link quality between nodes**

    This command allows you to send a frame to another cluster node on
    the network and get a return frame.  The time it takes to do this
    is a good indication of the quality of the link.  The actual time
    it takes is output to the console in seconds.
    Any visible cluster node can be PINGed.

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/ping.pl){ .md-button }

## Verify on a running node

```text
HELP PING
```

The built-in help is useful when checking the exact command set installed on a particular node.