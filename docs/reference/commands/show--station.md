# `SHOW/STATION`

<div class="command-hero" markdown>

**Show list of users in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/STATION [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command forms and examples

=== "Available form"

    ```text
    SHOW/STATION ALL [<regex>]
    ```

    **Show list of users in the system**


=== "Available form"

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

## Verify on a running node

```text
HELP SHOW/STATION
```

Use the node help to check for local overrides or differences in another installed revision.