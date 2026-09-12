# `MSG`

<div class="command-hero" markdown>

**Alter various message parameters**

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
MSG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::get()`, `DXMsg::queue_msg()`, `ref->from()`, `ref->keep()`, `ref->private()`, `ref->read()`, `ref->read_msg_body()`, `ref->rrreq()`, `ref->store()`, `ref->subject()`, `ref->to()`, `ref->waitt()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/msg.pl` · SHA-256 `43b13b1236fee86e773a20fd88c534bfaf9fef6d2c1d87e05deeaf4f6272415d`

```perl
L10: my ($self, $line) = @_;
L14: my @f = split /\s+/, $line, 3;
L21: $cmd = shift @f if @f && $f[0] =~ /^\w+$/;
L22: $msgno = shift @f if @f && $f[0] =~ /^\d+$/;
L25: if ($cmd =~ /^qu/i && !$msgno) {
L29: if ($cmd =~ /^qu/i) {
L35: $data = shift @f;
L44: if ($cmd =~ /^to/i) {
L48: } elsif ($cmd =~ /^fr/i) {
L52: } elsif ($cmd =~ /^pr/i) {
L57: } elsif ($cmd =~ /^nop/i || $cmd =~ /^bu/i) {
L62: } elsif ($cmd =~ /^re/i) {
L67: } elsif ($cmd =~ /^(nore|unre)/i) {
L72: } elsif ($cmd =~ /^rr/i) {
L77: } elsif ($cmd =~ /^norr/i) {
L82: } elsif ($cmd =~ /^ke/i) {
L87: } elsif ($cmd =~ /^noke/i) {
L92: } elsif ($cmd =~ /^node/i) {
L97: } elsif ($cmd =~ /^su/i) {
L101: } elsif ($cmd =~ /^wa/i) {
```

### Validation and access evidence

Source: `cmd/msg.pl` · SHA-256 `43b13b1236fee86e773a20fd88c534bfaf9fef6d2c1d87e05deeaf4f6272415d`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L21: $cmd = shift @f if @f && $f[0] =~ /^\w+$/;
L22: $msgno = shift @f if @f && $f[0] =~ /^\d+$/;
L25: if ($cmd =~ /^qu/i && !$msgno) {
L27: return (1, $self->msg('msg1'));
L29: if ($cmd =~ /^qu/i) {
L31: return (1, $self->msg('msg2'));
L34: return (1, $self->msg('msgu')) unless $cmd && $msgno;
L39: return (1, $self->msg('m13', $msgno)) unless $ref;
L44: if ($cmd =~ /^to/i) {
L107: return (1, $self->msg('e15', $cmd));
L112: return(1, $self->msg('msg3', $msgno, $m, $old, $new));
```

### Output and error evidence

Source: `cmd/msg.pl` · SHA-256 `43b13b1236fee86e773a20fd88c534bfaf9fef6d2c1d87e05deeaf4f6272415d`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L27: return (1, $self->msg('msg1'));
L31: return (1, $self->msg('msg2'));
L34: return (1, $self->msg('msgu')) unless $cmd && $msgno;
L39: return (1, $self->msg('m13', $msgno)) unless $ref;
L107: return (1, $self->msg('e15', $cmd));
L112: return(1, $self->msg('msg3', $msgno, $m, $old, $new));
```

### Message keys returned

`e15`, `e5`, `m13`, `msg1`, `msg2`, `msg3`, `msgu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
MSG <cmd> <msgno> [data ... ]
```

**Alter various message parameters**

## Details

Alter message parameters like To, From, Subject, whether private or bulletin
or return receipt (RR) is required or whether to keep this message from timing
out.

```text
MSG TO <msgno> <call>     - change TO callsign to <call>
MSG FRom <msgno> <call>   - change FROM callsign to <call>
MSG PRrivate <msgno>      - set private flag
MSG NOPRrivate <msgno>    - unset private flag
MSG RR <msgno>            - set RR flag
MSG NORR <msgno>          - unset RR flag
MSG KEep <msgno>          - set the keep flag (message won't be deleted ever)
MSG NOKEep <msgno>        - unset the keep flag
MSG SUbject <msgno> <new> - change the subject to <new>
MSG WAittime <msgno>      - remove any waitting time for this message
MSG NOREad <msgno>        - mark message as unread
MSG REad <msgno>          - mark message as read
MSG QUeue                 - queue any outstanding bulletins
MSG QUeue 1               - queue any outstanding private messages
```

You can look at the status of a message by using:-

```text
STAT/MSG <msgno>
```

This will display more information on the message than DIR does.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/msg.pl){ .md-button }

## Verify on a running node

```text
HELP MSG
```

Compare the installed handler with this page when local overrides or a different revision may be present.