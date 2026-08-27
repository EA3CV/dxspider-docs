# `LOAD/KEPS`

<div class="command-hero" markdown>

**Load new keps data**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    LOAD/KEPS
    ```

    **Load new keps data**


=== "SYSOP form"

    ```text
    LOAD/KEPS [nn]
    ```

    **Load new keps data from message**

    If there is no message number then reload the current Keps data from
    the Keps.pm data file. You create this file by running

     /spider/perl/convkeps.pl <filename>

    on a file containing NASA 2 line keps as a message issued by AMSAT.

    If there is a message number, then it will take the message, run
    convkeps.pl on it and then load the data, all in one step.

    These messages are sent to ALL by GB7DJK (and others) from time to time.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/keps.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/KEPS
```

The built-in help is useful when checking the exact command set installed on a particular node.