# `TALK`

<div class="command-hero" markdown>

**Send a private talk message or enter interactive talk mode.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Communications</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
TALK [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`BadWords::check()`, `DXProt::pc93()`, `Route::get()`, `me->normal()`, `self->badcount()`, `self->msg()`, `self->send_talks()`, `self->state()`, `self->talklist()`

### Argument parsing evidence

Source: `cmd/talk.pl` · SHA-256 `70e3b0d6411d53e2450b8dd1c9b478d101ec2347291aeac4cfb784e7d88ff1dd`

```perl
L12: my $line;
L25: $inline =~ s/(?:\s*>([A-Za-z0-9\-]+))\s*//;
L27: ($to, $line) = $inline =~ /^\s*([A-Za-z0-9\-]+)\s*(.*)?$/;
L56: if (@bad = BadWords::check($line)) {
L58: LogDbg('DXCommand', "$self->{call} swore: $line (with words:" . join(',', @bad) . ")");
L63: if ($line) {
L64: Log('talk', $to, $from, '>' . ($via || ($dxchan && $dxchan->call) || '*'), $line);
L66: $self->send_talks($to, $line);
```

### Validation and access evidence

Source: `cmd/talk.pl` · SHA-256 `70e3b0d6411d53e2450b8dd1c9b478d101ec2347291aeac4cfb784e7d88ff1dd`

```perl
L15: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L31: return (1, $self->msg('e8')) unless $to;
L35: return (1, $self->msg('e22', $to)) unless is_callsign($to);
L36: return (1, $self->msg('e28')) unless $self->isregistered || $to eq $main::myalias;
```

### Output and error evidence

Source: `cmd/talk.pl` · SHA-256 `70e3b0d6411d53e2450b8dd1c9b478d101ec2347291aeac4cfb784e7d88ff1dd`

```perl
L15: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L31: return (1, $self->msg('e8')) unless $to;
L35: return (1, $self->msg('e22', $to)) unless is_callsign($to);
L36: return (1, $self->msg('e28')) unless $self->isregistered || $to eq $main::myalias;
L72: $main::me->normal(DXProt::pc93($to, $self->call, $via, $self->msg('talkstart'), undef, $ipaddr));
L78: $main::me->normal(DXProt::pc93($to, $self->call, $via, $self->msg('talkstart'), undef, $ipaddr));
L79: push @out, $self->msg('talkinst');
L82: Log('talk', $to, $from, '>' . ($via || ($dxchan && $dxchan->call) || '*'), $self->msg('talkstart'), undef, $ipaddr);
L83: push @out, $self->talk_prompt;
L86: return (1, @out);
```

### Message keys returned

`e22`, `e28`, `e5`, `e7`, `e8`, `talkinst`, `talkstart`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    TALK <call> [<text>]
    ```

    **Send a text message to another station**


=== "Help variant"

    ```text
    TALK <call> > <node> [<text>]
    ```

    **Send a text message to another station via a node**

    Send a short message to any other station that is visible on the cluster
    system. You can send it to anyone you can see with a SHOW/CONFIGURATION
    command, they don't have to be connected locally.

    The second form of TALK is used when other cluster nodes are connected
    with restricted information. This usually means that they don't send
    the user information usually associated with logging on and off the cluster.

    If you know that G3JNB is likely to be present on GB7TLH, but you can only
    see GB7TLH in the SH/C list but with no users, then you would use the
    second form of the talk message.

    If you want to have a ragchew with someone you can leave the text message
    out and the system will go into 'Talk' mode. What this means is that a
    short message is sent to the recipient telling them that you are in a
    'Talking' frame of mind and then you just type - everything you send will
    go to the station that you asked for.

    All the usual announcements, spots and so on will still come out on your
    terminal.

    If you want to do something (such as send a spot) you preceed the normal
    command with a '/' character, eg:-

    ```text
     /DX 14001 G1TLH What's a B class licensee doing on 20m CW?
     /HELP talk
    ```

    To leave talk mode type:

    ```text
     /EX
    ```

    If you are in 'Talk' mode, there is an extention to the '/' command which
    allows you to send the output to all the people you are talking to. You do
    with the '//' command. For example:-

    ```text
    //sh/hftable
    ```

    will send the hftable as you have it to all the people you are currently
    talking to.

## Practical examples

### Send a message

```text
TALK G1ABC Hello John
```

### Route explicitly through a node

```text
TALK G1ABC > GB7DJK Hello John
```

### Run a DXSpider command while in talk mode

```text
/SHOW/DX
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/talk.pl){ .md-button }

## Related commands

- [`SHOW/TALK`](show--talk.md)
- [`SET/TALK`](set--talk.md)
- [`UNSET/TALK`](unset--talk.md)

## Verify on a running node

```text
HELP TALK
```

Compare the installed handler with this page when local overrides or a different revision may be present.