# `CHAT`

<div class="command-hero" markdown>

**Chat or Conference to a group**

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
CHAT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`BadWords::check()`, `self->badcount()`, `self->msg()`, `self->send_chats()`, `self->state()`, `self->talklist()`

### Argument parsing evidence

Source: `cmd/chat.pl` · SHA-256 `11c9aca8dc66e673a4a30036b5de19860c3d9d0720f2f5bdc2bb4dbdd423a424`

```perl
L10: my ($self, $line) = @_;
L13: my @f = split /\s+/, $line, 2;
L31: $line =~ s/\^/:/og;
L35: if (@bad = BadWords::check($line)) {
L37: LogDbg('DXCommand', "$self->{call} swore: $line (with words:" . join(',', @bad) . ")");
L38: Log('chat', $target, $from, "[to $from only] $line");
L39: return (1, "$target de $from <$t>: $line");
```

### Validation and access evidence

Source: `cmd/chat.pl` · SHA-256 `11c9aca8dc66e673a4a30036b5de19860c3d9d0720f2f5bdc2bb4dbdd423a424`

```perl
L14: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L15: return (1, $self->msg('e34')) unless @f >= 1;
L16: return (1, $self->msg('e28')) unless $self->isregistered;
L20: return (1, $self->msg('e35', $target)) unless grep uc $_ eq $target, @{$self->user->group};
```

### Output and error evidence

Source: `cmd/chat.pl` · SHA-256 `11c9aca8dc66e673a4a30036b5de19860c3d9d0720f2f5bdc2bb4dbdd423a424`

```perl
L14: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L15: return (1, $self->msg('e34')) unless @f >= 1;
L16: return (1, $self->msg('e28')) unless $self->isregistered;
L20: return (1, $self->msg('e35', $target)) unless grep uc $_ eq $target, @{$self->user->group};
L39: return (1, "$target de $from <$t>: $line");
L46: push @out, $self->msg('chattoomany', $target, $self->talklist->[0]);
L49: push @out, $self->msg('chatinst', $target);
L53: push @out, $self->chat_prompt;
L57: return (1, @out);
```

### Message keys returned

`chatinst`, `chattoomany`, `e28`, `e34`, `e35`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
CHAT <group> <text>
```

**Chat or Conference to a group**

## Details

It is now possible to JOIN a group and have network wide conferencing to that
group. DXSpider does not (and probably will not) implement the AK1A
conference mode as this seems very limiting, is hardly used and doesn't seem
to work too well anyway.

This system uses the existing ANN system and is compatible with both other
DXSpider nodes and AK1A clusters (they use ANN/<group>).

You can be a member of as many "groups" as you want. To join a group type:-

```text
JOIN FOC    (where FOC is the group name)
```

To leave a group type:-

```text
LEAVE FOC
```

You can see which groups you are in by typing:-

```text
STAT/USER
```

and you can see whether your mate is in the group, if he connects to the
same node as you, by typing:-

```text
STAT/USER g1tlh
```

To send a message to a group type:-

```text
CHAT FOC hello everyone
```

or

```text
CH #9000 hello I am back
```

See also JOIN, LEAVE, SHOW/CHAT

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/chat.pl){ .md-button }

## Verify on a running node

```text
HELP CHAT
```

Compare the installed handler with this page when local overrides or a different revision may be present.