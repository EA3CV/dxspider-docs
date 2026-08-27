# `SHOW/STATION`

<div class="command-hero" markdown>

**Show list of users in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-dual">User + SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SHOW/STATION ALL [<regex>]
    ```

    **Show list of users in the system**


=== "User form"

    ```text
    SHOW/STATION [<callsign> ..]
    ```

    **Show information about a callsign**

    Show the information known about a callsign and whether (and where)
    that callsign is connected to the cluster.

    ```text
    SH/ST G1TLH
    ```

    If no callsign is given then show the information for yourself.

!!! info "User and SYSOP forms"
    This command has distinct normal-user and administration forms. Use the form appropriate to what you are trying to do.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/station.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/STATION
```

The built-in help is useful when checking the exact command set installed on a particular node.