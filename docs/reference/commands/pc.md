# `PC`

<div class="command-hero" markdown>

**Send text (eg PC Protocol) to <call>**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    PC <call> <text>
    ```

    **Send text (eg PC Protocol) to <call>**

    Send some arbitrary text to a locally connected callsign. No
    processing is done on the text. This command allows you to send PC
    Protocol to unstick things if problems arise (messages get stuck
    etc). eg:-

    ```text
     pc gb7djk PC33^GB7TLH^GB7DJK^400^
    ```
    or
    ```text
     pc G1TLH Try doing that properly!!!
    ```

=== "SYSOP form"

    ```text
    PC <call> <text>
    ```

    **Send arbitrary text to a connected callsign**

    Send any text you like to the callsign requested. This is used mainly to send
    PC protocol to connected nodes either for testing or to unstick things.

    You can also use in the same way as a talk command to a connected user but
    without any processing, added of "from <blah> to <blah" or whatever.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/pc.pl){ .md-button }

## Verify on a running node

```text
HELP PC
```

The built-in help is useful when checking the exact command set installed on a particular node.