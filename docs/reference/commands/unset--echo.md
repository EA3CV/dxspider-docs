# `UNSET/ECHO`

<div class="command-hero" markdown>

**Stop the cluster echoing your input**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/ECHO
```

**Stop the cluster echoing your input**

## Details

If you are connected via a telnet session, different implimentations
of telnet handle echo differently depending on whether you are
connected via port 23 or some other port. You can use this command
to change the setting appropriately.

The setting is stored in your user profile.

YOU DO NOT NEED TO USE THIS COMMAND IF YOU ARE CONNECTED VIA AX25.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/echo.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/ECHO
```

The built-in help is useful when checking the exact command set installed on a particular node.