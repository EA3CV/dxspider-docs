# `KILL`

<div class="command-hero" markdown>

**Delete a message from the local system**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
KILL [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.
- Uses the internal message subsystem.

### Important calls

`DXChannel::broadcast_nodes()`, `DXMsg::get()`, `DXMsg::get_all()`, `DXProt::pc49()`, `ref->mark_delete()`, `ref->stop_msg()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/kill.pl` · SHA-256 `28caa872e21377f6acc76fe67a480184ea873cdb2ccbbce42137490b89671089`

```perl
L11: my ($self, $line) = @_;
L12: my @f = split /\s+/, $line;
L25: my $f = shift @f;
L26: if ($f =~ /^fu/io) {
L29: } elsif ($f =~ /^ex/io) {
L32: } elsif ($f =~ /^\d+$/o) {
L43: } elsif ($f =~ /(\d+)-(\d+)/) {
L48: } elsif ($f =~ /^fr/io) {
L49: $f = shift @f;
L53: @refs = grep { $_->from =~ m{$f}i } @refs;
L55: } elsif ($f =~ /^to/io) {
L56: $f = shift @f;
L60: @refs = grep { $_->to =~ m{$f}i } @refs;
```

### Validation and access evidence

Source: `cmd/kill.pl` · SHA-256 `28caa872e21377f6acc76fe67a480184ea873cdb2ccbbce42137490b89671089`

```perl
L26: if ($f =~ /^fu/io) {
L27: return (1, $self->msg('e5')) if $self->priv < 5;
L30: return (1, $self->msg('e5')) if $self->priv < 6;
L38: if ($self->priv < 5 && $ref->to ne $call && $ref->from ne $call) {
```

### Output and error evidence

Source: `cmd/kill.pl` · SHA-256 `28caa872e21377f6acc76fe67a480184ea873cdb2ccbbce42137490b89671089`

```perl
L27: return (1, $self->msg('e5')) if $self->priv < 5;
L30: return (1, $self->msg('e5')) if $self->priv < 6;
L35: push @out, "Msg $f not found";
L39: push @out, "Msg $f not available";
L63: push @out, "invalid argument '$f'";
L64: return (1, @out);
L70: push @out, $self->msg('m18', $ref->msgno);
L76: push @out, $self->msg('m12', $ref->msgno);
L83: return (1, @out);
```

### Message keys returned

`e5`, `m12`, `m18`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    KILL <msgno> [<msgno..]
    ```

    **Delete a message from the local system**


=== "Help variant"

    ```text
    KILL <from msgno>-<to msgno>
    ```

    **Delete a range of messages**


=== "Help variant"

    ```text
    KILL from <regex>
    ```

    **Delete messages FROM a callsign or pattern**


=== "Help variant"

    ```text
    KILL to <regex>
    ```

    **Delete messages TO a callsign or pattern**


=== "Help variant"

    ```text
    KILL FULL <msgno> [<msgno..]
    ```

    **Delete a message from the whole cluster**

    Delete a message from the local system. You will only be able to
    delete messages that you have originated or been sent (unless you are
    the sysop).

    ```text
    KILL 1234-1255
    ```

    Will delete all the messages that you own between msgnos 1234 and 1255.

    ```text
    KILL from g1tlh
    ```

    will delete all the messages from g1tlh (if you are g1tlh). Similarly:

    ```text
    KILL to g1tlh
    ```

    will delete all messages to g1tlh.

    ```text
    KILL FULL 1234
    ```

    will delete a message (usually a 'bulletin') from the whole cluster system.

    This uses the subject field, so any messages that have exactly the
    same subject will be deleted. Beware!

=== "Help variant"

    ```text
    KILL EXPunge <msgno> [<msgno..]
    ```

    **Expunge a message**

    Deleting a message using the normal KILL commands only marks that message
    for deletion. The actual deletion only happens later (usually two days later).

    The KILL EXPUNGE command causes the message to be truly deleted more or less
    immediately.

    It otherwise is used in the same way as the KILL command.

=== "Help variant"

    ```text
    KILL <msgno> [<msgno> ...]
    ```

    **Remove or erase a message from the system**

    You can get rid of any message to or originating from your callsign using
    this command. You can remove more than one message at a time.

=== "Help variant"

    ```text
    KILL <from>-<to>
    ```

    **Remove a range of messages from the system**


=== "Help variant"

    ```text
    KILL FROM <call>
    ```

    **Remove all messages from a callsign**


=== "Help variant"

    ```text
    KILL TO <call>
    ```

    **Remove all messages to a callsign**


=== "Help variant"

    ```text
    KILL FULL <msgno> [<msgno]
    ```

    **Remove a message from the entire cluster**

    Remove this message from the entire cluster system as well as your node.

=== "Help variant"

    ```text
    KILL
    ```

    ****

    As a sysop you can kill any message on the system.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/kill.pl){ .md-button }

## Verify on a running node

```text
HELP KILL
```

Compare the installed handler with this page when local overrides or a different revision may be present.