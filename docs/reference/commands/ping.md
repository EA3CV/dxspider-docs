# `PING`

<div class="command-hero" markdown>

**User level link check command**

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
PING [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXXml::Ping::add()`, `Route::Node::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/ping.pl` · SHA-256 `6f7626e693e193ebc66d6ab6d3150a3e0843a8df45d05bab96b31ee7dc111567`

```perl
L18: my $self = shift;
L19: my $line = uc shift; # only one callsign allowed
L20: my ($call) = $line =~ /^\s*(\S+)/;
```

### Validation and access evidence

Source: `cmd/ping.pl` · SHA-256 `6f7626e693e193ebc66d6ab6d3150a3e0843a8df45d05bab96b31ee7dc111567`

```perl
L24: if ($self->{priv} < 1) {
L32: return (1, $self->msg('e6')) if !$call;
L35: return (1, $self->msg('pinge1')) if $call eq $main::mycall;
L40: return (1, $self->msg('e7', $call)) unless $noderef;
L45: return (1, $self->msg('pingo', $call));
```

### Output and error evidence

Source: `cmd/ping.pl` · SHA-256 `6f7626e693e193ebc66d6ab6d3150a3e0843a8df45d05bab96b31ee7dc111567`

```perl
L26: return (1, "PONG $call");
L28: ++$counter, return (1, "PONG $counter")
L32: return (1, $self->msg('e6')) if !$call;
L35: return (1, $self->msg('pinge1')) if $call eq $main::mycall;
L40: return (1, $self->msg('e7', $call)) unless $noderef;
L45: return (1, $self->msg('pingo', $call));
```

### Message keys returned

`e6`, `e7`, `pinge1`, `pingo`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

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

=== "Help variant"

    ```text
    PING <node call>
    ```

    **Check the link quality between nodes**

    This command allows you to send a frame to another cluster node on
    the network and get a return frame.  The time it takes to do this
    is a good indication of the quality of the link.  The actual time
    it takes is output to the console in seconds.
    Any visible cluster node can be PINGed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/ping.pl){ .md-button }

## Verify on a running node

```text
HELP PING
```

Compare the installed handler with this page when local overrides or a different revision may be present.