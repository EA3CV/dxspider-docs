# `UNSET/ECHO`

<div class="command-hero" markdown>

**Stop the cluster echoing your input**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/ECHO
```

## Command description

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

## Verify on a running node

```text
HELP UNSET/ECHO
```

Use the node help to check for local overrides or differences in another installed revision.