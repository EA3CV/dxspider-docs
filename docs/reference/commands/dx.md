# `DX`

<div class="command-hero" markdown>

**Send a DX spot into the cluster network.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
DX [token ...]
```

### Who can use it

- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

    ```text
    DX <freq> <call> <remarks>
    ```

    **Send a DX spot**


=== "Available form"

    ```text
    DX [BY <call>] [ip <ipaddress>] <freq> <call> <remarks>
    ```

    **Send a DX spot**

    This is how you send a DX Spot to other users. You can, in fact, now
    enter the <freq> and the <call> either way round.

    ```text
     DX FR0G 144.600
     DX 144.600 FR0G
     DX 144600 FR0G
    ```

    will all give the same result. You can add some remarks to the end
    of the command and they will be added to the spot.

    ```text
     DX FR0G 144600 this is a test
    ```

    You can credit someone else by saying:-

    ```text
     DX by G1TLH FR0G 144.600 he isn't on the cluster
    ```

    The <freq> is compared against the available bands set up in the
    cluster.  See SHOW/BANDS for more information.

## Practical examples

### Normal spot

```text
DX 14025.0 K1ABC CQ
```

### With a short comment

```text
DX 50313.0 EA8XYZ FT8
```

## Related commands

- [`SHOW/DX`](show--dx.md)
- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)

## Verify on a running node

```text
HELP DX
```

Use the node help to check for local overrides or differences in another installed revision.