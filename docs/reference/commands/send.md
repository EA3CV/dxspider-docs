# `SEND`

<div class="command-hero" markdown>

**Send a message to one or more callsigns**

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
SEND <structured arguments>
```

The handler parses a structured list (for example comma-separated or key/value input). See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Uses the internal message subsystem.

### Recognized tokens, keys or enumerated values in this handler

`.#`, `<`, `B`, `C`, `CC`, `COPY`, `P`, `RR`, `SYSOP`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXMsg->alloc()`, `DXMsg::get()`, `DXMsg::next_transno()`, `DXMsg::queue_msg()`, `DXMsg::valid_bull_addr()`, `nref->add_dir()`, `nref->store()`, `oref->read_msg_body()`, `self->func()`, `self->msg()`, `self->state()`

### Argument parsing evidence

Source: `cmd/send.pl` · SHA-256 `4aa81f00d5f7530ae71395dd5f51dedc48ac04b4660a3d86ea702d4c3196be46`

```perl
L19: my ($self, $line) = @_;
L21: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
L36: my @f = split /([\s\@\$,])/, $line;
L45: my $f = uc shift @f;
L51: shift @f;
L56: my $m = shift @f;
L63: my $newcall = uc shift @f;
L75: my @list;
L81: push @list, $buf;
L82: push @list, $oref->read_msg_body();
L83: $nref->store(\@list);
L93: if ($notincalls && ($f eq 'B' || $f =~ /^NOP/oi)) {
L95: } elsif ($notincalls && ($f eq 'P' || $f =~ /^PRI/oi)) {
L100: $loc->{from} = uc shift @f;
L101: } elsif (($f =~ /^[\@\.\#\$]$/ || $f eq '.#') && @f) { # this is bbs syntax, for send it 'to node'
L102: shift @f;
L103: } elsif ($f =~ /^\$/) { # this is bbs syntax for a bid
L105: } elsif ($f =~ /^<(\S+)/) { # this is bbs syntax for from call
L107: } elsif ($f =~ /^\$\S+/) { # this is bbs syntax for bid
```

### Validation and access evidence

Source: `cmd/send.pl` · SHA-256 `4aa81f00d5f7530ae71395dd5f51dedc48ac04b4660a3d86ea702d4c3196be46`

```perl
L20: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L21: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
L41: return (1, $self->msg('e6')) if !@f;
L42: return (1, $self->msg('e28')) unless $self->isregistered || uc $f[0] eq $main::myalias;
L58: return (0, $self->msg('m4', $m)) unless $oref;
L59: return (0, $self->msg('m16')) unless @f;
L93: if ($notincalls && ($f eq 'B' || $f =~ /^NOP/oi)) {
L118: if ($self->priv < 5 && $f eq 'SYSOP') {
L140: if (($loc->{private} && is_callsign($f)) || (!$loc->{private} && DXMsg::valid_bull_addr($f))) {
L157: return (1, @out, $self->msg('e6'));
L160: unless (is_callsign($loc->{from})) {
L162: return (1, $self->msg('e22', $loc->{from}));
```

### Output and error evidence

Source: `cmd/send.pl` · SHA-256 `4aa81f00d5f7530ae71395dd5f51dedc48ac04b4660a3d86ea702d4c3196be46`

```perl
L20: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L21: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
L41: return (1, $self->msg('e6')) if !@f;
L42: return (1, $self->msg('e28')) unless $self->isregistered || uc $f[0] eq $main::myalias;
L58: return (0, $self->msg('m4', $m)) unless $oref;
L59: return (0, $self->msg('m16')) unless @f;
L85: push @out, $self->msg('m2', $oref->msgno, $newcall);
L89: return (1, @out);
L131: return (1, "Error in Distro $f.pl:", $@) if $@;
L142: push @out, $self->msg('m3', $f);
L147: push @out, $self->msg('m3', $f);
L157: return (1, @out, $self->msg('e6'));
L162: return (1, $self->msg('e22', $loc->{from}));
L169: push @out, $self->msg('m1');
L171: push @out, $self->msg('m17', $self->state);
L174: return (1, @out);
```

### Message keys returned

`e22`, `e28`, `e36`, `e5`, `e6`, `m1`, `m16`, `m17`, `m2`, `m3`, `m4`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SEND <call> [<call> ...]
    ```

    **Send a message to one or more callsigns**


=== "Help variant"

    ```text
    SEND RR <call>
    ```

    **Send a message and ask for a read receipt**


=== "Help variant"

    ```text
    SEND COPY <msgno> <call>
    ```

    **Send a copy of a  message to someone**


=== "Help variant"

    ```text
    SEND PRIVATE <call>
    ```

    **Send a personal message**


=== "Help variant"

    ```text
    SEND NOPRIVATE <call>
    ```

    **Send a message to all stations**

    All the SEND commands will create a message which will be sent either to
    an individual callsign or to one of the 'bulletin' addresses.

    SEND <call> on its own acts as though you had typed SEND PRIVATE, that is
    it will mark the message as personal and send it to the cluster node that
    that callsign is connected to. If the <call> you have specified is in fact
    a known bulletin category on your node (eg: ALL) then the message should
    automatically become a bulletin.

    You can have more than one callsign in all of the SEND commands.

    You can have multiple qualifiers so that you can have for example:-

    ```text
    SEND RR COPY 123 PRIVATE G1TLH G0RDI
    ```

    which should send a copy of message 123 to G1TLH and G0RDI and you will
    receive a read receipt when they have read the message.

    SB is an alias for SEND NOPRIVATE (or send a bulletin in BBS speak)
    SP is an alias for SEND PRIVATE

    The system will ask you for a subject. Conventionally this should be
    no longer than 29 characters for compatibility. Most modern cluster
    software should accept more.

    You will now be prompted to start entering your text.

    You finish the message by entering '/EX' on a new line. For instance:

    ```text
    ...
    bye then Jim
    73 Dirk
    /ex
    ```

    If you have started a message and you don't want to keep it then you
    can abandon the message with '/ABORT' on a new line, like:-

    ```text
    line 1
    line 2
    oh I just can't be bothered with this
    /abort
    ```

    If you abort the message it will NOT be sent.

    When you are entering the text of your message, most normal output (such
    as DX announcements and so on are suppressed and stored for latter display
    (upto 20 such lines are stored, as new ones come along, so the oldest
    lines are dropped).

    Also, you can enter normal commands commands (and get the output
    immediately) whilst in the middle of a message. You do this by typing
    the command preceeded by a '/' character on a new line, so:-

    ```text
    /dx g1tlh 144010 strong signal
    ```

    Will issue a dx annoucement to the rest of the cluster.

    Also, you can add the output of a command to your message by preceeding
    the command with '//', thus :-

    ```text
    //sh/vhftable
    ```

    This will show YOU the output from SH/VHFTABLE and also store it in the
    message.

    You can carry on with the message until you are ready to send it.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/send.pl){ .md-button }

## Verify on a running node

```text
HELP SEND
```

Compare the installed handler with this page when local overrides or a different revision may be present.