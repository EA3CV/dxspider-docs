# `UNSET/ECHO`

<div class="command-hero" markdown>

**Stop the cluster echoing your input**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
UNSET/ECHO
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `self->send_now()`, `user->wantecho()`

### Argument parsing evidence

Source: `cmd/unset/echo.pl` · SHA-256 `678db62831464bab173a9b8981ad8cea40de6e6833845b19586f79b050b62920`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/unset/echo.pl` · SHA-256 `678db62831464bab173a9b8981ad8cea40de6e6833845b19586f79b050b62920`

```perl
L11: return (1, $self->msg('echooff'));
```

### Output and error evidence

Source: `cmd/unset/echo.pl` · SHA-256 `678db62831464bab173a9b8981ad8cea40de6e6833845b19586f79b050b62920`

```perl
L11: return (1, $self->msg('echooff'));
```

### Message keys returned

`echooff`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/echo.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/ECHO
```

Compare the installed handler with this page when local overrides or a different revision may be present.